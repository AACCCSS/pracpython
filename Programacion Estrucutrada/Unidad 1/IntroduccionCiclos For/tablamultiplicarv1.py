# Contador de tabla 

# Contador de tabla (Ct)
# Contador de tabla (c)

ct = 0
c = 0
prod = 0

while (ct<10):
    
    ct = ct+1
    print(f"ct: {ct}")
        
    while(c<10):
        c = c+1    
        prod = ct*c
        print(f"{ct} x {c}  = {prod}")
    c = 0
    print("\n")
