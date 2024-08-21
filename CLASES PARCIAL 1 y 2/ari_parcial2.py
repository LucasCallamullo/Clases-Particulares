

# r4
def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    return False


def validar_mayusculas(i):
    if "A" <= i <= "Z":
        return True
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
    # if "a" <= i <= "z" and not i in "aeiou":
    if i.lower() in "bcdfghjklmnpqrstvwxyz":
        return True
    else:
        return False


def validar_vocales(i): # o
    # A -> a , .lower() transforma al caracter si se puede en minuscula
    if i.lower() in "aeiou":  # si la i esta en "aeiou"
        return True
    else:
        return False       # retornar o devolver


# r1
def validar_digitos_impar(i):
    if i in "13579":
        return True
    else:
        return False


def principal():

    fd = "archivito.txt"        # file description , nombre del archivo
    m = open(fd, "rt")          # read text , leer texto
    linea = m.readline()        # te recupera un str


    ''' 
    1 - Determinar la cantidad de palabras que empiecen con digito impar y contenga al menos una
"s" (mayuscula o minuscula) en la posicion 3, pero no contenga ninguna "p" y que ademas su longitud 
sea par.
    '''
    r1_palabras_cumplen = 0         # hace referencia a la respuesta
    r1_cont_caracteres = 0
    r1_empieza_digito_impar = False
    r1_tiene_s_pos3 = False
    r1_tiene_p = False

    ''' calcular   
    2 - calcular la longitud en cantidad de caracteres de la menor palabra que contenga en su
ultima letra una vocal, y contenga al menos dos "t"(mayuscula o minuscula).
    '''
    r2_menor = None         # hace referencia  ala respuesta
    r2_cont_caracteres = 0
    r2_ultima_letra = ""
    r2_cont_t = 0

    ''' 3 - calcular el porcentaje entero de las palabras (sobre el total de palabras) que contengan mas
vocales que consonantes, pero tales que sus caracteres son letras en minúsculas.
     # Porcentaje
     Total de palabras --- 100%
     Palabras Cumplen ---- X = Palabras Cumplen * 100 // Total de palabras
'''
    r3_porc = 0
    r3_total_palabras = 0
    r3_total_cumplen = 0
    r3_cont_vocales = 0
    r3_cont_consonantes = 0
    r3_todas_minusculas = True

    # pa                            SD DS BC
    # tiene_p = False
    # tiene_pa = False
    #
    ''' 4 - determinar la cantidad de palabras que contengan dos mayúsculas seguidas pero ademas
contenga un digito antes de encontrar la sigla '''
    r4_cumplen = 0          # hace referencia a la respuesta
    r4_tiene_mayus = False
    r4_tiene_dos_mayus = False
    r4_tiene_digito = False

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # r1
            r1_cont_caracteres += 1     # 4

            es_digito_impar_r1 = validar_digitos_impar(i)     # return True es digito impar, False si no lo es
            if r1_cont_caracteres == 1 and es_digito_impar_r1:
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
            es_vocal_r3 = validar_vocales(i)        # return True si es vocal o False si no
            if es_vocal_r3:
                r3_cont_vocales += 1

            es_consonante_r3 = validar_consonantes(i)   # return True si es consontante
            if es_consonante_r3:
                r3_cont_consonantes += 1

            es_minuscula_r3 = validar_minusculas(i)     # return True es minuscula
            if not es_minuscula_r3:
                r3_todas_minusculas = False

            # r4
            es_mayuscula_r4 = validar_mayusculas(i)
            if r4_tiene_mayus and es_mayuscula_r4:
                r4_tiene_dos_mayus = True
            elif es_mayuscula_r4:
                r4_tiene_mayus = True
            else:
                r4_tiene_mayus = False

            es_digito_r4 = validar_digitos(i)
            if es_digito_r4 and not r4_tiene_dos_mayus:
                r4_tiene_digito = True

        # Termino una palabra / Fuera de una palabra.
        else:
            # r1
            if r1_empieza_digito_impar and r1_tiene_s_pos3 and not r1_tiene_p and r1_cont_caracteres % 2 == 0:
                r1_palabras_cumplen += 1

            # r2
            es_vocal_r2 = validar_vocales(r2_ultima_letra)
            if r2_cont_t >= 2 and es_vocal_r2:
                if r2_menor is None or r2_cont_caracteres < r2_menor:
                    r2_menor = r2_cont_caracteres

            # r3
            r3_total_palabras += 1
            if r3_cont_vocales > r3_cont_consonantes and r3_todas_minusculas:
                r3_total_cumplen += 1

            # r4
            if r4_tiene_dos_mayus and r4_tiene_digito:
                r4_cumplen += 1

            # Reiniciar contadores / Apagar Banderas , etc
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
            r4_tiene_mayus = False
            r4_tiene_dos_mayus = False
            r4_tiene_digito = False

    # Fuera del ciclo for
    m.close()

    r3_porc = calcular_porcentaje(r3_total_palabras, r3_total_cumplen)

    print(" 1 - Resultados:", r1_palabras_cumplen)
    print(" 2 - Resultados:", r2_menor)
    print(" 3 - Resultados:", r3_porc)
    print(" 4 - Resultados:", r4_cumplen)


if __name__ == '__main__':
    principal()
    # main()
