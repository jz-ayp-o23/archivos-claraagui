#Tarea 4. Interpolación de texto
#Clara Paola Aguilar Casillas, 751097, Ingenieria en ciencia de datos.
#Algoritmos y programación.
#Grpo: B5
#Jorge Adalberto Zaldívar.
#02/10/2023
#3 horas.

def Round(value): 
    return int(10*value + 0.5)/10 #Agregue esto ya que a la hora de que el promedio se redondeaba, el .25 no se redondeba a .3, si no a .2
def promedio_calificaciones(archivo_entrada, archivo_salida):
    """Realiza el promedio del archivo entrada y lo guarda en archivo de salida."""
    lista_res = []
    sum_calificaciones = 0 #inicialice la suma de calificaciones
    with open(archivo_entrada, "r", encoding="utf8") as f: #abrí el archivo
        for linea in f: # Leer cada línea
            sum_calificaciones = 0
            linea = linea.lower()
            linea_lista = linea.split() #separe cada línea de la lista
#            print(linea_lista)
            aux = linea_lista[0] #utilizo la variable aux, 
            linea_lista[0] = linea_lista[1] #se reasigna
            linea_lista[1] = aux #se agrga el valor que se habia guardado previamente
#            print(linea)
            for i in range(0, len(linea_lista)):
#                print(linea_lista[i])
                if i == 1: #condición para el nombre del alumno
                    lista_res.append(linea_lista[i] + ': ') 
                if i == 0: #condición para el apellido del alumno
                    lista_res.append(linea_lista[i].upper() + ",")
                elif i > 1: #condición para las calificaciones, para resalizar el promedio.
                    sum_calificaciones = sum_calificaciones + int(linea_lista[i])
            promedio = Round(sum_calificaciones / (len(linea_lista)-2))
            lista_res.append(promedio) #se agrega el promedio a la lista
            lista_res.append("\n") #se identifica donde se termina cada alumno

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