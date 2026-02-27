import matplotlib.pyplot as plt

semana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")
temperaturas = []
for dia in semana:
    print(f"Temperatura del {dia}")
    temp = int(input())
    temperaturas.append(temp)
#La ventaja de los gráficos está en que si introducimos
#más series, podemos representarlas siempre que pongamos 
#distintas labels
plt.plot(semana, temperaturas, label="Semana 1")
temperaturas2 = [4, 18, 5, 23, 12]
plt.plot(semana, temperaturas2, label="Semana 2")
plt.legend()
plt.title("Temperaturas febrero")
plt.xlabel("Día semana")
plt.ylabel("Temperatura")
plt.show()