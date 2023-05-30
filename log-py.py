import matplotlib.pyplot as plt
import numpy as np


data = []
#Lee archivo
with open('/home/mateo/simulation_ws/src/circle.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        time = float(line[0])
        x = float(line[1]) 
        y = float(line[2]) 
        orientation = float(line[3])
        linear = float(line[4])
        angular = float(line[5])
        data.append((time, x, y, orientation, linear, angular))  


time_values = [item[0] for item in data]
x_values    = [item[1] for item in data]
y_values    = [item[2] for item in data]
or_values   = [item[3] for item in data]
lin_values  = [item[4] for item in data]
ang_values  = [item[5] for item in data]

fig, axs = plt.subplots(4, 1, figsize=(10, 15))



axs[0].scatter(x_values, y_values)
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')
axs[0].set_title('Camino')
axs[0].set_aspect('equal')


axs[1].plot(time_values, x_values, label='Posición X')
axs[1].plot(time_values, y_values, label='Posición Y')
axs[1].plot(time_values, or_values, label='Orientación')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('Valor')
axs[1].set_title('Pose del Robot con respecto al Tiempo')
axs[1].legend()


axs[2].plot(time_values, lin_values, label='Velocidad Lineal')
axs[2].set_xlabel('Tiempo')
axs[2].set_ylabel('Velocidad Lineal')
axs[2].set_title('Velocidad Lineal respecto al Tiempo')
axs[2].legend()

axs[3].plot(time_values, ang_values, label='Velocidad Angular')
axs[3].set_xlabel('Tiempo')
axs[3].set_ylabel('Velocidad Angular')
axs[3].set_title('Velocidad Angular respecto al Tiempo')
axs[3].legend()

plt.tight_layout()
plt.show()