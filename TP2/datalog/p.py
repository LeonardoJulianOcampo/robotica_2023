import matplotlib.pyplot as plt
import numpy as np
import math

odom_data = open("odom.txt", "r")
scan_data = open("scan.txt", "r")

odom_timestamps = []
odom_x = []
odom_y = []
odom_theta = []

scan_timestamps = []
scan_values = []
scan_angles = []

# Función para leer el archivo de odometría y extraer los valores de posición
def read_odometry(data):
    for line in data:
        elements = line.strip().split('\t')
        timestamp = float(elements[0])
        x = float(elements[1])
        y = float(elements[2])
        theta = float(elements[3])
        odom_timestamps.append(timestamp)
        odom_x.append(x)
        odom_y.append(y)
        odom_theta.append(theta)

# Función para leer el archivo de escaneo láser y extraer los valores de escaneo
def read_scan(data):
    for line in data:
        elements = line.strip().split('\t')
        timestamp = float(elements[0])
        values = [float(e) if e != 'inf' else float('inf') for e in elements[1:]]
        scan_timestamps.append(timestamp)
        scan_values.append(values)

read_odometry(odom_data)
read_scan(scan_data)

odom_data.close()
scan_data.close()

# Función para sincronizar los datos de odometría y escaneo láser
def synchronize_data(odometry, scan):
    synchronized_odom_x = []
    synchronized_odom_y = []
    synchronized_odom_theta = []
    synchronized_scan_values = []
    synchronized_scan_angles = []
    
    for timestamp in odom_timestamps:
        # Buscar el índice más cercano en el arreglo de tiempos de escaneo
        index = np.argmin(np.abs(scan_timestamps - timestamp))
        synchronized_odom_x.append(odom_x[index])
        synchronized_odom_y.append(odom_y[index])
        synchronized_odom_theta.append(odom_theta[index])
        synchronized_scan_values.append(scan_values[index])
        synchronized_scan_angles.append(scan_angles[index])
    
    return synchronized_odom_x, synchronized_odom_y, synchronized_odom_theta, synchronized_scan_values, synchronized_scan_angles

synchronized_odom_x, synchronized_odom_y, synchronized_odom_theta, synchronized_scan_values, synchronized_scan_angles = synchronize_data(odom_timestamps, scan_timestamps)

# Función para transformar las coordenadas de escaneo al marco de referencia de la base
def transform_base(odom_x, odom_y, scan_values, scan_angles, theta):
    coords_c = []
    for j in range(len(theta)):
        for i in range(len(scan_angles)):
            x_c = math.cos(-theta[j]) * scan_values[j][i] + odom_x[j]
            y_c = math.sin(-theta[j]) * scan_values[j][i] + odom_y[j]
            coords_c.append([x_c, y_c])
    return coords_c

coords_c = transform_base(synchronized_odom_x, synchronized_odom_y, synchronized_scan_values, synchronized_scan_angles, synchronized_odom_theta)

# Función para graficar los puntos
def plot_points(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.scatter(x, y, s=0.8, c='blue')
    plt.plot(synchronized_odom_x, synchronized_odom_y, c='red')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.title('Puntos de coordenadas')
    plt.xlim(-15, 15)
    plt.ylim(-15, 15)
    plt.show()

plot_points(coords_c)

