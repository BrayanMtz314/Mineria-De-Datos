#Mas informacion de este codigo en el notebook

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

data = pd.read_csv("../datasets/vgsales_clean.csv")
print(data.head())

#primero almacenamos todos los valores de consola dentro de una cadena de texto
text = ''
for consola in data["Plataforma"].values:
    text += consola + " " 



#Enseguida usamos la libreria wordcloud para generar la imagen
wordcloud_generator = WordCloud(
    width=800,
    height=400,
    background_color='white',
    min_font_size=10
).generate(text)


#para finalizar usamos matplotlib para mostrar la imagen generada por wordcloud
print("---------Mostrando Imagen---------")
plt.figure(figsize=(10, 5))  
plt.imshow(wordcloud_generator, interpolation='bilinear') 
plt.axis("off")  
plt.show()

wikitext = ''
nametxt = "textmining.txt"

#extraemos el docucumento txt
try:
    with open(nametxt, 'r', encoding='utf-8') as file:
        wikitext = file.read()
except FileNotFoundError:
    exit() 
except Exception as e:
    print(f"Ha ocurrido un error: {e}")
    exit()

#esta vez es necesario agregar un nuevo parametro denominado STOPWORDS, el cual es un conjunto de palabras que agrega muy poco significado a nuestro texto. 
wordcloud_generator = WordCloud(
    width=800,
    height=400,
    background_color='white',
    stopwords=STOPWORDS,
    min_font_size=10
).generate(wikitext)

print("---------Mostrando Imagen---------")
plt.figure(figsize=(10, 5))  
plt.imshow(wordcloud_generator, interpolation='bilinear') 
plt.axis("off")  
plt.show()


