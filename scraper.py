import requests
from bs4 import BeautifulSoup
import random

def obtener_precio_producto(url_producto):
    """
    URL de PlazaVea para extraer el nombre y precio actual.
    """
    
    # 1. Configuración anti-bloqueo (User-Agents rotativos)
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
    ]
    
    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept-Language': 'es-ES,es;q=0.9',
    }

    print(f"   Searching... 🔎 Conectando con PlazaVea...")

    try:
        # Usamos la variable 'url_producto', NO un link fijo
        response = requests.get(url_producto, headers=headers, timeout=10)
        
        if response.status_code == 200:
            return "Conexión Exitosa" # Temporalmente solo probamos conexión
        else:
            print(f"   [ERROR] La web respondió con código: {response.status_code}")
            return None

    except Exception as e:
        print(f"   [CRITICAL] Error en scraping: {e}")
        return None