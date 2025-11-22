#r4
def contiene_digito(caracter):
    if caracter in "0123456789":
        return True
    return False


#r3
def contiene_vocal(caracter):
    if caracter.lower() in "aeiou":
        return True
    return False


def principal():
    # m = open("entrada.txt", "rt")
    # linea = m.readline()
    # m.close()


    """
    1- Determinar la cantidad de palabras que tienen
    una "p" (minúscula o mayúscula) en la segunda o en la quinta posición.
    """
    r1 = 0
    indice = 0

    r1_tiene_p_pos2_o_5 = False

    """
    2- Determinar la longitud de la palabra más larga entre las que tienen
    al menos una "t" (minúscula o mayúscula) en cualquier lugar.
    """
    r2 = None
    r2_tiene_t = False

    """
    3- Determinar el promedio entero de caracteres por palabra, de las 
    palabras que comienzan con vocal (minúscula o mayúscula).
    """
    r3 = 0
    r3_acum_caracter = 0
    r3_cont_palabras = 0

    r3_tiene_vocal = False

    """
    4- Determinar cuántas palabras incluyen la expresión "pi" 
    (en minúsculas o mayúsculas) en cualquier lugar, pero tienen al menos un dígito después 
    de la tercera posición.
    """
    r4 = 0
    r4_tiene_pi = False
    r4_tiene_p = False

    r4_tiene_dig_pos4 = False


    linea = "papa appp."

    for caracter in linea:
        if caracter != " " and caracter != ".":

            indice += 1
            #r1
            if caracter.lower() == "p" and (indice == 2 or indice == 5):
                r1_tiene_p_pos2_o_5 += True         # aca el 1 no va a dar por esta linea es " = True "

            #r2
            if caracter.lower() == "t":
                r2_tiene_t += 1

            #r3
            es_vocal = contiene_vocal(caracter)
            if es_vocal is True and indice == 1:
                r3_tiene_vocal += True          # la tenes con el mas igual jajajaj

            #r4
            es_digito = contiene_digito(caracter)
            if es_digito is True and indice == 4:   # se refiere a -> indice > 3:  no solo el 4
                r4_tiene_dig_pos4 += 1

            # r4 aca va el bloque y este es el bloque bien hecho
            if r4_tiene_p and caracter.lower() == "i":
                r4_tiene_pi = True
            elif caracter.lower() == "p":
                r4_tiene_p = True
            else:
                r4_tiene_p = False

        else:
            #r1
            if r1_tiene_p_pos2_o_5 is True:
                r1 += 1

            #r2
            if r2 is None or r2 > indice:   # te olvidas agregar la condicion si tiene_t
                r2 = indice

            #r3
            if r3_tiene_vocal is True:
                r3_acum_caracter += indice
                r3_cont_palabras += 1

            #
            #r4     -# esto iba dentro de la palabra - este bloque esta todo mal jajaja
            if r4_tiene_p is True and indice == "i":    # aca no va lo del indice porque te dice cualquier lugar
                r4_tiene_pi += 1    # esto sería un True
            elif r4_tiene_pi is True:
                r4_tiene_p += 1     # esto sería un True
            else:
                r4_tiene_p = False

            # y fuera de la palabras preguntarias para r4
            # if r4_tiene_pi and r4_tiene_dig_pos4:
            #   r4 += 1



            # apagar banderas/ contadores
            #r1
            indice = 0
            r1_tiene_p_pos2_o_5 = False

            #r2
            r2_tiene_t = False

            #r3
            r3_tiene_vocal = 0

            #r4
            r4_tiene_pi = False
            r4_tiene_p = False

            r4_tiene_dig_pos4 = False

    if r3_cont_palabras > 0:
        r3 = r3_acum_caracter // r3_cont_palabras

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()