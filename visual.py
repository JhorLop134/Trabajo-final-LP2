import pandas as pd
import webbrowser
import os

def generar_html():
    print("🎨 Diseñando Dashboard...")
    
    # 1. PREPARAR LOS DATOS
    try:
        df = pd.read_csv('datos_productos.csv')
        
        precio_promedio = df['Precio soles'].mean()
        ultimo_dolar = df['TipodeCambio_día'].iloc[-1]
        total_productos = len(df)
        
        # SIMULACIÓN DE LA IA 
        prediccion_texto = "S/ 4.38"
        tendencia = "📉 Bajará levemente"
        mensaje_ia = "El modelo detecta una estabilidad en el tipo de cambio."
        
        tabla_html = df.to_html(classes='table table-hover table-bordered', index=False, border=0)
        
    except Exception as e:
        print(f"Error leyendo datos: {e}")
        tabla_html = "<div class='alert alert-danger'>No hay datos. Ejecuta main.py primero.</div>"
        precio_promedio = 0
        ultimo_dolar = 0
        prediccion_texto = "---"
        tendencia = "Esperando datos..."
        mensaje_ia = "Datos insuficientes para predecir."

    # 2. EL CÓDIGO HTML 
    contenido_web = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Dashboard Info-Canasta</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
            body {{ background-color: #f0f2f5; font-family: 'Segoe UI', sans-serif; }}
            .header-bg {{ background: linear-gradient(135deg, #0f9b0f 0%, #000000 100%); color: white; padding: 40px 0; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }}
            .card {{ border: none; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: transform 0.3s; }}
            .card:hover {{ transform: translateY(-5px); }}
            .icon-box {{ font-size: 2.5rem; color: #0f9b0f; }}
            .prediction-box {{ background: #e8f5e9; border-left: 5px solid #0f9b0f; }}
            .table-header {{ background-color: #2c3e50; color: white; }}
        </style>
    </head>
    <body>

        <div class="header-bg text-center">
            <h1><i class="fas fa-shopping-basket"></i> Proyecto Info-Canasta</h1>
            <p class="lead">Sistema de Monitoreo de Precios y Predicción IA</p>
            <small>Equipo: Megumi (Data) | Jhordy (API) | Estiven (Modelado)</small>
        </div>

        <div class="container">
            
            <div class="row mb-4">
                <div class="col-md-4">
                    <div class="card p-3">
                        <div class="d-flex justify-content-between align-items-center">
                            <div>
                                <h6 class="text-muted">Precio Promedio (Hoy)</h6>
                                <h3>S/ {precio_promedio:.2f}</h3>
                            </div>
                            <div class="icon-box"><i class="fas fa-tags"></i></div>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card p-3">
                        <div class="d-flex justify-content-between align-items-center">
                            <div>
                                <h6 class="text-muted">Dólar Actual (BCRP)</h6>
                                <h3>$ {ultimo_dolar:.2f}</h3>
                            </div>
                            <div class="icon-box"><i class="fas fa-money-bill-wave"></i></div>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card p-3 prediction-box">
                        <div class="d-flex justify-content-between align-items-center">
                            <div>
                                <h6 class="text-success fw-bold">🤖 Predicción IA (Mañana)</h6>
                                <h3>{prediccion_texto}</h3>
                                <small>{tendencia}</small>
                            </div>
                            <div class="icon-box"><i class="fas fa-robot"></i></div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-lg-8">
                    <div class="card p-4 mb-4">
                        <h4><i class="fas fa-list"></i> Historial de Precios</h4>
                        <hr>
                        <div class="table-responsive">
                            {tabla_html}
                        </div>
                    </div>
                </div>

                <div class="col-lg-4">
                    <div class="card p-4 mb-4">
                        <h4><i class="fas fa-chart-line"></i> Análisis Visual</h4>
                        <hr>
                        <img src='grafico_precios.png' class="img-fluid rounded" alt='Gráfico' onerror="this.src='https://via.placeholder.com/400x300?text=Gráfico+Pendiente'">
                        <br><br>
                        <div class="alert alert-info">
                            <strong><i class="fas fa-info-circle"></i> Insight del Modelo:</strong><br>
                            {mensaje_ia}
                        </div>
                    </div>
                </div>
            </div>

        </div> <footer class="text-center py-4 text-muted">
            <small>&copy; 2025 Universidad Agraria La Molina - Ingeniería Estadística e Informática</small>
        </footer>

    </body>
    </html>
    """

    # 3. GUARDAR Y ABRIR
    nombre_archivo = 'index.html'
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write(contenido_web)
    
    print(f"✅ ¡Dashboard Profesional creado!")
    ruta = 'file://' + os.path.realpath(nombre_archivo)
    webbrowser.open(ruta)

if __name__ == "__main__":
    generar_html()