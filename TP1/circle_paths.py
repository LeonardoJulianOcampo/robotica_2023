import matplotlib.pyplot as plt

# Leer el archivo generado por dump_odom.py y extraer los valores
data = []
cwPath1 = 'cw_0.5linear_0.49angular.txt'
cwPath2 = 'cw_0.5linear_1.0angular.txt'
cwPath3 = 'cw_0.5linear_2.14angular.txt'
cwPath4 = 'cw_0.15linear_1.0angular.txt'
cwPath5 = 'cw_0.23linear_0.49angular.txt'
cwPath6 = 'cw_1.07linear_1.0angular.txt'
cwPath7 = 'cw_1.52linear_2.04angular.txt'

ccwPath8 = 'ccw_0.5linear_1.0angular.txt'
ccwPath9 = 'ccw_0.15linear_1.0angular.txt'
ccwPath10 = 'ccw_1.07linear_1.0angular.txt'

pathList = [cwPath1, cwPath2, cwPath3, cwPath4, cwPath5, cwPath6, cwPath7, ccwPath8, ccwPath9, ccwPath10]

pathNumber = int(input("Para un camino horario, ingresar un numero del 0 al 6, para un camino antihorario ingresar del 7 al 9:"))

getPath = pathList[pathNumber]
with open(getPath, 'r') as file:
    for line in file:
        line = line.strip().split() 
        x = float(line[1]) 
        y = float(line[2])  
        orientation = float(line[3]) 
        data.append((x, y, orientation)) 

x_values = [item[0] for item in data]
y_values = [item[1] for item in data]

fig, ax = plt.subplots()


ax.plot(x_values, y_values, '-o')


if(pathNumber <= 6):
    sentido = 'Horario'
else:
    sentido = 'Antihorario'
ax.set_aspect('equal')
ax.set_xlabel('Posición en X')
ax.set_ylabel('Posición en Y')
ax.set_title('Camino Recorrido ' + sentido)


plt.show()