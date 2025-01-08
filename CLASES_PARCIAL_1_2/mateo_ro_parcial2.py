

# r2
def calcular_porcentaje(r2_total_palabras, r2_total_palabras_cumplen):
    porc = 0
    if r2_total_palabras != 0:
        porc = r2_total_palabras_cumplen * 100 // r2_total_palabras
    return porc


def validar_consonantes(i):
    # if "a" <= i.lower() <= "z" and not i.lower() in "aeiou":
    consonantes = "bcdfghjklmnpqrstvwxyz"
    if i.lower() in consonantes:
        return True
    else:
        return False


# r1
def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    else:
        return False


def validar_digitos_par(i):
    if i in "02468":
        return True
    else:
        return False


def validar_vocales(letra):
    # .lower() transforma los caracteres a minuscula / .upper() que transforma los caracteres a mayuscula
    if letra.lower() in "aeiou":  # si i esta en estos caracteres ("aeiou")
        return True
    else:  # todos los caracteres que no sean "aeiou"
        return False


def principal():

    fd = "archivito.txt"    # file description ; nombre del archivo
    m = open(fd, "rt")      # read text ; leer texto
    linea = m.readline()    # string , str

    #                     12345678012
    ''' 1 - Determinar la cantidad de palabras que empiezan con una vocal (mayúscula o minúscula) e
incluyen dos o más dígitos.
'''
    r1_cumplen = 0              # cantidad de palabras que cumplen
    r1_cont_caracteres = 0
    r1_empieza_vocal = False
    r1_cont_digitos = 0

    # sd ds cd cx cv
    ''' 2 - Determinar el porcentaje entero de palabras (con respecto al total de palabras del texto), de las
palabras que tienen al menos dos consonantes seguidas 
    # Porcentaje
    total_palabras --- 100 %
    palabras_cumplen --- porc = palabras_cumplen * 100 / total_palabras
'''
    r2_porc = 0  # la respuesta en porcentaje
    r2_total_palabras = 0
    r2_total_palabras_cumplen = 0
    r2_tiene_una_cons = False
    r2_tiene_dos_cons = False

    #                     longitud
    ''' 3 - Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que
terminan con una vocal y no contenga al menos una letra "b" (mayúscula o minúscula). '''

    r3_mayor = None             # calcular el mayor
    r3_cont_caracteres = 0
    r3_ultima_letra = ""
    r3_tiene_b = False

    ''' 4 - Determinar cuántas palabras incluyen la expresión “so” (con cualquiera de sus letras en minúscula
o mayúscula) pero de tal forma que antes de esa expresión haya aparecido una ‘p’ en cualquier
lugar '''

    r4_cumplen = 0
    r4_tiene_s = False
    r4_tiene_so = False
    r4_tiene_p = False

    # linea = "A23sd as."
    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":
            # r1
            r1_cont_caracteres += 1         # 5

            es_vocal_r1 = validar_vocales(i)        # return True si es vocal, return False si no lo es
            if r1_cont_caracteres == 1 and es_vocal_r1:
                r1_empieza_vocal = True

            es_digito_r1 = validar_digitos(i)       # return True si es digito, False si no lo es
            if es_digito_r1:
                r1_cont_digitos += 1        # 2

            # r2
            es_consonante_r2 = validar_consonantes(i)   # return True si es consonnante,  false si no lo es

            if r2_tiene_una_cons and es_consonante_r2:
                r2_tiene_dos_cons = True

            elif es_consonante_r2:
                r2_tiene_una_cons = True

            else:
                r2_tiene_una_cons = False

            # r3
            r3_cont_caracteres += 1
            r3_ultima_letra = i

            if i.lower() == "b":
                r3_tiene_b = True

            # r4
            if r4_tiene_s and i.lower() == "o":
                r4_tiene_so = True
            elif i.lower() == "s":      # i == "S" or i == "s":
                r4_tiene_s = True
            else:
                r4_tiene_s = False

            if i.lower() == "p" and not r4_tiene_so:
                r4_tiene_p = True

        # Estoy fuera de una palabra / Termino una palabra
        else:                   # si i == " " or i == "."

            # r1
            if r1_empieza_vocal and r1_cont_digitos >= 2:
                r1_cumplen += 1

            # r2
            r2_total_palabras += 1
            if r2_tiene_dos_cons:
                r2_total_palabras_cumplen += 1

            # r3
            es_ult_letra_vocal_r3 = validar_vocales(r3_ultima_letra)
            if not r3_tiene_b and es_ult_letra_vocal_r3:
                # 6
                if r3_mayor is None or r3_cont_caracteres > r3_mayor:
                    r3_mayor = r3_cont_caracteres       # 6

            # r4
            if r4_tiene_so and r4_tiene_p:
                r4_cumplen += 1

            # Apagar Banderas, Reiniciar contadores, etc
            # r1
            r1_cont_caracteres = 0
            r1_empieza_vocal = False
            r1_cont_digitos = 0

            # r2
            r2_tiene_una_cons = False
            r2_tiene_dos_cons = False

            # r3
            r3_cont_caracteres = 0
            r3_ultima_letra = ""
            r3_tiene_b = False

            # r4
            r4_tiene_s = False
            r4_tiene_so = False
            r4_tiene_p = False

    # Estoy fuera del ciclo for
    m.close()

    r2_porc = calcular_porcentaje(r2_total_palabras, r2_total_palabras_cumplen)


    print("1 - Resultados:", r1_cumplen)
    print("2 - Resultados:", r2_porc)
    print("3 - Resultados:", r3_mayor)

    print("4 - Resultados:", r4_cumplen)


if __name__ == '__main__':
    principal()


