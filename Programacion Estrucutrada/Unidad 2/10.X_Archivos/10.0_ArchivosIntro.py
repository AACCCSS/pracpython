# r leer
# w Escribir
# a Agregar
# x Crear


def graba():
    with open("C:/Users/Nichi/Documents/gitcontrol/Python/Programacion Estrucutrada/Unidad 2/10.X_Archivos/10.0_datos.txt", "w") as archivo:
        archivo.write("24 \n")
        archivo.write("25 \n")
        archivo.write("26 \n")
        archivo.write("27 \n")

def lee():
    suma = 0
    contador = 0
    with open("C:/Users/Nichi/Documents/gitcontrol/Python/Programacion Estrucutrada/Unidad 2/10.X_Archivos/10.0_datos.txt", "r") as archivo:
        for linea in archivo:
            temperatura = float(linea)
            suma = suma + temperatura
            contador = contador + 1
        promedio = suma / contador
        print("Promedio:", promedio)

while True:
    print("1.-Graba")
    print("2.-Lee")
    print("3.-Salir")
    op = int(input("Teclea opcion: "))
    if op == 1:
        graba()
    elif op == 2:
        lee()
    elif op == 3:
        break
    else:
        print("Error")