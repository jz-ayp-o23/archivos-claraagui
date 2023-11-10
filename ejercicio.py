def Round(value): 
    return int(10*value + 0.5)/10
def promedio_calificaciones(archivo_entrada, archivo_salida):
    """Realiza el promedio del archivo entrada y lo guarda en archivo de salida."""
    lista_res = []
    sum_calificaciones = 0
    with open(archivo_entrada, "r", encoding="utf8") as f:
        # Leer cada línea
        for linea in f:
            sum_calificaciones = 0
            linea = linea.lower()
            linea_lista = linea.split() #
#            print(linea_lista)
            aux = linea_lista[0]
            linea_lista[0] = linea_lista[1] #se reasigna
            linea_lista[1] = aux #se agrga el valor que se habia guardado previamente
#            print(linea)
            for i in range(0, len(linea_lista)):
#                print(linea_lista[i])
                if i == 1:
                    lista_res.append(linea_lista[i] + ': ')
                if i == 0:
                    lista_res.append(linea_lista[i].upper() + ",")
                elif i > 1:
                    sum_calificaciones = sum_calificaciones + int(linea_lista[i])
            promedio = Round(sum_calificaciones / (len(linea_lista)-2))
            lista_res.append(promedio)
            lista_res.append("\n")
#            print(lista_res)

    # Escribir el archivo de salida
    linea_out = ""
    with open(archivo_salida, "w", encoding="utf8") as f:
        for elemento in lista_res:
            if elemento == "\n":
                linea = f"{linea_out} \n"
                f.write(linea)
                linea_out = ""
            else:
                linea_out = linea_out + ' ' + str(elemento)

def main():
    """Probar la función"""
    archivo = "data/calificaciones.txt"
    salida = "data/promedios.txt"
    prueba = promedio_calificaciones(archivo, salida)
main()