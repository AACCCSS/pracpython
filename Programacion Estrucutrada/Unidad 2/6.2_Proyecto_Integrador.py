"""
========= Proyecto Integrador para los Alumnos =========

========= * ========= Monitoreo de una Línea de Producción de Semiconductores ========= * =========

Situación 
Una planta registra la temperatura de 4 hornos durante 5 días.
Cada fila representa un horno.
Cada columna representa un día.

X       | Día1 | Día2 | Día3 | Día4 | Día5
        |------------------------------
Horno1  |
Horno2  |
Horno3  |
Horno4  |



El programa debe:

-> Capturar las temperaturas.  // h_captura()
    ├── Guardarlas en una matriz.  

-> Mostrar la matriz completa. // h_mostrar() 
-> Calcular la temperatura promedio de cada horno. // h_prom_temp()
-> Encontrar la temperatura máxima registrada. // h_max_temp()
-> Determinar qué horno tuvo la temperatura promedio más alta. // h_max_prom_temp()
-> Mostrar el promedio general de toda la planta. // h_prom_todo()


Ejemplo de salida
Promedio Horno 1: 205.4 °C
Promedio Horno 2: 198.6 °C
Promedio Horno 3: 210.8 °C
Promedio Horno 4: 203.2 °C

Temperatura máxima: 225 °C

Promedio general: 204.5 °C

Horno con mayor promedio: Horno 3

"""


temperatura = [
   [210,205,208,212,215],
   [198,200,195,202,199],
   [220,225,218,222,219],
   [205,207,203,206,204] 
]

for horno in range(4): 
    fila = []
    for dia in range(5):
        temp = float(input(f"Horno: {horno+1},Dia: {dia+1}"))
        fila.append(temp)    
    temperatura.append(fila)


print("Matriz de temperaturas: ")

for fila in temperatura: 
    print(fila)


# Promedios

