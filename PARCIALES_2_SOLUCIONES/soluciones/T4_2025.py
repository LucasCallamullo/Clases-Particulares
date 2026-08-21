# función para determinar si un caracter es un digito.
def es_digito(car):
    return "0" <= car <= "9"


# función para determinar si un caracter es una vocal.
def es_vocal(car):
    return car in "aeiouáéíóúAEIOUÁÉÍÓÚ"


# función para determinar si un caracter es una vocal en minúscula...
def es_vocal_minuscula(car):
    return car in "aeiouáéíóú"


# función para determinar si un caracter es una consonante.
def es_consonante(car):
    return car in "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"


# función para calcular el porcentaje entero entre sus parámetros.
def calcular_porcentaje(contador_parcial, contador_total):
    porcentaje = 0
    if contador_total != 0:
        porcentaje = contador_parcial * 100 // contador_total
    return porcentaje


# función principal del programa.
def principal():
    # inicialización de variables de resultados..
    r1 = r3 = r4 = 0
    r2 = None

    # contador de letras en una palabra...
    contador_letras = 0

    # item 1: contadores para r1 y para r3...
    cant_consonantes = cant_vocales = 0

    # item 2: contadores para r2...
    cant_digitos = cant_vocales_minuscula = 0

    # item 3: contadores finales para r3...
    cantidad_palabras = cant_palabras_solo_vocales_o_una_consonante = 0

    # item 4: flags para v, vi y n...
    tiene_t_en_primeras_tres = tiene_te_en_primeras_tres = False
    anterior = " "

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # texto = "El tenista atenta contra el estandarte."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if contador_letras > 0:
                # item 1...
                if cant_consonantes == 3 and cant_vocales == 2:
                    r1 += 1

                # item 2...
                if cant_digitos >= 1 and cant_vocales_minuscula >= 1:
                    if r2 is None or contador_letras < r2:
                        r2 = contador_letras

                # item 3...
                cantidad_palabras += 1
                if cant_vocales == contador_letras or cant_consonantes == 1:
                    cant_palabras_solo_vocales_o_una_consonante += 1

                # item 4...
                if tiene_te_en_primeras_tres and es_vocal(anterior):
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            contador_letras = 0

            # item 1 e item 3...
            cant_consonantes = cant_vocales = 0

            # item 2...
            cant_digitos = cant_vocales_minuscula = 0

            # item 4...
            tiene_t_en_primeras_tres = tiene_te_en_primeras_tres = False
            anterior = " "

        else:
            # caracter dentro de la palabra... contarlo...
            contador_letras += 1

            # item 1 e item 3...
            if es_consonante(car):
                cant_consonantes += 1
            elif es_vocal(car):
                cant_vocales += 1

            # item 2...
            if es_digito(car):
                cant_digitos += 1
            elif es_vocal_minuscula(car):
                cant_vocales_minuscula += 1

            # item 4...
            #             elif i.lower() == 't':
            #                 r4_tiene_t = True
            if car in "tT" and contador_letras <= 3:
                tiene_t_en_primeras_tres = True
            else:
                #             if r4_tiene_t and i.lower() == 'e':
                #                 r4_tiene_te = True
                if tiene_t_en_primeras_tres and car in "eéEÉ":
                    tiene_te_en_primeras_tres = True

                #             else:
                #                 r4_tiene_t = False
                tiene_t_en_primeras_tres = False

            anterior = car

    # cálculo del porcentaje para r3...
    r3 = calcular_porcentaje(cant_palabras_solo_vocales_o_una_consonante, cantidad_palabras)

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()
