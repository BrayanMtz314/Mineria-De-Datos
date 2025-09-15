import pandas as pd

#---- Aqui comienza practica 2 ----
#Medimos promedio, mediana y suma total de cada columna de ventas

def dat_descriptivos(df):
    """obtiene  datos descriptivos por medio de agreagaciones"""
    print("--------------------- DATOS DESCRIPTIVOS -------------------------")
    resumen = data[["Ventas_Globales", "Ventas_Otros", "Ventas_Japón","Ventas_Europa", "Ventas_Norteamérica"]].agg(["mean", "median", "sum", "var", "std", "kurt"])
    print(resumen)
    print()

def top_juegos_mas_vendidos(df):
    """Despliega los primeros 10 juegos mas vendidos con respecto a ventas globales"""
    print("------------------------ TOP JUEGOS MAS VENDIDOS -------------------------------")
    print(data.sort_values(by="Ventas_Globales", ascending=False).head(10)['Nombre'])
    print()

def total_por_genero(df):
    """Despliega una tabla con la suma total de ganancias por genero y lugar de ventas"""
    print("------------------------ TOTAL VENTAS POR GENERO -------------------------------")
    tabla = df.pivot_table(
    values=["Ventas_Globales", "Ventas_Otros", "Ventas_Japón",
            "Ventas_Europa", "Ventas_Norteamérica"],
    index="Género",
    aggfunc=["sum"])
    print(tabla)
    print()

def total_por_anio(df):
    "Obtenemos una tabla con el total de ventas por anio"
    print("------------------------ TOTAL VENTAS POR AÑO -------------------------------")
    tabla = df.pivot_table(
    values=["Ventas_Globales"],
    index="Año",
    aggfunc=["sum"])
    print(tabla)
    print()

def top_publicadores(df, n=5):
    print("------------------------ TOP PUBLICADORES ----------------------------------")
    ventas_pub = df.groupby("Publicador")["Ventas_Globales"].sum().sort_values(ascending=False)
    top_n = ventas_pub.head(n)
    otros = ventas_pub.iloc[n:].sum()
    tabla = pd.concat([top_n, pd.Series({"Otros": otros})])
    tabla = tabla.reset_index()
    tabla.columns = ["Publicador", "Ventas_Globales"]
    total = tabla["Ventas_Globales"].sum()
    tabla["Porcentaje"] = (tabla["Ventas_Globales"] / total) * 100
    print(tabla)
    print()

#USO
top_juegos_mas_vendidos(data)
dat_descriptivos(data)
total_por_genero(data)
total_por_anio(data)
top_publicadores(data)