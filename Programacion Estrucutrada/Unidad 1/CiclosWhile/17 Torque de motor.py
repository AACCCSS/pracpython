# 17 Torque de motor: pedir valores hasta que torque sea menor a 50 Nm.



t=100 # Torque


while (t>50):
    t = int(input("Ingrese el valor del torque: "))

print("Torque ejercido es menor a 50. \n Programa terminado...")