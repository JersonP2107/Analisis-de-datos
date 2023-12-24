import pandas as pd
import matplotlib.pyplot as plt

# Descargar el conjunto de datos
# Descargar el conjunto de datos
url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
df = pd.read_csv(url)

# Crear una lista con las condiciones que quieres graficar
condiciones = ["anaemia", "diabetes", "smoking", "DEATH_EVENT"]

# Crear una figura con subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

for i, condicion in enumerate(condiciones):
    # Calcular la distribución de cada condición
    distribucion = df[condicion].value_counts()

    # Crear una gráfica de torta en el subplot correspondiente
    axs[i // 2, i % 2].pie(distribucion, labels=["No", "Sí"], autopct="%1.1f%%")
    axs[i // 2, i % 2].set_title(f"Distribución de {condicion}")

# Mostrar la figura con todas las gráficas de torta
plt.tight_layout()
plt.show()
