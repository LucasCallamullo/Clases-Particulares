# función para determinar si un caracter es un digito.
def es_digito(car):
    return "0" <= car <= "9"


# función para determinar si un caracter es un digito impar.
def es_digito_impar(car):
    return car in "13579"


# función para determinar si un caracter es una vocal.
def es_vocal(car):
    return car in "aeiouáéíóúAEIOUÁÉÍÓÚ"


# función para determinar si un caracter es una consonante.
def es_consonante(car):
    return car in "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"


# función para calcular el promedio entero entre sus parámetros.
def calcular_promedio(acumulador, contador):
    promedio = 0
    if contador != 0:
        promedio = acumulador // contador
    return promedio


# función principal del programa.
def principal():
    # inicialización de variables de resultados..
    r1 = r3 = r4 = 0
    r2 = None

    # contador de letras en una palabra...
    contador_letras = 0

    # item 1: flag de mayuscula y flag de digito en cuarta...
    comienza_con_mayuscula = tiene_consonante_en_tercera = False

    # item 2: flag de inclusión de "p" o de "n"...
    tiene_digito = False

    # item 3: acumuladores, contadores y flags para r3...
    total_letras_palabras_promediar = contador_palabras_a_promediar = contador_vocales = contador_consonantes = 0

    # item 4: flag para j y contador de silaba...
    tiene_j = False

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # texto = "En esa hora ocurre todo."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if contador_letras > 0:
                # item 1...
                if comienza_con_mayuscula or tiene_consonante_en_tercera:
                    r1 += 1

                # item 2...
                if not tiene_digito:
                    if r2 is None or contador_letras < r2:
                        r2 = contador_letras

                # item 3...
                if contador_vocales == 1 or contador_consonantes == 2:
                    contador_palabras_a_promediar += 1
                    total_letras_palabras_promediar += contador_letras

            # resetear variables para la siguiente palabra...
            # contador de letras...
            contador_letras = 0

            # item 1...
            comienza_con_mayuscula = tiene_consonante_en_tercera = False

            # item 2...
            tiene_digito = False

            # item 3...
            contador_vocales = contador_consonantes = 0

            # item 4...
            tiene_j = 0

        else:
            # caracter dentro de la palabra... contarlo...
            contador_letras += 1

            # item 1...
            if car.isupper() and contador_letras == 1:
                comienza_con_mayuscula = True
            elif es_consonante(car) and contador_letras == 3:
                tiene_consonante_en_tercera = True

            # item 2...
            if es_digito(car):
                tiene_digito = True

            # item 3...
            if es_vocal(car):
                contador_vocales += 1
            elif es_consonante(car):
                contador_consonantes += 1

            # item 4...
            if car in "jJ":
                tiene_j = True
            else:
                if tiene_j and car in "aáAÁ":
                    r4 += 1
                tiene_j = False

    # cálculo del promedio para r3...
    r3 = calcular_promedio(total_letras_palabras_promediar, contador_palabras_a_promediar)

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()
