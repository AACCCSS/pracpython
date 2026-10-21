"""
======== 4. Coordenadas de un brazo robótico ======== 
Enunciado:

Utiliza una tupla para almacenar la posición de un brazo robótico en tres ejes:

(X, Y, Z)

El programa debe:

Mostrar las coordenadas.
Determinar cuál eje tiene el valor más alto.
Calcular la suma total de desplazamientos.
"""

posicion = (3,4,2)

# Posicion
print(posicion)

# Recorre todas la tupla para encontrar eje mayor y sumar valores
indice = 0
mayor = max(posicion)
sum =0 

for i in range(len(posicion)):
    # Obtener valor de posición
    if(posicion[i]==mayor):
        indice = i
    # Suma posiciones
    sum = sum + posicion[i]

match(indice): 
    case 0: 
        print("El eje con mayor valor es: X con valor: ",mayor)
    case 1: 
        print("El eje con mayor valor es: Y con valor: ",mayor)
    case 2: 
        print("El eje con mayor valor es: Z con valor: ",mayor)


print("Suma total de desplazamientos: ",sum)


