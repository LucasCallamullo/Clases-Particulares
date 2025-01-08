

# r5
def calcular_porcentaje(r5_cont_palabras_cumplen, r5_cont_total_palabras):
    # total_palabras --- 100%
    # palabras_cumplne --- X =
    porc = 0
    if r5_cont_total_palabras != 0:
        porc = r5_cont_palabras_cumplen * 100 // r5_cont_total_palabras
    return porc


def validar_minusculas(i):
    if "a" <= i <= "z":
        return True
    else:
        return False


def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    else:
        return False


def validar_consonantes(i):
    # if "a" <= i <= "z" and not i in "aeiou":
    #    return True
    # return False
    consonantes = "bcdfghjklmnpqrstvwxyz"
    if i.lower() in consonantes:
        return True
    else:
        return False


def validar_vocales(car):       # O -> o
    # .lower() transforma el caracter a minusscula / .upper() transforma el caracter a mayuscula
    if car.lower() in "aeiou":  # si caracter esta en "aeiou" vocales
        return True         #
    else:
        return False        #


def principal():

    fd = "archivito.txt"        # file description; nombre del archivo
    m = open(fd, "rt")          # read text , leeer texto

    # forma 1
    linea = m.readline()

    ''' 1 - Determinar la cantidad de palabras que comienzan con un dígito, pero tales que el resto de sus
caracteres son letras en minúsculas.
    '''
    r1 = 0              # un contador de la cantidad de palabras que cumplan
    r1_cont_caracteres = 0
    r1_tiene_digito_pos1 = False
    r1_todas_minusculas = True

    ''' 2 - Determina la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que
contienen al menos una ‘c’.  '''
    r2 = None           # La longitud mayor
    r2_cont_caracters = 0
    r2_tiene_c = False

    ''' 3 - Determinar cuántas palabras tienen tienen más consonantes que vocales, pero no contienen
ninguna ‘m’ ni tampoco ninguna ‘a’ '''
    r3 = 0              # un contador de la cantidad de palabras que cumplan
    r3_cont_consonantes = 0
    r3_cont_vocales = 0
    r3_tiene_ma = False

    ''' 4 - Determinar cuántas palabras incluyen una sola vez la expresión “se” (con cualquiera de sus letras
en minúscula o mayúscula) pero de tal forma que la palabra no tenga ninguna otra ‘s’ ni ninguna
otra ‘e’ que las requeridas en la única expresión ‘se’ permitida. '''
    r4 = 0              # un contador de la cantidad de palabras que cumplan
    r4_tiene_s = False
    r4_tiene_se = False
    r4_cont_s = 0
    r4_cont_e = 0

    # ss ss dd
    ''' 5 - Determinar el porcentaje entero de palabras (con respecto al total de palabras del texto), de las
palabras que tienen al menos dos consonantes seguidas
'''
    r5 = 0          # porcentaje
    r5_cont_total_palabras = 0
    r5_cont_palabras_cumplen = 0
    r5_tiene_una_cons = False
    r5_tiene_dos_cons = False

    #
    # linea = casa ca casas.
    for i in linea:
        #     1, 2  3  4
        # i = c, a, s, a,  ,

        # Estoy dentro de una palabra
        if i != " " and i != ".":       # if not i in " .":

            # r1
            r1_cont_caracteres += 1

            es_digito = validar_digitos(i)
            if r1_cont_caracteres == 1 and es_digito:
                r1_tiene_digito_pos1 = True

            es_minuscula = validar_minusculas(i)
            if not es_minuscula and r1_cont_caracteres > 1:
                r1_todas_minusculas = False

            # r2
            r2_cont_caracters += 1
            if i.lower() == "c":
                r2_tiene_c = True

            # r3
            es_vocal_r3 = validar_vocales(i)        # return True Si es vocal, o No es vocal
            if es_vocal_r3:
                r3_cont_vocales += 1

            es_consonante_r3 = validar_consonantes(i)       # True
            if es_consonante_r3:
                r3_cont_consonantes += 1

            if i.lower() == "a" or i.lower() == "m":    # if i.lower() in "ma":
                r3_tiene_ma = True

            # r4
            if r4_tiene_s and i.lower() == "e":
                r4_tiene_se = True

            elif i.lower() == "s":
                r4_tiene_s = True

            else:
                r4_tiene_s = False

            if i.lower() == "s":
                r4_cont_s += 1
            elif i.lower() == "e":
                r4_cont_e += 1

            # r5
            es_consonante_r5 = validar_consonantes(i)
            if r5_tiene_una_cons and es_consonante_r5:
                r5_tiene_dos_cons = True
            elif es_consonante_r5:
                r5_tiene_una_cons = True
            else:
                r5_tiene_una_cons = False


        # Estoy fuera de una palabra / Termino una palabra
        else:
            # r1
            if r1_tiene_digito_pos1 and r1_todas_minusculas:
                r1 += 1

            # r2 = mayor, 4, 2, 5
            if r2_tiene_c:
                if r2 is None or r2_cont_caracters > r2:
                    r2 = r2_cont_caracters

            # r3
            if r3_cont_consonantes > r3_cont_vocales and not r3_tiene_ma:
                r3 += 1

            # r4
            if r4_cont_s == 1 and r4_cont_e == 1 and r4_tiene_se:
                r4 += 1

            # r5
            r5_cont_total_palabras += 1
            if r5_tiene_dos_cons:
                r5_cont_palabras_cumplen += 1

            # APAGAR LAS BANDERAS, reiniciar contadores, etc
            # r1
            r1_cont_caracteres = 0
            r1_tiene_digito_pos1 = False
            r1_todas_minusculas = True

            # r2
            r2_cont_caracters = 0
            r2_tiene_c = False

            # r3
            r3_cont_consonantes = 0
            r3_cont_vocales = 0
            r3_tiene_ma = False

            # r4
            r4_tiene_s = False
            r4_tiene_se = False
            r4_cont_s = 0
            r4_cont_e = 0

            # r5
            r5_tiene_una_cons = False
            r5_tiene_dos_cons = False


    # Estoy Fuera del ciclo for
    r5 = calcular_porcentaje(r5_cont_palabras_cumplen, r5_cont_total_palabras)

    m.close()

    print(" 1 - Resultados:", r1)
    print(" 2 - Resultados:", r2)
    print(" 3 - Resultados:", r3)
    print(" 4 - Resultados:", r4)
    print(" 5 - Resultados:", r5)


if __name__ == '__main__':
    principal()

