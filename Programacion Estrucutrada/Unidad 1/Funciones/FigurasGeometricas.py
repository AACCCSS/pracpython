
import math 

def cuadrado (L):
    return L*L

def rectangulo (b,h):
    return b*h

def triangulo(b,h):
    return (b*h)/2

def circulo(r):
    return math.pi*r*r


while True: 
    print( "1.cuadrado")
    print( "2.rectangulo")
    print( "3.triangulo")
    print( "4.circulo ")

    op = int(input("Teclee opcion. "))

    match op:

        case 1: 
            L = int(input("Ingrese lado: "))
            print(f"El area de cuadrado es",cuadrado(L))

        case 2: 
            b = int(input("Ingrese base: "))
            h = int(input("Ingrese altura: "))
            print(f"El area de rectangulo es: ",rectangulo(b,h))
        
        case 3: 
            b = int(input("Ingrese base: "))
            h = int(input("Ingrese altura: "))
            print(f"El area de triangulo es: ",triangulo(b,h))

        case 4: 
            r = int(input("Ingrese radio: "))
            print("El area de circulo es: ",circulo(r))

        
