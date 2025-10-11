#Para mas informacion de este codigo, ir al notebook

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import math

data = pd.read_csv("../datasets/vgsales_clean.csv")
data.sort_values(by="Ventas_Norteamérica", ascending=True).head()
data.head()

plt.figure(figsize=(10,6))
plt.xlabel('Ventas Norteamerica')
plt.ylabel('Ventas Europa')
plt.title("Ventas Norteamerica vs Europa")
plt.scatter(data['Ventas_Norteamérica'], data['Ventas_Europa'], c='red')
plt.show()

def distancia_euclidiana(punto1, punto2):
    """Retorna la distancia entre dos puntos (x,y) dados"""
    distance = 0
    for i in range(len(punto1)):
        distance += (punto2[i] - punto1[i])**2
    return math.sqrt(distance)

def listaPuntos(x,y):
    """retorna una lista de puntos (x,y)"""
    puntos = [[x[i],y[i]] for i in range(len(x))]
    return puntos

def calcular_centroide(puntos):
    """Calcula el centroide para un conjunto de puntos"""
    if not puntos:
        return []
    centroid = [0] * len(puntos[0])
    
    # Sumamos todas las coordenadas de los puntos
    for punto in puntos:
        for i in range(len(punto)):
            centroid[i] += punto[i]
            
    # formamos las nuevas coordenadas encontrando del promedio (suma de las coordenadas entre el numero de puntos)
    coordenada = [coor/len(puntos) for coor in centroid]
    return coordenada

def kmeans(data, k, iteraciones=100):
    """
    Realiza el algoritmo K-means para una lista de datos (x,y)
    
    Args:
        data: Lista de datos (x,y).
        k: numero de conjuntos.
        iteraciones (int): numero maximo de iteraciones.
        
    Returns:
        el centroide final y la lista de conjuntos.
    """
    # 1. Se inicializa el centroide de forma aleatoria
    centroids = random.sample(data, k)
    
    for i in range(iteraciones):
        # 2. Asignamos puntos para los centroides
        clusters = [[] for _ in range(k)] 
        
        for punto in data:
            distancias = [distancia_euclidiana(punto, centroid) for centroid in centroids]
            index_centroide_cercano = distancias.index(min(distancias))
            clusters[index_centroide_cercano].append(punto)
        
        # Almacenamos centroides antiguos para checar convergencia
        centroids_viejos = centroids
        
        # 3. Calculamos nuevos centroides
        centroids = [calcular_centroide(cluster) for cluster in clusters]
        
        # 4. revisar convergencia
        Converge = True
        for j in range(k):
            # usamos un numero pequeno para la tolerancia
            if distancia_euclidiana(centroids_viejos[j], centroids[j]) > 0.0001:
                print(f"iteracion: {i+1}")
                converge = False
                break
        
        if converge:
            print(f"numero total de iteraciones: {i+1}")
            break
            
    return centroids, clusters

 
# Numero de conjuntos
K = 2

puntos = listaPuntos(data['Ventas_Norteamérica'], data['Ventas_Europa'])

random.seed(42)
    
final_centroids, final_clusters = kmeans(puntos, K)
    
print("\nFinal Centroids:")
for i, centroid in enumerate(final_centroids):
     print(f"  Cluster {i+1}: {centroid}")
      

plt.figure(figsize=(13,8))
plt.xlabel('Ventas Norteamerica')
plt.ylabel('Ventas Europeas')
plt.title("Ventas Norteamericana vs Europeas")
for i, cluster in enumerate(final_clusters):
    for punto in cluster:
        if i == 0:
            plt.scatter(punto[0], punto[1], c='red')
        else:
           plt.scatter(punto[0], punto[1], c='blue')
plt.show()