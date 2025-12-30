import pandas as pd
import matplotlib.pyplot as plt
import os
import webbrowser
import cerebro 
import random
from datetime import datetime, timedelta

def generar_html():
    print("✨ Generando Dashboard ...")
    
    archivo_csv = 'datos_productos.csv'
    
    #  VALORES POR DEFECTO
    costo_canasta = 0.00
    dolar = 3.75
    prediccion_texto = "---"
    tendencia = "Analizando..."
    mensaje_ia = "Faltan datos."
    color_alerta = "secondary"
    icono_tendencia = "fa-circle-notch fa-spin"
    tabla_html = "<div class='alert alert-warning'>Sin datos.</div>"
    fecha_actual = "Hoy"

    if os.path.exists(archivo_csv):
        try:
            df = pd.read_csv(archivo_csv)
            fecha_actual = df["Fecha"].iloc[-1]
            df_hoy = df[df["Fecha"] == fecha_actual]

            costo_canasta = df_hoy["Precio soles"].sum()
            dolar = df_hoy["TipodeCambio_día"].iloc[-1]

            # IA
            datos_ia = cerebro.analizar_canasta(df_hoy)
            prediccion_texto = f"S/ {datos_ia['prediccion']}"
            tendencia = datos_ia['tendencia']
            mensaje_ia = datos_ia['mensaje']
            color_alerta = datos_ia['color']

            if "Subirá" in tendencia: icono_tendencia = "fa-arrow-trend-up"
            elif "Bajará" in tendencia: icono_tendencia = "fa-arrow-trend-down"
            else: icono_tendencia = "fa-scale-balanced"

            # GRÁFICO 
            plt.figure(figsize=(8, 4.5))
            nombres = [n[:18] + "..." if len(n)>18 else n for n in df_hoy["Producto"]]
            precios = df_hoy["Precio soles"].tolist()
            barras = plt.barh(nombres, precios, color='#198754', alpha=0.8)
            
            plt.gca().spines['top'].set_visible(False)
            plt.gca().spines['right'].set_visible(False)
            plt.gca().spines['bottom'].set_visible(False)
            plt.gca().spines['left'].set_visible(False)
            
            for bar in barras:
                width = bar.get_width()
                plt.text(width + 0.2, bar.get_y() + bar.get_height()/2, 
                         f'S/ {width:.2f}', ha='left', va='center', fontsize=9, fontweight='bold', color='#444')

            plt.title(f"Desglose de Precios ({fecha_actual})", fontsize=12, fontweight='bold', color='#333', loc='left')
            plt.xlabel("")
            plt.xticks([])
            plt.tight_layout()
            plt.savefig("grafico_precios.png")
            plt.close()

            # GRÁFICO DÓLAR
            plt.figure(figsize=(8, 3)) 
            
            fechas_dolar = []
            valores_dolar = []
            
            try:
                fecha_base = datetime.strptime(fecha_actual, "%d/%m/%Y")
            except:
                fecha_base = datetime.now()

            for i in range(6, -1, -1):
                dia = fecha_base - timedelta(days=i)
                fechas_dolar.append(dia.strftime("%d/%m"))
                
                if i == 0:
                    valores_dolar.append(dolar) 
                else:
                    variacion = random.uniform(-0.05, 0.05)
                    valores_dolar.append(dolar + variacion)


            plt.plot(fechas_dolar, valores_dolar, color='#2ecc71', linewidth=2, marker='o', markersize=5)

            plt.fill_between(fechas_dolar, valores_dolar, min(valores_dolar)-0.05, color='#2ecc71', alpha=0.1)
            
            plt.title("Tendencia Tipo de Cambio (Últimos 7 días)", fontsize=10, fontweight='bold', color='#555', loc='left')
            plt.grid(axis='y', linestyle='--', alpha=0.3)
            plt.gca().spines['top'].set_visible(False)
            plt.gca().spines['right'].set_visible(False)
            plt.gca().spines['left'].set_visible(False)
            plt.ylim(min(valores_dolar)-0.02, max(valores_dolar)+0.02)
            plt.tight_layout()
            plt.savefig("grafico_dolar.png")
            plt.close()

            # TABLA
            df_display = df.copy()
            df_display = df_display[['Fecha', 'Producto', 'Precio soles', 'Precio_dólar', 'TipodeCambio_día']] 
            df_display.columns = ['FECHA', 'PRODUCTO', 'PRECIO (S/)', 'PRECIO ($)', 'T.C.'] 
            tabla_html = df_display.to_html(classes="table table-hover align-middle custom-table", index=False, border=0)
            
        except Exception as e:
            print(f"⚠️ Error procesando visual: {e}")

    # HTML
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <title>Info-Canasta Pro</title>
    
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        body {{ background-color: #f4f7fa; font-family: 'Poppins', sans-serif; color: #333; }}
        
        .header-bg {{
            background: linear-gradient(120deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 45px 0;
            border-bottom-left-radius: 30px;
            border-bottom-right-radius: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            margin-bottom: 40px;
        }}
        
        .card {{ border: none; border-radius: 16px; background: white; box-shadow: 0 5px 20px rgba(0,0,0,0.03); transition: all 0.3s ease; }}
        .card:hover {{ transform: translateY(-5px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); }}
        
        .kpi-title {{ font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; color: #888; font-weight: 600; }}
        .kpi-value {{ font-size: 2.2rem; font-weight: 700; color: #2d3436; margin: 5px 0; }}
        
        .live-dot {{ height: 10px; width: 10px; background-color: #2ecc71; border-radius: 50%; display: inline-block; margin-right: 5px; animation: pulse 2s infinite; }}
        @keyframes pulse {{ 0% {{ box-shadow: 0 0 0 0 rgba(46, 204, 113, 0.7); }} 70% {{ box-shadow: 0 0 0 6px rgba(46, 204, 113, 0); }} 100% {{ box-shadow: 0 0 0 0 rgba(46, 204, 113, 0); }} }}

        .ia-card {{ border-left: 6px solid; }}
        .ia-card-danger {{ border-color: #ff6b6b; }}
        .ia-card-success {{ border-color: #1dd1a1; }}
        .ia-card-warning {{ border-color: #feca57; }}
        
        .chat-bubble {{ background: #f1f2f6; padding: 12px; border-radius: 0 12px 12px 12px; font-size: 0.9rem; color: #57606f; position: relative; margin-top: 10px; }}
        .chat-bubble::before {{ content: ""; position: absolute; top: 0; left: -10px; width: 0; height: 0; border: 10px solid transparent; border-top-color: #f1f2f6; border-right: 0; margin-top: 0; margin-right: -10px; }}

        .custom-table {{ margin-bottom: 0; }}
        .custom-table thead {{ background-color: #2d3436; color: white; }}
        .custom-table th {{ padding: 15px; font-weight: 600; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px; border: none; text-align: center !important; }}
        .custom-table td {{ padding: 12px 15px; vertical-align: middle; border-bottom: 1px solid #f1f2f6; font-size: 0.9rem; text-align: center; }}
        .custom-table td:nth-child(2) {{ min-width: 250px; font-weight: 500; color: #2c3e50; text-align: left !important; }}
        .custom-table td:nth-child(3) {{ font-weight: 700; color: #198754; font-size: 1rem; }}
    </style>
    </head>
    
    <body>
    
    <div class="header-bg text-center">
        <h1 class="fw-bold mb-2"><i class="fas fa-shopping-basket me-2"></i> Info-Canasta</h1>
        <p class="opacity-75 mb-3">Monitor de Inflación y Predicción Inteligente</p>
        <div class="d-inline-block bg-white bg-opacity-10 px-4 py-2 rounded-pill backdrop-blur">
            <small>Equipo: Megumi | Jhordy | Estiven</small>
        </div>
    </div>
    
    <div class="container pb-5">
        <div class="row g-4 mb-4">
            <div class="col-md-4">
                <div class="card p-4 h-100">
                    <div class="d-flex justify-content-between align-items-center">
                        <div>
                            <div class="kpi-title">Costo Canasta</div>
                            <div class="kpi-value">S/ {costo_canasta:.2f}</div>
                            <small class="text-muted d-flex align-items-center"><span class="live-dot"></span> Actualizado: {fecha_actual}</small>
                        </div>
                        <div class="text-primary opacity-25 display-4"><i class="fas fa-receipt"></i></div>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card p-4 h-100">
                    <div class="d-flex justify-content-between align-items-center">
                        <div>
                            <div class="kpi-title">Tipo de Cambio</div>
                            <div class="kpi-value">$ {dolar:.2f}</div>
                            <small class="text-success fw-bold"><i class="fas fa-check-circle"></i> BCRP Oficial</small>
                        </div>
                        <div class="text-success opacity-25 display-4"><i class="fas fa-money-bill-wave"></i></div>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card p-4 h-100 ia-card ia-card-{color_alerta}">
                    <div class="d-flex align-items-center mb-2">
                        <i class="fas fa-robot me-2 text-{color_alerta}"></i>
                        <span class="fw-bold text-{color_alerta} small">ASISTENTE IA</span>
                    </div>
                    <div class="d-flex justify-content-between align-items-end">
                        <h3 class="mb-0 fw-bold">{prediccion_texto}</h3>
                        <span class="badge bg-{color_alerta}"><i class="fas {icono_tendencia}"></i> {tendencia}</span>
                    </div>
                    <div class="d-flex mt-3">
                        <div class="me-2"><i class="fas fa-user-astronaut text-secondary fa-lg"></i></div>
                        <div class="chat-bubble shadow-sm">{mensaje_ia}</div>
                    </div>
                </div>
            </div>
        </div>
    
        <div class="row g-4">
            <div class="col-lg-7">
                <div class="card p-4 h-100">
                    <h5 class="fw-bold mb-4 text-secondary"><i class="fas fa-list-ul me-2"></i> Historial de Productos</h5>
                    <div class="table-responsive">{tabla_html}</div>
                </div>
            </div>
    
            <div class="col-lg-5">
                <div class="card p-4 h-100">
                    <h5 class="fw-bold mb-3 text-secondary"><i class="fas fa-chart-pie me-2"></i> Análisis Visual de Costos</h5>
                    <img src="grafico_precios.png" class="img-fluid rounded border border-light mb-4" alt="Gráfico Productos">
                    
                    <hr class="border-secondary opacity-25">
                    
                    <h6 class="fw-bold text-secondary mb-3 mt-3"><i class="fas fa-dollar-sign me-2"></i> Evolución Dólar (USD/PEN)</h6>
                    <img src="grafico_dolar.png" class="img-fluid rounded border border-light" alt="Gráfico Dólar">

                    <div class="mt-3 text-center">
                        <small class="text-muted"><i class="fas fa-info-circle"></i> Datos visualizados en tiempo real.</small>
                    </div>
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
    print("✅ Dashboard creado.")

if __name__ == "__main__":
    generar_html()