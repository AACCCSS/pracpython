"""
=============== 7. Producción diaria de una celda robotizada =============== 
Enunciado:

Almacena en una lista la cantidad de piezas producidas durante 7 días.

El programa debe:

Mostrar la producción de cada día.
Calcular la producción total.
Calcular el promedio de producción.
Identificar el día más productivo.

"""

Produccion_diaria = []
sum = 0


# Recorrido para ingresar valores segun los numeros del dia
for i in range(7): 
    print("Ingrese la cantidad de piezas producidas del dia: ", i+1)
    op = int(input())
    Produccion_diaria.append(op)
    sum = sum + Produccion_diaria[i]
print("\n")


# Mostrar producción de cada dia:
print("Producción de cada dia:")
print(Produccion_diaria)

# Calcula produccion total:
print("Producción total: ",sum)

# Calcula promedio de producción
print("Promedio de la producción: ",round(sum/7,2))

# Identifica dia mas productivo
print("El dia más productivo fue el dia# ",max(Produccion_diaria))

# Indica la cantidad de produccion mayor
op = 0
for i in range(7):
    if (Produccion_diaria[i] == max(Produccion_diaria)):
        op = i
print("Con un valor de: ",Produccion_diaria[op])

