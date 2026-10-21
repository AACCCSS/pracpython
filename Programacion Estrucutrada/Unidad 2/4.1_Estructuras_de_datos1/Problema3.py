"""
======== 3. Catálogo de sensores de una estación automática ========
Enunciado:

Crea una tupla () 
Con nombres de los sensores instalados en una estación automatizada:

Temperatura
Humedad
Proximidad
Ultrasonido
Presión
El programa debe:

Mostrar todos los sensores.
Permitir buscar un sensor.
Mostrar cuántos sensores contiene la estación."""

Sensores = (
    "Temperatura",
    "Humedad",
    "Proximidad", 
    "Ultrasonido",
    "Presion"
)
print(Sensores)

op = int(input("Ingrese el numero de sensor que desee consultar: "))
print(Sensores[op])

print("La estacion contiene: {0} sensores".format(len(Sensores)))