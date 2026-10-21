"""
========= 9. Diagnóstico de un sistema automatizado ========= 
Enunciado:

Utiliza una lista para almacenar los códigos de error generados durante una jornada.

Ejemplo:
101
302
150
404
210
El programa debe:

Mostrar todos los códigos.
Contar cuántos errores existen.
Determinar cuántos son mayores a 300.
Mostrar el error más alto.

Función iterativa que registre los valores indefinidamente hasta que se ingrese un valor no valido. 

"""

# Registro de errores de jornada:
Errores_de_jornada = []
Codigo_Referencia_Mayor = 300

while(True):    
    # Uso de try y excepciones para el registro de errores indefinidamente:
    try: 
        op = int(input("Ingrese enumeración de codigos de errores: "))
        Errores_de_jornada.append(op)
    except ValueError:
        print("Finalizando jornada") 
        break 



# Mostrar todos los ccodigos:
print("Codigos de errores de jornada: ",Errores_de_jornada)



# Contar cuantos errores existen: 
print("Total de errores existentes: ",len(Errores_de_jornada))



# Mostrar cuantos errores son mayores a codigo 300
cc = 0
for i in range(len(Errores_de_jornada)):
    if(Errores_de_jornada[i] >300):
        cc +=1
print("Total de errores mayores a 300: ",cc)
    
# Mostar el error más alto: 
print("El código de error mas alto es: ",max(Errores_de_jornada))
