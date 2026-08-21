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

    # item 1: flag de consonante y flag de digito...
    comienza_con_consonante = tiene_digito_en_segunda = False

    # item 2: contador de vocales...
    contador_vocales = False

    # item 3: contador, acumulador y flag para r3...
    tiene_digito_impar = False
    total_letras_en_palabras_con_digito_impar = contador_palabras_con_digito_impar = 0

    # item 4: flags para f, fa y r...
    tiene_f = tiene_fa = tiene_r = False

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # texto = "El favorito es un famoso y afianzado fabricante."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if contador_letras > 0:
                # item 1...
                if comienza_con_consonante and tiene_digito_en_segunda:
                    r1 += 1

                # item 2...
                if contador_vocales >= 2:
                    if r2 is None or contador_letras < r2:
                        r2 = contador_letras

                # item 3...
                if tiene_digito_impar:
                    total_letras_en_palabras_con_digito_impar += contador_letras
                    contador_palabras_con_digito_impar += 1

                # item 4...
                if tiene_fa and not tiene_r:
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            contador_letras = 0

            # item 1...
            comienza_con_consonante = tiene_digito_en_segunda = False

            # item 2...
            contador_vocales = 0

            # item 3...
            tiene_digito_impar = False

            # item 4...
            tiene_f = tiene_fa = tiene_r = False

        else:
            # caracter dentro de la palabra... contarlo...
            contador_letras += 1

            # item 1...
            if es_consonante(car) and contador_letras == 1:
                comienza_con_consonante = True
            elif es_digito(car) and contador_letras == 2:
                tiene_digito_en_segunda = True

            # item 2...
            if es_vocal(car):
                contador_vocales += 1

            # item 3...
            if es_digito_impar(car):
                tiene_digito_impar = True

            # item 4...
            if car in "fF" and contador_letras == 1:
                tiene_f = True
            else:
                if tiene_f and car in "aáAÁ":
                    tiene_fa = True
                tiene_f = False

            if car in "rR":
                tiene_r = True

    # cálculo del porcentaje para r3...
    r3 = calcular_promedio(total_letras_en_palabras_con_digito_impar, contador_palabras_con_digito_impar)

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()
