# 2 Temperatura de horno: pedir temperatura hasta que sea menor a 200°C.

import random
import time

te = random.randrange(190,800)

while(te > 200):
    print(f"Temperatura actual: {te:.2f} grados")
    
    te = random.randrange(190,800)

    if(te<200):
        print(f"Temperatura actual: {te:.2f} grados")
        break

