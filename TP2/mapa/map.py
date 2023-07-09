import matplotlib as plt
import numpy as np

odom_data = open("odom.txt","r")
scan_data = open("scan.txt","r")

odom_timestamps = []
odom_measures   = []
odom_measures_x = []
odom_measures_y = []

scan_timestamps = []
scan_measures   = []
scan_measures_x = []
scan_measures_y = []

# la funcion timestamps toma los datos leidos de un archivo de medicion (puede ser scan u odom) y extrae unicamente los timestamps de cada archivo, retornando una lista con ellos.

def timestamps(data):
    timestamps = []  # Lista para almacenar los timestamps
    for line in data:
        elements = line.strip().split('\t')
        if elements:
            timestamp = float(elements[0])  # Convertir el timestamp a número flotante
            timestamps.append(timestamp)
    
    return timestamps

# la funcion pose lee el archivo de odometría para extraer los valores x,y,theta y retornar una lista
# compuesta por 3 listas: cada una de las listas almacena los valores de cada una de las variables x,y,theta

def pose(data):
    
    pose  = []
    x     = []
    y     = []
    theta = []

    for line in data:
        elements = line.strip().split('\t')
        if elements:
            x_v = float(elements[1])
            y_v = float(elements[2])
            th_v = float(elements[3])
            x.append(x_v)
            y.append(y_v)
            th.append(t_v)

    pose = [x,y,th]

    return pose


def lidar(data):

    values = []
    x = []
    y = []
    angles = np.linspace((-3/4)*np.pi, (3/4)*np.pi, len(data[0][1:]))
    

            



# Llamada a la función para extraer los timestamps
odom_timestamps = timestamps(odom_data)
scan_timestamps = timestamps(scan_data)


