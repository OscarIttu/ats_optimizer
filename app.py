import streamlit as st
import json
# Importamos las funciones que ya programaste y funcionan perfectamente
from extractor import extraer_texto_de_cv  # Asegúrate de que se llama así tu función de extraer PDF
from ai_analyzer import analizar_cv_con_claude

# Configuración de la página web
st.set_page_config(
    page_title="Optimizador de CV para ATS",
    page_icon="💼",
    layout="wide"
)

# Título y presentación
st.title("💼 Optimizador de Currículum para Filtros ATS")
st.markdown("""
    Esta herramienta analiza tu CV frente a una oferta de empleo utilizando **Gemini 2.5 Flash** para ayudarte a superar los filtros automatizados (ATS) de las empresas.
""")

st.divider()

# Creamos dos columnas en la pantalla para organizar el formulario
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Datos de la Oferta")
    texto_oferta = st.text_area(
        "Copia y pega la descripción del puesto o requisitos aquí:",
        height=250,
        placeholder="Requisitos: Experiencia en Python, FastAPI, bases de datos..."
    )

with col2:
    st.subheader("2. Tu Currículum")
    archivo_pdf = st.file_uploader("Sube tu CV en formato PDF:", type=["pdf"])

st.divider()

# Botón central para ejecutar el análisis
if st.button("🚀 Analizar y Optimizar CV", use_container_width=True):
    # Validamos que el usuario haya rellenado ambos campos
    if not texto_oferta:
        st.error("Por favor, introduce el texto de la oferta de empleo.")
    elif not archivo_pdf:
        st.error("Por favor, sube tu currículum en formato PDF.")
    else:
        with st.spinner("Analizando tu currículum con Inteligencia Artificial..."):
            try:
                # 1. Extraemos el texto del PDF subido
                # Pasamos los bytes del archivo directamente a tu extractor
                texto_cv = extraer_texto_de_cv(archivo_pdf)
                
                # 2. Llamamos a tu función de Gemini (que la renombramos en el paso anterior)
                respuesta_json_str = analizar_cv_con_claude(texto_cv, texto_oferta)
                
                # 3. Parseamos el texto JSON para convertirlo en un diccionario de Python
                reporte = json.loads(respuesta_json_str)
                
                st.success("¡Análisis completado con éxito!")
                st.divider()
                
                # =============================================================
                # MOSTRAR RESULTADOS EN PANTALLA
                # =============================================================
                
                # Fila superior con la nota global
                score = reporte.get("score_ats", 0)
                if score >= 70:
                    st.metric(label="Puntuación ATS", value=f"{score} / 100", delta="¡Buen Match!")
                else:
                    st.metric(label="Puntuación ATS", value=f"{score} / 100", delta="- Necesita optimización", delta_color="inverse")
                
                # Dos columnas para palabras clave y brechas
                c1, c2 = st.columns(2)
                with c1:
                    st.warning("⚠️ Palabras Clave Faltantes")
                    for palabra in reporte.get("palabras_clave_faltantes", []):
                        st.markdown(f"- **{palabra}**")
                        
                with c2:
                    st.error("🔍 Brechas Semánticas Detectadas")
                    for brecha in reporte.get("brechas_semanticas", []):
                        st.markdown(f"- {brecha}")
                
                st.divider()
                
                # Sección de mejoras de redacción
                st.subheader("✍️ Sugerencias de Redacción Específicas")
                for mejora in reporte.get("mejoras_redaccion", []):
                    with st.expander(f"Optimizar: \"{mejora.get('frase_original')}\""):
                        st.markdown(f"**Propuesta ATS:** `{mejora.get('frase_sugerida')}`")
                        st.caption(f"**Motivo:** {mejora.get('motivo')}")
                
                # Sección de apartados extra
                st.divider()
                st.subheader("📂 Secciones recomendadas a añadir")
                for seccion in reporte.get("secciones_a_anadir", []):
                    st.info(f"📌 {seccion}")
                    
            except Exception as e:
                st.error(f"Ocurrió un error durante el procesamiento: {str(e)}")