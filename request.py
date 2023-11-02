import requests


def descargar_datos_csv(url, archivo_destino):
    try:
        # Realizar una solicitud GET para descargar los datos
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la solicitud fue exitosa

        # Guardar la respuesta en un archivo CSV
        with open(archivo_destino, "wb") as archivo:
            archivo.write(response.content)

        print(f"Los datos se han descargado y guardado en {archivo_destino}")
    except Exception as e:
        print(f"Ocurrió un error al descargar los datos: {str(e)}")


# Llamar a la función para descargar los datos desde la URL proporcionada
url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
archivo_destino = "heart_failure_dataset.csv"
descargar_datos_csv(url, archivo_destino)
