from api_data import tipo_de_cambio_actual
from data_manager import guardar_datos
from scraper import scraper_tottus
from datetime import datetime

# URLs de productos a monitorear (canasta piloto)
PRODUCTOS_TOTTUS = [
    "https://www.tottus.com.pe/tottus-pe/articulo/122585079/leche-laive-light-sin-lactosa-botella-390-g/122585081",
    # Puedes agregar más productos aquí
]

def ejecutar_sistema():
    print("============================================================")
    print("INICIANDO SISTEMA INFO-CANASTA")
    print(f" Fecha y hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("============================================================")

    # 1. Obtener tipo de cambio desde la API del BCRP
    tc = tipo_de_cambio_actual()
    print(f"Tipo de cambio usado: S/ {tc}")
    print("------------------------------------------------------------")

    # 2. Scraping de productos
    for url in PRODUCTOS_TOTTUS:
        resultado = scraper_tottus(url)

        if resultado:
            producto = resultado["producto"]
            # Convertimos el precio numérico a texto para data_manager
            precio_texto = f"S/ {resultado['precio']}"

            # 3. Guardar datos en CSV
            guardar_datos(producto, precio_texto, tc)
        else:
            print(" No se pudo procesar el producto.")

    print("============================================================")
    print("EJECUCIÓN FINALIZADA. DATOS ACTUALIZADOS.")
    print("============================================================")

if __name__ == "__main__":
    ejecutar_sistema()
