

# r3
def calcular_porcentaje(r3_total_cumplen, r3_total_palabras):
    porc = 0
    if r3_total_palabras != 0:
        porc = r3_total_cumplen * 100 // r3_total_palabras
    return porc


# r2
def validar_digitos(i):
    # if i in "0123456789"
    if "0" <= i <= "9":
        return True
    else:
        return False


def validar_digitos_impares(i):
    # return i in "13579"
    if i in "13579":
        return True
    return False


def validar_vocales(i):     # A -> a
    # .lower() transforma el caracter a minuscula
    if i.lower() in "aeiou":  # si la i esta en "aeiou"
        return True
    else:
        return False


def validar_consonantes(i):
    # if "a" <= i <= "z" and i not in "aeiou":
    # .lower() transforma el caracter a minuscula
    if i.lower() in "bcdfghijklmnpqrstvwxyz":  # si la i esta en "aeiou"
        return True
    else:
        return False


# r1
def validar_minusculas(i):
    if "a" <= i <= "z":
        return True
    return False


# r5
def validar_mayusculas(i):
    if "A" <= i <= "Z":
        return True
    return False


def principal():

    m = open("entrada.txt", "rt")   # read text ; leer texto
    linea = m.readline()            # nos trae un str

    ''' 1 - Determinar la cantidad de palabras tienen un solo dígito y además todo el resto
de sus caractres son minúsculas 
'''
    r1 = 0
    r1_cont_digitos = 0
    r1_todas_minusculas = True

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más corta de aquellas 
que tienen al menos un dígito y que su longitud sea par pero no tenga "t" '''
    r2 = None
    r2_cont_caracteres = 0
    r2_tiene_digito = False
    r2_tiene_t = False

    #                                1234560120123456780
    ''' 3 - Determinar el porcentaje entero de palabras (con respecto al total de palabras del texto), 
de las palabras que empiezen con una vocal (en minúscula o mayúscula) y finalizan con un dígito 
    # Porcentaje
        Total_Palabras --- 100 %
        palabras_cumplen --- porc = palabras_cumplen * 100 // Total_Palabras
'''
    r3 = 0
    r3_total_palabras = 0
    r3_total_cumplen = 0
    r3_cont_caracteres = 0
    r3_empieza_vocal = False
    r3_ultimo_caracter = ""

    # de  so  sp ts ls
    ''' 4 - Determinar cuántas palabras incluyen la expresión "de" (con cualquiera de sus letras en 
minúscula o mayúscula) pero de tal forma que después de ella(la sigla) aparezca una "t" 
(minúscula o mayúscula) en cualquier lugar '''
    r4 = 0
    r4_tiene_d = False
    r4_tiene_de = False
    r4_tiene_t = False
    # no comiencen con la expresión "de"
    r4_cont_caracteres = 0
    r4_empieza_de = False

    ''' 5 - Determinar la cantidad de palabras que tienen un dígito en la segunda y en la 
cuarta posición, pero de tal forma que el resto de sus caracteres son letras mayúsculas.  '''
    r5 = 0
    r5_cont_caracteres = 0
    r5_tiene_digitos = True
    r5_todas_mayusculas = True

    for i in linea:

        # Estoy dentro de la palabra
        if i != " " and i != ".":

            # r1
            es_digito_r1 = validar_digitos(i)
            if es_digito_r1:
                r1_cont_digitos += 1
            else:
                es_minuscula_r1 = validar_minusculas(i)     # return True si minus, False si no lo es
                if not es_minuscula_r1:
                    r1_todas_minusculas = False

            # r2
            r2_cont_caracteres += 1

            es_digito_r2 = validar_digitos(i)
            if es_digito_r2:
                r2_tiene_digito = True

            if i.lower() == "t":
                r2_tiene_t = True

            # r3
            r3_cont_caracteres += 1
            r3_ultimo_caracter = i

            es_vocal_r3 = validar_vocales(i)        # return True si era Vocal, False si no lo es
            if r3_cont_caracteres == 1 and es_vocal_r3:
                r3_empieza_vocal = True

            # r4
            r4_cont_caracteres += 1

            if r4_tiene_d and i.lower() == "e":
                r4_tiene_de = True

                if r2_cont_caracteres == 2:
                    r4_empieza_de = True

            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

            if i.lower() == "t" and r4_tiene_de:
                r4_tiene_t = True

            # r5
            r5_cont_caracteres += 1
            if r5_cont_caracteres == 2 or r5_cont_caracteres == 4:
                es_digito_r5 = validar_digitos(i)
                if not es_digito_r5:
                    r5_tiene_digitos = False

            else:
                es_mayuscula_r5 = validar_mayusculas(i)
                if not es_mayuscula_r5:
                    r5_todas_mayusculas = False

        # Termine una palabra
        else:

            # r1
            if r1_todas_minusculas and r1_cont_digitos == 1:
                r1 += 1

            # r2
            if r2_tiene_digito and not r2_tiene_t and r2_cont_caracteres % 2 == 0:
                if r2 is None or r2_cont_caracteres < r2:
                    r2 = r2_cont_caracteres

            # r3
            r3_total_palabras += 1

            es_digito_r3 = validar_digitos(r3_ultimo_caracter)  # return True si es digito o False si nol oes
            if r3_empieza_vocal and es_digito_r3:
                r3_total_cumplen += 1

            # r4
            if r4_tiene_de and not r4_empieza_de and r4_tiene_t:
                r4 += 1

            # r5
            if r5_tiene_digitos and r5_todas_mayusculas:
                r5 += 1

            # Reiniciar banderas y contadores

            # r1
            r1_cont_digitos = 0
            r1_todas_minusculas = True

            # r2
            r2_cont_caracteres = 0
            r2_tiene_digito = False
            r2_tiene_t = False

            # r3
            r3_cont_caracteres = 0
            r3_empieza_vocal = False
            r3_ultimo_caracter = ""

            # r4
            r4_tiene_d = False
            r4_tiene_de = False
            r4_tiene_t = False
            r4_cont_caracteres = 0
            r4_empieza_de = False

            # r5
            r5_cont_caracteres = 0
            r5_tiene_digitos = True
            r5_todas_mayusculas = True

    # Termino el ciclo
    m.close()

    r3 = calcular_porcentaje(r3_total_cumplen, r3_total_palabras)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)
    print("Quinto resultado:", r5)


if __name__ == "__main__":
    principal()