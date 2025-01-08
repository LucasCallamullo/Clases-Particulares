





# r1
def validar_minusculas(i):
    # return "a" <= i <= "z"
    if "a" <= i <= "z":
        return True
    return False


def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    else:
        return False


# r3
def validar_consonantes(i):
    # if "a" <= i.lower() <= "z":
    #    if not i.lower() in "aeiou":
    #        return True
    # return False
    consonantes = "bcdfghjklmnpqrstvwxyz"
    if i.lower() in consonantes:
        return True
    return False


def validar_vocales(i):
    # .lower() lo que hace es transformar los caracteres a minuscula / .upper() lo que hace es transformar los caracteres a mayuscula
    vocales = "aeiou"
    if i.lower() in vocales:  # Si i(caracter) esta en "aeiou"
        return True            #
    else:
        return False


def principal():

    fd = "archivito.txt"     # fd ; file description ; nombre del archivo
    m = open(fd, "rt")      # read text ; leer texto
    linea = m.readline()


    ''' 1 - Determinar la cantidad de palabras que comienzan con un dígito, pero tales que el resto de sus
caracteres son letras en minúsculas '''
                        # 12
    r1 = 0              # la cantidad de palabras que cumplieron las condicones
    r1_cont_caracteres = 0
    r1_tiene_digito_pos1 = False
    r1_todas_minusculas = True

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que
contienen al menos una ‘c’ '''
    r2 = None           # mayor longitud
    r2_cont_caracteres = 0
    r2_tiene_c = False


    ''' 3 - Determinar cuántas palabras tienen tienen más consonantes que vocales, pero no contienen
ninguna ‘m’ ni tampoco ninguna ‘a' '''
    r3 = 0      # la cantidad de palabras que cumplieron las condicones
    r3_cont_consonantes = 0
    r3_cont_vocales = 0
    r3_tiene_ma = False




    ''' 4 - . Determinar cuántas palabras incluyen una sola vez la expresión “se” (con cualquiera de 
    sus letras en minúscula o mayúscula) pero de tal forma que la palabra no tenga ninguna otra ‘s’ 
    ni ninguna otra ‘e’ que las requeridas en la única expresión ‘se’ permitida. 
    '''
    r4 = 0          # la cantidad de palabras que cumplieron las condicones
    r4_tiene_s = False
    r4_tiene_se = False
    r4_cont_e = 0
    r4_cont_s = 0


    # linea = "ese se pase."
    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # r1
            r1_cont_caracteres += 1

            es_digito = validar_digitos(i)      # return True si es digito, return False si no lo es
            if r1_cont_caracteres == 1 and es_digito:
                r1_tiene_digito_pos1 = True

            es_minuscula = validar_minusculas(i) # return True si es minus, return False si no lo es
            if not es_minuscula and r1_cont_caracteres > 1:
                r1_todas_minusculas = False

            # r2
            r2_cont_caracteres += 1
            if i.lower() == "c":
                r2_tiene_c = True

            # r3
            es_vocal = validar_vocales(i)
            if es_vocal:
                r3_cont_vocales += 1

            es_consonante = validar_consonantes(i)
            if es_consonante:
                r3_cont_consonantes += 1

            if i.lower() == "m" or i.lower() == "a":    # if not i in "ma"  # si i no esta en "ma"
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

        # Estoy fuera de una palabra o termino una palabra
        else:

            # r1
            if r1_tiene_digito_pos1 and r1_todas_minusculas:
                r1 += 1

            # r2 = mayor
            if r2_tiene_c:
                if r2 is None or r2_cont_caracteres > r2:
                    r2 = r2_cont_caracteres

            # r3
            if not r3_tiene_ma and r3_cont_consonantes > r3_cont_vocales:
                r3 += 1

            # r4
            if r4_tiene_se and r4_cont_s == 1 and r4_cont_e == 1:
                r4 += 1

            # APAGAR BANDERAS, REINICIAR CONTADORES etc
            # r1
            r1_cont_caracteres = 0
            r1_tiene_digito_pos1 = False
            r1_todas_minusculas = True

            # r2
            r2_cont_caracteres = 0
            r2_tiene_c = False

            # r3
            r3_tiene_ma = False
            r3_cont_vocales = 0
            r3_cont_consonantes = 0

            # r4
            r4_tiene_s = False
            r4_tiene_se = False
            r4_cont_e = 0
            r4_cont_s = 0

    # Estoy fuera del ciclo for
    m.close()

    print("1 - Respuesta:", r1)
    print("2 - Respuesta:", r2)
    print("3 - Respuesta:", r3)
    print("4 - Respuesta:", r4)


if __name__ == '__main__':
    principal()

    # forma 2
    # for linea in m:
    #    print(linea)
    #    for i in linea:
