#13 Resistencia eléctrica: pedir valores hasta que resistencia sea menor a 10 Ω.

R = 200

while(R > 10):
    R = int(input("Ingrese Resistencia: "))
    
print("Resistencia menor a 10 detectado", R)