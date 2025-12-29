import pandas as pd
from datetime import datetime
import os

def limpiar_precio(precio_sucio):
    precio_limpio = precio_sucio.replace("S/", "").replace(",", "").strip()
    return float(precio_limpio)

def guardar_datos(producto, precio_texto, tc):
    precio_soles = limpiar_precio(precio_texto)
    precio_dolar = round(precio_soles / tc, 2)
    
    nueva_fila = {
        'Fecha': datetime.now().strftime('%d/%m/%Y'),
        'Producto': producto,
        'Precio soles': precio_soles,
        'Precio_dólar': precio_dolar,
        'TipodeCambio_día': tc
    }
    df = pd.DataFrame([nueva_fila])

    nombre_archivo = 'datos_productos.csv'
    if not os.path.isfile(nombre_archivo):
        df.to_csv(nombre_archivo, index= False, encoding= 'utf-8')
    else:
        df.to_csv(nombre_archivo, mode= 'a', index= False, header= False,
                  encoding= 'utf-8')
    print(f"Producto '{producto}' guardado correctamente")