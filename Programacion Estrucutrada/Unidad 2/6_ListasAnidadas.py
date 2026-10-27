# Matriz como lista anidada

matriz =  [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Imprime toda la matriz
print(matriz)

# Imprime un elemento de la matriz
print(matriz[1][2])

# Recorriendo matriz
for fila in matriz:
    for elemento in fila: 
        print(elemento,end=" ")
    print()
