#Enumeracion de lotes
lote1 = 0; 
lote2 = 0;
lote3 = 0;
lote4 = 0;
lote5 = 0; 

# Declaración de defectos lotes
defecto_lote1 = 0;
defecto_lote2 = 0;
defecto_lote3 = 0;
defecto_lote4 = 0;
defecto_lote5 = 0;


# Clasificacion de lotes 
clasificaciondelote1 = "Sin clasificación" 
clasificaciondelote2 = "Sin clasificación"
clasificaciondelote3 = "Sin clasificación"
clasificaciondelote4 = "Sin clasificación"
clasificaciondelote5 = "Sin clasificación"


# Función de registro de lote más su valor de contaminación


def registrar_lote():
    print(" ======= Registrando lotes ======= ")
    global lote1,lote2,lote3,lote4,lote5
    global defecto_lote1,defecto_lote2,defecto_lote3,defecto_lote4,defecto_lote5

    for i in range(5):
        a = int(input("Ingrese la enumeración de lote# "))

        b = int(input("Ingrese el porcentaje de defecto de lote#"))

        match i:
            case 0: 
                lote1 = a
                defecto_lote1 = b
            case 1: 
                lote2 = a
                defecto_lote2 = b
            case 2: 
                lote3 = a
                defecto_lote3 = b
            case 3: 
                lote4 = a
                defecto_lote4 = b
            case 4: 
                lote5 = a
                defecto_lote5 = b



# Imprime los lotes
def Consultar_lote():
    print(" ======= Consultando lotes ======= ")
    global lote1,lote2,lote3,lote4,lote5
    global defecto_lote1,defecto_lote2,defecto_lote3,defecto_lote4,defecto_lote5

    for i in range(5):
        match i:
            case 0: 
                print("Lote1: ",lote1)
                print("Contaminación: ",defecto_lote1)
                print("Clasificación: ",clasificaciondelote1)
            case 1: 
                print("Lote2: ",lote2)
                print("Contaminación: ",defecto_lote2)
                print("Clasificación: ",clasificaciondelote2)
            case 2: 
                print("Lote3: ",lote3)
                print("Contaminación: ",defecto_lote3)
                print("Clasificación: ",clasificaciondelote3)
            case 3: 
                print("Lote4: ",lote4)
                print("Contaminación: ",defecto_lote4)3
                print("Clasificación: ",clasificaciondelote4)
            case 4: 
                print("Lote5: ",lote5)
                print("Contaminación: ",defecto_lote5)
                print("Clasificación: ",clasificaciondelote5)

# Funcion que optimiza el proceso de clasificar
def clasificar( lote ):
    if(lote<=2):
        return "Excelente"
    elif (lote>2 or lote<=5):
        return "Bueno"
    elif(lote>5 or lote <= 10):
        return "Regular"
    elif(lote>10):
        return "Rechazado"

# Llama funcion que clasifica y lo coloca en el valor de clasificaicón correspondiente al lote
# Si el valor de lote es 0, significa que no se registro por lo que no se evaluara.
def clasificar_lote():
    global clasificaciondelote1, clasificaciondelote2,clasificaciondelote3,clasificaciondelote4,clasificaciondelote5
    global lote1,lote2,lote3,lote4,lote5

    for i in range(5):
        match i: 
            case 0: 
                if(lote1!= 0):
                    clasificaciondelote1= clasificar(defecto_lote1)
                    print(clasificaciondelote1)
            case 1: 
                if(lote2!= 0):
                    clasificaciondelote2= clasificar(defecto_lote2)
                    print(clasificaciondelote2)
            case 2: 
                if(lote3!= 0):
                    clasificaciondelote3= clasificar(defecto_lote3)
                    print(clasificaciondelote3)
            case 3: 
                if(lote4!= 0):
                    clasificaciondelote3= clasificar(defecto_lote4)
                    print(clasificaciondelote4)
            case 4: 
                if(lote5!= 0):
                    clasificaciondelote3= clasificar(defecto_lote5)
                    print(clasificaciondelote5)

      
def mostrar_estadistica():
    global clasificaciondelote1, clasificaciondelote2,clasificaciondelote3,clasificaciondelote4,clasificaciondelote5
    global lote1,lote2,lote3,lote4,lote5   
    sum = 0;
    cc = 0; 
    for i in range(5):
        match i: 
            case 0: 
                if(lote1!= 0):
                    sum = sum+defecto_lote1
                    cc = cc+1
            case 1: 
                if(lote2!= 0):
                    sum = sum+(defecto_lote2)
                    cc = cc+1
            case 2: 
                if(lote3!= 0):
                    sum = sum+(defecto_lote3)
                    cc = cc+1
            case 3: 
                if(lote4!= 0):
                    sum = sum+(defecto_lote4)
                    cc = cc+1
            case 4: 
                if(lote5!= 0):
                    sum = sum+(defecto_lote5)
                    cc = cc+1
    print("Valor promedio de defectos de lotes: ",(sum/cc))



while(True):
    print("Selecciona opcion: ")
    print("1. Registrar lote")
    print("2. Clasificar lotes")
    print("3. Mostrar estadisticas")
    print("4. Consultar lotes")
    print("5. Fin/Salir")
    op = int(input())

    match op:
        case 1: 
            registrar_lote()
        case 2: 
            clasificar_lote()
        case 3: 
            mostrar_estadistica()
        case 4: Consultar_lote()
        case 5: 
            print("Saliendo...")
            break