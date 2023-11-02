import requests
import pandas as pd


def descargar_datos_csv(url, archivo_destino):
    try:
        # Realizar una solicitud GET para descargar los datos
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la solicitud fue exitosa

        # Guardar la respuesta en un archivo CSV
        with open(archivo_destino, "wb") as archivo:
            archivo.write(response.content)

        print(f"Los datos se han descargado y guardado en {archivo_destino}")

        # Llamar a la función para limpiar y preparar los datos
        df = pd.read_csv(archivo_destino)
        limpiar_y_preparar_datos(df)
    except Exception as e:
        print(f"Ocurrió un error al descargar los datos: {str(e)}")


def limpiar_y_preparar_datos(df):
    # Verificar valores faltantes
    if df.isnull().values.any():
        print("Existen valores faltantes en el DataFrame.")
        df.dropna(inplace=True)  # Eliminar filas con valores faltantes

    # Verificar filas repetidas
    filas_repetidas = df.duplicated().sum()
    if filas_repetidas > 0:
        print(f"Existen {filas_repetidas} filas repetidas en el DataFrame.")
        df.drop_duplicates(keep="first", inplace=True)  # Eliminar filas duplicadas

    # Verificar y eliminar valores atípicos (puedes ajustar los criterios según tus necesidades)
    df = df[
        (df["edad"] >= 0) & (df["edad"] <= 100)
    ]  # Supongamos que la edad debe estar en el rango [0, 100]

    # Crear una columna que categorice por edades
    def categorizar_edades(edad):
        if edad <= 12:
            return "Niño"
        elif 13 <= edad <= 19:
            return "Adolescente"
        elif 20 <= edad <= 39:
            return "Jóvenes adulto"
        elif 40 <= edad <= 59:
            return "Adulto"
        else:
            return "Adulto mayor"

    df["categoria_edad"] = df["edad"].apply(categorizar_edades)

    # Guardar el resultado como un nuevo archivo CSV
    df.to_csv("datos_limpios.csv", index=False)

    print(
        "Limpieza y preparación de datos completada. Resultados guardados en 'datos_limpios.csv'."
    )


# Llamar a la función para descargar los datos desde la URL proporcionada
url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
archivo_destino = "heart_failure_dataset.csv"
descargar_datos_csv(url, archivo_destino)
