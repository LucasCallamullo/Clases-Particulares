

# r4
def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    else:
        return False


# r3
def validar_minuscula(i):
    if "a" <= i <= "z":
        return True
    else:
        return False


def validar_consonantes(i):
    if i.lower() in "bcdfghjklmnpqrstvwxyz":
        return True
    else:
        return False


def validar_vocales(i): # o
    # .lower() Transformar al caracter si pudiera en una minuscula / .upper() Transformar al caracter si pudiera en una mayuscula
    # A -> a
    if i.lower() in "aeiou":  # si la i esta en "aeiou"
        return True         # devolver o retornar
    else:
        return False


# r1
def validar_digitos_impares(i): # s
    if i in "13579":
        return True
    else:
        return False


def principal():

    fd = "entrada.txt"      # file description ; nombre del archivo
    m = open(fd, "rt")      # read text ; leer texto
    linea = m.readline()    # les recupera un str

    #                     1234567801
    ''' 1 - determinar la cantidad de palabras que empiezen con digito impar y contenga al menos una
"s" (mayuscula o minuscula) en la posicion 3, pero no contenga ninguna "p", ademas que su longitud
sea de un tamaño impar. '''
    r1_cumplen = 0      # hace referencia a la respuesta del enunciado
    r1_cont_caracteres = 0
    r1_empieza_digito_impar = False
    r1_tiene_s_pos3 = False
    r1_tiene_p = False

    #
    ''' 2 - calcular la longitud en cantidad de caracteres de la menor palabra que contenga en su
ultima letra una vocal, y contenga al menos dos "t"(mayuscula o minuscula). '''
    r2_menor = None
    r2_cont_caracteres = 0
    r2_ultima_letra = ""
    r2_cont_t = 0

    #                              112233
    ''' 3 - calcular el porcentaje entero de las palabras (sobre el total de palabras) que contengan mas
vocales que consonantes, pero tales que el resto de sus caracteres son letras en minúsculas.
    # Porcentaje
        Total_palabras ---- 100 %
        palabras_cumplen --- X = palabras_cumplen * 100 // Total_palabras
'''
    r3_porc = 0
    r3_cont_total_palabras = 0
    r3_cont_total_cumplen = 0
    r3_cont_vocales = 0
    r3_cont_consonantes = 0
    r3_todas_minusculas = True

    # da de di do du                HC      SO TS
    ''' 4 - determinar la cantidad de palabras que contengan "d + vocal" pero ademas
contenga un digito antes de encontrar la sigla. '''
    r4_cumplen = 0      # hace referencia a la respuesta del enunciado
    r4_tiene_d = False
    r4_tiene_d_vocal = False
    r4_tiene_digito = False

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # r1
            r1_cont_caracteres += 1         # 3

            es_digito_impar_r1 = validar_digitos_impares(i)     # return True si es digito impar, False si no lo es
            # es_digito_impar_r1 = True

            if r1_cont_caracteres == 1 and es_digito_impar_r1:  # es_digito_impar_r1 esta em True
                r1_empieza_digito_impar = True

            if r1_cont_caracteres == 3 and i.lower() == "s":    # if r1_cont_caracteres == 3 and (i == "s" or i == "S"):
                r1_tiene_s_pos3 = True

            if i.lower() == "p":
                r1_tiene_p = True

            # r2
            r2_cont_caracteres += 1
            r2_ultima_letra = i

            if i.lower() == "t":
                r2_cont_t += 1

            # r3
            es_vocal_r3 = validar_vocales(i)        # return True si es vocal False sino lo es
            if es_vocal_r3:
                r3_cont_vocales += 1

            es_consonante_r3 = validar_consonantes(i)
            if es_consonante_r3:
                r3_cont_consonantes += 1

            es_minuscula_r3 = validar_minuscula(i)
            if not es_minuscula_r3:
                r3_todas_minusculas = False

            # r4
            es_vocal_r4 = validar_vocales(i)
            # True

            if i.lower() == "d":
                r4_tiene_d = True
            elif r4_tiene_d and es_vocal_r4:
                r4_tiene_d_vocal = True
            else:
                r4_tiene_d = False

            es_digito_r4 = validar_digitos(i)
            if es_digito_r4 and not r4_tiene_d_vocal:
                r4_tiene_digito = True

        # Termino una palabra / Estoy fuera de una palabra
        else:
            # r1
            if r1_empieza_digito_impar and r1_tiene_s_pos3 and not r1_tiene_p and r1_cont_caracteres % 2 != 0:
                r1_cumplen += 1

            # r2
            es_vocal_ult_letra_r2 = validar_vocales(r2_ultima_letra)    # return True si es vocal, False si no lo es
            if r2_cont_t >= 2 and es_vocal_ult_letra_r2:
                if r2_menor is None or r2_cont_caracteres < r2_menor:
                    r2_menor = r2_cont_caracteres

            # r3
            r3_cont_total_palabras += 1
            if r3_cont_vocales > r3_cont_consonantes and r3_todas_minusculas:
                r3_cont_total_cumplen += 1

            # r4
            if r4_tiene_digito and r4_tiene_d_vocal:
                r4_cumplen += 1

            # Apagar Las banderas / Reiniciar los contadores
            # r1
            r1_cont_caracteres = 0
            r1_empieza_digito_impar = False
            r1_tiene_s_pos3 = False
            r1_tiene_p = False

            # r2
            r2_cont_caracteres = 0
            r2_ultima_letra = ""
            r2_cont_t = 0

            # r3
            r3_cont_vocales = 0
            r3_cont_consonantes = 0
            r3_todas_minusculas = True

            # r4
            r4_tiene_d = False
            r4_tiene_d_vocal = False
            r4_tiene_digito = False

    # Sali del ciclo For
    m.close()

    # r3
    r3_porc = 0
    if r3_cont_total_palabras != 0:
        r3_porc = r3_cont_total_cumplen * 100 // r3_cont_total_palabras

    print(" 1 - Resultados:", r1_cumplen)
    print(" 2 - Resultados:", r2_menor)
    print(" 3 - Resultados:", r3_porc)
    print(" 4 - Resultados:", r4_cumplen)


if __name__ == '__main__':
    principal()
