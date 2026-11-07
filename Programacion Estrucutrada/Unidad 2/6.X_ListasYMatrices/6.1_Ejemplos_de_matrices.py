"""
Ejemplos matrices

"""
print("\n")
print("\n")
print("\n")

print("\n")
print("\n")
print("\n")
# Ejemplo 1 Sensor toma 3 mediciones 3 momentos distintos

lecturas = [
    [12,15,18],
    [20,22,24],
    [30,32,35]
]

print(lecturas)


# Ejemplo 2: 
voltajes = [
    [3.3,5.0,12.0],
    [3.1,4.9,11.8],
    [3.4,5.,12.2]
]

print("Voltaje 1:", voltajes[0][0])
print("Voltaje central:", voltajes[1][1])
print("Último voltaje:", voltajes[2][2])

# Ejemplo 3:
temperaturas = [

[180, 185, 190],
[195, 200, 205],
[210, 215, 220]
]

for fila in temperaturas:
    for dato in fila:
        print(dato, end=" ")
    print() 


# Ejemplo 4 Consumo de Corriente de un Robot
corriente = [
[2, 3, 1],
[4, 2, 5],
[3, 1, 2]
]

suma = 0
for fila in corriente:
    for dato in fila:
        suma += dato

print("Consumo total:", suma)


# Ejemplo  5 Buscar el Valor Máximo de un Sensor

presion = [
[12, 15, 18],
[20, 25, 22],
[19, 17, 14]
]

mayor = presion[0][0]

for fila in presion:
   for dato in fila:
        if dato > mayor:
            mayor = dato

 

print("Máxima presión:", mayor)