# Control de Calificaciones(leer 3 sacar promedio y decir si aprobo o reprobo)

calificacion1 = int(input("Ingrese calificacion 1: "))
calificacion2 = int(input("Ingrese calificacion 2: "))
calificacion3 = int(input("Ingrese calificacion 3: "))

promedio = (calificacion1+calificacion2+calificacion3)/3

if(promedio >=70):
    print("Promedio aprobatorio, su calificacion es de: ",promedio)
if(promedio<70): 
    print("Promedio NO aprobatorio, su calificacion es de: ",promedio)

print("Fin de programa")
