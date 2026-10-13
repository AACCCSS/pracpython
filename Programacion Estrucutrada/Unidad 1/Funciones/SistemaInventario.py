    # Sistema inventario de refacciones industriales

    # Python, administra inventario en empreas industrial. 
    # Usa funciones, parametros, valores de retorno. 

    # Empresa dedicada al mantenimiento de maquinaria industrial almacena: 

    # Variables: Tornillos, tuercas, sensores, motores, bandas_transportadoras. 

    # Necesita un sistema que le permita registrar entradas de material.
    # Necesita consulta existencias.
    # Necesita generar reportes de inventario.


    # Formato  del menu: (def_menu()) OK
    # 1 Alta de inventario inicial 
    # 2 Entrada de articulos
    # 3 Salida de articulos 
    # 4 Consulta de existencias
    # 5 Reporte general 
    # 6 Salir

    # Funciones: 
    # Alta de inventario incial.  (def alta_inventario() ) Ok
    #    Ingreso de cantidades de tornillos, tuercas, sensores, motores, bandas transportadoras. 

    # Entradas de articulos. (def entrada_articulos() ) ok
    #    Selecciona un articulo 
    #    Registra cantidad que ingresa al almacen. 

    # Salida de articulos (def salida_articulos()) ----
    #    Selecciona articulo
    #    Registra cantidad que sale

    # Consulta Existencias (def consulta_existencias() ) ok
    # Muestra cantidades de todos los articulos  
    # Ejemplo: Tornillos: 150
    # Tuercas: 120
    # Sensores: 25
    # Motores: 10
    # Bandas: 5

    # Reporte general ( def reporte_general() )
    # Muestra:  Qty, total, status
    #   Existencia de cada articulo
    #   Total general de piezas almacenadas
    #   Estado del inventario Si es menor a 20 piezas (critico, no critico)





    #####  Ejemplo:
    #####  Existencia actual: 20
    #####  Cantidad a retirar: 25
    #####     Error, Existencia insuficiente
    #####  Candidad a ingresar: 24







# ==================== Funcion Menu ======================= 
# 1 Alta de inventario inicial 
# 2 Entrada de articulos
# 3 Salida de articulos 
# 4 Consulta de existencias
# 5 Reporte general 
# 6 Salir



global tornillos, tuercas, sensores, motores, bandas_transportadoras

def menu():
    opcion = int(input("\n\nSeleccione una opción: \n[1] Alta de inventario iventario inicial.\n[2] Entrada de articuos.\n[3] Salida de articulos.\n[4] Consulta de existencias.\n[5] Reporte general.\n[6] Salir.\n"))
    match opcion:
        case 6: 
            return 0
        case 5: 
            reporte_general()
            return 1
        case 4: 
            consulta_existencias()
            return 1
        case 3: 
            salida_articulos()
            return 1
        case 2: 
            entrada_articulos()
            return 1
        case 1: 
            alta_inventario()
            return 1
        case default:
            print("Ingree nuevamente la selección, opcion no disponible.") 
            return 1
        


def alta_inventario():
    global tornillos, tuercas, sensores, motores, bandas_transportadoras 

    tornillos = int(input("\nIngrese el valor de tornillos inicial: "))
    tuercas = int(input("\nIngrese el valor de tuercas inicial: "))
    sensores = int(input("\nIngrese valor de sensores: "))
    motores = int(input("\nIngrese valor de motores: "))
    bandas_transportadoras = int(input("Ingrese el valor de bandas transportadoas "))
    consulta_existencias()
    
def entrada_articulos():
    global tornillos, tuercas, sensores, motores, bandas_transportadoras 
    seleccion = int(input("Seleccione el articulo:\n[1] tornillos\n[2] tuercas\n[3] sensores\n[4] motores\n[5] bandas_transportadoras\n[6] Salir"))

    match seleccion: 
        case 1: 
            tornillos = tornillos+int(input("Valor a adicionar: "))
        case 2: 
            tuercas=tuercas+int(input("Valor a adicionar: "))
        case 3: 
            sensores=sensores+int(input("Valor a adicionar: "))
        case 4: 
            motores=motores+int(input("Valor a adicionar: "))
        case 5:
            bandas_transportadoras =bandas_transportadoras +int(input("Valor a adicionar: "))
        case 6: 
            print("Cerrando...\n")

# Complemento para Resta y no restar numeros negativos.
def verificacion_resta(a,b):
    # A es valor de base, B es la resta
    c = a-b
    if(c<0):
        print("Error, Existencia insuficiente")
        return 0
    else: 
        return c

def salida_articulos():
    global tornillos, tuercas, sensores, motores, bandas_transportadoras 
    seleccion = int(input("\nSeleccione el articulo:\n[1] tornillos\n[2] tuercas\n[3] sensores\n[4] motores\n[5] bandas_transportadoras\n[6] Salir"))
    
    match seleccion: 
        case 1: 
            sustrayendo = int(input("Valor a restar: "))
            tornillos = verificacion_resta(tornillos,sustrayendo)
        case 2: 
            sustrayendo = int(input("Valor a restar: "))
            tuercas=verificacion_resta(tuercas,sustrayendo)
        case 3: 
            sustrayendo = int(input("Valor a restar: "))
            tuercas=verificacion_resta(tuercas,sustrayendo)
        case 4: 
            sustrayendo = int(input("Valor a restar: "))
            sensores=verificacion_resta(sensores,sustrayendo)
        case 5:
            sustrayendo = int(input("Valor a restar: "))
            motores=verificacion_resta(motores,sustrayendo)
        case 6: 
            print("Cerrando...\n")   
  
def consulta_existencias():
    global tornillos, tuercas, sensores, motores, bandas_transportadoras
    print(f"Inventario incializado\nTornillos: {tornillos}\nTuercas: {tuercas}\nSensores: {sensores}\nMotores: {motores}\nBandas transportadoras: {bandas_transportadoras}")

#no hay macros
def reporte_general():
    sum = tornillos+tuercas+sensores+motores+bandas_transportadoras

    print(f"\nTotal de piezas: {sum}")
    print("Piezas criticas (menor a 20): ")
    
    if(tornillos<20):
        print(f"Tornillos: {tornillos}")

    if(tuercas<20):
        print(f"Tuercas: {tuercas}")

    if(sensores<20):
        print(f"sensores: {sensores}")

    if(motores<20):
        print(f"motores: {motores}")

    if(bandas_transportadoras <20):
        print(f"bandas_transportadoras : {bandas_transportadoras }")

    

while(True):
    if(not int(menu())):
        break

    