import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import time

def scraper_tottus(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    print("\n" + "═"*60)
    print(f"🛒  BUSCANDO EN TOTTUS...") 
    print("═"*60)

    try:
        time.sleep(1) 
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # 1. NOMBRE
            h1 = soup.find('h1')
            nombre = h1.text.strip() if h1 else "Producto Tottus"

            # 2. PRECIO 
            precio_final = 0.0
            
            elementos_precio = soup.find_all(string=re.compile(r'S/\s*\d+\.\d+'))
            
            candidatos = []
            for texto in elementos_precio:
                match = re.search(r'(\d+\.\d+)', texto)
                if match:
                    valor = float(match.group(1))
                    candidatos.append(valor)

            if candidatos:
                precio_final = candidatos[0]

            # REPORTE
            ahora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            print(f"✅  DATOS DEL PRODUCTO")
            print(f"┌──────────────────────────────────────────────────────────┐")
            print(f"  📦 PRODUCTO: {nombre[:45]}")
            print(f"  💰 PRECIO:   S/ {precio_final:.2f}")
            print(f"  📅 FECHA:    {ahora}")
            print(f"└──────────────────────────────────────────────────────────┘")
            
            return {"producto": nombre, "precio": precio_final}
        
        else:
            print(f"❌ ERROR HTTP: {response.status_code}")
            return None

    except Exception as e:
        print(f"⚠️ ERROR: {e}")
        return None
    
    
# PRUEBAA
if __name__ == "__main__":
    link = "https://www.tottus.com.pe/tottus-pe/articulo/122585079/leche-laive-light-sin-lactosa-botella-390-g/122585081"
    scraper_tottus(link)