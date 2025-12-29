from api_data import tipo_de_cambio_actual
from data_manager import guardar_datos, reiniciar_archivo
from scraper import scraper_tottus 
from datetime import datetime
import visual  

# URLs de productos a monitorear
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
    
    # 0. Limpieza del archivo antiguo
    try:
        reiniciar_archivo()
    except Exception as e:
        print(f" ⚠️ No se pudo reiniciar el archivo ⚠️: {e}")
    
    # 1. Obtener tipo de cambio desde la API del BCRP 
    try:
        tc = tipo_de_cambio_actual()
        print(f"💵 Tipo de cambio BCRP usado: S/ {tc}")
    except Exception as e:
        print(f"⚠️ Advertencia: Usando T.C. por defecto (3.75) - {e}")
        
    print("------------------------------------------------------------")

    # 2. Scraping de productos
    datos_nuevos = False 
    
    for url in PRODUCTOS_TOTTUS:
        try:
            resultado = scraper_tottus(url)

            if resultado:
                producto = resultado["producto"]
                precio_texto = f"S/ {resultado['precio']}"

                # 3. Guardar datos en CSV
                guardar_datos(producto, precio_texto, tc)
                datos_nuevos = True
            else:
                print(f"⚠️ No se pudo procesar el link...")
        except Exception as e:
             print(f"❌ Error en scraping: {e}")

    print("============================================================")
    
    # 4. Generar el Reporte Visual HTML 
    if datos_nuevos:
        print("🎨 Generando página web actualizada...")
        visual.generar_html() 
    else:
        print("⚠️ No hubo datos nuevos para actualizar el reporte.")

    print("EJECUCIÓN FINALIZADA.")
    print("============================================================")

if __name__ == "__main__":
    ejecutar_sistema()