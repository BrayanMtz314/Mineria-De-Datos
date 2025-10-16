# Explicaciones con detalle en el notebook

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv("../datasets/vgsales_clean.csv")
total_anios = data.groupby(["Año"])["Ventas_Globales"].sum()
total_anios

# Mostramos distribucion de los datos por anios
plt.figure(figsize=(12, 7))
sns.lineplot(x=total_anios.index, y=total_anios.values, marker='o')
plt.title('Promedio de ventas globales por año')
plt.xlabel('Año')
plt.ylabel('Promedio de ventas globales')
plt.grid(True)
plt.show()

def modelo_lineal_simple(X, y):
    """Imprime un grafico de la regresion lineal junto a los datos originales, aparte de 
    retornar el modelo de regresion"""
    X = np.array(X).reshape(-1, 1)
    y = np.array(y)

    # Crear y entrenar el modelo
    modelo = LinearRegression()
    modelo.fit(X, y)

    # Predicciones
    y_pred = modelo.predict(X)

    # Calcular R²
    r2 = r2_score(y, y_pred)

    if r2 > 0.80:
        print(f"R² Score: {r2:.4f}   ---   El modelo predice con exito la variable dependiente", end="\n\n")
    else:
        print(f"R² Score: {r2:.4f}   ---   El modelo no predice con exito la variable dependiente", end="\n\n")
    

    # Graficar la recta de regresión junto con los datos originales
    plt.figure(figsize=(8, 6))
    plt.scatter(X, y, color='blue', label='Datos reales', alpha=0.6)
    plt.plot(X, y_pred, color='red', linewidth=2, label='Recta de regresión')
    plt.xlabel('Variable independiente (X)')
    plt.ylabel('Variable dependiente (y)')
    plt.title('Regresión lineal simple')
    plt.legend()
    plt.grid(True)
    plt.show()

    return modelo


X = total_anios.index  # variable independiente
y = total_anios.values      # variable dependiente
#uso del modelo
modelo = modelo_lineal_simple(X, y)


anios_acortados =  total_anios.loc[1980:2010]
anios_acortados
X = anios_acortados.index  # variable independiente
y = anios_acortados.values      # variable dependiente
#uso del modelo
modelo = modelo_lineal_simple(X, y)


#----------- PREDICCIONES ---------------
#inicializamos valores
anio = 2012
valor_a_predecir = np.array([[anio]])

# Se usa el método .predict() del modelo
prediccion = modelo.predict(valor_a_predecir)

print(f"Para el anio {anio}, se predicen {prediccion[0]:.2f} millones en ventas globales.")

# Lista de anios
anios = [2011, 2012, 2013, 2014]
valores_a_predecir = np.array(anios).reshape(-1, 1)

# Realizar las predicciones
predicciones_multiples = modelo.predict(valores_a_predecir)

print("--- Predicciones Múltiples ---")
for valor, pred in zip(anios, predicciones_multiples):
    print(f"Anio: {valor} -> Total de Ventas Globales: {pred:.2f}")