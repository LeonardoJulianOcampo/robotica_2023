#!/usr/bin/env python

"""
Nodo para comandar un robot de tracción diferencial
"""

import rospy
from geometry_msgs.msg import Twist

class Squarepath:
    """ Clase del nodo """

    def __init__(self):
        """ Constructor """

        # Publicador de comandos de velocidad
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

        # Se registra la función para fijar v=0 al finalizar
        rospy.on_shutdown(self.stop_robot)

        # Función de ejecución del camino
        self.square_path()

    def square_path(self):
        """ Función de ejecución del camino """

        rospy.loginfo('Ejecutando el camino...')

        # Espera a que se establezca la conexión
        n_sub = self.pub.get_num_connections()
        while n_sub == 0:
            rospy.loginfo('Esperando conexión')
            rospy.sleep(1.0)
            n_sub = self.pub.get_num_connections()

        # Completar el código
        vel = Twist()
        count = 0
        while(count < 4):
            vel.linear.x = 1.0 #setea velocidad lineal en 1 m/s
            vel.angular.z = 0.0 #velocidad angular en 0 debido a que recorre un tramo derecho
            self.pub.publish(vel) #publicación del mensaje tipo Twist en el tópico /cmd_vel
            rospy.sleep(2.0) #delay de 2 segundos que establece el tiempo de recorrido

            vel.linear.x = 0.0 #seteo ambas velocidades en 0 para realizar el giro de 90°
            vel.angular.z = 0.0 
            self.pub.publish(vel)
            rospy.sleep(0.5)

            vel.linear.x = 0.0 
            vel.angular.z = 0.785 # en rad/seg, establezco el giro de 90° en 2 segundos 
            self.pub.publish(vel)
            rospy.sleep(2)

            vel.linear.x = 0.0 
            vel.angular.z = 0.0 # en rad/seg, establezco el giro de 90° en 2 segundos 
            self.pub.publish(vel)
            rospy.sleep(0.5)
            count+1

        # FIN: fija velocidad 0
        rospy.loginfo('Stop')
        self.pub.publish(Twist())

    def stop_robot(self):
        """ Detiene el robot al finalizar el programa """
        rospy.loginfo('Stop!')
        self.pub.publish(Twist())

if __name__ == '__main__':
    rospy.init_node('square_path')
    Squarepath()
    rospy.spin()
