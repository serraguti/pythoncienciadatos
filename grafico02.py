import matplotlib.pyplot as plt

#La mayoría de los gráficos dibujan sus elementos 
#a partir de datos X, Y
x = ["Atletico de Madrid", "Real Madrid", "Barcelona", "Betis"]
#Valor del mercado
y = [30, 400, 66, 20]
#Para crear el grafico debemos darle los datos a la 
#librería mediante plt.bar
plt.scatter(x, y)
#Personalizamos el gráfico
plt.title("Grafico de dispersión")
plt.xlabel("Equipos")
plt.ylabel("Presupuesto")
#Podemos guardar los gráficos en imágenes
plt.savefig('images/dispersion.png')
plt.show()