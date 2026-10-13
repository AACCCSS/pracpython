# Monitoreo de sensor de temperatura

import random
import time

limite = 85 # Limite critico


c  = 0 # Contador
n_registros = 0 


sensor_val = random.randint(-80,100)

while(sensor_val>-1):
    if(sensor_val > 85):
        c = c+1
    sensor_val = sensor_val+1
    n_registros = n_registros +1
    print("Sensor val: {0}, Numero de lecturas: {1}, Limite superado: {2} veces".format(sensor_val,n_registros,c))
    