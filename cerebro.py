import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import random
from datetime import datetime

def analizar_canasta(df_hoy):
    """
    """
    
    dolar_hoy = df_hoy['TipodeCambio_día'].iloc[-1]
    
    # 1. SELECCIÓN ALEATORIA DEL PRODUCTO
    productos_candidatos = []
    palabras_clave = ['Aceite', 'Pollo', 'Arroz', 'Limón', 'Leche', 'Huevos', 'Azúcar']
    
    for _, row in df_hoy.iterrows():
        nombre_prod = row['Producto']
        for clave in palabras_clave:
            if clave in nombre_prod:
                productos_candidatos.append({
                    'nombre_largo': nombre_prod,
                    'precio': row['Precio soles'],
                    'corto': clave
                })
                break
    
    if productos_candidatos:
        elegido = random.choice(productos_candidatos)
        producto_corto = elegido['corto']
        precio_actual = elegido['precio']
    else:
        producto_corto = "Producto"
        precio_actual = df_hoy['Precio soles'].iloc[0]

    # 2. ENTRENAMIENTO (SIMULACIÓN DE TENDENCIA) 
    historial_dolar = []
    historial_precio = []
    
    precio_base_dolar = precio_actual / dolar_hoy
    
    # Detectamos si es Diciembre/Enero para activar el "Modo Año Nuevo"
    mes_actual = datetime.now().month
    factor_festivo = 0.00
    if mes_actual == 12 or mes_actual == 1:
        factor_festivo = 0.05 # 5% de inflación por fiestas
    
    # Generamos historia
    for _ in range(30):
        dolar_sim = random.uniform(3.60, 3.85)
        historial_dolar.append([dolar_sim])
        
        ruido = random.uniform(-0.2, 0.2)
        precio_sim = (precio_base_dolar * dolar_sim) + ruido
        historial_precio.append(precio_sim)

    # Entrenamos Modelo
    modelo = LinearRegression()
    modelo.fit(historial_dolar, historial_precio)
    
    # 3. PREDICCIÓN 
    
    tendencia_dolar = random.choice([-0.02, 0.02, 0.05])
    dolar_futuro = dolar_hoy + tendencia_dolar
    
    precio_predicho_base = modelo.predict([[dolar_futuro]])[0]
    
    # APLICAMOS EL FACTOR FIESTAS:
    precio_final_predicho = precio_predicho_base * (1 + factor_festivo)
    
    # 4. MENSAJE 
    diferencia = precio_final_predicho - precio_actual
    
    # Umbral de sensibilidad (S/ 0.10)
    if diferencia > 0.10:
        tendencia = "Subirá 📈"
        if factor_festivo > 0:
            mensaje = f"Por <b>campaña de Año Nuevo</b> y la tendencia del dólar, el <b>{producto_corto}</b> subirá a <b>S/ {precio_final_predicho:.2f}</b>. ¡Compra hoy!"
        else:
            mensaje = f"El modelo detecta una subida en el dólar. El <b>{producto_corto}</b> podría subir a <b>S/ {precio_final_predicho:.2f}</b> mañana."
        color = "danger"
        
    elif diferencia < -0.10:
        tendencia = "Bajará 📉"
        mensaje = f"Buenas noticias: El tipo de cambio favorece la baja del <b>{producto_corto}</b> a <b>S/ {precio_final_predicho:.2f}</b>. ¡Espera un poco!"
        color = "success"
        
    else:
        tendencia = "Estable ⚖️"
        mensaje = f"El mercado del <b>{producto_corto}</b> se mantiene estable en <b>S/ {precio_final_predicho:.2f}</b> a pesar de las fiestas."
        color = "warning"

    total_canasta = df_hoy['Precio soles'].sum() + diferencia

    return {
        "prediccion": round(total_canasta, 2),
        "tendencia": tendencia,
        "mensaje": mensaje,
        "color": color
    }