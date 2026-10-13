#8 Presión hidráulica: pedir valores hasta que presión sea menor a 200 Pa.


Pa = 230

while(Pa>200):
    print("Reduciendo presion Hidraulica\n Lectura actual:", Pa)
    Pa = float(input("Ingrese Presion: "))
    print("\n")

print("Presion reducida a: 200 Pa")