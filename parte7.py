import pandas as pd
import matplotlib.pyplot as plt

# Descargar el conjunto de datos
url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
df = pd.read_csv(url)

# Graficar la distribución de edades con un histograma
plt.figure(figsize=(10, 6))
plt.hist(df["age"], bins=30, edgecolor="black")
plt.title("Distribución de Edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()

# Crear una lista con las condiciones que quieres graficar
condiciones = ["anaemia", "diabetes", "smoking", "DEATH_EVENT"]

for condicion in condiciones:
    # Graficar histogramas agrupados por hombre y mujer
    plt.figure(figsize=(10, 6))
    df[df["sex"] == 1][condicion].hist(
        alpha=0.5, bins=30, label="Hombre", edgecolor="black"
    )
    df[df["sex"] == 0][condicion].hist(
        alpha=0.5, bins=30, label="Mujer", edgecolor="black"
    )
    plt.title(f"Distribución de {condicion} por Sexo")
    plt.xlabel(condicion)
    plt.ylabel("Frecuencia")
    plt.legend()
    plt.show()
