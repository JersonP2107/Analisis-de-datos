import argparse
import pandas as pd
import requests


def descargar_datos_desde_url(url):
    # Descargar los datos desde la URL
    response = requests.get(url)

    if response.status_code == 200:
        # Crear un DataFrame a partir de los datos descargados
        df = pd.read_csv(url)
        return df
    else:
        print(f"Error al descargar datos desde la URL: {response.status_code}")
        return None


def categorizar_datos(df):
    return df


def exportar_a_csv(df, nombre_archivo):
    # Exportar el DataFrame a un archivo CSV
    df.to_csv(nombre_archivo, index=False)


if __name__ == "__main__":
    # Configurar los argumentos de la línea de comandos
    parser = argparse.ArgumentParser(description="Proyecto Integrador Script")
    parser.add_argument("url", help="URL de los datos a descargar")
    parser.add_argument("archivo_csv", help="Nombre del archivo CSV de salida")

    args = parser.parse_args()

    # Descargar datos desde la URL
    df = descargar_datos_desde_url(args.url)

    if df is not None:
        # Categorizar los datos
        df_categorizado = categorizar_datos(df)

        # Exportar a CSV
        exportar_a_csv(df_categorizado, args.archivo_csv)
        print(f"Datos exportados a {args.archivo_csv}")
