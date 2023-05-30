import matplotlib.pyplot as plt
import numpy as np
import random

data = []
p1 = []
p2 = []
p3 = []

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

datalen = len(data)

time_values = [item[0] for item in data]
x_values    = [item[1] for item in data]
y_values    = [item[2] for item in data]
or_values   = [item[3] for item in data]
lin_values  = [item[4] for item in data]
ang_values  = [item[5] for item in data]

fig, axs = plt.subplots(2, 1, figsize=(10, 15))

p1 = data[random.randint(1, datalen-1)]
p2 = data[random.randint(1, datalen-1)]
p3 = data[random.randint(1, datalen-1)]

p1_time = p1[0]
p1_x = p1[1]
p1_y = p1[2]

p2_time = p2[0]
p2_x = p2[1]
p2_y = p2[2]

p3_time = p3[0]
p3_x = p3[1]
p3_y = p3[2]


axs[0].scatter(x_values, y_values)
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')
axs[0].scatter(p1_x, p1_y, color = 'red')
axs[0].scatter(p2_x, p2_y, color = 'green')
axs[0].scatter(p3_x, p3_y, color = 'yellow')
axs[0].set_title('Camino')
axs[0].set_aspect('equal')


axs[1].plot(time_values, x_values, label='Posición X')
axs[1].plot(time_values, y_values, label='Posición Y')
axs[1].plot(time_values, or_values, label='Orientación')
axs[1].scatter(p1_time, p1_x, color = 'red')
axs[1].scatter(p2_time, p2_x, color = 'green')
axs[1].scatter(p3_time, p3_x, color = 'yellow')
axs[1].scatter(p1_time, p1_y, color = 'red')
axs[1].scatter(p2_time, p2_y, color = 'green')
axs[1].scatter(p3_time, p3_y, color = 'yellow')
axs[1].set_xlabel('Tiempo')
axs[1].set_ylabel('Valor')
axs[1].set_title('Pose del Robot con respecto al Tiempo')
axs[1].legend()

plt.tight_layout()
plt.show()