"""
========== 8. Base de datos de actuadores ==========
Enunciado:

Utiliza un diccionario para almacenar los datos de un actuador:

Nombre
Tipo
Voltaje
Estado

El programa debe:

Mostrar la información.
Verificar si el voltaje es mayor a 24 V.
Mostrar un mensaje de advertencia si está fuera del rango permitido.


"""
# Diccionario que contiene el actuador:
actuador = {
    "Nombre":"Actuador1",
    "Tipo":"DC",
    "Voltaje":24,
    "Estado":"Activo"
}
LimiteVoltaje = 24


# Mostrar información del diccionario: 
print("Información del actuador: ")
print(f"Nombre: {actuador['Nombre']}")
print(f"Tipo: {actuador['Tipo']}")
print(f"Voltaje: {actuador['Voltaje']}")
print(f"Estado: {actuador['Estado']}")

if(actuador["Voltaje"]>LimiteVoltaje):
    print(f"Warning: Voltaje supera rango permitido: {actuador['Voltaje']} encima de {LimiteVoltaje}")
else: 
    print("Voltaje dentro del rango funcional")