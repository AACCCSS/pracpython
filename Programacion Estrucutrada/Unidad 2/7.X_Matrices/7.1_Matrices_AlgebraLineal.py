"""
Proyecto #1 
Proyecto para Mecatrónica  
Análisis de sensores de temperatura 
Cada fila es un sensor. Cada columna una lectura. 

datos = [ 
[24,25,24,26], 
[23,24,25,24], 
[26,27,27,28] 
] 


Que el programa calcule: 
• Promedio por sensor.  prom()
• Sensor más estable.  stable()
• Sensor con mayor temperatura. mayor() 
• Matriz de diferencias respecto al promedio.  diffe()
"""

datos = [ 
    [24, 25, 24, 26], 
    [23, 24, 25, 24], 
    [26, 27, 27, 28] 
] 

# Vector de promedios (lista simple, no lista de listas)
promedios = [0] * len(datos)

# Vector de promedios de ruido
prom_ruido = [0] * len(datos)


def prom():
    """Calcula el promedio de lecturas por sensor."""
    for sensor in range(len(datos)):
        total = 0
        for lectura in range(len(datos[sensor])):
            total += datos[sensor][lectura]
        promedios[sensor] = total / len(datos[sensor])
    
    print("Promedios por sensor:")
    for i, p in enumerate(promedios):
        print(f"  Sensor {i+1}: {p:.2f}")
    
    return promedios


def stable():
    """Encuentra el sensor más estable (menor promedio de ruido)."""
    menor_ruido = float('inf')
    sensor_n = 0

    for sensor in range(len(datos)):
        total_dif = 0
        
        for lectura in range(len(datos[sensor]) - 1):
            dif = abs(datos[sensor][lectura] - datos[sensor][lectura + 1])
            total_dif += dif
        
        prom_ruido[sensor] = total_dif / (len(datos[sensor]) - 1)
        
        if prom_ruido[sensor] < menor_ruido:
            menor_ruido = prom_ruido[sensor]
            sensor_n = sensor
    
    print(f"\nSensor más estable: Sensor #{sensor_n + 1}")
    print(f"Promedio de ruido por sensor: {[round(r, 2) for r in prom_ruido]}")
    
    return sensor_n


def mayor():
    """Encuentra el sensor con la mayor temperatura promedio."""
    prom()  # Calcular promedios primero
    
    mayor_temp = promedios[0]
    sensor_n = 0
    
    for sensor in range(1, len(promedios)):
        if promedios[sensor] > mayor_temp:
            mayor_temp = promedios[sensor]
            sensor_n = sensor
    
    print(f"\nSensor con mayor temperatura: Sensor #{sensor_n + 1}")
    print(f"Temperatura promedio: {mayor_temp:.2f}")
    
    return sensor_n


def diffe():
    """Genera una matriz de diferencias respecto al promedio."""
    prom()  # Calcular promedios primero
    
    print("\nMatriz de diferencias respecto al promedio:")
    for sensor in range(len(datos)):
        diferencias = []
        for lectura in range(len(datos[sensor])):
            diff = datos[sensor][lectura] - promedios[sensor]
            diferencias.append(round(diff, 2))
        print(f"  Sensor {sensor + 1}: {diferencias}")
    
    return None


# Ejecutar todas las funciones
print("=" * 40)
print("ANÁLISIS DE SENSORES DE TEMPERATURA")
print("=" * 40)

prom()
stable()
mayor()
diffe()
