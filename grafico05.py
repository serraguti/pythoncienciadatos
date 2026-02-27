import matplotlib.pyplot as plt

productos = []
ventas = []
#Deseamos pedir 5 productos
for i in range(1, 6):
    print("Nombre del producto")
    prod = input()
    productos.append(prod)
    print("Introduzca número de ventas")
    num = int(input())
    ventas.append(num)
plt.pie(ventas, labels=productos)
plt.show()
    