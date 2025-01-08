

# r3
def calcular_promedio(r3_acumulador, r3_cant_palabras):
    prom = 0
    if r3_cant_palabras > 0:
        prom = r3_acumulador // r3_cant_palabras
    return prom


# ========================================================
#                   r1
# ========================================================
def validar_consonantes(letra):
    consonantes = "bcdfghjklmnpqrstvwxyzñ"
    # lower() transforma al caracter en minuscula   // .upper() transforma al caracter en mayuscula
    if letra.lower() in consonantes:  # si letra esta en consonantes,
        return True
    else:
        return False


def validar_vocales(letra):     # a A
    vocales = "aeiou"
    # lower() transforma al caracter en minuscula
    if letra.lower() in vocales:            # si letra esta en vocales,
        return True
    else:
        return False




def principal():

    archivo = "entrada.txt"
    m = open(archivo, "rt")     # read text , leer texto,
    contador_lineas = 0

    # r1
    ''' Determinar la cantidad de palabras cuya longitud sea par, y que estén conformadas por vocales y
    consonantes en partes iguales '''
    r1 = 0
    r1_longtud = 0
    r1_cont_vocales = 0
    r1_cont_consonantes = 0

    # r2
    ''' Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que
tienen al menos un dígito y no tienen una "p" (mayúscula o minúscula). '''
    r2 = None               # hace referencia a la mayor longitud
    r2_longitud = 0
    r2_es_digito = False
    r2_tiene_p = False

    # r3
    ''' Determinar el promedio entero de caracteres por palabra entre las palabras que tienen más de
dos caracteres pero incluyen una o más veces una "s" '''
    # Promedio = es la suma de caracteres / sobre la cantidad palabras que sumamos sus caracteres
    r3_longitud = 0
    r3_acumulador = 0
    r3_cant_palabras = 0
    r3_tiene_s = False

    # r4
    '''Determinar cuántas palabras incluyen la expresión "ra" (con cualquiera de sus letras en minúscula
o mayúscula) pero de tal forma que la palabra además tenga una vocal (mayúscula o minúscula)
entre sus dos primeros caracteres.'''
    r4_es_vocal = False
    r4_indice = 0
    r4_tiene_r = False
    r4_tiene_ra = False
    r4 = 0                  # contador palabras cumplen

    # r5
    ''' contar la cantidad de palabras, pero tomando en cuenta posibles errores por espacios en blanco seguidos'''
    es_palabra = False
    r5_cant_palabras = 0

    for linea in m:
        contador_lineas += 1

        if contador_lineas >= 3:
            # linea = "pata pelota pelado."

            for i in linea:
                # i = p, a, t, a,  ,
                # if not i in " .":D

                # estamos dentro de una palabra
                if i != " " and i != ".":

                    # r1
                    r1_longtud += 1

                    es_vocal = validar_vocales(i)       # Return True Es vocal, Si retorna False no es vocal
                    if es_vocal:
                        r1_cont_vocales += 1

                    es_consonante = validar_consonantes(i)
                    if es_consonante:
                        r1_cont_consonantes += 1

                    # r2
                    r2_longitud += 1
                    if "0" <= i <= "9":
                        r2_es_digito = True

                    if i.lower() == "p":
                        r2_tiene_p = True

                    # r3
                    r3_longitud += 1
                    if i.lower() == "s":
                        r3_tiene_s = True

                    # r4
                    r4_indice += 1

                    if i.lower() in "aeiou" and r4_indice <= 2:
                        r4_es_vocal = True

                    # rara rocasion
                    if i.lower() == "r":
                        r4_tiene_r = True

                    elif i.lower() == "a" and r4_tiene_r:
                        r4_tiene_ra = True

                    else:
                        r4_tiene_r = False

                    # r5
                    es_palabra = True


                # termine una palabra
                else:
                    # r1
                    if r1_longtud % 2 == 0 and r1_cont_consonantes == r1_cont_vocales:
                        r1 += 1

                    # r2
                    if r2_es_digito and not r2_tiene_p:     # para indicar que tiene p estan en false
                        if r2 is None or r2_longitud > r2:
                            r2 = r2_longitud

                    # r3
                    if r3_tiene_s and r3_longitud > 2:
                        r3_acumulador += r3_longitud
                        r3_cant_palabras += 1

                    # r4
                    if r4_tiene_ra and r4_es_vocal:
                        r4 += 1

                    # r5
                    if es_palabra:
                        r5_cant_palabras += 1


                    # apagar banderas, reiniciar contadores etc
                    # r1
                    r1_longtud = 0
                    r1_cont_consonantes = 0
                    r1_cont_vocales = 0

                    # r2
                    r2_es_digito = False
                    r2_tiene_p = False
                    r2_longitud = 0

                    # r3
                    r3_longitud = 0
                    r3_tiene_s = False

                    # r4
                    r4_es_vocal = False
                    r4_indice = 0
                    r4_tiene_r = False
                    r4_tiene_ra = False


    r3 = calcular_promedio(r3_acumulador, r3_cant_palabras)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()