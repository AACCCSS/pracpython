"""
Ejercicio 3. Consumo energético de actuadores
Durante tres horas se registra el consumo de energía de tres actuadores.
[
[2,3,1],
[3,2,2],
[4,3,2]
]

Cada fila representa una hora y cada columna un actuador.

Se pide:

Crear la matriz.
Calcular el consumo total del sistema.
Obtener el consumo total de cada actuador.
Obtener el consumo total por hora.
Determinar qué actuador consumió más energía.
 

"""
import numpy as np
# Crear la matriz
Consumo_actuadores = np.array([
[2,3,1],
[3,2,2],
[4,3,2]
])

# Calculo de consumo total del sistema usando np.sum(matriz)
consumo_total = np.sum(Consumo_actuadores)

# Calculo de consumo de cada actuador considerando actuador como filas: 
consumo_actuador1 = np.sum(Consumo_actuadores,axis=1)
print("Consumo Actuador : ",consumo_actuador1)

# Calculo de consumo por hora como columnas. 
consumo_actuador = np.sum(Consumo_actuadores,axis=0)
print("Consumo por hora:",consumo_actuador)

# Cual actuador consume mas energia
print(consumo_actuador1.max())