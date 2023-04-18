
def segundos_a_segundos_minutos_y_horas(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"


segundos_lista = [10, 100, 40, 1500, 6000, 7999, 8932, 99999]
for cantidad_segundos in segundos_lista:
    convertido = segundos_a_segundos_minutos_y_horas(cantidad_segundos)
    print(f"Los {cantidad_segundos} segundos se convierten a {convertido}")


#segundos_de_entrada = int(input("ingrese los segundos a convertir: "))
for cantidad_segundos in segundos_lista: 
    segundos_de_entrada = cantidad_segundos
    segundos = 0 
    minutos = 0
    horas = 0 
    dias = 0 
    anos = 0
    decadas = 0
    while( segundos_de_entrada > 0): 
        segundos = segundos + 1

        if (segundos == 60):
            segundos = 0 
            minutos += 1
            if (minutos == 60):
                minutos = 0
                horas += 1 
                if (horas == 24):
                    horas = 0
                    dias += 1
                    if (dias == 365):
                        dias = 0
                        anos += 1
                        if (anos == 10):
                            anos = 0
                            decadas += 1
        
        segundos_de_entrada -= 1 

    print("decadas: " + str(decadas)+ "   anos: " + str(anos)+ "   dias: " + str(dias)+ "   horas: " + str(horas)
    + "   minutos: " + str(minutos) + "   segundos: " + str(segundos ))
