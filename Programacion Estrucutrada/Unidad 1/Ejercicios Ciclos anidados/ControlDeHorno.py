"""
horno = true
temp = int(input("leer temperatura) 
if (temp>200):
	horno = false
	print("Activar alarma") 
else: 
	if( temp <150):
		print("resistencia de apoyo")


"""


"""
Control de temperatura en horno industrial
Si la temperatura > 200°C → activar alarma.
"""


horno = "encendido"
temperatura = int(input("Ingrese temperatura de horno: "))

if(temperatura>220):
    horno = "apagado"
    print("Estado del horno: {0}\n Alarma: Activada \n Temperatura: {1}\n".format(horno,temperatura))
if(temperatura <220):
    horno = "encendido"
    print("Estado del horno: {0}\n Alarma: Activada \n Temperatura: {1}\n".format(horno,temperatura))

print("Fin de programa")