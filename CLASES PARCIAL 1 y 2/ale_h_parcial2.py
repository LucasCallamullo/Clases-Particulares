


# r1
def validar_minusculas(i):
    if "a" <= i <= "z":
        return True
    return False


def validar_digitos_impares(i):
    if i in "13579":
        return True
    else:
        return False


def validar_digitos(i):
    # if i in "0123456789":
    if "0" <= i <= "9":
        return True
    return False


# r3
def calcular_promedio(cont, acum):
    prom = 0
    if cont != 0:
        prom = acum // cont
    return prom


def validar_consonantes(i):
    # if "a" <= i.lower() <= "z" and not i in "aeiou":
    consonantes = "bcdfghjklmnpqrstvwxyz"
    if i.lower() in consonantes:
        return True
    else:
        return False


def validar_mayusculas(i):
    if "A" <= i <= "Z":
        return True
    else:
        return False


# r2
def validar_vocales(letra):     # o
    # .lower() transoformo el caracter a minuscula / .upper() transforma a mayuscula
    if letra.lower() in "aeiou":  # si i esta en "aeiou"
        return True
    else:
        return False            # return retornar regresar devolver


def principal():

    fd = "entrada.txt"      # file description ; nombre del archivo
    m = open(fd, "rt")      # read text         ; leer texto
    linea = m.readline()    # str

    #       1234567
    ''' 1 - Determinar la cantidad de palabras comienzan con un dígito impar, pero tales que el 
resto de sus caracteres son letras en minúsculas. '''

    r1_cumplen = 0      # hace referencia a al arespueta
    r1_cont_caracteres = 0
    r1_empieza_digito_impar = False
    r1_todas_minusculas = True

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas 
que su ultima letra es una vocal y contenga al menos una letra "b" (mayúscula o minúscula). '''
    r2_mayor = None
    r2_cont_caracteres = 0
    r2_ultima_letra = ""
    r2_tiene_b = False

    ''' 3 - Determinar el promedio entero de caracteres por palabra entre las palabras que tienen más
consonantes que vocales, pero no contienen ninguna "m" ni tampoco ninguna "a" 
    # Promedio = una sumatoria de cosas (acumulador) / la cantidad de cosas que sumamos (contador)
    r3_cont_caracteres = 0
    r3_acum_total = 0
    r3_cont_total = 0
'''
    r3_prom = 0         # la respuesta prom
    r3_cont_total = 0
    r3_acum_total = 0
    r3_cont_caracteres = 0
    r3_cont_vocales = 0
    r3_cont_consonantes = 0
    r3_tiene_m_a = False

    # da de di do du            # SO     DS as mp ea
    # si te pidieran dos mayusculas
    # r4_tiene_una_mayus = False
    # r4_tiene_dos_mayus = False
    ''' 4 - Determinar cuántas palabras incluyen dos o más veces la expresión que conforman la letra "d"
mas una vocal (con cualquiera de sus letras en minúscula o mayúscula) pero de tal forma que antes de la
sigla aparezca una p. '''
    r4_cumplen = 0      # hace referencia a la respuesta del enunciado
    r4_tiene_d = False
    r4_tiene_d_vocal = False
    r4_cont_d_vocal = 0
    r4_tiene_p = False

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # r1
            r1_cont_caracteres += 1

            es_digito_impar_r1 = validar_digitos_impares(i) # true si es digito impar, false si no lo es
            if es_digito_impar_r1 and r1_cont_caracteres == 1:
                r1_empieza_digito_impar = True

            es_minusculas_r1 = validar_minusculas(i)        # true si es consonante, false si no lo es
            if not es_minusculas_r1 and r1_cont_caracteres > 1:
                r1_todas_minusculas = False

            # r2
            r2_cont_caracteres += 1
            r2_ultima_letra = i

            if i.lower() == "b":        # if i == "b" or i == "B":
                r2_tiene_b = True

            # r3
            r3_cont_caracteres += 1

            es_vocal_r3 = validar_vocales(i)    # true si es vocal, false si no lo es
            if es_vocal_r3:
                r3_cont_vocales += 1

            es_consonante_r3 = validar_consonantes(i)   # true si es cons, false si no lo es
            if es_consonante_r3:
                r3_cont_consonantes += 1

            if i.lower() == "m" or i.lower() == "a":
                r3_tiene_m_a = True

            # r4
            es_vocal_r4 = validar_vocales(i)
            if r4_tiene_d and es_vocal_r4:
                r4_tiene_d_vocal = True
            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

            if r4_tiene_d_vocal:
                r4_cont_d_vocal += 1
                r4_tiene_d_vocal = False

            # if i.lower() == "p" and not r4_tiene_d_vocal:
            if i.lower() == "p" and r4_cont_d_vocal == 0:
                r4_tiene_p = True

        # Estoy fuera de una palabra / Termino una palabra
        else:

            # r1
            if r1_todas_minusculas and r1_empieza_digito_impar:
                r1_cumplen += 1

            # r2
            es_vocal_r2 = validar_vocales(r2_ultima_letra)     # True si era vocal, False si no lo es
            if es_vocal_r2 and r2_tiene_b:
                if r2_mayor is None or r2_cont_caracteres > r2_mayor:
                    r2_mayor = r2_cont_caracteres

            # r3
            if r3_cont_consonantes > r3_cont_vocales and not r3_tiene_m_a:
                r3_acum_total += r3_cont_caracteres
                r3_cont_total += 1

            # r4
            if r4_cont_d_vocal >= 2 and r4_tiene_p:
                r4_cumplen += 1

            # Apagar banderas, Reiniciar contadores, etc etc
            # r1
            r1_cont_caracteres = 0
            r1_empieza_digito_impar = False
            r1_todas_minusculas = True

            # r2
            r2_cont_caracteres = 0
            r2_ultima_letra = ""
            r2_tiene_b = False

            # r3
            r3_cont_caracteres = 0
            r3_cont_vocales = 0
            r3_cont_consonantes = 0
            r3_tiene_m_a = False

            # r4
            r4_tiene_d = False
            r4_tiene_d_vocal = False
            r4_cont_d_vocal = 0
            r4_tiene_p = False

    # Estoy fuera del ciclo for
    m.close()

    r3_prom = calcular_promedio(r3_cont_total, r3_acum_total)

    print(" 1 - Resultados:", r1_cumplen)
    print(" 2 - Resultados:", r2_mayor)
    print(" 3 - Resultados:", r3_prom)
    print(" 4 - Resultados:", r4_cumplen)


if __name__ == "__main__":
    principal()
