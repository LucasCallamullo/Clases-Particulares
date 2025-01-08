

# r4
def validar_mayusculas(i):
    if "A" <= i <= "Z":
        return True
    return False


def validar_digitos(i):
    # return "0" <= i <= "9"
    if "0" <= i <= "9":
        return True
    return False


# r3
def calcular_porcentaje(r3_total_palabras, r3_total_palabras_cumplen):
    porc = 0
    if r3_total_palabras != 0:
        porc = r3_total_palabras_cumplen * 100 // r3_total_palabras
    return porc


def validar_minusculas(i):
    if "a" <= i <= "z":
        return True
    return False


def validar_consonantes(i):
    # if "a" <= i.lower() <= "z" and not i in "aeiou":
    consonantes = "bcdfghjklmnpqrstvwxyzñ"
    if i.lower() in consonantes:
        return True
    return False


# r1
def validar_digitos_impares(i):
    if i in "13579":
        return True
    else:
        return False


def validar_vocales(letra):     # o
    # .lower() transforma el caracter si puede a minuscula / .upper() transforma el caracter si puede a mayuscula
    if letra.lower() in "aeiou":  # si la i esta en "aeiou"
        return True     # retornar, devolver,
    else:
        return False


def principal():

    fd = "entrada.txt"  # file description ; nombre del archivo
    m = open(fd, "rt")  # read text ; leer texto
    linea = m.readline()    # str

    #                     12345678
    ''' 1 - determinar la cantidad de palabras que empiezen con digito y contenga al menos 
    una "s" (mayuscula o minuscula) en la posicion 3, pero no contenga ninguna "p".
    '''
    r1_cumplen = 0      # hace referencia a las palabras que cumplan
    r1_cont_caracteres = 0
    r1_empieza_digito_impar = False
    r1_tiene_s_pos3 = False
    r1_tiene_p = False

    #                   longitud
    ''' 2 - calcular la longitud en cantidad de caracteres de la menor palabra que contenga en 
su ultima letra una vocal, contenga al menos dos "t"(mayuscula o minuscula).
    '''
    r2_menor = None         # hace referencia al menor
    r2_cont_caracteres = 0
    r2_cont_t = 0
    r2_ultima_letra = ""

    #                              112233
    ''' 3 - calcular el porcentaje entero de las palabras (sobre el total de palabras) que 
    contengan mas vocales que consonantes, pero tales que el resto de sus
    caracteres son letras en minúsculas.
        # Porcentaje
        Total_palabras --- 100% 
        Palabras_cumplen --- X = palabras_cumplen * 100 // Total_palabras
    '''
    r3_porc = 0             # hace referencia a la rta
    r3_total_palabras = 0
    r3_total_palabras_cumplen = 0
    r3_cont_vocales = 0
    r3_cont_consonantes = 0
    r3_todas_minusculas = True

    ''' 4 - determinar la cantidad de palabras que contengan dos digitos seguidos pero ademas 
    contenga una mayuscula antes de encontrar la sigla.
     # HC SC
    # r_tiene_h = False
    # r_tiene_hc = False 
    # r_tiene_s = False
    # r_tiene_sc = False
    '''
    r4_cumplen = 0          # hace referencia ala RPTA
    r4_tiene_un_digito = False
    r4_tiene_dos_digitos = False
    r4_tiene_mayus = False

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":
            # r1
            r1_cont_caracteres += 1

            es_digito_impar_r1 = validar_digitos_impares(i)     # return True si es digito impar, False si no lo es

            if r1_cont_caracteres == 1 and es_digito_impar_r1:
                r1_empieza_digito_impar = True

            if r1_cont_caracteres == 3 and i.lower() == "s":
                r1_tiene_s_pos3 = True

            if i.lower() == "p":
                r1_tiene_p = True

            # r2
            if i.lower() == "t":
                r2_cont_t += 1

            r2_cont_caracteres += 1
            r2_ultima_letra = i

            # r3
            es_vocal_r3 = validar_vocales(i)    # True si es Vocal, False si no lo es
            if es_vocal_r3:
                r3_cont_vocales += 1

            es_consonante_r3 = validar_consonantes(i)       # True si es consonante, False si no lo es
            if es_consonante_r3:
                r3_cont_consonantes += 1

            es_minuscula_r3 = validar_minusculas(i)     # True si es minuscula, False si no lo es
            if not es_minuscula_r3:
                r3_todas_minusculas = False

            # r4
            es_digito_r4 = validar_digitos(i)       # True si es digito, False si no lo es
            if r4_tiene_un_digito and es_digito_r4:
                r4_tiene_dos_digitos = True
            elif es_digito_r4:
                r4_tiene_un_digito = True
            else:
                r4_tiene_un_digito = False

            es_mayuscula_r4 = validar_mayusculas(i)
            if es_mayuscula_r4 and not r4_tiene_dos_digitos:
                r4_tiene_mayus = True

        # Estoy fuera de una palabra. / Termino una palabra.
        else:
            # r1
            if r1_empieza_digito_impar and r1_tiene_s_pos3 and not r1_tiene_p:
                r1_cumplen += 1

            # r2
            es_vocal_r2 = validar_vocales(r2_ultima_letra)
            if r2_cont_t >= 2 and es_vocal_r2:
                if r2_menor is None or r2_cont_caracteres < r2_menor:
                    r2_menor = r2_cont_caracteres

            # r3
            r3_total_palabras += 1
            if r3_cont_vocales > r3_cont_consonantes and r3_todas_minusculas:
                r3_total_palabras_cumplen += 1

            # r4
            if r4_tiene_dos_digitos and r4_tiene_mayus:
                r4_cumplen += 1

            # Apagar Banderas, Reiniciar contadores , etc
            # r1
            r1_cont_caracteres = 0
            r1_empieza_digito_impar = False
            r1_tiene_s_pos3 = False
            r1_tiene_p = False

            # r2
            r2_cont_caracteres = 0
            r2_cont_t = 0
            r2_ultima_letra = ""

            # r3
            r3_cont_vocales = 0
            r3_cont_consonantes = 0
            r3_todas_minusculas = True

            # r4
            r4_tiene_un_digito = False
            r4_tiene_dos_digitos = False
            r4_tiene_mayus = False

    # Estoy fuera del ciclo for
    m.close()

    # r3
    r3_porc = calcular_porcentaje(r3_total_palabras, r3_total_palabras_cumplen)  # 0

    print(" 1 - Resultado:", r1_cumplen)
    print(" 2 - Resultado:", r2_menor)
    print(" 3 - Resultado:", r3_porc)
    print(" 4 - Resultado:", r4_cumplen)


if __name__ == '__main__':
    principal()