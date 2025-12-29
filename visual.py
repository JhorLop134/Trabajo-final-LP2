import pandas as pd
import webbrowser
import os
import cerebro  

def generar_html():
    print("🎨 Restaurando diseño con Banner y Nombres...")
    
    archivo_csv = 'datos_productos.csv'
    
    # Valores por defecto
    costo_canasta = 0.00
    prediccion_texto = "---"
    tendencia = "..."
    mensaje_ia = "Faltan datos."
    color_alerta = "secondary"
    icono_tendencia = "fa-minus"
    tabla_html = ""

    try:
        if os.path.exists(archivo_csv):
            df = pd.read_csv(archivo_csv)
            
            # FILTRAR
            fecha_actual = df['Fecha'].iloc[-1]
            df_hoy = df[df['Fecha'] == fecha_actual]
            
            # CÁLCULOS
            costo_canasta = df_hoy['Precio soles'].sum()
            dolar_hoy = df['TipodeCambio_día'].iloc[-1]
            
            # IA INTELIGENTE
            datos_ia = cerebro.predecir_futuro(costo_canasta, dolar_hoy)
            prediccion_texto = f"S/ {datos_ia['prediccion']}"
            tendencia = datos_ia['tendencia']
            mensaje_ia = datos_ia['mensaje']
            color_alerta = datos_ia['color']
            
            # Icono según color
            if color_alerta == "danger": icono_tendencia = "fa-arrow-trend-up"
            elif color_alerta == "success": icono_tendencia = "fa-arrow-trend-down"
            else: icono_tendencia = "fa-scale-balanced"
            
            # Tabla
            tabla_html = df.to_html(classes='table table-hover table-bordered', index=False, border=0)

    except Exception as e:
        print(f"Error: {e}")

    # EL HTML CON EL BANNER Y LOS NOMBRES 
    contenido_web = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Dashboard Info-Canasta</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            body {{ background-color: #f0f2f5; font-family: 'Segoe UI', sans-serif; }}
            
            /* ESTE ES EL BANNER QUE QUERÍAS */
            .header-bg {{ 
                background: linear-gradient(135deg, #0f9b0f 0%, #000000 100%); 
                color: white; 
                padding: 40px 0; 
                margin-bottom: 30px; 
                box-shadow: 0 4px 15px rgba(0,0,0,0.2); 
            }}
            
            .card {{ border: none; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: transform 0.3s; }}
            .card:hover {{ transform: translateY(-5px); }}
            .icon-box {{ font-size: 2.5rem; color: #0f9b0f; }}
            
            /* TARJETA IA INTELIGENTE */
            .prediction-box {{ border-left: 5px solid; }}
            .prediction-box-danger {{ border-color: #dc3545; background: #fff5f5; }}
            .prediction-box-success {{ border-color: #198754; background: #f0fff4; }}
            .prediction-box-primary {{ border-color: #0d6efd; background: #f0f8ff; }}
            
            .mensaje-ia {{ font-style: italic; background: white; padding: 10px; border-radius: 8px; margin-top: 10px; border: 1px solid #ddd; }}
            .table-header {{ background-color: #2c3e50; color: white; }}
        </style>
    </head>
    <body>

        <div class="header-bg text-center">
            <h1><i class="fas fa-shopping-basket"></i> Proyecto Info-Canasta</h1>
            <p class="lead">Sistema de Monitoreo de Precios y Predicción IA</p>
            <small class="opacity-75">Equipo: Megumi (Data) | Jhordy (API) | Estiven (Modelado)</small>
        </div>

        <div class="container">
            
            <div class="row mb-4">
                <div class="col-md-4">
                    <div class="card p-3 h-100">
                        <div class="d-flex justify-content-between align-items-center">
                            <div>
                                <h6 class="text-muted">Costo Total Canasta</h6>
                                <h3>S/ {costo_canasta:.2f}</h3>
                            </div>
                            <div class="icon-box"><i class="fas fa-receipt"></i></div>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card p-3 h-100">
                        <div class="d-flex justify-content-between align-items-center">
                            <div>
                                <h6 class="text-muted">Dólar Actual (BCRP)</h6>
                                <h3>$ {dolar_hoy:.2f}</h3>
                            </div>
                            <div class="icon-box"><i class="fas fa-money-bill-wave"></i></div>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="card p-3 h-100 prediction-box prediction-box-{color_alerta}">
                        <div class="d-flex justify-content-between align-items-start">
                            <div>
                                <h6 class="text-{color_alerta} fw-bold">🤖 Predicción IA</h6>
                                <h3>{prediccion_texto}</h3>
                                <span class="badge bg-{color_alerta} mb-2">
                                    <i class="fas {icono_tendencia}"></i> {tendencia}
                                </span>
                            </div>
                            <div class="icon-box text-{color_alerta}"><i class="fas fa-robot"></i></div>
                        </div>
                        <div class="mensaje-ia text-muted small">
                            "{mensaje_ia}"
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
                        <div class="alert alert-info small">
                            <strong><i class="fas fa-info-circle"></i> Nota:</strong><br>
                            El modelo utiliza Regresión Lineal basada en la volatilidad del dólar.
                        </div>
                    </div>
                </div>
            </div>

            <footer class="text-center py-4 text-muted">
                <small>&copy; 2025 Universidad Agraria La Molina - Ingeniería Estadística e Informática</small>
            </footer>

        </div>
    </body>
    </html>
    """

    # 3. GUARDAR
    nombre_archivo = 'index.html'
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(contenido_web)
        
        print(f"✅ ¡Dashboard Original (Con Nombres) Restaurado!")
        ruta = 'file://' + os.path.realpath(nombre_archivo)
        webbrowser.open(ruta)
    except Exception as e:
        print(f"Error escribiendo archivo: {e}")

if __name__ == "__main__":
    generar_html()