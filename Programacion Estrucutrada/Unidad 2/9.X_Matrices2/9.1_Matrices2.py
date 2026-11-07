"""

Mecatrónica

Ejercicio 1. Calibración de sensores

Un robot móvil tiene tres sensores de distancia que reportan las siguientes mediciones:
[20, 15, 30]

Los factores de calibración para cada sensor son:
[1.1, 0.9, 1.05]

Se pide:
Crear ambos vectores utilizando NumPy.-ok 
Obtener las lecturas calibradas. - ok
Mostrar el promedio de las lecturas calibradas. - ok
Identificar cuál sensor tiene la lectura calibrada más alta. 
 
"""

import numpy as np

a = np.array([])

sensor_distancia = np.array([20,15,30])
sensor_calibracion = np.array([1.1,0.9,1.05])
sensores_calibrados = np.array([0,0,0])

sensores_calibrados = sensor_calibracion*sensor_distancia


print("Lecturas calibrasdas: \n",sensor_calibracion*sensor_distancia)


mayor = 0

for i in range(len(sensores_calibrados)):
    print(sensores_calibrados[i])
    if(mayor < sensores_calibrados[i]):
        mayor = sensores_calibrados[i]

print("Valor mayor: ",mayor)
