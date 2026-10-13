import random 
import time



# Requerimientos:

 
# Robot de inpsección
#   [1] Generar datos del robot
#   [2] Consulta estado de batería
#   [3] Consulta temperatura
#   [4] Consulta distancia
#   [5] Reporte general
#   [6] Salir 
# n

# Evaluar_Bateria
def evaluar_bateria(valor): 
    if(valor<20):
            print("Estado:  Critica")
            print("🚨 ALARMA ACTIVADA 🚨")
            print("ESTADO DE LA BATERIA MUY BAJA!!")
    if(valor>20 and valor<60): 
        print("Estado: Advertencia")

    if(valor>60):
         print("Estado: Normal")


# Evaluar_Temperatura 
def evaluar_temperatura(valor):
    if(valor<40):
         print("Estado: Normal")
    if(valor >40 and valor<70):
         print("Estado: ADVERTENCIA!")
    if(valor>70):
         print("Estado: SOBRECALENTAMIENTO!" )
         print("🚨 ALARMA ACTIVADA 🚨")
         print("TEMPERATURA MUY ALTA!")


     
# Evaluación de la distancia
def evaluar_distancia(valor):
    if(valor<20):
        print("Estado: Obstaculo")
        print("🚨 ALARMA ACTIVADA 🚨")
        print(" OBSTACULO OBSTRUYENDO EL CAMINO")
    if(valor >20 and valor<50):
         print("Estado: Precaución")
    if(valor>50):
         print("Estado: Libre")



# Generar bateria

def generar_bateria():
     bateria = random.randint(0,100)
     return bateria


# Generar temperatura
def generar_temperatura():
    temperatura = random.randint(0,150)
    return temperatura

    
# Generar distancia     
def generar_distancia():
     distancia = random.randint(0,70)
     return distancia


# Reporte general
def reporte_general():
     print("Realizando reporte general...    \n")
     bateria = generar_bateria()
     temperatura = generar_temperatura()
     distancia = generar_distancia()

     print("Bateria: ",bateria)
     evaluar_bateria(bateria)
     print("\n")

     print("Temperatura: ",temperatura)
     evaluar_temperatura(temperatura)
     print("\n")

     print("Distancia: ",distancia)
     evaluar_distancia(distancia)
     print("\n")


# Ciclo Menú

def menu():

    seleccion = int(input("[1] Generar datos\n[2] Consultar estado de batería\n[3] Consulta temperatura\n[4] Consulta distancia\n[5] Reporte general\n[6] Salir"))
    print("\n")

    match(seleccion):
        case 1: 
            print("Temperatura:",generar_temperatura())

            print("Bateria:",generar_distancia())

            print("Distancia:",generar_distancia())
            print("\n")

        case 2: 
            print("Bateria:")
            print(generar_bateria())
            print("")
            print("\n")
              
        case 3: 
            print("temperatura:")
            print(generar_temperatura())
            print("")
            print("\n")

            
        case 4: 
            print("distancia:")
            print(generar_distancia())
            print("")
            print("\n")


        case 5: 
              reporte_general()
              print("\n")

        case 6: 
              print("Saliendo...")
              print("\n")
              return 6
    return 0




while(True):

     if(menu()==6):
          break
    
