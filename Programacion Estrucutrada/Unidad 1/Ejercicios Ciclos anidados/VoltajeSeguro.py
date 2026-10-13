"""
Diseña un algoritmo que reciba el voltaje de una máquina
y determine si está dentro del rango seguro (≤220 V) o si es peligroso (>220 V).
"""

voltaje = int(input("Ingrese el voltaje de maquina: "))

if(voltaje<=220):
    print("Voltaje es seguro {0}v".format(voltaje))

if(voltaje>220):
    print("Voltaje NO es seguro {0}v".format(voltaje))

print("Fin de programa")