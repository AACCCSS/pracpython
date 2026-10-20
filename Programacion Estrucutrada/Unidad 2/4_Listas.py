
# Funciones de listas
materias = ["Matematicas","Porgramación","Física"]
print(materias)


print(materias[0])

print("Adición de la materia electrónica:")
materias.append("Electrónica")
print(materias)

print("Eliminando la materia programación:")
materias.pop(1)
print(materias)


# Tuplas
""" Usa parentesis para su declaración: """

print("\n Usando tuplas: ")
dias = ("lunes", "martes","miercoles")
print(dias)
print(dias[1])

# dias[0] = "domingo"
print("Tipo lista pero con información constante, no se pueden modificar. ")


# Diccionarios
""" Utiliza varios campos para almacenar claves y valores """
print("Diccionarios:")

alumno = {
    "nombre":"Juan",
    "edad":18, 
    "carrera":"Ingenieria"

}

print("Acceso a nombres")
print(alumno.get("nombre"))


