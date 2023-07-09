
import numpy as np
import matplotlib.pyplot as plt

def find_nearest_timestamps(odometry_timestamps, laser_timestamps):
    nearest_indices = []
    odometry_timestamps = np.array(odometry_timestamps)  # Convertir a arreglo numpy
    for laser_timestamp in laser_timestamps:
        nearest_index = np.abs(odometry_timestamps - laser_timestamp).argmin()
        nearest_indices.append(nearest_index)
    return nearest_indices

# Ejemplo de datos de timestamp
odom_timestamps = []
scan_timestamps = []
odom_c = []


odom_data = open("odom.txt","r")
scan_data = open("scan.txt","r")

def timestamps(data):
    timestamps = []  # Lista para almacenar los timestamps
    for line in data:
        elements = line.strip().split('\t')
        if elements:
            timestamp = float(elements[0])  # Convertir el timestamp a número flotante
            timestamps.append(timestamp)
    
    return timestamps

# Llamada a la función para extraer los timestamps
odom_timestamps = timestamps(odom_data)
scan_timestamps = timestamps(scan_data)
# Imprimir los timestamps extraídos
print(odom_timestamps)

odom_data.close()  # Cerrar el archivo después de leerlo
scan_data.close()  # Cerrar el archivo después de leerlo

nearest_indices = find_nearest_timestamps(odom_timestamps[:100], scan_timestamps[:100])

# Gráfico de los instantes de tiempo
plt.figure(figsize=(10, 6))
plt.plot(odom_timestamps, np.zeros_like(odom_timestamps), 'bo', label='Odometría')
plt.plot(scan_timestamps, np.zeros_like(scan_timestamps), 'ro', label='Sensor láser')


for idx in nearest_indices:
    odom_c.append(odom_timestamps[idx])

# Resaltar los instantes de tiempo más cercanos
plt.plot(odom_c[:100],np.zeros_like(odom_c[:100]), 'go',label='Mas cercano')

plt.xlabel('Tiempo')
plt.ylabel('Sensor')
plt.legend()
plt.show()

