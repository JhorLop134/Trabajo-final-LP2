import matplotlib
matplotlib.use("TkAgg")

import pandas as pd
import matplotlib.pyplot as plt

def graficar_precios():
    df = pd.read_csv("datos_productos.csv")

    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')

    print("Datos cargados correctamente:")
    print(df)

    plt.figure()
    plt.plot(df['Fecha'], df['Precio soles'], marker='o')
    plt.xlabel("Fecha")
    plt.ylabel("Precio (S/)")
    plt.title("Evolución del precio - Info Canasta")
    plt.grid(True)

    plt.show(block=True)
    input("Presiona ENTER para cerrar el gráfico...")

if __name__ == "__main__":
    graficar_precios()
