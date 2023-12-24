from request import limpiar_y_preparar_datos
import requests
import pandas as pd
import argparse


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


def main():
    parser = argparse.ArgumentParser(
        description="Descargar y procesar datos desde una URL"
    )
    parser.add_argument("url", type=str, help="URL de los datos a procesar")
    parser.add_argument(
        "--archivo_destino",
        type=str,
        default="heart_failure_dataset.csv",
        help="Nombre del archivo de destino",
    )

    args = parser.parse_args()

    # Llamar a la función para descargar los datos desde la URL proporcionada
    descargar_datos_csv(args.url, args.archivo_destino)

    if __name__ == "__main__":
        main()
