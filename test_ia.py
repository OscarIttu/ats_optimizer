import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

print("--- INICIANDO TEST DE CONEXIÓN ---")
print(f"¿Existe la variable ANTHROPIC_API_KEY?: {'SÍ' if os.getenv('ANTHROPIC_API_KEY') else 'NO'}")

try:
    # Inicializamos el cliente forzando la URL oficial
    client = Anthropic(base_url="https://api.anthropic.com")
    
    # Intentamos una petición ultra simple
    print("Enviando mensaje de prueba a Claude...")
    respuesta = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=10,
        messages=[{"role": "user", "content": "Responde solo con la palabra OK"}]
    )
    print("\n¡CONEXIÓN EXITOSA!")
    print(f"Respuesta de Claude: {respuesta.content[0].text}")

except Exception as e:
    print("\n❌ LA CONEXIÓN HA FALLADO")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Mensaje de error: {str(e)}")