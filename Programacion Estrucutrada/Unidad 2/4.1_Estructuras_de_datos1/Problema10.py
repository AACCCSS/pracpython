"""

========== 10. Sistema de inspección de calidad ==========
Enunciado:

Desarrolla un programa que utilice:

Una lista para almacenar las medidas de 10 piezas.
Una tupla para guardar las tolerancias máximas y mínimas.
Un diccionario para almacenar el resultado final.
El sistema debe:

Verificar si cada pieza cumple la tolerancia.
Contar piezas aceptadas y rechazadas.
Guardar el resultado en un diccionario.
Mostrar un reporte final.

"""

medidas = [4.97,4.98,4.99,5,5.001,5.01,5.1,5.2,5.3,5.4,5.6]

Medida_estandar = 5

tolerancia = (0.2,0.01) # Tolerancias: (Maxima,Minima), es decir, pieza con máximo +0.2, con mínimo de -0.01
limite_superior = Medida_estandar+tolerancia[0] # Maximo que alcanza arriba
limite_inferior = Medida_estandar-tolerancia[1] # Minimo que debe alcanzar abajo


resultado = {
    "aceptado":0,
    "rechazado":0
}



# Verifica tolerancia de piezas y guardando resultados en diccionario


print("Verificando tolerancia de las piezas: ")
for i in range(len(medidas)):
    print(f"Checando pieza# {i}, Tolerancia maxima:{limite_superior}, Tolerancia minima: {limite_inferior}, Valor de pieza actual: {medidas[i]}")
    if(medidas[i]<= limite_superior):
        if(medidas[i]>= limite_inferior):
            print(f"Pieza#{i} dentro de tolerancias")
            resultado["aceptado"] = resultado["aceptado"] + 1
        else:
            print(f"Pieza# {i} fuera de rango! ")
            resultado["rechazado"] = resultado["rechazado"] +1

    else:
        print(f"Pieza# {i} fuera de rango! ")
        resultado["rechazado"] = resultado["rechazado"] +1
    print("\n")

# Retornar piezas y reporte final:
print("Reporte final:  ")
print("Cantidad de piezas aceptadas: ",resultado["aceptado"])
print("Cantidad de piezas rechazadas: ",resultado["rechazado"])