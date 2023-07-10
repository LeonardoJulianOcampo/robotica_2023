import numpy as np
import matplotlib.pyplot as plt

# Cargar datos de odometría y sensor de barrido láser desde los archivos de texto
odom_data = np.loadtxt('odom.txt')
scan_data = np.loadtxt('scan.txt')

# Extraer timestamps de odometría y sensor de barrido láser
odom_timestamps = odom_data[:, 0]
scan_timestamps = scan_data[:, 0]

# Encontrar índices de los timestamps de odometría más cercanos a los de sensor de barrido láser
nearest_indices = np.searchsorted(odom_timestamps, scan_timestamps)

# Gráfico de los timestamps de odometría y sensor de barrido láser
plt.figure(figsize=(10, 6))
plt.scatter(odom_timestamps, np.zeros_like(odom_timestamps), label='Odometría', s=10)
plt.scatter(scan_timestamps, np.ones_like(scan_timestamps), label='Sensor de barrido láser', s=10)
plt.scatter(odom_timestamps[nearest_indices], np.zeros_like(nearest_indices), color='red', label='Odometría más cercana')
plt.xlabel('Tiempo (s)')
plt.yticks([0, 1], ['Odometría', 'Sensor de barrido láser'])
plt.title('Mediciones de Odometría y Sensor de Barrido Láser')
plt.legend()

# Mostrar solo una fracción del tiempo total de simulación (ajustar los límites del eje x según sea necesario)
plt.xlim(odom_timestamps[0], odom_timestamps[-1])

# Filtrar valores inf en los datos de barrido láser
scan_data[np.isinf(scan_data)] = np.nan

# Generar mapa a partir de las mediciones del sensor de barrido láser
x_laser = np.cos(scan_data[:, 1:543]) * scan_data[:, 543:]
y_laser = np.sin(scan_data[:, 1:543]) * scan_data[:, 543:]

# Transformar los puntos de medición del sensor láser al sistema de coordenadas de odometría
x_odom = []
y_odom = []

for i, idx in enumerate(nearest_indices):
    x_odom.append(odom_data[idx, 1] + x_laser[i])
    y_odom.append(odom_data[idx, 2] + y_laser[i])

x_odom = np.concatenate(x_odom)
y_odom = np.concatenate(y_odom)

# Gráfico del mapa y camino seguido por el robot
plt.figure(figsize=(8, 8))
plt.scatter(x_odom, y_odom, s=1, color='blue', label='Mapa')
plt.plot(odom_data[:, 1], odom_data[:, 2], color='red', label='Camino del Robot')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Mapa Generado a partir del Sensor de Barrido Láser')
plt.legend()

# Mostrar el gráfico del mapa
plt.show()

