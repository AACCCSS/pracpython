import math

# P2 Conversion de unidades rectangulares a polar

# Conversion de Unidades rectangulares a polares 

#Ingrese Z1, Z2. Que quiere hacer con estas operaciones?


# Solicitando Z1. 
x = int(input("Ingrese el valor real de Z1:"))
i = int(input("Ingrese el valor imaginario (i) de Z1: "))


r = ((x**2+i**2)**1/2)
theta = math.atan(i/x)

print("Su forma polar: {0} ∠ {1}".format(r,round(theta,3)))
