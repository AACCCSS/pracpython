"""
Nivel de líquido en tanque

Si nivel < 30% → encender bomba de llenado.

Si nivel > 90% → apagar bomba y activar alarma de sobrellenado.

"""

nivel = int(input("Ingrese el porcentaje del nivel del tanque a llenar: "))

if(nivel>30):
    print("Encender bomba de llenado \napagar alarma")
if(nivel >90): 
    print("Apagar bomba de llenado \nencender alarma")


print("\nFin de programa")