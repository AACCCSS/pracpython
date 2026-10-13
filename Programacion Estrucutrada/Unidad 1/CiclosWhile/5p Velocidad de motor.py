# 5 Velocidad de motor: pedir rpm hasta que sea menor a 3000.

RPM = 3200

while (RPM>=3000):
    print("Reduciendo RPM, RPM actual:",RPM)
    RPM = int(input("Ingrese lectura de RPM: "))

print("Fin de desaceleracion...")