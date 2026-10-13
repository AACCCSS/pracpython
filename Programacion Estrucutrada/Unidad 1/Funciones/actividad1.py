# Pedir 2 numeros hacerlo  funcion y llamar las funciones
# Efectua operaciones +,-,*,/.

n1 = 0
n2 = 0


def solicitaN():
    global n1,n2
    n1 = int(input("Ingrese valor 1: "))
    n2 = int(input("Ingrese valor 2: "))
    

def operacion_suma(x,y):
    return x+y

def operacion_resta(x,y):
    return x-y

def operacion_multiplicacion(x,y):
    return x*y

def operación_division(x,y):
    return x/y

while(True): 

    solicitaN()

    op = int(input("Que operacion desea hacer?:\nSuma: [1]\nResta: [2]\nMultiplicacion: [3]\nDivision: [4]"))

    match(op):
        case 1: 
            print(operacion_suma(n1,n2))
        case 2: 
            print(operacion_resta(n1,n2))
        case 3: 
            print(operacion_multiplicacion(n1,n2))
        case 4: 
            print(operación_division(n1,n2))


        




