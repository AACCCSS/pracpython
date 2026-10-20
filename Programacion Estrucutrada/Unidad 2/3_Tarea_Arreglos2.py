
"""
# Control de temperaturas de motores
## Se manejan dos vectores:
### motores: nombres o códigos de los motores.
### temperaturas: temperatura registrada en cada motor.

## El programa permite:
### Dar de alta motores.
### Consultar la temperatura de un motor.
### Mostrar reportes de temperatura máxima, mínima y promedio.
"""
# Menu de seleccion, registro y operaciones de motores

# 2 Vectores: 
## Motores
## Temperatura

# Funciones: 
## 1 Dar de alta (Usa .append)
## 2 Consulta temperatura de un motor 
## 3 Mostrar reporte: 
    ### Temperatura Máxima
    ### Temperatura Mínima
    ### Temperatura Promedio
## 4 Dar de baja motor (Usa .pop)


motores = []
temperatura = []


def alta_motor ():
    nuevo_motor = int(input("Ingrese Id del motor: "))
    motores.append(nuevo_motor)

    nueva_temperatura = input("Ingrese el valor de la temperatura: ")
    temperatura.append(nueva_temperatura)

def consulta_motor():
    consulta = int(input("Ingrese el numero del motor a consultar: "))
    print("Motor: {0}".format(motores[consulta-1]))
    print("Temperatura: {0}".format(temperatura[consulta-1]))

def reporte_motor():
    
    for i in range(len(motores)):
        print("Motor id: {0}".format(motores[i]))
        print("Temperatura: {0}".format(temperatura[i]))
    print("\n")

def baja_motor():
    baja = int(input("Ingrese el numero de motor a borrar: "))
    motores.pop(baja-1)
    temperatura.pop(baja-1)

while(True):
    print(" ======== Menu principal ======== ")
    print("1. Dar de alta")
    print("2. Consulta temperatura de motor")
    print("3. Mostrar reporte")
    print("4. Dar de baja de motor")
    print("5. Salir")
    op = int(input("Ingrese opción:"))
    print("\n")

    match op: 
        case 1:
            alta_motor()
            print("\n")
        case 2: 
            consulta_motor()
            print("\n")
        case 3: 
            reporte_motor()
            print("\n")
        case 4:
            baja_motor()
            print("\n")
        case 5: 
            print("Fin de programa")
            break

    
