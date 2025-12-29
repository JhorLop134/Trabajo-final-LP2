import pandas as pd
from datetime import datetime
import os

def limpiar_precio(precio_sucio):
    precio_limpio = precio_sucio.replace("S/", "").replace(",", "").strip()
    return float(precio_limpio)

