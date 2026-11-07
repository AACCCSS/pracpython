calif = []

def captura(): 
    # Ingreso de alumnos
    
    nom = input("Nombre de alumno: ")
    cal = input("calificación del alumno: ")
    calif.append([nom,cal])

def mostrar():
    # Mostrar todo
    print(calif)


# Promedio
def promedio():
    sum = 0 
    prom = 0 
    for i in range(len(calif)):
        print(calif[i][1])
        sum = sum+ int(calif[i][1])

    print("promedio:")
    prom = sum/len(calif)
    print(prom)


while True: 
    print("" \
    "\n1.- Captura" \
    "\n2.- Informe" \
    "\n3.- Promedio" \
    "\n4.- Salir")
    op= int(input("Seleccione opcion: "))    

    if op == 1: 
        captura()
    elif op==2: 
        mostrar()
    elif op==3: 
        promedio()
    elif op==4: 
        print("Fin de programa")
        break