import numpy as np
from sklearn.linear_model import LinearRegression
import random

def predecir_futuro(precio_actual_soles, valor_dolar_hoy):
    
    # 1. SIMULACIÓN DE DATOS 
    dolares_historicos = []
    precios_historicos = []
    precio_base_dolar = precio_actual_soles / valor_dolar_hoy
    
    for _ in range(30):
        dolar_sim = random.uniform(3.60, 3.90)
        dolares_historicos.append([dolar_sim])
        ruido = random.uniform(-0.5, 0.5) 
        precio_sim = (precio_base_dolar * dolar_sim) + ruido
        precios_historicos.append(precio_sim)

    # 2. ENTRENAMIENTO
    modelo = LinearRegression()
    modelo.fit(dolares_historicos, precios_historicos)
    
    # 3. PREDICCIÓN
    variacion_dolar = random.choice([-0.05, 0.05, 0.00]) 
    dolar_futuro = np.array([[valor_dolar_hoy + variacion_dolar]]) 
    precio_predicho = modelo.predict(dolar_futuro)[0]
    
    diferencia = precio_predicho - precio_actual_soles
    
    # 4. GENERACIÓN DE MENSAJES 
    productos_clave = ["el Aceite", "el Pollo", "los Huevos", "el Arroz"]
    producto_random = random.choice(productos_clave)

    if diferencia > 0.10:
        tendencia = "Subirá 📈"
        mensaje = f"¡Alerta! El modelo detecta presión en el tipo de cambio. {producto_random} podría subir de precio mañana. ¡Compra hoy!"
        color = "danger" # Rojo
    elif diferencia < -0.10:
        tendencia = "Bajará 📉"
        mensaje = f"Buenas noticias. La tendencia indica una baja en {producto_random}. Si puedes, espera a mañana para hacer mercado."
        color = "success" # Verde
    else:
        tendencia = "Estable ⚖️"
        mensaje = f"El mercado está tranquilo. Es el momento perfecto para comprar {producto_random} y abarrotes antes de la próxima subida."
        color = "primary" # Azul 
        
    return {
        "prediccion": round(precio_predicho, 2),
        "tendencia": tendencia,
        "mensaje": mensaje,
        "color": color
    }