# Ucan reqquiere sistema para control de calificaciones
## Pedir un arreglo: nombre de alumno
## Pedir en arreglo 2: Caliificaciones
## Funciones altas, reportes, busqueda (Busca por nombre la calificacion retornando posición).

## Modificaciones de clase 13 - Octubre 2026: 
### Plus: Dar de baja al alumno  
### Plus: Modificar nombre de alumno
### Modificación: Obtener el promedio grupal

alumnos = []
calificacion = []


def alta_alumno():
    temp = (input("Ingrese el nombre de alumno: "))
    alumnos.append(temp)
    print("Registrado correctamente.\n")
    temp  = int(input("Ingrese calificacion del alumno (10 max, 0 min): "))
    calificacion.append(temp)

# Baja,  retirar al alumno del registro
def bajar_alumno():
    temp = input("Ingrese el nombre para dar de baja: ")
    if temp in alumnos:
        # Obtenemos el índice exacto de ese alumno
        i = alumnos.index(temp)
        
        print("Dando de baja alumno: {0}".format(alumnos[i]))
        # Borramos de forma segura en ambos arreglos usando el mismo índice
        alumnos.pop(i)
        calificacion.pop(i)
    else:
        print("Alumno no encontrado")
    print("\n")

# Modificar nombres
def modifica_alumnos():
    nombre = input("Ingrese nombre a modificar: ")
    encontrado = False
    for i in range(len(alumnos)):
        if alumnos[i] == nombre: 
            alumnos[i] = input ("Nuevo nombre: ")
            encontrado = True
    if(not encontrado):
        print("Nombre no encontrado!")

def reporte_alumnos():
    if len(alumnos) == 0:
        print("No hay alumnos registrados.\n")
        return

    print("\n--- REPORTE DE ALUMNOS ---\n")
    for i in range(len(calificacion)):
        print("Alumno: {0}, Registro# {1}, Calificación: {2} ".format(alumnos[i],i+1,calificacion[i]))

    promedio = sum(float(cal) for cal in calificacion) / len(calificacion)

    print(f"\nPromedio: {promedio:.2f}")
    print(f"calificacion máxima: {max(calificacion)}")
    print(f"calificacion mínima: {min(calificacion)}")
    print()

def buscar_calificacion():
    if len(alumnos) == 0:
        print("No hay alumnos registrados.\n")
        return

    buscada = (input("Ingrese nombre de alumno para mostrar calificacion: "))
    encontrado = False
    for i in range(len(alumnos)):
        if alumnos[i] == buscada:
            print("\nCalificacion de {0} es: {1} con #Registro {2}".format(alumnos[i],calificacion[i],i+1))
            encontrado = True

    if not encontrado:
        print("Alumno no encontrado.")
    print("\n")



while True:
    print("===== CALIFICACIONES DE ALUMNOS =====")
    print("1. Dar de alta un alumno")
    print("2. Ver reporte")
    print("3. Buscar calificacion de alumno")
    print("4. Dar de baja alumno")
    print("5. Modificar nombre de alumno")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        alta_alumno()
    elif opcion == "2":
        reporte_alumnos()
    elif opcion == "3":
        buscar_calificacion()
    elif opcion == "4":
        bajar_alumno()

    elif opcion == "5":
        modifica_alumnos()

    elif(opcion == "6"):
        print("Programa finalizado.")
        break
    
    else:
        print("Opción incorrecta.\n")
