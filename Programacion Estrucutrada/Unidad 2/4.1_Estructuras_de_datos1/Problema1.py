# Proyecto estrucutra de datos 1


## Recordatorio: 
### Tuplas ()
### Diccionarios {}
### Listas []

"""
================= Programa 1 =================
Registro de temperaturas de motores ingresado por el usuario
Desarrolla programa que:
Almacene (lista)  temperaturas registradas de 10 motores industriales. 

Funciones:
Mostar() - Mostrar todas las temperaturas.
Promedio() - Calcular el promedio.
MaxMin() - Indicar la temperatura más alta y la más baja.
MayorLimite() - Contar cuántos motores superan los 80°C.
"""


temp_motor = []
def M_IngreseTemperatura():
    for i in range(10):
        print("Ingrese el valor del motor: ",i+1)
        op = int(input(""))
        temp_motor.append(op)
            

def Mostrar():
    print(temp_motor)

def Promedio():
    sum = 0
    for i in range(10):
        sum += temp_motor[i]
    print("Promedio: ", sum/10)

def MaxMin():
    print("Motor con maxima temperatura: ",max(temp_motor))
    print("Motor con minima temperatura: ",min(temp_motor))

def Mayor_lim():
    print("Motores con temperatura mayor a 80: ")
    for i in range(10):
        if(temp_motor[i]>80):
            print("Motor# ",i) 
            print("Temperatura: ",temp_motor[i])


M_IngreseTemperatura()
Mostrar()
Promedio()
MaxMin()
Mayor_lim()


    




