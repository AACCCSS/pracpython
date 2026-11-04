"""
Proyecto #2 
Simulador de producción de una fábrica de semiconductores 
Matriz: 
• Filas = máquinas. 
• Columnas = días. 
• produccion = [ 
•     [120,130,125,128,140],  # Maquina 1
•     [110,115,118,120,122],  # Maquina 2 
•     [150,148,151,152,155]   # Maquina 3
• ] 


Que el sistema: 
1. Muestre la producción total. - ok
2. Encuentre la máquina más productiva. - ok
3. Obtenga promedios. - ok
4. Genere una matriz de eficiencia.- ok
5. Compare semanas. - ok
6. Grafique resultados (si ya vieron matplotlib). 


"""

produccion = [ # Lunes, Martes, Miercoles, Jueves, Viernes
     [120,130,125,128,140],  # Maquina 1
     [110,115,168,120,122],  # Maquina 2 
     [150,148,151,152,150]   # Maquina 3
 ] 



def mostrar_produccion():
    print(produccion)

def mostrar_mayorProduccion():
    mayor = 0
    columna_mayor = 0
    fila_mayor = 0


    for fila in range(len(produccion)):
        for columna in range(len(produccion[0])):
            if(produccion[fila][columna] > mayor):
                mayor = produccion[fila][columna]              
                columna_mayor = columna
                fila_mayor = fila
            
    print(f"Numero de Maquina con ",
          f"mayor producción: {fila_mayor+1}",
          f"en el dia {columna_mayor+1} ",
          f"con un valor de {mayor}")
    return mayor

def mostrar_promedios(): 
    suma = 0
    conteo = 0
    promedio = 0
    for filas in range(len(produccion)):
        for columnas in range(len(produccion[0])):
            suma = suma+produccion[filas][columnas]
            conteo = conteo+1
    promedio = suma/conteo
    #print(f"Promedio total de producción por todas las maquinas: {produccion}")
    return (promedio)

# eficiencia = (producción real /producción estándar) x 100
def mostrar_eficiencia(): 
    print(f"Eficiencia de producción de cada maquina según el promedio {round(mostrar_promedios(),2)}")
    
    prom = mostrar_promedios()
    produccion1_suma = 0
    produccion2_suma = 0
    produccion3_suma = 0


    for filas in range(len(produccion)):   
        for columnas in range(len(produccion[0])):
            if filas == 0:
                produccion1_suma = produccion1_suma+produccion[filas][columnas]
            elif filas == 1: 
                produccion2_suma = produccion2_suma+produccion[filas][columnas]

            elif filas == 2:
                produccion3_suma = produccion3_suma+produccion[filas][columnas]


    print(f"Eficiencia de maquina 1: {round((calcula_promedio(produccion1_suma,5)/prom)*100,2)}")
    print(f"Eficiencia de maquina 2: {round((calcula_promedio(produccion2_suma,5)/prom)*100,2)}")
    print(f"Eficiencia de maquina 3: {round((calcula_promedio(produccion3_suma,5)/prom)*100,2)}")
    return 1

def calcula_promedio(total, suma):
    return (total/suma)


def compara_semanas(): 
    maquina_No = 0
    dia_No = 0
    mayor = 0


    for filas in range(len(produccion)):
        maquina_No = filas
        for columnas in range(len(produccion[0])):
            #print(produccion[filas][columnas])
            if(mayor<produccion[filas][columnas]):
                mayor = produccion[filas][columnas]
                dia_No = columnas
        print(f"La maquina #{maquina_No+1} tuvo mayor producción el dia #{dia_No+1} con valor de: {mayor} ")
        mayor = 0


    return 1

print("Producción completa, Filas como maquina Vs Columna como dias:")

mostrar_produccion()
mostrar_mayorProduccion()
mostrar_promedios()
mostrar_eficiencia()
compara_semanas()