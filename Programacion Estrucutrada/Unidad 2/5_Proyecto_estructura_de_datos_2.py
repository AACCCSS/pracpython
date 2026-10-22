"""
 ================ 5. Proyecto integrador (más retador) ================ 
Control de una banda transportadora inteligente

Crear un menú que permita:

Registrar piezas producidas (lista).
Mostrar sensores instalados (tupla).
Administrar información de la banda (diccionario).
Mostrar reportes.
Salir.
Este proyecto debe usar:

Variables
Condicionales
Ciclos
Funciones
Listas
Tuplas
Diccionarios

"""
# De la función Registrar pieza: 
piezas = []


# De la función Mostrar sensores:
sensores = ("Sensor de metal", "Sensor capacitivo","Sensor de velocidad", "Sensor de temperatura", "Sensor de humedad")

# De la función administrar info que registra los objetos dentro de la banda
banda = {
    "Piezas":piezas,
    "Sensores":sensores
}






# Iteradamente e indefinidamente solicitar el ingreso de la producción
# Utiliza ciclo while para ingreso con el uso de try catch error para indicar terminacion de ingreso de piezas
# Implementa un conteo de piezas para llevar el registro de 
def registra_pieza():
    conteo_piezas = 0
    while(True):
        print(" ===== Ingrese numero de piezas producidas por ===== ")
        print("Indique el final con una lerta cualquiera")
        
        try:
            op = int(input())
            piezas.append(op)
            conteo_piezas = conteo_piezas + 1

        except ValueError:
            print("Terminando ingreso de piezas\n")
            break


# Imprime toda la tupla de sensores
def mostrar_sensores():
    print("========== Imprimiendo sensores en la banda ========== ")
    print(sensores)



# Implementación de administración de piezas, pudiendo modificar las cantidades de los registros
# Asegura que se hallan agregado piezas antes de modifiar comparando el tamaño de la lista piezas menor a 1
# Implementa bandera para asegurar que el valor sea correcto implmeneta try y except para no romper el programa mientras se ingresa un valor no valido
# Se tiene en consideracion -1 unidad en el valor que eliga el usuario modificar para que coincida con la enumeración 1234, y no 0123
# Mensaje de registro modificado
def administra_info():
    print("\n ======= Piezas producidas =======")
    
    if(len(piezas)<1):
        print("Sin registro para leer!! ")
        
    else: 
        bandera_valido = False # Valor ingresado válido.
        while(not bandera_valido):
            print(piezas)
            try:
                
                op = int(input("Seleccione que valor de la producción desea modificar : ")) -1 
                if( op>=len(piezas)):
                    print("Valor fuera de rango, intente con un valor menor a ",len(piezas)-1)
                else:
                    nue = int(input("Ingrese nuevo valor: "))
                    piezas[op] = nue
                    bandera_valido = True
            

            except ValueError:
                print("Ingrese un valor válido")
                bandera_valido = False

            print("Registro modificado! \n")
            if(bandera_valido):
                break
            

    
# Muestra el valor de piezas producidas, asegurandose que no imprima una lista vacia con la condicional de que longitud de lista de piezas no sea menor a 1. 
# Muestra el valor de sensores
def mostrar_reporte():
    print("==== Mostrando reporte ====")
    print("Piezas producidas: ")
    if(len(piezas)<1):
        print("Sin registros")
    else:
        print(banda["Piezas"])
        
    print("Sensores en banda: ")
    print(banda["Sensores"])


# Ciclo principal 
# muestra opciones a elegir que llama las funciones asignadas
# uso de try except para controlar mejor las entradas validas
# uso de match para controlar la selección del usuario

while(True): 
    
    print(" ======= Menu principal =======  ")
    print("1. Registrar piezas producidas")
    print("2. Mostrar sensores instalados")
    print("3. Administración información de la banda")
    print("4. Mostrar reportes")
    print("5. Salir")

    try: 
        op = int(input("\n Ingrese selección: "))

        match(op): 
            case 1:
                registra_pieza()
            case 2: 
                mostrar_sensores()
            case 3: 
                administra_info()
            case 4:
                mostrar_reporte()
            case 5: 
                print("Saliendo")
                break

    except ValueError: 
        print("\n Porfavor, ingrese numeros indicados en el menu!!!! \n")