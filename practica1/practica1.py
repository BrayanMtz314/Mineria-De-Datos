#practica 1 - data cleaning
#es lo mismo que se hizon en el notebook

import pandas as pd

#pasanmos el csv a un datadrame
data = pd.read_csv("../datasets/vgsales.csv")

#verificamos informacion
data.info()

#verificamos forma del dataframe 
data.head()

#remplazamos valores que podrian ser nulos
data.replace(["N/A", "unknown", ""], pd.NA, inplace=True)

#cantidades de valores nulos (si habia)
data.isnull().sum()

#cantidades de valores duplicados (no habia)
data.duplicated(keep=False).sum()

#borramos valores nulos
data = data.dropna()

#eliminamos columna innecesaria
data = data.drop(columns=["Rank"])

#verificamos que ya no haya valores nulos 
data.info()

#nueva forma del dataframe 
data.head()

#guardamos el dataframe como el csv
data.to_csv("../datasets/vgsales.csv", index=False)