
# Guardar variables ram, a futuro será grabar en disco duro.

temp = [10,11,15]
print(temp[2])


# Definción de vector o arreglo unidimencional: Arreglo de 1 fila .
vectores = [1,2,3,4]
print(vectores)



# Recorrer arreglo con ciclos 
temperatura = [22,24,23,25,26]
print("Temperatura:",temperatura)


## Usando ciclo for
for i in range(len(temperatura)):
    print(temperatura[i])
print("End for")

## Usando ciclo while
cc = 0
while(cc in range(len(temperatura))):
    cc=cc+1
    print(temperatura[i])
print("While")


# Sistema de monitorieo de temperaturas
## Programa para cargar datos al vector, imprimir y buscar un dato

temperatura = []
### Condicional si no hay temperaturas registradas. 
##############################
# Sistema de Monitoreo de Temperaturas
temperaturas = []

def alta_temperatura():
    temp = float(input("Ingrese la temperatura: "))
    temperaturas.append(temp)
    print("Temperatura registrada correctamente.\n")

def reporte_temperaturas():
    if len(temperaturas) == 0:
        print("No hay temperaturas registradas.\n")
        return

    print("\n--- REPORTE DE TEMPERATURAS ---\n")
    for i in range(len(temperaturas)):
        print(f"Registro {i + 1}: {temperaturas[i]} °C")

    promedio = sum(temperaturas) / len(temperaturas)
    print(f"\nPromedio: {promedio:.2f} °C")
    print(f"Temperatura máxima: {max(temperaturas)} °C")
    print(f"Temperatura mínima: {min(temperaturas)} °C")
    print()

def buscar_temperatura():
    if len(temperaturas) == 0:
        print("No hay temperaturas registradas.\n")
        return

    buscada = float(input("Ingrese la temperatura a buscar: "))
    encontrada = False
    for i in range(len(temperaturas)):
        if temperaturas[i] == buscada:
            print(f"Temperatura encontrada en el registro {i + 1}")
            encontrada = True

    if not encontrada:
        print("Temperatura no encontrada.")
    print()

while True:
    print("===== MONITOREO DE TEMPERATURAS =====")
    print("1. Dar de alta temperatura")
    print("2. Ver reporte")
    print("3. Buscar temperatura")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        alta_temperatura()
    elif opcion == "2":
        reporte_temperaturas()
    elif opcion == "3":
        buscar_temperatura()
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opción incorrecta.\n")
