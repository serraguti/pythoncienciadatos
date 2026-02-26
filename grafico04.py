import matplotlib.pyplot as plt

#La mayoría de los gráficos dibujan sus elementos 
#a partir de datos X, Y
equipos = ["Atletico de Madrid", "Real Madrid", "Barcelona", "Betis"]
#Valor del mercado
valores = [30, 400, 66, 20]
#Para crear el grafico debemos darle los datos a la 
#librería mediante plt.bar
plt.pie(valores, labels=equipos)
#Personalizamos el gráfico
plt.title("Grafico Quesos")
plt.xlabel("Equipos")
plt.ylabel("Presupuesto")
#Podemos guardar los gráficos en imágenes
plt.savefig('images/circular.png')
plt.show()