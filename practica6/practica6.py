# ------------------MAS INFORMACION DE ESTE CODIGO EN EL NOTEBOOK ----------------------------


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("../datasets/vgsales_clean.csv")
data.head()

plataformas = data['Plataforma'].unique()
print(plataformas)

fig, ax = plt.subplots(figsize=(8, 6))
for plataforma in plataformas:
    subset = data[data['Plataforma'] == plataforma]

    ax.scatter(
        subset['Ventas_Norteamérica'],
        subset['Ventas_Japón'],
        label=plataforma
    )

ax.legend(title='Plataforma')
ax.set_title('Distribucion de consolas segun ventas')
ax.set_xlabel('Ventas Norteamericanas')
ax.set_ylabel('Ventas Europeas')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

def distancia_euclidiana(punto1, punto2):
    """Retorna la distancia entre dos puntos (x,y) dados"""
    distance = 0
    for i in range(len(punto1)):
        distance += (punto2[i] - punto1[i])**2
    return math.sqrt(distance)

def knn(data, punto, k):
    """Usa el algortimo de k-nearest neighbors para predecir la clasificacion del nuevo dato"""

    distances = []
    for index in range(len(data)):
        punto2 = np.array(data.loc[index][['Ventas_Norteamérica','Ventas_Japón']])
        dist =  distancia_euclidiana(punto, punto2)
        distances.append((data.loc[index]["Plataforma"], dist))

    distances.sort(key=lambda x: x[1])

    vecinos = []
    for i in range(k):
        vecinos.append(distances[i][0])

    prediccion = max(vecinos)

    print(f'Tomando en cuenta las ventas del norteamericanas y japonesas del juego proporcionado, es mas probable que sea de la consola: {prediccion}')


#------------ COORDENADA DEL NUEVO JUEGO (Ventas norteamericanas, ventas japonesas) y numero de vecinos
punto = [20,8]
vecinos = 3


#------------ USO DE KNN ---------------------------
knn(data, punto, vecinos)


#----------- GRAFICA DE LA RESPUESTA -------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))
for plataforma in plataformas:
    subset = data[data['Plataforma'] == plataforma]

    ax.scatter(
        subset['Ventas_Norteamérica'],
        subset['Ventas_Japón'],
        label=plataforma
    )
ax.scatter(punto[0],punto[1], c='black', label="NUEVO JUEGO")

ax.legend(title='Plataforma')
ax.set_title('Distribucion de ')
ax.set_xlabel('Ventas Norteamericanas')
ax.set_ylabel('Ventas Europeas')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()