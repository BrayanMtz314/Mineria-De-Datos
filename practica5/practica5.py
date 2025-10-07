# Mas informacion de este codigo en el notebook


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv("../datasets/vgsales_clean.csv")

data.head()
data.sort_values(by='Ventas_Globales', ascending=False).head()


def mostrar_correlacion(data):
    """Muestra un mapa de calor con las correlaciones entre variables numéricas."""
    corr = data.corr(numeric_only=True)
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Matriz de correlación')
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
    print(f"R² Score: {r2:.4f}")

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

# Mostrar correlaciones
mostrar_correlacion(data)

#elegimos usar como variable x ventas_norteamerica ya que era la que contaba con mayor correlacion
#hacia la variable de ventas globales


X = data['Ventas_Norteamérica']  # variable independiente
y = data['Ventas_Globales']      # variable dependiente
#uso del modelo
modelo = modelo_lineal_simple(X, y)
