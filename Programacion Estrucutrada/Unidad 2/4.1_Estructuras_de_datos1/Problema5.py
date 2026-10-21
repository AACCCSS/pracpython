"""
============ 5 Inventario de herramientas de mantenimiento ============
Enunciado:

Utiliza un diccionario {} para almacenar información de una herramienta:

Nombre
Cantidad
Estado

El programa debe:

Mostrar toda la información.
Permitir actualizar la cantidad.
Indicar si la herramienta necesita reposición cuando la cantidad sea menor a 5.

"""

herramienta = {
    "nombre":"Llave Stilson",
    "Cantidad":2,
    "Estado":"Deteriorado"
}


# Mostrar toda información
print(herramienta)

#Actualizar cantidad: 
op = int(input("Ingrese cantidad nueva: "))
herramienta["Cantidad"] = op


# Inidica requerimiento de repuesto (menor a 5)
if(herramienta["Cantidad"] <5):
    print("Herramienta requiere repuesto, valor actual: ",herramienta["Cantidad"])
