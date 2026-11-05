"""

Ejercicio 5. Sistema básico de decisión para un robot

Los sensores detectan:

 

[

[1],

[0],

[1]

]

Los pesos asignados a los sensores son:

 

[

[0.5, 1.0, 0.5]

]

Se pide:

Crear las matrices correspondientes.
Calcular la salida mediante multiplicación matricial.
Interpretar qué significa el resultado obtenido.
Cambiar un sensor a 1 y analizar qué ocurre.
 

Ejercicio 6. Producción industrial

Una máquina produce diariamente:

 

[

[10,5],

[8,7],

[12,4]

]

Las columnas representan:

Producto A
Producto B
Los precios son:

 

[

[50],

[80]

]

Se pide:

Calcular los ingresos diarios.
Determinar qué día tuvo mayores ingresos.
Calcular el ingreso total de los tres días.
Obtener el ingreso promedio diario.


"""
import numpy as np

# Producción diaria: cada fila es un día, columna 0 = Producto A, columna 1 = Producto B
produccion = np.array([
    [10, 5],
    [8, 7],
    [12, 4]
])

# Precios: Producto A = 50, Producto B = 80
precios = np.array([
    [50],
    [80]
])

# 1. Calcular los ingresos diarios
# Para cada día: (cantidad A * precio A) + (cantidad B * precio B)
ingresos_diarios = np.dot(produccion, precios)

print("Ingresos diarios:")
print(ingresos_diarios)

# 2. Determinar qué día tuvo mayores ingresos
dia_mayor = np.argmax(ingresos_diarios)
mayor_ingreso = ingresos_diarios[dia_mayor]
print(f"\nDía con mayores ingresos: Día {dia_mayor + 1}")
print(f"Ingreso: ${mayor_ingreso}")

# 3. Calcular el ingreso total de los tres días
ingreso_total = np.sum(ingresos_diarios)
print(f"\nIngreso total de los tres días: ${ingreso_total}")

# 4. Obtener el ingreso promedio diario
ingreso_promedio = np.mean(ingresos_diarios)
print(f"Ingreso promedio diario: ${ingreso_promedio}")
