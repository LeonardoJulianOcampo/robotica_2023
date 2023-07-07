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

indice_linea = 16400  # Índice de la línea que deseas graficar
print(datos[indice_linea])

theta = np.linspace((-3/4)*np.pi, (3/4)*np.pi, len(datos[indice_linea][1:]))
r = datos[indice_linea][1:]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, polar=True)

ax.scatter(theta, r)
ax.set_title("Gráfico en coordenadas polares")
ax.grid(True)

plt.show()

