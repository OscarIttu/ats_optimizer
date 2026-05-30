import os
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv

# Cargamos la clave desde el archivo .env
load_dotenv()

# =====================================================================
# 1. ESTRUCTURA DEL REPORTE (Se mantiene idéntica para no romper main.py)
# =====================================================================
class SugerenciaRedaccion(BaseModel):
    frase_original: str = Field(description="La frase o sección exacta extraída del CV del candidato.")
    frase_sugerida: str = Field(description="La propuesta optimizada para el ATS, incluyendo palabras clave y enfoque en logros.")
    motivo: str = Field(description="Explicación técnica de por qué este cambio ayuda a superar el filtro.")

class ReporteATS(BaseModel):
    score_ats: int = Field(description="Puntuación de optimización global de 0 a 100 basada en la oferta.")
    palabras_clave_faltantes: List[str] = Field(description="Habilidades, herramientas o conceptos críticos que faltan en el CV.")
    brechas_semanticas: List[str] = Field(description="Incongruencias detectadas entre los requisitos y la experiencia descrita.")
    mejoras_redaccion: List[SugerenciaRedaccion] = Field(description="Lista de sugerencias de cambios de texto específicos.")
    secciones_a_anadir: List[str] = Field(description="Apartados o información crucial que falta por completo en el documento.")

# =====================================================================
# 2. FUNCIÓN DE CONEXIÓN CON GEMINI
# =====================================================================
def analizar_cv_con_claude(texto_cv: str, texto_oferta: str) -> str:
    """
    Envía el CV y la oferta a Gemini (gemini-2.5-flash) y fuerza la respuesta
    para que se adapte exactamente al formato JSON de Pydantic.
    """
    # Inicializa el cliente de Gemini (busca automáticamente la variable GEMINI_API_KEY)
    client = genai.Client()
    
    prompt_sistema = (
        "Eres un sistema experto en auditoría de talento y optimización de currículums para Sistemas de Seguimiento de Candidatos (ATS). "
        "Tu objetivo es analizar el CV del usuario y compararlo con la oferta, identificando dónde falla frente a los filtros automatizados."
    )
    
    prompt_usuario = f"""
    Analiza detalladamente el siguiente Currículum Vitae frente a la Descripción de la Oferta de Empleo.
    
    [CURRÍCULUM VITAE]
    {texto_cv}
    
    [DESCRIPCIÓN DE LA OFERTA]
    {texto_oferta}
    """

    # Hacemos la llamada configurando el formato de salida estructurado
    respuesta = client.models.generate_content(
        model='gemini-2.5-pro', 
        contents=prompt_usuario,

        config=types.GenerateContentConfig(
            system_instruction=prompt_sistema,
            temperature=0.2,
            # Forzamos a Gemini a devolver el JSON bajo el molde de Pydantic
            response_mime_type="application/json",
            response_schema=ReporteATS,
        ),
    )
    
    # Devolvemos el texto de la respuesta (que ya es el JSON limpio)
    return respuesta.text