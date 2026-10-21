"""
============ 6. Monitoreo de sensores en una línea de producción ===========
Enunciado:

Utiliza un diccionario {} donde la clave sea el nombre del sensor y el valor la lectura obtenida.

Ejemplo:

Python

{

"Temperatura":85,

"Presion":120,

"Proximidad":15

}

El programa debe:

Mostrar todas las lecturas.
Determinar cuál sensor tiene la lectura más alta.
Generar una alerta si alguna temperatura supera los 90°C.

Nota: Se implementará banderas para este ejercicio: 

valor_maximo = None
clave_maxima = None

Metodo para recorrer diccionario. 

"""
# Declaración de Sensores
Sensores = {
    "Temperatura":0,
    "Presion":0,
    "Proximidad":0
}

valor_maximo= None
clave_maxima = None

limite = 90


# Toma de lectura
Sensores["Temperatura"] = int(input("Ingrese el valor de la lectura de temperatura: "))
Sensores["Presion"] = int(input("Ingrese el valor de la lectura de la presión: "))
Sensores["Proximidad"] = int(input("Ingrese el valor de la lectura de la proximidad: "))

# Mostrar todas las lecturas
print(Sensores)


# Recorrer el diccionario: 
# for i, valor in Sensores.items():
for clave, valor in Sensores.items(): 
    # Verificar si el valor actual es mayor que el valor maximo registrado
    if valor_maximo is None or valor>valor_maximo: 
        valor_maximo = valor
        clave_maxima = clave
    
# Determinación de lectura con mayor valor
# Generación de alerta si la temperatura supera 90°C
if valor_maximo>limite:
    print(f"El valor maximo es: {valor_maximo} que supera el limite ({limite}. Cuya clave es: {clave_maxima})")
else: 
    print(f"El valor maximo es: {valor_maximo} y no supera el limite de {limite}°C")

