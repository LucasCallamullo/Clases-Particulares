

# r5
def calcular_porcentaje(r5_total_palabras, r5_total_cumplen):
    porc = 0
    if r5_total_palabras != 0:
        porc = r5_total_cumplen * 100 // r5_total_palabras
    return porc


def validar_consonantes(i):
    # if "A" <= i.upper() <= "Z" and i.lower() not in "aeiou":
    if i in "bcdfghjklmnpqrstvwxyz":
        return True
    return False
    # if i in "qwrtypsdfghjklzxcvbnm":


# r1
def validar_mayusculas(i):
    if "A" <= i <= "Z":
        return True
    return False


def validar_digitos(i):
    # return "0" <= i <= "9"
    if "0" <= i <= "9":
        return True
    return False


def validar_digitos_impares(i):
    '''
        if "0" <= i <= "9":
            if int(i) % 2 != 0:
                return True
        return False
    '''
    if i in "13579":
        return True
    return False


def validar_vocales_sin_u(i):
    # .lower() transforma el caracter a minuscula / .upper() a mayuscula
    if i.lower() in "aeio":  # si la i esta en "aeio"
        return True  # retornar devolver
    else:
        return False


def validar_vocales(i): # o
    # .lower() transforma el caracter a minuscula / .upper() a mayuscula
    if i.lower() in "aeiou":  # si la i esta en "aeiou"
        return True         # retornar devolver
    else:
        return False


def principal():

    m = open("entrada.txt", "rt")   # read text ; leer texto
    linea = m.readline()            # nos trae un str
    m.close()

    ''' 1 - Determinar la cantidad de palabras que tienen un dígito en la segunda y en la cuarta 
posición, pero de tal forma que el resto de sus caracteres son letras mayúsculas. '''
    r1 = 0
    r1_cont_caracteres = 0
    r1_tiene_dos_digitos = True
    r1_todas_mayusculas = True

    ''' 2 -         
    Determinar la longitud (en cantidad de caracteres) de la palabra más corta entre aquellas que 
comienzan con una "t" (minúscula o mayúscula) ademas esa longitud debe ser par.
'''
    r2 = None
    r2_cont_caracteres = 0
    r2_empieza_t = False

    ''' 3 - Determinar cuántas palabras están conformadas solo por vocales (minúsculas o mayúsculas), 
pero no contienen ninguna "u" (minúscula o mayúscula). ademas que termine con la letra "A" (mayus o minus) '''
    r3 = 0
    r3_todas_vocales = True
    r3_ultima_letra = ""

    # mp hc
    ''' 4 - Determinar cuántas palabras incluyen la expresión "di" (con cualquiera de sus letras en 
minúscula o mayúscula) pero de tal forma que a su vez no comiencen con la expresión "di" '''
    r4 = 0
    r4_cont_caracteres = 0
    r4_tiene_d = False
    r4_tiene_di = False
    r4_empieza_di = False

    ''' 5 - Determinar el porcentaje entero de palabras (con respecto al total de palabras del texto),
de las palabras que tienen dos vocales (en minúscula o mayúscula) y finalizan con un consonante 
    # Porcentaje
        Total_Palabras --- 100 %
        Palabras_Cumplen --- X = Palabras_Cumplen * 100 // Total_Palabras
'''
    r5 = 0
    r5_total_palabras = 0
    r5_total_cumplen = 0
    r5_cont_vocales = 0
    r5_ultima_letra = ""

    for i in linea:

        # Estoy dentro de la palabra
        if i != " " and i != ".":

            # r1
            r1_cont_caracteres += 1

            if r1_cont_caracteres == 2 or r1_cont_caracteres == 4:
                es_digito_r1 = validar_digitos(i)   # return True si es digito, False si no lo es
                if not es_digito_r1:        # si esta en false o sea que no es digito apago mi bandera
                    r1_tiene_dos_digitos = False

            else:
                es_mayusculas_r1 = validar_mayusculas(i)    # return True si es mayus, False si no lo es
                if not es_mayusculas_r1:
                    r1_todas_mayusculas = False

            # r2
            r2_cont_caracteres += 1

            if r2_cont_caracteres == 1 and i.lower() == "t":
                r2_empieza_t = True

            # r3
            es_vocal_sin_u = validar_vocales_sin_u(i)     # return True si es vocal, False si no lo es
            if not es_vocal_sin_u:
                r3_todas_vocales = False

            r3_ultima_letra = i

            # r4
            r4_cont_caracteres += 1
            if r4_tiene_d and i.lower() == "i":
                r4_tiene_di = True

                # if r2_cont_caracteres == 2:
                #    r4_empieza_di = True

            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

            # que encuentres una "p" antes de la sigla
            if i.lower() == "p" and not r4_tiene_di:
                pass
            # que encuentres una "p" despues de la sigla
            if i.lower() == "p" and r4_tiene_di:
                pass

            # r5
            es_vocal_r5 = validar_vocales(i)
            if es_vocal_r5:
                r5_cont_vocales += 1

            r5_ultima_letra = i

        # Estoy Fuera de la palabra / Termino la palabra
        else:

            # r1
            if r1_tiene_dos_digitos and r1_todas_mayusculas:
                r1 += 1

            # r2
            if r2_empieza_t and r2_cont_caracteres % 2 == 0:
                if r2 is None or r2_cont_caracteres < r2:
                    r2 = r2_cont_caracteres

            # r3
            # si te pidieran que termine en vocal
            # es_vocal_r3 = validar_vocales(r3_ultima_letra)
            if r3_todas_vocales and r3_ultima_letra.lower() == "a":
                r3 += 1

            # r4
            if r4_tiene_di and not r4_empieza_di:
                r4 += 1

            # r5
            r5_total_palabras += 1

            es_consonante_r5 = validar_consonantes(r5_ultima_letra)
            if r5_cont_vocales == 2 and es_consonante_r5:
                r5_total_cumplen += 1

            # Reiniciar / Apagar banderas, contadores
            # r1
            r1_cont_caracteres = 0
            r1_tiene_dos_digitos = True
            r1_todas_mayusculas = True

            # r2
            r2_cont_caracteres = 0
            r2_empieza_t = False

            # r3
            r3_todas_vocales = True

            # r4
            r4_cont_caracteres = 0
            r4_tiene_d = False
            r4_tiene_di = False
            r4_empieza_di = False

            # r5
            r5_cont_vocales = 0
            r5_ultima_letra = ""

    # Termino el ciclo

    r5 = calcular_porcentaje(r5_total_palabras, r5_total_cumplen)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)
    print("Quinto resultado:", r5)


if __name__ == "__main__":
    principal()

