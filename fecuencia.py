def frecuencia_palabras_en_archivo(archivo_entrada, archivo_salida):
    frecuencias = {}
    with open(archivo_entrada, "r", encoding="utf8") as f:
        for linea in f:
            linea = linea.lower()
            letras = ""
            for caracter in linea:
                if caracter.isalpha() or caracter == " ":
                    letras += caracter
            palabras = letras.split()
            for palabra in palabras:
                if palabra in frecuencias:
                    frecuencias[palabra] += 1
                else:
                    frecuencias[palabra] = 1
    items = frecuencias.items()

    items = sorted(items, key=lambda item: item[1], reverse=True)
    frecuencias = dict(items)
    with open(archivo_salida, "w", encoding="utf8") as f:
        for palabra in frecuencias:
            linea = f"{palabra}: {frecuencias[palabra]}\n"
            f.write(linea)
    return frecuencias

def main():
    archivo = "data/Asimov, Isaac - Cómo ocurrió.txt"
    salida = "data/Asimov-análisis.txt"
    prueba = frecuencia_palabras_en_archivo(archivo, salida)
    i = 0
    for palabra in prueba:
        print(f"{palabra}: {prueba[palabra]}")
        i += 1
        if i >= 10:
            break

main()