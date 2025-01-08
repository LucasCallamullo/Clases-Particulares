


def validar_consonantes(i):
    ''' Devuelve True si es consonante, O Devuelve False si no es consonante.'''
    consonante = "bcdfghjklmnpqrstvwxyz"
    if i.lower() in consonante:  # # si el caracter esta en vocales
        return True
    else:
        return False


def validar_vocales(i):
    ''' Devuelve True si es vocal, O Devuelve False si no es vocal.'''
    vocales = "aeiou"
    if i.lower() in vocales:  # # si el caracter esta en vocales
        return True
    else:
        return False


def principal():
    archivo = "archivo.txt"
    m = open(archivo, "rt")         # read text ; leer texto

    contador_lineas = 0


    ''' 1 - Determinar la cantidad de palabras cuya longitud sea par, y que estén conformadas por vocales y
consonantes en partes iguales (minúsculas o mayúsculas).
    '''
    r1 = 0          # r1 = contador de palabras que cumplen las condiciones del punto 1
    r1_cont_letras = 0
    r1_cont_vocales = 0
    r1_cont_consonantes = 0


    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que
tienen al menos un dígito y no tienen una "p" (mayúscula o minúscula).   
    '''
    r2 = None                  # hace referencia a la mayor longitud
    r2_cont_letras = 0
    tiene_digito = False
    tiene_p = False



    ''' 4 Determinar cuántas palabras incluyen la expresión "ra" (con cualquiera de sus letras en minúscula
o mayúscula) pero de tal forma que la palabra además tenga una vocal (mayúscula o minúscula)
entre sus dos primeros caracteres.
    '''

    r4 = 0                  # cantidad pálabras cumplen
    r4_empieza_vocal = False
    r4_cont_letras = 0
    tiene_r = False
    tiene_ra = False





    ''' 5 - detectar que la frase solo tenga digitos y letras, y que no tenga dos mayusculas seguidas,
    si cumple mostrar "es una frase valida" si no cumple mostrar "es una frase invalida"
    '''
    # r5
    r5_cumple_condiciones = True
    r5_tiene_mayus = False

    # AbA AB AC AD



    # forma 1
    for linea in m:
        contador_lineas += 1

        if contador_lineas == 1:
            pass

        else:
            #          12340123450
            # linea = "Hace falta coraje para saltar de ese punto."
            for i in linea:
                # i = H, B, A, c, e, $,  , f

                # estamos dentro de una palabra
                if i != " " and i != ".":           # if i not in " .":

                    # r1
                    r1_cont_letras += 1
                    es_vocal = validar_vocales(i)       # return True si era vocal
                    if es_vocal:
                        r1_cont_vocales += 1

                    es_consonante = validar_consonantes(i)
                    if es_consonante:
                        r1_cont_consonantes += 1

                    # r2
                    r2_cont_letras += 1
                    if "0" <= i <= "9":
                        tiene_digito = True

                    if i.lower() == "p":
                        tiene_p = True

                    # r4
                    r4_cont_letras += 1
                    r4_vocal = validar_vocales(i)

                    if r4_cont_letras <= 2 and r4_vocal:
                        r4_empieza_vocal = True

                    if i.lower() == "r":
                        tiene_r = True

                    elif tiene_r and i.lower() == "a":
                        tiene_ra = True

                    else:
                        tiene_r = False

                    # r5
                    if not "a" <= i.lower() <= "z" and not "0" <= i <= "9":
                        r5_cumple_condiciones = False

                    if r5_tiene_mayus and "A" <= i <= "Z":
                        r5_cumple_condiciones = False
                    elif "A" <= i <= "Z":
                        r5_tiene_mayus = True
                    else:
                        r5_tiene_mayus = False

                # termine una palabra
                else:

                    # r1
                    if r1_cont_letras % 2 == 0 and r1_cont_vocales == r1_cont_consonantes:
                        r1 += 1

                    # r2        - buscaba la mayor longitud
                    if not tiene_p and tiene_digito:
                        if r2 is None or r2_cont_letras > r2:
                            r2 = r2_cont_letras

                    # r4
                    if r4_empieza_vocal and tiene_ra:
                        r4 += 1


                    # apagar las banderas, reiniciar contadores etc
                    # r1
                    r1_cont_letras = 0
                    r1_cont_vocales = 0
                    r1_cont_consonantes = 0

                    # r2
                    r2_cont_letras = 0
                    tiene_digito = False
                    tiene_p = False

                    # r4
                    r4_empieza_vocal = False
                    r4_cont_letras = 0
                    tiene_r = False
                    tiene_ra = False


            # termina la frase


    # Termina el archivo
    m.close()

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    # print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)




    if r5_cumple_condiciones:
        print("Frase valida")
    else:
        print("Frase Invalida")





if __name__ == '__main__':
    principal()