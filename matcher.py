from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calcular_similitud_coseno(texto_cv: str, texto_oferta: str) -> float:
    """
    Compara el texto del CV y de la oferta de empleo de forma matemática.
    Devuelve un porcentaje de coincidencia entre 0.0 y 100.0.
    """
    # Si alguno de los dos textos está vacío, la coincidencia es cero
    if not texto_cv or not texto_oferta:
        return 0.0

    # Configuramos el vectorizador para que ignore palabras comunes que no aportan valor
    # como "el", "la", "de", "un", "y" (las llamadas 'stop words')
    vectorizador = TfidfVectorizer(stop_words='spanish')
    
    try:
        # Convertimos los dos textos en matrices numéricas (vectores)
        tfidf_matrix = vectorizador.fit_transform([texto_cv, texto_oferta])
        
        # Calculamos la similitud del coseno entre el CV (posición 0) y la oferta (posición 1)
        similitud = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        
        # Pasamos el resultado a porcentaje (ej: de 0.75 a 75.0) y redondeamos a dos decimales
        return round(float(similitud[0][0]) * 100, 2)
        
    except ValueError:
        # Si los textos no tienen suficientes palabras válidas para comparar, devolvemos 0
        return 0.0