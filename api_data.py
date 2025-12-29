import requests

def tipo_de_cambio_actual():

    url = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD04640MD/json"

    try:
        response = requests.get(url)
        datos = response.json()
        ultimo_dato = datos['periods'][-1]
        tipo_de_cambio = float(ultimo_dato['values'][0])

        print(f"Tipo de cambio: {tipo_de_cambio}")
        return tipo_de_cambio
    except:
        print("No se obtuvo un tipo de cambio. Usaremos 3.75 por defecto")
        return 3.75
