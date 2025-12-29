import pandas as pd
import matplotlib.pyplot as plt
import os
import webbrowser
import cerebro

def generar_html():
<<<<<<< Updated upstream
    archivo_csv = "datos_productos.csv"
=======
    print("🎨 Diseñando...")
    
    archivo_csv = 'datos_productos.csv'
    
    # Valores por defecto
    costo_canasta = 0.00
    prediccion_texto = "---"
    tendencia = "..."
    mensaje_ia = "Faltan datos."
    color_alerta = "secondary"
    icono_tendencia = "fa-minus"
    tabla_html = ""
>>>>>>> Stashed changes

    if not os.path.exists(archivo_csv):
        print("❌ No existe datos_productos.csv")
        return

    df = pd.read_csv(archivo_csv)

    # === DATOS ACTUALES ===
    fecha_actual = df["Fecha"].iloc[-1]
    df_hoy = df[df["Fecha"] == fecha_actual]

    costo_canasta = df_hoy["Precio soles"].sum()
    dolar = df_hoy["TipodeCambio_día"].iloc[-1]

    # === IA ===
    datos_ia = cerebro.predecir_futuro(costo_canasta, dolar)

    # === GRÁFICO (SE REGENERA SIEMPRE) ===
    plt.figure(figsize=(6,4))
    plt.barh(df_hoy["Producto"], df_hoy["Precio soles"])
    plt.title("Precios actuales de la Canasta Básica")
    plt.xlabel("Precio (S/)")
    plt.tight_layout()
    plt.savefig("grafico_precios.png")
    plt.close()

    # === TABLA HTML ===
    tabla_html = df.to_html(
        classes="table table-hover table-bordered",
        index=False,
        border=0
    )

    # === HTML VERDE (MISMO DISEÑO QUE TENÍAS) ===
    html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Dashboard Info-Canasta</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<style>
body {{ background-color: #f0f2f5; font-family: 'Segoe UI', sans-serif; }}

.header-bg {{
background: linear-gradient(135deg, #0f9b0f 0%, #000000 100%);
color: white;
padding: 40px 0;
margin-bottom: 30px;
}}

.card {{
border-radius: 15px;
box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}}

.icon-box {{
font-size: 2.5rem;
color: #0f9b0f;
}}

.prediction-box {{
border-left: 5px solid #0d6efd;
background: #f0f8ff;
}}
</style>
</head>

<body>

<div class="header-bg text-center">
<h1><i class="fas fa-shopping-basket"></i> Proyecto Info-Canasta</h1>
<p>Sistema de Monitoreo de Precios y Predicción IA</p>
<small>Equipo: Megumi | Jhordy | Estiven</small>
</div>

<div class="container">

<div class="row mb-4">
<div class="col-md-4">
<div class="card p-3">
<h6>Costo Total Canasta</h6>
<h3>S/ {costo_canasta:.2f}</h3>
</div>
</div>

<div class="col-md-4">
<div class="card p-3">
<h6>Dólar Actual (BCRP)</h6>
<h3>$ {dolar}</h3>
</div>
</div>

<div class="col-md-4">
<div class="card p-3 prediction-box">
<h6>🤖 Predicción IA</h6>
<h3>S/ {datos_ia["prediccion"]}</h3>
<p>{datos_ia["mensaje"]}</p>
</div>
</div>
</div>

<div class="row">
<div class="col-lg-8">
<div class="card p-4">
<h4>Historial de Precios</h4>
{tabla_html}
</div>
</div>

<div class="col-lg-4">
<div class="card p-4">
<h4>Análisis Visual</h4>
<img src="grafico_precios.png" class="img-fluid rounded">
</div>
</div>
</div>

</div>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    webbrowser.open("file://" + os.path.realpath("index.html"))
    print("✅ Dashboard actualizado correctamente")
