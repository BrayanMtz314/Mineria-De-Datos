# Codigo en funciones
def prueba_normalizacion(df):
    """Hace uso de la prueba Shapiro para comprobar la normalidad de los datos"""
    for genero, grupo in df.groupby("Género"):
        valores = grupo["Ventas_Globales"].values
        if len(valores) >= 3:  
            #Prueba shapiro
            stat, p_value = stats.shapiro(valores)
            if p_value < 0.05:
                print(f"Género: {genero:<20} p-value: {p_value:.2e}    LOS DATOS NO SON NORMALES")
            elif p_value >= 0.05:
                print(f"Género: {genero:<20} p-value: {p_value:.2e}    LOS DATOS SON NORMALES")

def prueba_grupos(df):
    """HAce uso de la prueba Kruskal-Wallis para comprobar la diferencias entre grupos"""
    grupos = [grupo["Ventas_Globales"].values 
          for nombre, grupo in df.groupby("Género")]

    # Kruskal-Wallis
    h_stat, p_value = stats.kruskal(*grupos)
    print("Estadístico H:", h_stat)
    if p_value < 0.05:
            print(f"p-value: {p_value:.2e}    hay diferencias significativas entre al menos un par de géneros")
    elif p_value >= 0.05:
            print(f"p-value: {p_value:.2e}    no hay evidencia suficiente para decir que los géneros difieran en ventas globales")

#USO
prueba_normalizacion(data)
prueba_grupos(data)


#Mas informacion de las pruebas de hipotesis en el notebook
#La conclusion final fue: Existe al menos un genero en el cual se vende mas o menos que los otros
