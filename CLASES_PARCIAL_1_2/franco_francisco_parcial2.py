

# r3
def validar_mayusculas(i):
    if "A" <= i <= "Z":
        return True
    else:
        return False


# r2
def calcular_porcentaje(r2_total_palabras, r2_palabras_cumplen):
    porc = 0
    if r2_total_palabras > 0:
        porc = r2_palabras_cumplen * 100 // r2_total_palabras

    return porc


def validar_consonantes(i):
    consonantes = "bcdfghjklmnpqrstvwxyzñ"
    if i.lower() in consonantes:
        return True
    else:
        return False


# r1
def validar_digitos_impares(i):
    if i in "13579":
        return True
    else:
        return False


def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    else:
        return False


def validar_vocales(i):     # A -> a
    # .lower() transforma los caracteres a minuscula / .upper() transforma los caracteres a mayusculas
    if i.lower() in "aeiou":  # si i esta in "aeiou":
        return True

    return False        #


def principal():

    fd = "entrada.txt"      # file description ; nombre del archivo
    m = open(fd, "rt")      # read text ; leer texto
    linea = m.readline()    # un str

    ''' 1 - Determinar la cantidad de palabras que empiezan con una vocal (mayúscula o minúscula) e
incluyen dos o más dígitos '''
    r1_cumplen = 0      # hace referencia a las palabras que cumplen
    r1_cont_caracteres = 0
    r1_empieza_vocal = False
    r1_cont_digitos = 0

    ''' 2 - Determinar el porcentaje entero de palabras (con respecto al total de palabras del texto),
de las palabras que tienen al menos dos consonantes seguidas. 
    # Porcentaje
    total_palabras ---- 100%
    palabras_cumplen -- porc = palabras_cumplen * 100 / total_palabras
'''
    r2_porc = 0
    r2_total_palabras = 0
    r2_palabras_cumplen = 0
    r2_tiene_una_cons = False
    r2_tiene_dos_cons = False

    ''' 3 - Determinar cuántas palabras tienen más de dos caracteres pero menos de ocho, una 
consonante en la posición 5 y una mayúscula cualquiera en la posición 6 y ademas la ultima letra
de la palabra sea una vocal. '''
    r3_cumplen = 0  # hace referencia a las palabras que cumplen
    r3_cont_caracteres = 0
    r3_tiene_cons_pos5 = False
    r3_tiene_mayus_pos6 = False
    r3_ultima_letra = ""

    ''' 4 - Determinar cuántas palabras incluyen la expresión “so” (con cualquiera de sus letras 
en minúscula o mayúscula) pero de tal forma que antes de esa expresión haya aparecido una ‘p’ 
en cualquier lugar '''
    r4_cumplen = 0
    r4_tiene_s = False
    r4_tiene_so = False
    r4_tiene_p = False

    # linea = "AH23ola Mundo."
    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # r1
            r1_cont_caracteres += 1

            es_vocal_r1 = validar_vocales(i)      # True si es vocal, False si no lo es
            if r1_cont_caracteres == 1 and es_vocal_r1:
                r1_empieza_vocal = True

            es_digito_r1 = validar_digitos(i)     # True si es digito, False si no lo es
            if es_digito_r1:
                r1_cont_digitos += 1

            # r2
            es_consonante_r2 = validar_consonantes(i)    # True si es cons, false si no lo es

            if r2_tiene_una_cons and es_consonante_r2:
                r2_tiene_dos_cons = True
            elif es_consonante_r2:
                r2_tiene_una_cons = True
            else:
                r2_tiene_una_cons = False

            # r3
            r3_cont_caracteres += 1
            es_consonante_r3 = validar_consonantes(i)  # True si es cons, false si no lo es
            if r3_cont_caracteres == 5 and es_consonante_r3:
                r3_tiene_cons_pos5 = True

            es_mayus_r4 = validar_mayusculas(i)     # True si es mayus , False si no lo es
            if r3_cont_caracteres == 6 and es_mayus_r4:
                r3_tiene_mayus_pos6 = True

            r3_ultima_letra = i

            # r4
            if r4_tiene_s and i.lower() == "o":
                r4_tiene_so = True
            elif i.lower() == "s":
                r4_tiene_s = True
            else:
                r4_tiene_s = False

            if i.lower() == "p" and not r4_tiene_so:
                r4_tiene_p = True

        # Estoy fuera de una palabra / Termino una palabra
        else:

            # r1
            if r1_empieza_vocal and r1_cont_digitos >= 2:
                r1_cumplen += 1

            # r2
            r2_total_palabras += 1
            if r2_tiene_dos_cons:
                r2_palabras_cumplen += 1

            # r3
            es_vocal_r3 = validar_vocales(r3_ultima_letra)      # true es vocal , false no lo es
            if r3_tiene_cons_pos5 and r3_tiene_mayus_pos6 and es_vocal_r3 and 2 <= r3_cont_caracteres <= 8:
                r3_cumplen += 1

            # r4
            if r4_tiene_so and r4_tiene_p:
                r4_cumplen += 1

            # Apagar Banderas , Reiniciar contadores
            # r1
            r1_cont_caracteres = 0
            r1_empieza_vocal = False
            r1_cont_digitos = 0

            # r2
            r2_tiene_una_cons = False
            r2_tiene_dos_cons = False

            # r3
            r3_cont_caracteres = 0
            r3_tiene_cons_pos5 = False
            r3_tiene_mayus_pos6 = False
            r3_ultima_letra = ""

            # r4
            r4_tiene_s = False
            r4_tiene_so = False
            r4_tiene_p = False

    # Termino el ciclo for
    m.close()

    r2_porc = calcular_porcentaje(r2_total_palabras, r2_palabras_cumplen)

    print(" 1 - Resultados:", r1_cumplen)
    print(" 2 - Resultados:", r2_porc)
    print(" 3 - Resultados:", r3_cumplen)
    print(" 4 - Resultados:", r4_cumplen)


if __name__ == "__main__":
    principal()