from api_data import tipo_de_cambio_actual
from data_manager import guardar_datos
from scraper import scraper_tottus
from datetime import datetime
import visual  

# URLs de productos a monitorear (canasta piloto)
PRODUCTOS_TOTTUS = [
    "https://www.tottus.com.pe/tottus-pe/articulo/144942887/Leche%20UHT%20Entera%20Gloria%20Caja%20946%20mL/144942888",
    "https://www.tottus.com.pe/tottus-pe/articulo/113706444/aceite-vegetalprimor-900-ml/113706446",
    "https://www.tottus.com.pe/tottus-pe/articulo/113707060/arroz-extra-faraon-5-kg/113707061",
    "https://www.tottus.com.pe/tottus-pe/articulo/113927690/huevos-pardos-tottus-bandeja-15-und/113927691",
    "https://www.tottus.com.pe/tottus-pe/articulo/117026658/pollo-fresco-con-menudencia-x-kg/117026659",
    "https://www.tottus.com.pe/tottus-pe/articulo/115830731/limon-sutil-tottus/115830732"
]

def ejecutar_sistema():
    print("============================================================")
    print("INICIANDO SISTEMA INFO-CANASTA")
    print(f" Fecha y hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("============================================================")

    # 1. Obtener tipo de cambio desde la API del BCRP
    try:
        tc = tipo_de_cambio_actual()
        print(f"Tipo de cambio usado: S/ {tc}")
    except:
        tc = 3.75 # Valor por defecto si la API falla
        print("⚠️ Advertencia: Usando T.C. por defecto (3.75)")
        
    print("------------------------------------------------------------")

    # 2. Scraping de productos
    datos_nuevos = False # Bandera para saber si hubo cambios
    
    for url in PRODUCTOS_TOTTUS:
        resultado = scraper_tottus(url)

        if resultado:
            producto = resultado["producto"]
            # Tu scraper ya devuelve el float, lo convertimos para mostrarlo
            precio_texto = f"S/ {resultado['precio']}"

            # 3. Guardar datos en CSV
            guardar_datos(producto, precio_texto, tc)
            datos_nuevos = True
        else:
            print(" No se pudo procesar el producto.")

    print("============================================================")
    
    # 4. [NUEVO] Generar el Reporte Visual HTML
    if datos_nuevos:
        print("🎨 Generando página web actualizada...")
        visual.generar_html() # <--- Aquí Python crea el archivo index.html
    else:
        print("⚠️ No hubo datos nuevos para actualizar el reporte.")

    print("EJECUCIÓN FINALIZADA. DATOS ACTUALIZADOS.")
    print("============================================================")

if __name__ == "__main__":
    ejecutar_sistema()