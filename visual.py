import pandas as pd
import webbrowser  # Para abrir el navegador
import os          # Para encontrar la ruta del archivo

def generar_html():
    print("🔨 Construyendo página web...")
    
    # 1. LEER TUS DATOS (El CSV)
    try:
        df = pd.read_csv('datos_productos.csv')
        # Convertimos la tabla a HTML
        tabla_html = df.to_html(classes='estilo-tabla', index=False, border=0)
    except:
        tabla_html = "<p>⚠️ No hay datos todavía. ¡Ejecuta el scraper primero!</p>"

    # 2. DEFINIR EL CONTENIDO HTML (¡Esta es la parte que te faltaba!)
    contenido_web = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Info-Canasta: Reporte Final</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; background-color: #f4f4f9; }}
            h1 {{ color: #2c3e50; }}
            .card {{ background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }}
            .estilo-tabla {{ width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 16px; }}
            .estilo-tabla th {{ background-color: #009432; color: white; padding: 12px; text-align: left; }}
            .estilo-tabla td {{ border-bottom: 1px solid #ddd; padding: 12px; }}
            .estilo-tabla tr:hover {{ background-color: #f1f1f1; }}
            img {{ max-width: 100%; border-radius: 10px; margin-top: 20px; border: 1px solid #ddd; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🛒 Proyecto Info-Canasta</h1>
            <p><strong>Integrantes:</strong> Megumi, Jhordy, Estiven</p>
            <hr>
            
            <h2>📊 Precios Actuales (Tottus)</h2>
            {tabla_html}
            
            <h2>📈 Gráfico de Análisis</h2>
            <img src='grafico_precios.png' alt='Gráfico de Precios' onerror="this.style.display='none'">
            
            <br><br>
            <small><em>Reporte generado automáticamente por Python.</em></small>
        </div>
    </body>
    </html>
    """

    # 3. GUARDAR EL ARCHIVO
    nombre_archivo = 'index.html'
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(contenido_web) # Ahora sí existe la variable
        
        print(f"✅ ¡HTML creado correctamente en tu carpeta!")
        
        # 4. ABRIR AUTOMÁTICAMENTE
        ruta = 'file://' + os.path.realpath(nombre_archivo)
        webbrowser.open(ruta)
        print("🚀 Abriendo navegador...")
        
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")

# Esto permite probar visual.py solo, sin correr todo el main
if __name__ == "__main__":
    generar_html()