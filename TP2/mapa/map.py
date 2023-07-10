import matplotlib as plt
import numpy as np
import math

odom_data = open("odom.txt","r")
scan_data = open("scan.txt","r")

odom_timestamps = []
odom_measures   = []
odom_x = []
odom_y = []
odom_theta      = []


scan_timestamps = []
scan_values   = []
scan_x = []
scan_y = []
scan_angles = []


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
    out = []
    elements = [] 
    pose  = []
    x     = []
    y     = []
    theta = []
    raw_data_line = []

    for line in data:                        # leo cada una de las lineas del objeto data resultante de la lectura del archivo
        elements = line.strip().split('\t')  # separo los elementos de cada linea. el separador es el caracter \t
        elements = list(map(float,elements)) # convierto la lista de str a float para poder trabajar con los elementos
        raw_data_line.append(elements)       # lista que contiene cada una las listas que contienen los datos de cada linea del archivo. A esta lista despues la tengo que analizar y extraer los elementos que correspondan
        
    time_stamps = [e[0] for e in raw_data_line] # extraigo los timestamps de raw_data_line y los almaceno en time_stamps que es una lista
    x = [e[1] for e in raw_data_line]           # idem que arriba pero para las coordenadas de x
    y = [e[2] for e in raw_data_line]           # idem que arriba pero para las coordenadas de y 
    theta = [e[3] for e in raw_data_line]       # lo mismo pero para theta
    out = [time_stamps,x,y,theta]
    return out                                  #retorna una lista con los datos diferenciados



def lidar(data):
    out = []
    values = []
    x = []
    y = []
    raw_data_line = []

    angles = np.linspace((-3/4)*np.pi, (3/4)*np.pi, 540)
    for line in data:
        elements = line.strip().split('\t')
        elements = list(map(float,elements))
        raw_data_line.append(elements)

    time_stamps =  [e[0] for e in raw_data_line]
#   values      =  [e[1:540] for e in raw_data_line]
    values.append(raw_data_line[1:541])      #values es una lista que contiene listas. Cada una de ellas posee las 540 mediciones del lidar

    return time_stamps,values,angles


# Una vez formateados los datos a un formato acorde, se procede a emplearlos para confeccionar el mapa
# Primero tomamos las coordenadas polares obtenidas por el lidar y los convierto a coordenadas rectangulares

def pol2rect(scan_values,modules):   #recibe una lista de los modulos y angulos theta del robot. tengo un total de 540 mediciones por lo que cada lista tiene esa cant de elementos
    x_coord = []
    y_coord = []
    rect_coords = []            #almacena las coordenadas x,y resultantes de la conversion en el formato [x,y] (lista de listas) 
    angles = np.linspace((-3/4)*np.pi, (3/4)*np.pi, 540)   
    for i in range(len(scan_values)):
        x_coord.append(math.cos(angles[i])*modules[i])
        y_coord.append(math.sin(angles[i])*modules[i])
    return x_coord,y_coord


# Despues de la conversion se tiene que hacer el cambio de base mediante la respectiva matriz de cambio de base

def tr_base(scan_x,scan_y,angle):                            # angles en este caso es el tita del robot y no del lidar!!!
    coords_c = []                                           # lista donde se almacenan las coordenadas de los vectores luego del cambio de base expresados en referencia a la base canonica
    for j in range(len(angle)):
        for i in range(len(angle[0])):
            Pbc = np.array([[np.cos(angle[i] - np.pi / 2), np.cos(angle[i])],[np.sin(angle[i] - np.pi / 2), np.sin(angle[i])]])
            Wb  = np.array([[scan_x[i]],[scan_y[i]]])
            Wc  = Pbc.dot(Wb)                     # producto matricial entre la matriz de c de base y el vector expresado en la base B da como resultado el vector expr. en la base c
            coords_c.append(Wc)                            # cada vector transformado se agrega a la lista de almacenamiento
        
    return coords_c                                    #devuelvo la lista con las coordenadas convertidas a la base canonica


# Una vez convertidas las coordenadas de los vectores puedo probar graficarlas


odom_timestamps,odom_x,odom_y,theta = pose(odom_data)
scan_timestamps,scan_values,scan_angles = lidar(scan_data)

scan_x,scan_y = pol2rect(scan_values,scan_angles)
coords_c      =  tr_base(scan_x,scan_y,theta)



# Llamada a la función para extraer los timestamps
#odom_timestamps = timestamps(odom_data)
#scan_timestamps = timestamps(scan_data)


