# función para determinar si un caracter es un digito.
def es_digito(car):
    return "0" <= car <= "9"


# función para determinar si un caracter es una vocal.
def es_vocal(car):
    return car in "aeiouáéíóúAEIOUÁÉÍÓÚ"


# función para determinar si un caracter es una consonante.
def es_consonante(car):
    return car in "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"


# función para determinar si un caracter es una mayuscula.
def es_mayuscula(car):
    return car in "AÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ"


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

    # item 1: flag de letra p...
    tiene_p = False

    # item 2: contador de vocales y de letras m...
    contador_vocales = contador_m = 0

    # item 3: flag, acumulador y contador para r3...
    tiene_digito_en_456 = False
    total_letras_en_palabras_con_digito_en_456 = contador_palabras_con_digito_en_456 = 0

    # item 4: flags para r y re, y contador de mayusculas...
    tiene_re = tiene_r = False
    contador_mayusculas = 0

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # texto = "Madre de muchos por momentos se molesta."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if contador_letras > 0:
                # item 1...
                if tiene_p and contador_letras < 6:
                    r1 += 1

                # item 2...
                if contador_vocales >= 2 and contador_m == 1:
                    if r2 is None or contador_letras < r2:
                        r2 = contador_letras

                # item 3...
                if tiene_digito_en_456:
                    total_letras_en_palabras_con_digito_en_456 += contador_letras
                    contador_palabras_con_digito_en_456 += 1

                # item 4...
                if tiene_re and contador_mayusculas >= 2:
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            contador_letras = 0

            # item 1...
            tiene_p = False

            # item 2...
            contador_vocales = contador_m = 0

            # item 3...
            tiene_digito_en_456 = False

            # item 4...
            tiene_re = tiene_r = False
            contador_mayusculas = 0

        else:
            # caracter dentro de la palabra... contarlo...
            contador_letras += 1

            # item 1...
            if car in "pP":
                tiene_p = True

            # item 2...
            if es_vocal(car):
                contador_vocales += 1
            elif car in "mM":
                contador_m += 1

            # item 3...
            if es_digito(car) and contador_letras in (4, 5, 6):
                tiene_digito_en_456 = True

            # item 4...
            if car in "rR":
                tiene_r = True
            else:
                if tiene_r and car in "eéEÉ":
                    tiene_re = True
                tiene_r = False

            if es_mayuscula(car):
                contador_mayusculas += 1

    # cálculo del porcentaje para r3...
    r3 = calcular_promedio(total_letras_en_palabras_con_digito_en_456, contador_palabras_con_digito_en_456)

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()
