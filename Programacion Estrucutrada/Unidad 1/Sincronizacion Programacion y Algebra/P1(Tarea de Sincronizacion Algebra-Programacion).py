# Proyecto sincronizador (Programacion y Algebra Lineal)

# P1 Menu de operaciones para las unidades rectangulares ( (s)+, (r)-, (d)/, (m)*)

#Ingrese Z1, Z2. Que quiere hacer con estas operaciones?

print("\n\n")
print("\n======================================================================\n")
# Solicitando Z1. 
Z1r = int(input("Ingrese el valor real de Z1:"))
Z1i = int(input("Ingrese el valor imaginario (i) de Z1: "))


# Solicitando Z2. 
Z2r = int(input("Ingrese el valor real de Z2: "))
Z2i = int(input("Ingrese el valor imaginario (i) de Z2: "))

# Formateando
print("\n======================================================================\n")
print("Valor Z1: {0} + ({1})i".format(Z1r,Z1i))
print("Valor Z2: {0} + ({1})i".format(Z2r,Z2i))

# Solicitando operacion a realizar
op = (input("\n ======== Que operacion quiere hacer? ======== \n Multiplicacion [m] \n Division [d] \n Suma [s] \n Resta [r] \n")) 

Zfr = 0
Zfi = 0


# Evaluando seleccion de operacion 

# [s] Suma
if( op == "s"):
    print("Seleccion: Suma")
    print("Z1 + Z2")
    Zfr = Z1r+Z2r
    Zfi = Z1i+Z2i

# [r] Resta    
elif( op == "r"):
    print("Seleccion: Resta")
    print("Z1 - Z2")
    Zfr = Z1r-Z2r
    Zfi = Z1i-Z2i

elif( op == "m"):
    print("Seleccion: Multiplicacion")
    print("Z1 * Z2")
    Z1rm1 = Z1r*Z2i
    Z1rm2 = Z1r*Z2r

    Z1im1 = Z1i*Z2i
    Z1im2 = Z1i*Z2r

    Zfr = Z1rm2  + ((-1)*Z1im1)
    Zfi = Z1rm1 + Z1im2

elif(op=="d"):
    print("Seleccion: Division")
    print("Z1 / Z2")
    Z2i = Z2i*(-1)
    Z1rm1 = Z1r*Z2i
    Z1rm2 = Z1r*Z2r

    Z1im1 = Z1i*Z2i
    Z1im2 = Z1i*Z2r

    Z3r = Z1rm2  + ((-1)*Z1im1)
    Z3i = Z1rm1 + Z1im2 

    # print("Z3r: ",Z3r)
    # print("Z3i: ",Z3i)


    Z2r2 = Z2r**2 
    Z2i2 = Z2i**2
    # print("Z2r**2: ",Z2r2)
    #print("Z2i**2: ", Z2i2)

    Z2 = Z2r2+Z2i2
    # print("Z2: ",Z2)
    

    Zfr = Z3r/Z2
    Zfi = Z3i/Z2




	

if(Zfi<0):
    print("Resultado es: {0} {1}i".format(Zfr,Zfi))

else:
    print("Resultado es: {0} + {1}i".format(Zfr,Zfi))


