import requests
from datetime import datetime, timedelta

# CÓDIGO BCRP: PD04640PD = Tipo de Cambio Venta (El que se usa para costos)
URL_BASE = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD04640PD/json"

def tipo_de_cambio_actual():
    """
    Obtiene SOLO el último precio del dólar (para el número grande del Dashboard).
    """
    try:
        # Pedimos los últimos 7 días por si es fin de semana (el BCRP no publica sáb/dom)
        hoy = datetime.now()
        hace_una_semana = hoy - timedelta(days=7)
        
        # Armamos la URL con fechas para asegurar datos recientes
        url = f"{URL_BASE}/{hace_una_semana.strftime('%Y-%m-%d')}/{hoy.strftime('%Y-%m-%d')}"
        
        response = requests.get(url, timeout=5)
        datos = response.json()

        # Tomamos el último disponible
        ultimo_dato = datos['periods'][-1]
        tipo_de_cambio = float(ultimo_dato['values'][0])

        print(f"💵 Dólar actual (BCRP): {tipo_de_cambio}")
        return tipo_de_cambio
    except Exception as e:
        print(f"⚠️ Error obteniendo dólar actual: {e}")
        return 3.75 # Valor por defecto

def obtener_historial_dolar():
    """
    [NUEVA FUNCIÓN] 
    Descarga la lista de precios de los últimos 10 días para el gráfico.
    Retorna dos listas: Fechas y Precios.
    """
    fechas = []
    precios = []
    
    try:
        hoy = datetime.now()
        inicio = hoy - timedelta(days=10) # Pedimos 10 días atrás
        
        url = f"{URL_BASE}/{inicio.strftime('%Y-%m-%d')}/{hoy.strftime('%Y-%m-%d')}"
        
        response = requests.get(url, timeout=5)
        datos = response.json()
        
        if 'periods' in datos:
            for periodo in datos['periods']:
                # BCRP da la fecha como "27.Dic.23", la guardamos tal cual o la limpiamos
                fecha_raw = periodo['name'] 
                precio = float(periodo['values'][0])
                
                fechas.append(fecha_raw)
                precios.append(precio)
                
        print(f"✅ Historial descargado: {len(precios)} días encontrados.")
        
    except Exception as e:
        print(f"⚠️ Error en historial: {e}")
        # Si falla, devolvemos listas vacías (visual.py usará simulación)
        
    return fechas, precios

# Prueba rápida
if __name__ == "__main__":
    tipo_de_cambio_actual()
    f, p = obtener_historial_dolar()
    print("Historial:", p)