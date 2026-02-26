#Necesitamos la librería de Pandas
import pandas as pd

#Las Series tienen que ser iguales entre ellas.
#Representan elementos de datos.
#Vamos a crear un diccionario
datos = {
    'Nombres': ['Ana', 'Adrian', 'Lucia', 'Antonia'],
    'Edad': [23, 25, 12, 40],
    'Ciudades': ['Madrid', 'Sevilla', 'Toledo', 'Gijon']
    }

#Estas series de datos se almacenan dentro de objetos
#llamados DataFrame de la librería Pandas
df = pd.DataFrame(datos)
#Mis primeros datos
print(df)
#Podemos filtrar los datos si lo deseamos
# df[df['DATO'] = > valor]
print("--------DataFrame filtrado-----")
dffiltrado = df[df['Edad'] > 24]
print(dffiltrado)
print("-----DataFrame ordenado------")
dforden = df.sort_values('Edad')
print(dforden)
