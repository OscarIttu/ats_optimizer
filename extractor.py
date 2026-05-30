import pdfplumber

def extraer_texto_de_cv(archivo_pdf) -> str:
    """
    Acepta un archivo PDF (ya sea una ruta en el ordenador o un archivo subido a la API)
    y extrae todo su texto plano legible.
    """
    texto_completo = []
    
    # Abrimos el archivo PDF usando pdfplumber
    with pdfplumber.open(archivo_pdf) as pdf:
        # Recorremos el PDF página por página
        for numero_pagina, pagina in enumerate(pdf.pages, start=1):
            texto_pagina = pagina.extract_text()
            
            # Si la página tiene texto legible, lo guardamos
            if texto_pagina:
                texto_completo.append(texto_pagina)
            else:
                # Esto avisa si una página está vacía o es una imagen escaneada sin texto real
                print(f"Advertencia: La página {numero_pagina} no contiene texto indexable.")
                
    # Unimos todas las páginas en un único bloque de texto separado por saltos de línea
    return "\n\n".join(texto_completo).strip()