#practica 1 - data cleaning
#es lo mismo que se hizon en el notebook pero resumido

import pandas as pd

def limpiar_datos():
    #importamos datos
    data = pd.read_csv("../datasets/vgsales.csv")
    #sustituimos datos que pueden ser nulos
    data.replace(["N/A", "unknown", ""], pd.NA, inplace=True)
    #dropemaos columna innecesaria
    data = data.drop(columns=["Rank"])
    #dropeamos juegos que se repiten
    data = data.drop_duplicates(subset="Name", keep="first")
    #nuevos nombres
    nuevos_nombres = {
        "Name": "Nombre",
        "Platform": "Plataforma",
        "Year": "Año",
        "Genre": "Género",
        "Publisher": "Publicador",
        "NA_Sales": "Ventas_Norteamérica",
        "EU_Sales": "Ventas_Europa",
        "JP_Sales": "Ventas_Japón",
        "Other_Sales": "Ventas_Otros",
        "Global_Sales": "Ventas_Globales"
    }
    # Renombrar columnas
    data = data.rename(columns=nuevos_nombres)
    #valor enteroa  anio 
    data["Año"] = data["Año"].astype("Int64")
    #dropeamos valores nulos
    data = data.dropna()
    #guardamos en un nuevo csv
    data.to_csv("../datasets/vgsales_clean.csv", index=False)

#uso
limpiar_datos()