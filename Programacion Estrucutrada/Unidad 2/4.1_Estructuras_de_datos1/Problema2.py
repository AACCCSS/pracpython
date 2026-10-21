"""
========= 2. Control de velocidades de un robot móvil =========
Enunciado:

Almacena en una lista
Velocidades registradas por un robot durante 8 recorridos.

El programa debe:

Mostrar cada velocidad.
Determinar la velocidad máxima.
Determinar la velocidad mínima.
Indicar cuántas veces el robot superó los 3 m/s.
"""

# Lista que almacena las velocidades:
Velocidad_recorridos = []

# Recorrido que solicita las velocidades: 
for i in range(8):
        print("Ingrese el valor de velocidad en recorrido: ",i+1)
        op = int(input(""))
        Velocidad_recorridos.append(op)

print("\n ")
# Imprimir lista
print(Velocidad_recorridos)

# Calulando promedio, usa sum para guardar valores
sum = 0
for i in range(8):
    sum += int(Velocidad_recorridos[i])
print("Promedio: ", sum/8)


# Maximos y minimos
print("Velocidad máxima registrada: ",max(Velocidad_recorridos))
print("Velocidad minima registrada: ",min(Velocidad_recorridos))

# Superacion de limite
print("Velocidades registradas con velocidad mayor a 3m/s: ")
for i in range(8):
    if(Velocidad_recorridos[i]>3):
        print("Recorrido#",i) 
        print("Velocidad:",Velocidad_recorridos[i])
        
        