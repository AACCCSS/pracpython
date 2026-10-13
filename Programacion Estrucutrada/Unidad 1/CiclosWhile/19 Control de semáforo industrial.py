# 19 Control de semáforo industrial: repetir colores hasta completar 10 ciclos.


contador = 0

while(contador != 10):

    print("Semaforo color: Rojo")
    print("Semaforo color: Verde")
    print("Semaforo color: Amarillo")
    print("Conteo acumulado: {0}\n".format(contador))
    contador = contador+1

print("\n")
print("Fin de conteo...")