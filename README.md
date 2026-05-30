```markdown
# 💼 AI ATS Optimizer — Auditor Experto de CVs con Gemini 2.5

Este proyecto es un **Optimizador de Currículums automatizado** diseñado para ayudar a los candidatos a superar los filtros de los Sistemas de Seguimiento de Candidatos (ATS) que utilizan las empresas en sus procesos de selección. 

La aplicación analiza el texto de un CV en formato PDF frente a los requisitos de una oferta de empleo real y devuelve un informe detallado con una puntuación de compatibilidad y sugerencias de mejora semántica.

La combinación de extracción local de datos y un LLM de última generación garantiza un análisis profundo, estructurado y **libre de alucinaciones**.

---

## 🏗️ Arquitectura del Sistema

El flujo de información sigue una estructura de procesamiento y validación semántica optimizada para entornos locales y APIs de producción:

1. **Extracción del Documento:** El archivo del currículum se sube en formato PDF y se procesa localmente utilizando `pdfplumber` para extraer el texto plano de forma limpia y estructurada.
2. **Ingesta de la Oferta:** El usuario introduce la descripción del puesto de trabajo a través de la interfaz web, sirviendo como el marco de requisitos de referencia.
3. **Modelado Estricto de Datos:** Se define un esquema rígido en el backend mediante **Pydantic**, mapeando las variables clave que los filtros ATS analizan (puntuación, palabras clave faltantes, brechas semánticas y sugerencias de redacción).
4. **Análisis Semántico Avanzado:** Se inyecta el texto del CV y de la oferta en **Gemini 2.5 Flash** (o Pro), utilizando *Structured Outputs* para obligar al modelo a responder bajo el JSON estricto de Pydantic.
5. **Renderizado Dinámico:** La interfaz web de **Streamlit** captura el objeto JSON devuelto por la IA y lo dibuja en pantalla en tiempo real utilizando componentes visuales (métricas, expansores y tarjetas de alerta).

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
git clone [https://github.com/OscarIttu/optimizador_ats.git](https://github.com/OscarIttu/optimizador_ats.git)
cd optimizador_ats

```

### 2. Instalar las dependencias

Se recomienda usar un entorno virtual. Instala los paquetes requeridos ejecutando:

```bash
pip install -r requirements.txt

```

### 3. Configurar las variables de entorno

Crea un archivo `.env` en la raíz del proyecto y añade tu clave de Google AI Studio con saldo de prepago activo:

```env
GEMINI_API_KEY=tu_api_key_aqui

```

### 4. Lanzar la application

Arranca el servidor local de Streamlit:

```bash
python -m streamlit run app.py

```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`.

---

## 🌟 Características Clave del Reporte JSON

El motor de IA audita el currículum devolviendo obligatoriamente un objeto estructurado basado en los siguientes puntos clave:

* **Puntuación ATS Global:** Una métrica de 0 a 100 que calcula el nivel de compatibilidad.
* **Palabras Clave Faltantes:** Identificación de habilidades técnicas, herramientas o certificaciones críticas que exige la oferta pero no están en el CV.
* **Brechas Semánticas:** Incongruencias o debilidades conceptuales entre la experiencia redactada y el puesto.
* **Sugerencias de Redacción:** Propuestas exactas en formato *Frase Original* ➡️ *Frase Sugerida*, acompañadas del motivo de optimización técnica.
* **Secciones Recomendadas:** Apartados ausentes indispensables para el perfil (ej. Portafolio, Certificaciones).

---

Desarrollado con 🧠 enfocado en la integración de Inteligencia Artificial en entornos de Talento y Software.

```

```