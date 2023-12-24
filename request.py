import requests
import pandas as pd


def descargar_datos_csv(url, archivo_destino):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(archivo_destino, "wb") as archivo:
            archivo.write(response.content)

        print(f"Los datos se han descargado y guardado en {archivo_destino}")

        # Leer el archivo CSV descargado y llamar a la función para limpiar y preparar los datos
        df = pd.read_csv(archivo_destino)
        df = limpiar_y_preparar_datos(df)

        return df
    except requests.HTTPError as e:
        print(f"Error al descargar los datos: {e}")
    except requests.ConnectionError as e:
        print(f"Error de conexión: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def limpiar_y_preparar_datos(df):
    # Verificar valores faltantes
    if df.isnull().values.any():
        print("Existen valores faltantes en el DataFrame.")
        df.dropna(inplace=True)

    # Verificar filas repetidas
    filas_repetidas = df.duplicated().sum()
    if filas_repetidas > 0:
        print(f"Existen {filas_repetidas} filas repetidas en el DataFrame.")
        df.drop_duplicates(keep="first", inplace=True)

    # Filtrar valores atípicos de la columna 'edad'
    df = df[(df["edad"] >= 0) & (df["edad"] <= 100)]

    # Crear una columna 'categoria_edad'
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

    return df


# Llamar a la función para descargar y limpiar los datos
url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
archivo_destino = "heart_failure_dataset.csv"
datos_limpios = descargar_datos_csv(url, archivo_destino)
