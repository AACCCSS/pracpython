"""

Ejercicio 2. Control de velocidad de motores
Un sistema tiene tres motores con velocidades iniciales:
[100, 150, 200]

Se desea aumentar la velocidad de cada motor en:

 

[20, 20, 20]

Se pide:

Crear ambos vectores.
Obtener las nuevas velocidades.
Mostrar la velocidad máxima.
Mostrar la velocidad mínima.
Calcular la velocidad promedio.
 
"""

import numpy as np

# Vectores
velocidades = np.array([100,150,200])
incremento = np.array([20,20,20])

#Nuevas velocidades: 
n_velocidades = np.array([0,0,0])
n_velocidades = velocidades*incremento
print("N velocidades: ",n_velocidades)


# Velocidad maxima: 
print("velocidad maxima:",n_velocidades.max())

# Velocidad minima: 
print("Velocidad minima: ",n_velocidades.min())

# Velocidad promedio: 
print("Velocidad promedio",n_velocidades.mean())


