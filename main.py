from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

# Importamos las funciones de los archivos que has creado antes
from extractor import extraer_texto_de_cv
from matcher import calcular_similitud_coseno
from ai_analyzer import analizar_cv_con_claude

# Inicializamos la aplicación FastAPI
app = FastAPI(
    title="Optimización de CV para ATS",
    description="API para analizar y adaptar currículums frente a ofertas de empleo usando IA.",
    version="1.0"
)

# Configuración de CORS: Permite que interfaces web (Frontend) se conecten a esta API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/analizar")
async def analizar_cv(
    oferta_texto: str = Form(..., description="El texto completo de la oferta de empleo de la empresa"),
    file: UploadFile = File(..., description="El archivo PDF del currículum vitae")
):
    # 1. Validación de seguridad básica: Asegurar que el archivo es un PDF
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(
            status_code=400, 
            detail="Formato de archivo no válido. Debe subir obligatoriamente un archivo PDF."
        )
    
    try:
        # 2. Extracción: Convertimos el archivo PDF recibido en texto plano
        contenido_cv = extraer_texto_de_cv(file.file)
        
        if not contenido_cv:
            raise HTTPException(
                status_code=400, 
                detail="No se pudo extraer texto indexable del PDF. Asegúrese de que no sea una imagen escaneada."
            )
        
        # 3. Módulo Matemático: Calculamos la afinidad superficial con Scikit-learn
        score_matematico = calcular_similitud_coseno(contenido_cv, oferta_texto)
        
        # 4. Módulo de IA: Enviamos los textos a Claude para el análisis profundo
        respuesta_raw_claude = analizar_cv_con_claude(contenido_cv, oferta_texto)
        
        # 5. Procesamiento: Transformamos el texto devuelto por la IA en un objeto JSON nativo de Python
        analisis_ia = json.loads(respuesta_raw_claude)
        
        # 6. Consolidación: Unimos el resultado matemático y el cualitativo en un único reporte
        reporte_final = {
            "score_matematico_superficial": score_matematico,
            "analisis_profundo_ia": analisis_ia
        }
        
        return reporte_final

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500, 
            detail="Error al procesar la respuesta de la IA. El formato devuelto no fue un JSON válido."
        )
    except Exception as e:
        import traceback
        error_detallado = traceback.format_exc()
        print(error_detallado) # Esto pintará el error real en tu terminal negra
        raise HTTPException(
            status_code=500, 
            detail=f"ERROR REAL: {str(e)} | DETALLE: {error_detallado}"
        )

# Código para arrancar el servidor directamente si ejecutamos este archivo
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)