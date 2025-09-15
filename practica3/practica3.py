import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("../datasets/vgsales_clean.csv")

#------ PRACTICA 3 -------
# se agrego a las funciones hechas en la practica 2 sus graficas respectivas


def dat_descriptivos(df):
    """Obtiene datos descriptivos y los grafica como heatmap"""
    print("--------------------- DATOS DESCRIPTIVOS -------------------------")
    resumen = df[["Ventas_Globales", "Ventas_Otros", "Ventas_Japón",
                  "Ventas_Europa", "Ventas_Norteamérica"]].agg(
                    ["mean", "median", "sum", "var", "std", "kurt"])
    print(resumen)
    print()

    # mapa de calor de las estadísticas
    plt.figure(figsize=(8, 5))
    sns.heatmap(resumen, annot=True, fmt=".2f", cmap="Blues")
    plt.title("Estadísticas descriptivas de ventas")
    plt.show()


def top_juegos_mas_vendidos(df):
    """Top 10 juegos más vendidos y gráfico de barras"""
    print("------------------------ TOP JUEGOS MAS VENDIDOS -------------------------------")
    #se agreago la columna ventas globales para crear la barra
    top10 = df.sort_values(by="Ventas_Globales", ascending=False).head(10)[["Nombre", "Ventas_Globales"]]
    print(top10["Nombre"])
    print()

    # grafico de barras horizontales
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top10, y="Nombre", x="Ventas_Globales")
    plt.title("Top 10 Juegos más vendidos (Ventas Globales)")
    plt.xlabel("Ventas Globales (millones)")
    plt.ylabel("Juego")
    plt.show()


def total_por_genero(df):
    """Suma total de ventas por género (gráfico de barras)"""
    print("------------------------ TOTAL VENTAS POR GENERO -------------------------------")
    tabla = df.pivot_table(
        values=["Ventas_Globales"],
        index="Género",
        aggfunc="sum").reset_index()
    tabla = tabla.sort_values(by="Ventas_Globales", ascending=False)
    print(tabla)
    print()

    # barras por género
    plt.figure(figsize=(10, 6))
    sns.barplot(data=tabla, x="Ventas_Globales", y="Género")
    plt.title("Ventas Globales por Género")
    plt.xlabel("Ventas Globales (millones)")
    plt.ylabel("Género")
    plt.show()


def total_por_anio(df):
    """Ventas globales totales por año (gráfico de línea temporal)"""
    print("------------------------ TOTAL VENTAS POR AÑO -------------------------------")
    tabla = df.pivot_table(
        values=["Ventas_Globales"],
        index="Año",
        aggfunc="sum").reset_index()
    print(tabla)
    print()

    # línea temporal
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=tabla, x="Año", y="Ventas_Globales", marker="o")
    plt.title("Evolución de ventas globales por Año")
    plt.xlabel("Año")
    plt.ylabel("Ventas Globales (millones)")
    plt.show()


def top_publicadores(df, n=5):
    """Top N publicadores + Otros, gráfico de pastel"""
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

    # gráfico de pastel
    plt.figure(figsize=(8, 8))
    plt.pie(tabla["Ventas_Globales"], labels=tabla["Publicador"], autopct="%1.1f%%", startangle=140)
    plt.title("Top Publicadores de Videojuegos (Ventas Globales)")
    plt.show()


# === USO ===
top_juegos_mas_vendidos(data)
dat_descriptivos(data)
total_por_genero(data)
total_por_anio(data)
top_publicadores(data)