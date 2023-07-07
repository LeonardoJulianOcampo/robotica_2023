import numpy as np
import matplotlib.pyplot as plt

def find_nearest_timestamps(odometry_timestamps, laser_timestamps):
    nearest_indices = []
    for laser_timestamp in laser_timestamps:
        nearest_index = np.abs(odometry_timestamps - laser_timestamp).argmin()
        nearest_indices.append(nearest_index)
    return nearest_indices

# Ejemplo de datos de timestamp
odometry_timestamps = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1])
laser_timestamps = np.array([0.15, 0.35, 0.55, 0.75, 0.9, 1.05, 1.2, 1.35])

nearest_indices = find_nearest_timestamps(odometry_timestamps, laser_timestamps)

# Gráfico de los instantes de tiempo
plt.figure(figsize=(10, 6))
plt.plot(odometry_timestamps, np.zeros_like(odometry_timestamps), 'bo', label='Odometría')
plt.plot(laser_timestamps, np.zeros_like(laser_timestamps), 'ro', label='Sensor láser')

# Resaltar los instantes de tiempo más cercanos
plt.figure(figsize=(10,6))
plt.plot(odometry_timestamps, np.zeros_like(odometry_timestamps), 'bo', label='Odometría')
plt.plot(laser_timestamps, np.zeros_like(laser_timestamps), 'ro', label='Sensor láser')

for idx in nearest_indices:
    plt.plot(odometry_timestamps[idx], 0, 'go')

plt.xlabel('Tiempo')
plt.ylabel('Sensor')
plt.legend()
plt.show()

