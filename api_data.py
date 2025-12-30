import requests
from datetime import datetime, timedelta

URL_BASE = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD04640PD/json"

def tipo_de_cambio_actual():
    try:
        hoy = datetime.now()
        hace_una_semana = hoy - timedelta(days=7)
        
        url = f"{URL_BASE}/{hace_una_semana.strftime('%Y-%m-%d')}/{hoy.strftime('%Y-%m-%d')}"
        
        response = requests.get(url, timeout=5)
        datos = response.json()
        ultimo_dato = datos['periods'][-1]
        tipo_de_cambio = float(ultimo_dato['values'][0])

        print(f"💵 Dólar actual (BCRP): {tipo_de_cambio}")
        return tipo_de_cambio
    except Exception as e:
        print(f" Error obteniendo dólar actual: {e}")
        return 3.75 

def obtener_historial_dolar():

    fechas = []
    precios = []
    
    try:
        hoy = datetime.now()
        inicio = hoy - timedelta(days=10) 
        
        url = f"{URL_BASE}/{inicio.strftime('%Y-%m-%d')}/{hoy.strftime('%Y-%m-%d')}"
        
        response = requests.get(url, timeout=5)
        datos = response.json()
        
        if 'periods' in datos:
            for periodo in datos['periods']:
                fecha_raw = periodo['name'] 
                precio = float(periodo['values'][0])
                
                fechas.append(fecha_raw)
                precios.append(precio)
                
        
    except Exception as e:
        print(f"⚠️ Error en historial: {e}")
        
    return fechas, precios

# Prueba rápida
if __name__ == "__main__":
    tipo_de_cambio_actual()
    f, p = obtener_historial_dolar()
    print("Historial:", p)