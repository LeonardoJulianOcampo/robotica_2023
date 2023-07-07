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

indice_linea = 0  # Índice de la linea a graficar
print(datos[indice_linea])

r = datos[indice_linea][1:]
theta = np.linspace(0, 2*np.pi, len(r))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, polar=True)

ax.scatter(theta, r)
ax.set_title("Gráfico en coordenadas polares")
ax.grid(True)


ax.scatter(theta, datos[1300][1:])
ax.set_title("grafico2")
ax.grid(True)

plt.show()

