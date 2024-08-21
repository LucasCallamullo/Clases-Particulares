

# r4
def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    else:
        return False


# r3
def calcular_porcentaje(r3_total_palabras, r3_total_cumplen):
    porc = 0
    if r3_total_palabras != 0:
        porc = r3_total_cumplen * 100 // r3_total_palabras
    return porc


def validar_minusculas(i):
    if "a" <= i <= "z":
        return True
    else:
        return False


def validar_consonantes(i):
    if i.lower() in "bcdfghjklmnpqrstvwxyz":
        return True
    else:
        return False


def validar_vocales(letra): # o
    # .lower() transforma al caracter si puediera en minuscula
    if letra.lower() in "aeiou":  # si la i esta en "aeiou"
        return True                 # devolver o retornar
    else:
        return False


# r1
def validar_digitos_impares(i):
    if i in "13579":
        return True
    else:
        return False


def principal():

    fd = "entrada.txt"      # file description ; nombre del archivo
    m = open(fd, "rt")      # read text ; leer texto
    linea = m.readline()    # nos recupera la primera linea del archivo, y lo tomo un str

    ''' 1 - Determinar la cantidad de palabras que empiecen con digito impar y contenga al menos una
"s" (mayuscula o minuscula) en la posicion 3, pero no contenga ninguna "p", ademas tenga una 
longitud par. '''
    r1_cumplen = 0          # hacer referencia a las palabras que cumplan las condiciones
    r1_cont_caracteres = 0
    r1_empieza_digito_impar = False
    r1_tiene_s_pos3 = False
    r1_tiene_p = False

    #
    ''' 2 - calcular la longitud en cantidad de caracteres de la menor palabra que contenga en su
ultima letra una vocal, y contenga al menos dos "t"(mayuscula o minuscula). '''
    r2_menor = None         # hace referencia a la respuesta
    r2_cont_caracteres = 0
    r2_ultima_letra = ""
    r2_cont_t = 0

    ''' 3 - calcular el porcentaje entero de las palabras (sobre el total de palabras) que contengan mas
vocales que consonantes, pero tales que sus caracteres son letras en minúsculas. 
    # Porcentaje
        Total_Palabras ---- 100%
        Palabras_CUmplen --- X = Palabras_CUmplen * 100 / Total_Palabras
'''
    r3_porc = 0
    r3_total_palabras = 0
    r3_total_cumplen = 0
    r3_cont_consonantes = 0
    r3_cont_vocales = 0
    r3_todas_minusculas = True

    ''' 4 - determinar la cantidad de palabras que contengan "d+vocal" (mayus o minus) seguidas pero ademas
contenga un digito antes de encontrar la sigla 
    
    # ra                                    MS DS SD LK
    # tiene_r = False                       tiene_una_mayus = False
    # tiene_ra = False                      tiene_dos_mayus = False
'''
    r4_cumplen = 0      # hace referencia a la respuesta del punto
    r4_tiene_d = False
    r4_tiene_d_vocal = False
    r4_tiene_digito = False

    for i in linea:

        # Estoy dentro de la palabra
        if i != " " and i != ".":
            # r1
            r1_cont_caracteres += 1         # 4

            es_digito_impar = validar_digitos_impares(i)    # return True si es digito impar, FAlse si nolo es
            if r1_cont_caracteres == 1 and es_digito_impar:
                r1_empieza_digito_impar = True

            if r1_cont_caracteres == 3 and i.lower() == "s":
                r1_tiene_s_pos3 = True

            if i.lower() == "p":
                r1_tiene_p = True

            # r2
            r2_cont_caracteres += 1
            r2_ultima_letra = i

            if i.lower() == "t":
                r2_cont_t += 1

            # r3
            es_consonante_r3 = validar_consonantes(i) # return True si es consonante
            if es_consonante_r3:
                r3_cont_consonantes += 1

            es_vocal_r3 = validar_vocales(i)    # return True si es vocal
            if es_vocal_r3:
                r3_cont_vocales += 1

            es_minuscula_r3 = validar_minusculas(i) # return True si es minus
            if not es_minuscula_r3:
                r3_todas_minusculas = False

            # r4
            es_vocal_r4 = validar_vocales(i)
            if r4_tiene_d and es_vocal_r4:
                r4_tiene_d_vocal = True
            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

            es_digito_r4 = validar_digitos(i)
            if es_digito_r4 and not r4_tiene_d_vocal:
                r4_tiene_digito = True

        # Termine una palabra / Estamos fuera de la palabra
        else:

            # r1
            if r1_empieza_digito_impar and r1_tiene_s_pos3 and not r1_tiene_p and r1_cont_caracteres % 2 == 0:
                r1_cumplen += 1

            # r2
            es_vocal_ult_r2 = validar_vocales(r2_ultima_letra)   # return True si es vocal False si no lo es
            if r2_cont_t >= 2 and es_vocal_ult_r2:
                if r2_menor is None or r2_cont_caracteres < r2_menor:
                    r2_menor = r2_cont_caracteres

            # r3
            r3_total_palabras += 1
            if r3_todas_minusculas and r3_cont_vocales > r3_cont_consonantes:
                r3_total_cumplen += 1

            # r4
            if r4_tiene_d_vocal and r4_tiene_digito:
                r4_cumplen += 1

            # Reiniciar Contadores / Apagar banderas
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
            r3_cont_consonantes = 0
            r3_cont_vocales = 0
            r3_todas_minusculas = True

            # r4
            r4_tiene_d = False
            r4_tiene_d_vocal = False
            r4_tiene_digito = False

    # Termino el ciclo
    m.close()

    r3_porc = calcular_porcentaje(r3_total_palabras, r3_total_cumplen)

    print(" 1 - Resultados:", r1_cumplen)
    print(" 2 - Resultados:", r2_menor)
    print(" 3 - Resultados:", r3_porc)
    print(" 4 - Resultados:", r4_cumplen)


if __name__ == '__main__':
    principal()
