# 💼 AI ATS Optimizer — Auditor Experto de CVs con Gemini 2.5

Este proyecto es un **Optimizador de Currículums automatizado** diseñado para ayudar a los candidatos a superar los filtros de los Sistemas de Seguimiento de Candidatos (ATS) que utilizan las empresas en sus procesos de selección. 

La aplicación analiza el texto de un CV en formato PDF frente a los requisitos de una oferta de empleo real y devuelve un informe detallado con una puntuación de compatibilidad y sugerencias de mejora semántica.

---

## 🚀 Características Clave

* **Análisis Semántico Avanzado:** Conexión directa con la API de **Gemini 2.5 Flash / Pro** para auditar el contenido.
* **Structured Outputs:** Uso de moldes estrictos de **Pydantic** para forzar al modelo de IA a responder en JSON nativo sin alucinaciones.
* **Extracción Limpia de PDF:** Procesamiento de documentos estructurados mediante `pdfplumber`.
* **Interfaz Web Interactiva:** UI moderna, rápida y limpia desarrollada íntegramente con **Streamlit**.

---

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.x
* **Core IA:** Google GenAI SDK (`gemini-2.5-flash`)
* **Modelado de Datos:** Pydantic
* **Frontend:** Streamlit
* **Gestión de Entorno:** Python-dotenv

---

## 💻 Instalación y Uso Local

Sigue estos pasos para clonar y ejecutar el proyecto en tu máquina local:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/TU_USUARIO_DE_GITHUB/ats_optimizer.git](https://github.com/TU_USUARIO_DE_GITHUB/ats_optimizer.git)
cd ats_optimizer

2. Instalar las dependencias
Se recomienda usar un entorno virtual. Instala los paquetes requeridos ejecutando:
pip install -r requirements.txt

3. Configurar las variables de entorno
Crea un archivo .env en la raíz del proyecto y añade tu clave de Google AI Studio con saldo de prepago activo:
GEMINI_API_KEY=tu_api_key_aqui

4. Lanzar la aplicación
Arranca el servidor local de Streamlit:
python -m streamlit run app.py

La aplicación se abrirá automáticamente en tu navegador en http://localhost:8501.

## 🌟 Características Clave del Reporte
El motor de IA audita el currículum devolviendo obligatoriamente los siguientes puntos estructurados:

Puntuación ATS Global: Una métrica de 0 a 100 que calcula el nivel de compatibilidad.

Palabras Clave Faltantes: Identificación de habilidades técnicas, herramientas o certificaciones críticas que exige la oferta pero no están en el CV.

Brechas Semánticas: Incongruencias o debilidades conceptuales entre la experiencia redactada y el puesto.

Sugerencias de Redacción: Propuestas exactas en formato Frase Original ➡️ Frase Sugerida, acompañadas del motivo de optimización técnica.

Secciones Recomendadas: Apartados ausentes indispensables para el perfil (ej. Portafolio, Certificaciones).

Desarrollado con 🧠 enfocado en la integración de Inteligencia Artificial en entornos de Talento y Software.