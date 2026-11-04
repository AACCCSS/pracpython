""" 
En el siguiente programa pide el numero de personas y nos da el pago 
de la gente que asiste al cine,
hacer una matriz para que se acomoden en los asientos
"""
sala_cine =[
    [0,0,0,0,0,],
    [0,0,0,0,0,],
    [0,0,0,0,0,],
    [0,0,0,0,0,],
    [0,0,0,0,0,]
]
tp=0
t=0
while True:
    for i in sala_cine:
        print(i)
    p = int(input("numero de personas: "))
    print("su pago es: ",p*120)
    tp=tp+p
    t=t+p*120
    for k in range(p):
        while True:
            f = int(input("fila (1-5): "))
            c = int(input("columna (1-5): "))
            if sala_cine[f-1][c-1]==1:
                print("ocupado")
            else:
                sala_cine[f-1][c-1]=1
                break
    for i in sala_cine:
        print(i)
    op = input("salir s/n: ")
    if op=="s":
        break
print("personas: ",tp)
print("total: ",t)