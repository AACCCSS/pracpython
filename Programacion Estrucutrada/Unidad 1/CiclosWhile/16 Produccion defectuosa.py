#16 Producción defectuosa: acumular defectos hasta que lleguen al 5%.

defectos = 0

while(defectos<5):
    defectos = defectos+ int(input("Ingrese el porcentaje de defectos por acumular: "))

print("Limite de defectos ha sido alcanzado (5%).\nDescartando producto...")
