import numpy as np
from datasets import load_dataset
import pandas as pd

# Cargar el conjunto de datos
heart_failure = load_dataset("mstz/heart_failure")
train_data = heart_failure["train"]

# Paso 1: Convertir el Dataset en un DataFrame
df = pd.DataFrame(train_data)

# Paso 2: Separar el DataFrame en dos DataFrames basados en el valor de "is_dead"
df_perecidos = df[df["is_dead"] == 1]
df_sobrevivientes = df[df["is_dead"] == 0]

# Paso 3: Calcular el promedio de edades para cada DataFrame
promedio_edades_perecidos = df_perecidos["age"].mean()
promedio_edades_sobrevivientes = df_sobrevivientes["age"].mean()

# Paso 4: Imprimir los promedios de edades
print("Promedio de edades de personas que perecieron:", promedio_edades_perecidos)
print(
    "Promedio de edades de personas que sobrevivieron:", promedio_edades_sobrevivientes
)

# Paso 5: Verificar tipos de datos en cada columna
tipos_de_datos = df.dtypes
print("Tipos de datos en el DataFrame:")
print(tipos_de_datos)

# Paso 6: Calcular la cantidad de hombres fumadores vs mujeres fumadoras
cantidad_hombres_fumadores = df[
    (df["gender"] == "Male") & (df["smoking"] == "Yes")
].shape[0]
cantidad_mujeres_fumadoras = df[
    (df["gender"] == "Female") & (df["smoking"] == "Yes")
].shape[0]

print("Cantidad de hombres fumadores:", cantidad_hombres_fumadores)
print("Cantidad de mujeres fumadoras:", cantidad_mujeres_fumadoras)
