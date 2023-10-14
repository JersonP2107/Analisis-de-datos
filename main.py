import numpy as np
from datasets import load_dataset

# Cargar el conjunto de datos
heart_failure = load_dataset("mstz/heart_failure")
train_data = heart_failure["train"]

# Extraer las edades de los pacientes
ages = train_data['age']

# Convertir las edades en un arreglo de numpy
ages_np = np.array(ages)

# Calcular el promedio de las edades
average_age = np.mean(ages_np)

# Imprimir el resultado usando un f-string
print(f"El promedio de edad de los pacientes es: {average_age:.2f}")
