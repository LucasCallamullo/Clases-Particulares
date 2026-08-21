# función para determinar si un caracter es un digito.
def es_digito(car):
    return "0" <= car <= "9"


# función para determinar si un caracter es una vocal.
def es_vocal(car):
    return car in "aeiouáéíóúAEIOUÁÉÍÓÚ"


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

    # contador de palabras del texto...
    cant_palabras = 0

    # item 1: flag para vocal en cuarta...
    tiene_vocal_en_cuarta = False

    # item 2: flag para comienzo con consonante...
    comienza_con_consonante = False

    # item 3: flag para p, t y s, acumulador de longitudes y contador de palabras...
    tiene_p_o_t = tiene_s = False
    cant_pal_con_p_o_t_pero_no_s = 0

    # item 4: flags para t y te...
    tiene_g = tiene_ge = tiene_digito = False

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # texto = "El libro GE982 es del agente 04GeK y no del 6greNT."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if contador_letras > 0:
                # total de palabras del texto...
                cant_palabras += 1

                # item 1...
                if tiene_vocal_en_cuarta:
                    r1 += 1

                # item 2...
                if comienza_con_consonante:
                    if r2 is None or contador_letras < r2:
                        r2 = contador_letras

                # item 3...
                if tiene_p_o_t and not tiene_s:
                    cant_pal_con_p_o_t_pero_no_s += 1

                # item 4...
                if tiene_ge and tiene_digito:
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            contador_letras = 0

            # item 1...
            tiene_vocal_en_cuarta = False

            # item 2...
            comienza_con_consonante = False

            # item 3...
            tiene_p_o_t = tiene_s = False

            # item 4...
            tiene_g = tiene_ge = tiene_digito = False

        else:
            # caracter dentro de la palabra... contarlo...
            contador_letras += 1

            # item 1...
            if es_vocal(car) and contador_letras == 4:
                tiene_vocal_en_cuarta = True

            # item 2...
            if es_consonante(car) and contador_letras == 1:
                comienza_con_consonante = True

            # item 3...
            if car in "pPtT":
                tiene_p_o_t = True
            if car in "sS":
                tiene_s = True

            # item 4...
            if car in "gG":
                tiene_g = True
            else:
                if tiene_g and car in "eéEÉ":
                    tiene_ge = True
                tiene_g = False

            if es_digito(car):
                tiene_digito = True

    # cálculo del promedio para r3...
    r3 = calcular_porcentaje(cant_pal_con_p_o_t_pero_no_s, cant_palabras)

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()
