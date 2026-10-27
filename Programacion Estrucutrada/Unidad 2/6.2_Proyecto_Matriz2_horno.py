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

temperaturas = []

# Captura de datos
for horno in range(4):
    fila = []

    for dia in range(5):
        temp = float(input(f"Horno {horno+1}, Día {dia+1}: "))
        fila.append(temp)

    temperaturas.append(fila)

print("\nMATRIZ DE TEMPERATURAS")

for fila in temperaturas:
    print(fila)

# Promedios por horno
promedios = []

for i in range(4):
    promedio = sum(temperaturas[i]) / len(temperaturas[i])
    promedios.append(promedio)
    print(f"Promedio Horno {i+1}: {promedio:.2f} °C")

# Temperatura máxima
maxima = temperaturas[0][0]

for fila in temperaturas:
    for temperatura in fila:
        if temperatura > maxima:
            maxima = temperatura

print(f"\nTemperatura máxima: {maxima:.2f} °C")

# Promedio general
suma = 0
cantidad = 0

for fila in temperaturas:
    for temperatura in fila:
        suma += temperatura
        cantidad += 1

promedio_general = suma / cantidad

print(f"\nPromedio general: {promedio_general:.2f} °C")

# Horno con mayor promedio
mayor_promedio = max(promedios)
horno_mayor = promedios.index(mayor_promedio) + 1

print(f"\nHorno con mayor promedio: Horno {horno_mayor}")