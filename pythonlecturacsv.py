import pandas as pd

#Vamos a leer datos de nuestro CSV
#Creamos un dataframe a partir del fichero
df =pd.read_csv('data/datos.csv', delimiter=';')
#Pintamos el Dataframe
print(df)
#Podemos indicar el número de filas a mostrar
print("Primeras 7 filas")
print(df.head(7))
#Podemos convertir los datos en diccionarios
#para trabajar con Python puro.
diccionario = df.to_dict(orient='records')
for registro in diccionario:
    print(registro)
#Podemos hacer cálculos, por ejemplo, la media
media = df['edad'].mean()
print(media)
#Podemos agrupar por una columna si lo deseamos
df_grupo = df.groupby('ocupacion')
print(df_grupo.size())