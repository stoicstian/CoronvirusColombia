import pandas as pd
# import numpy as np
# import seaborn as sns
import matplotlib.pyplot as plt
from os import path, system
from datetime import datetime


def data_default(nombre):
    if bool(nombre) is False:
        return "defecto.csv"
    else:
        return nombre + ".csv"


# RUTA DE LA CARPETA DONDE ESTA GUARDADA EL PROYECTO: CARPETA CORONAVIRUS
DIR_BASE = path.dirname(path.abspath(__file__))

# RUTA DE LA CARPETA DONDE ESTA GUARDADA LA DATA: CARPETA DATA
DIR_DATA = path.join(DIR_BASE, "data")

# CADENA DE TEXTO CON EL NOMBRE DEL DÍA A ANALIZAR
FILE_DATA_NAME = input(
    "Ingrese el nombre del archivo en el formato YYYY-MM-DD: ")

FILE_DATA_NAME = data_default(FILE_DATA_NAME)

# RUTA DEL ARCHIVO DATA A ANALIZAR
PATH_DATA_NAME = path.join(DIR_DATA, FILE_DATA_NAME)

FILE_RESULTADOS_NAME = path.join(
    DIR_BASE, "resultados/{}".format(FILE_DATA_NAME))


# CARGA DEL DATAFRAME DE DATOS A ANALIZAR
df = pd.read_csv(PATH_DATA_NAME)


# SEGÚN SEXO
casos_sexo = pd.DataFrame(df.groupby(by="Sexo").count()["ID de caso"])
casos_sexo.columns = ["Casos"]


# SEGÚN ORIGEN
casos_origen = pd.DataFrame(df.groupby(by="Tipo*").count()["ID de caso"])
casos_origen.columns = ["Casos"]


# TOP 10 PAISES CASOS IMPORTADOS A COLOMBIA.
casos_importados = pd.DataFrame(df.groupby(by="País de procedencia").count(
)["ID de caso"].sort_values(ascending=False).iloc[1:, ].head(10))
casos_importados.columns = ["Casos"]


# TOP CIUDADES CON MAS CASOS
casos_ciudades = pd.DataFrame(df.groupby(by="Ciudad de ubicación").count()[
    "ID de caso"].sort_values(ascending=False).head(10))
casos_ciudades.columns = ["Casos"]


# TOP DEPARTAMENTOS CON MÁS CASOS, INCLUYE CAPITAL
casos_departamentos = pd.DataFrame(df.groupby(by="Departamento").count()[
    "ID de caso"].sort_values(ascending=False).head(10))
casos_departamentos.columns = ["Casos"]

fecha = datetime.today()

# CREAR Y MODIFICA ARCHIVO TXT CON RESULTADOS

myfile = open(f"resultados/{FILE_DATA_NAME}", "w")
myfile.write("Datos Coronavirus Colombia\n")
myfile.write(f"Fecha (aaaa-mm-dd): {datetime.today().date()}\n")
myfile.write(f"Total casos: {len(df)}\n\n")
myfile.close()

casos_sexo.to_csv(FILE_RESULTADOS_NAME, sep=":", mode="a")

myfile = open(f"resultados/{FILE_DATA_NAME}", "a")
myfile.write("\n")
myfile.close()

casos_origen.to_csv(FILE_RESULTADOS_NAME, sep=":", mode="a")

myfile = open(f"resultados/{FILE_DATA_NAME}", "a")
myfile.write("\n")
myfile.write("TOP 10\n")
myfile.close()

casos_importados.to_csv(FILE_RESULTADOS_NAME, sep=":", mode="a")

myfile = open(f"resultados/{FILE_DATA_NAME}", "a")
myfile.write("\n")
myfile.write("TOP 10\n")
myfile.close()

casos_ciudades.to_csv(FILE_RESULTADOS_NAME, sep=":", mode="a")

myfile = open(f"resultados/{FILE_DATA_NAME}", "a")
myfile.write("\n")
myfile.seek(0,0)
myfile.write("(TOP 10 - Incluye Distrito Capital)\n")
myfile.close()

casos_departamentos.to_csv(FILE_RESULTADOS_NAME, sep=":", mode="+a")

myfile = open(f"resultados/{FILE_DATA_NAME}", "a")
