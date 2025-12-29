import matplotlib.pyplot as plt
import pandas as pd

print(">>> EJECUTANDO visual.py NUEVO <<<")

def graficar_precios():
    df = pd.read_csv("datos_productos.csv")

    print("Datos leídos:")
    print(df)

    # Usar fechas como texto (NO datetime)
    fechas = df['Fecha'].astype(str)
    precios = df['Precio soles']

    plt.figure(figsize=(7, 5))

    # BARRAS ROJAS (para que no haya duda)
    plt.bar(fechas, precios, color='red')

    for i, v in enumerate(precios):
        plt.text(i, v + 0.03, f"S/ {v:.2f}", ha='center', fontweight='bold')

    plt.title("PRECIO DEL PRODUCTO - INFO CANASTA", fontweight='bold')
    plt.xlabel("Fecha")
    plt.ylabel("Precio (S/)")
    plt.grid(axis='y')

    plt.tight_layout()

    plt.savefig("grafico_precios.png")
    print(">>> IMAGEN GUARDADA <<<")

    plt.show()

if __name__ == "__main__":
    graficar_precios()
