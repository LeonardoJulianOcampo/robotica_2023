import matplotlib.pyplot as plt
import numpy as np


archivo = open("scan.txt", "r")
datos = []

for linea in archivo:
    elementos = linea.strip().split('\t')
    datos_linea = []

    for elemento in elementos:
        datos_linea.append(float(elemento))

    datos.append(datos_linea)

archivo.close()

print(datos[1300])


theta = np.linspace((-3/4)*np.pi,(3/4)*np.pi,len(datos[0][1:]))
r = datos[0:-1][0]

fig = plt.figure()
ax = fig.add_subplot(1,1,1,polar=True)


print(theta[1])
print(r[1])

print(len(theta))
print(len(datos[0][1:]))

ax.scatter(theta, datos[1300][1:])


ax.set_title("Gráfico en coordenadas polares")
ax.grid(True)

plt.show()
