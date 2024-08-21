

# r3
def validar_consonante(i):
    consonantes = "bcdfghjklmnpqrstvwxyzñ"
    if i.lower() in consonantes:
        return True
    return False


def calcular_promedio(r3_acumulador_caracteres, r3_contador_palabras_cumplen):
    prom = 0
    if r3_contador_palabras_cumplen > 0:
        prom = r3_acumulador_caracteres // r3_contador_palabras_cumplen
    return prom


# r2
def validar_vocales(letra):
    vocales = "aeiou"
    if letra.lower() in vocales:    # .lower() transforma a la letra en minuscula   // .upper() transforma todo a mayuscula
        return True             # devolver True si es una vocal
    else:
        return False


# r1
def validar_minusculas(i):
    minus = "abcdefghijklmnopqrstuvwxyzñ"
    # if i in minus:
    if "a" <= i <= "z" or i == "ñ":
        return True
    else:
        return False


def principal():

    archivo = "entrada.txt"
    m = open(archivo, "rt")     # read text, leer texto


    # r1
    ''' 
    Determinar la cantidad de palabras comienzan con un dígito impar, pero tales que el resto de sus
caracteres son letras en minúsculas.
    # 12340
    # HOLA 1MUNDO 
    '''
    r1 = 0              # r1 se refiere a palabras que cumplen
    r1_indice = 0
    r1_digito_impar = False
    r1_todas_minusculas = False

    # r2
    ''' 
    Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que
comienzan con una vocal y contenga al menos una letra "b" (mayúscula o minúscula). 
    '''
    r2_longitud = 0
    r2_comienza_vocal = False
    r2_tiene_b = False
    r2 = None              # r2 se refiere a la longitud mas grande palabras

    # r3
    ''' 
     Determinar el promedio entero de caracteres por palabra entre las palabras que tienen más
consonantes que vocales, pero no contienen ninguna "m" ni tampoco ninguna "a"
'''
    r3_cont_letras = 0
    r3_cont_vocales = 0
    r3_cont_consonantes = 0
    r3_tiene_ma = False
    r3_acumulador_caracteres = 0
    r3_contador_palabras_cumplen = 0

    # r4
    ''' 
    # da de di do du
    Determinar cuántas palabras incluyen dos o más veces la expresión que conforman la letra "d"
mas una vocal (con cualquiera de sus letras en minúscula o mayúscula) pero de tal forma que la
palabra termine además con una vocal.
    '''
    r4_tiene_d = False
    r4_tiene_d_mas_vocal = False
    r4_cont_d_mas_vocal = 0
    r4_ult_caracter = None
    r4 = 0

    for linea in m:
        # linea = "1hola 1asdAa."
        for i in linea:

            # estoy dentro de una palabra
            if i != " " and i != ".":                   # if i not in " .":

                # r1
                r1_indice += 1
                es_minuscula = validar_minusculas(i)    # return True si es minuscula y False si no lo es

                if r1_indice == 1 and i in "13579":
                    r1_digito_impar = True

                # if r1_digito_impar and es_minuscula:
                elif r1_digito_impar and es_minuscula:
                    r1_todas_minusculas = True

                # if r1_digito_impar and not es_minuscula:
                else:
                    r1_todas_minusculas = False
                    r1_digito_impar = False

                # r2
                r2_longitud += 1
                es_vocal = validar_vocales(i)       # return True si es vocal y False si no lo es
                if r2_longitud == 1 and es_vocal:
                    r2_comienza_vocal = True

                if i.lower() == "b":
                    r2_tiene_b = True

                # r3
                r3_cont_letras += 1
                if es_vocal:
                    r3_cont_vocales += 1

                es_consonante = validar_consonante(i)
                if es_consonante:
                    r3_cont_consonantes += 1

                if i.lower() == "m" or i.lower() == "a":
                    r3_tiene_ma = True

                # r4
                es_vocal4 = validar_vocales(i)
                if i.lower() == "d":
                    r4_tiene_d = True

                elif r4_tiene_d and es_vocal4:
                    r4_tiene_d_mas_vocal = True

                else:
                    r4_tiene_d = False

                if r4_tiene_d_mas_vocal:
                    r4_cont_d_mas_vocal += 1
                    r4_tiene_d_mas_vocal = False

                r4_ult_caracter = i

            # termino una palabra
            else:

                # r1
                if r1_digito_impar and r1_todas_minusculas:
                    r1 += 1

                # r2
                if r2_comienza_vocal and r2_tiene_b:
                    if r2 is None or r2_longitud > r2:
                        r2 = r2_longitud

                # r3
                if r3_cont_consonantes > r3_cont_vocales and not r3_tiene_ma:
                    r3_acumulador_caracteres += r3_cont_letras
                    r3_contador_palabras_cumplen += 1

                # r4
                es_vocal_r4 = validar_vocales(r4_ult_caracter)
                if r4_cont_d_mas_vocal >= 2 and es_vocal_r4:
                    r4 += 1

                # Apagar banderas, reiniciar contadores etc
                # r1
                r1_todas_minusculas = False
                r1_digito_impar = False
                r1_indice = 0

                # r2
                r2_longitud = 0
                r2_comienza_vocal = False
                r2_tiene_b = False

                # r3
                r3_cont_letras = 0
                r3_cont_vocales = 0
                r3_cont_consonantes = 0
                r3_tiene_ma = False

                # r4
                r4_tiene_d = False
                r4_tiene_d_mas_vocal = False
                r4_cont_d_mas_vocal = 0
                r4_ult_caracter = None

    # estoy fuera del archivo
    r3 = calcular_promedio(r3_acumulador_caracteres, r3_contador_palabras_cumplen)


    # resultados:
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()