"""

Ejercicio 4. Transformación de posiciones de un brazo robótico

Las posiciones de tres articulaciones son:
[
[10],
[20],
[30]
]

La matriz de transformación es:
[
[1,0,0],
[0,2,0],
[0,0,3]
]

Se pide:
Crear la matriz de transformación.
Crear el vector de posiciones.
Realizar la multiplicación matricial.
Mostrar las nuevas posiciones obtenidas.
Explicar qué efecto tiene la matriz sobre cada articulación.
 
"""

import numpy as np

# 1. Crear la matriz de transformación
matriz_transformacion = np.array([
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]
])

# 2. Crear el vector de posiciones (como columna, forma 3x1)
posiciones = np.array([
    [10],
    [20],
    [30]
])

# 3. Realizar la multiplicación matricial
nuevas_posiciones = np.dot(matriz_transformacion, posiciones)

# 4. Mostrar las nuevas posiciones
print("Matriz de transformación:")
print(matriz_transformacion)
print("\nVector de posiciones original:")
print(posiciones)
print("\nNuevas posiciones:")
print(nuevas_posiciones)
