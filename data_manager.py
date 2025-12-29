import pandas as pd
from datetime import datetime
import os

def limpiar_precio(precio_sucio):
    """
    Convierte 'S/ 14.50' (texto) a 14.50 (número decimal).
    """
    if not precio_sucio: return 0.0
    # Quitamos símbolos de moneda y espacios
    limpio = precio_sucio.replace('S/', '').replace('s/', '').replace(',', '').strip()
    try:
        return float(limpio)
    except ValueError:
        return 0.0
def guardar_en_csv(datos_fila):
    """
    Recibe un diccionario y lo guarda en 'historico_canasta.csv'.
    Usa mode='a' (append) para no borrar los datos anteriores.
    """
    archivo = 'historico_canasta.csv'
    df_nuevo = pd.DataFrame([datos_fila])
    # Si el archivo no existe, escribimos con cabecera. Si existe, sin cabecera.
    if not os.path.isfile(archivo):
        df_nuevo.to_csv(archivo, index=False, encoding='utf-8')
    else:
        df_nuevo.to_csv(archivo, mode='a', header=False, index=False, encoding='utf-8')
    print(f" [OK] ✅ Datos guardados exitosamente en {archivo}")