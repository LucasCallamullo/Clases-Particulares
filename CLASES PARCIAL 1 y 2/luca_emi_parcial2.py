
# r4
def validar_digitos(i):
    # if i in "0123456789"
    if "0" <= i <= "9":
        return True
    return False


# r3
def calcular_porcentaje(r3_cant_total_cumplen, r3_cant_total_palabras):
    porc = 0
    if r3_cant_total_palabras != 0:
        porc = r3_cant_total_cumplen * 100 // r3_cant_total_palabras
    return porc

def validar_minusculas(i):
    if "a" <= i <= "z":
        return True
    return False


def validar_consonantes(i):
    if i.lower() in "bcdfghjklmnpqrstvwxyz":
        return True
    else:
        return False


# r1
def validar_digitos_impares(i):
    if i in "13579":
        return True
    else:
        return False


def validar_vocales(i):   # o
    if i.lower() in "aeiou":  # si la i esta en "aeiou"
        return True
    else:
        return False                   # retornar devolver


def principal():

    fd = "archivito.txt"    # file description ; nombre del archivo
    m = open(fd, "rt")      # read text ; leer texto
    linea = m.readline()    # te devuelve str

    ''' 
    #              
    1 - determinar la cantidad de palabras que empiezen con digito impar y contenga al menos 
    una "s" (mayuscula o minuscula) en la posicion 3, pero no contenga ninguna "p".
    '''
    r1_cumplen = 0  # hace referencia a la respuesta del punto 1
    r1_cont_caracteres = 0
    r1_empíeza_digito_impar = False
    r1_tiene_s_pos3 = False
    r1_tiene_p = False

    '''          12 12345678
    2 - calcular la longitud en cantidad de caracteres de la menor palabra que contenga en 
su ultima letra una vocal, contenga al menos dos "t"(mayuscula o minuscula).
    '''
    r2_menor = None         #
    r2_cont_caracteres = 0
    r2_ultima_letra = ""
    r2_cont_t = 0

    ''' 3 - calcular el porcentaje entero de las palabras (sobre el total de palabras) que 
    contengan mas vocales que consonantes, pero tales que el resto de sus
    caracteres son letras en minúsculas. 
    # Porcentaje
    Total_Palabras --- 100%
    Palabras_Cumplen --- X = Palabras_Cumplen * 100 // Total_Palabras
    '''
    r3_porc = 0
    r3_cant_total_palabras = 0
    r3_cant_total_cumplen = 0
    r3_cont_vocales = 0
    r3_cont_consonantes = 0
    r3_todas_minusculas = True


    # ae ea io iu
    # r4_tiene_una_vocal = False
    # r4_tiene_dos_vocal = False
    ''' 4 - determinar la cantidad de palabras que contengan "mp" pero ademas 
    contenga un digito antes de encontrar la sigla. '''
    r4_cumplen = 0
    r4_tiene_m = False
    r4_tiene_mp = False
    r4_tiene_digito = False

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":
            # r1
            r1_cont_caracteres += 1

            es_digito_impar_r1 = validar_digitos_impares(i)     # return True si es digito impar, False si no lo es
            if r1_cont_caracteres == 1 and es_digito_impar_r1:
                r1_empíeza_digito_impar = True

            if i.lower() == "s" and r1_cont_caracteres == 3:
                r1_tiene_s_pos3 = True

            if i.lower() == "p":
                r1_tiene_p = True

            # r2
            r2_cont_caracteres += 1
            r2_ultima_letra = i

            if i.lower() == "t":
                r2_cont_t += 1

            # r3
            es_vocal_r3 = validar_vocales(i)    # return True si es vocal, False si no lo es
            if es_vocal_r3:
                r3_cont_vocales += 1

            es_consonante_r3 = validar_consonantes(i) # return True si es consonantes, False si no lo es
            if es_consonante_r3:
                r3_cont_consonantes += 1

            es_minuscula_r3 = validar_minusculas(i)  # return True si es minusculas, False si no lo es
            if not es_minuscula_r3:
                r3_todas_minusculas = False

            # r4
            if r4_tiene_m and i.lower() == "p":
                r4_tiene_mp = True
            elif i.lower() == "m":
                r4_tiene_m = True
            else:
                r4_tiene_m = False

            es_digito_r4 = validar_digitos(i)       # return True si es digito, False si no lo es
            if es_digito_r4 and not r4_tiene_mp:
                r4_tiene_digito = True

        # Estoy fuera de una palabra / Termino una palabra
        else:
            # r1
            if r1_empíeza_digito_impar and r1_tiene_s_pos3 and not r1_tiene_p:
                r1_cumplen += 1

            # r2
            es_vocal_r2 = validar_vocales(r2_ultima_letra)      # return True si es vocal, False si no lo es
            if r2_cont_t >= 2 and es_vocal_r2:
                if r2_menor is None or r2_cont_caracteres < r2_menor:
                    r2_menor = r2_cont_caracteres       # 5, 3

            # r3
            r3_cant_total_palabras += 1
            if r3_cont_vocales > r3_cont_consonantes and r3_todas_minusculas:
                r3_cant_total_cumplen += 1

            # r4
            if r4_tiene_digito and r4_tiene_mp:
                r4_cumplen += 1

            # Apagar Banderas, Reiniciar contadores, etc
            # r1
            r1_cont_caracteres = 0
            r1_empíeza_digito_impar = False
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
            r4_tiene_m = False
            r4_tiene_mp = False
            r4_tiene_digito = False

    # Termino el ciclo
    m.close()

    r3_porc = calcular_porcentaje(r3_cant_total_cumplen, r3_cant_total_palabras)

    # print("Primer resultado:", r1)
    # print("Segundo resultado:", r2)
    # print("Tercer resultado:", r3)
    # print("Cuarto resultado:", r4)

    print(" 1 - Resultados:", r1_cumplen)
    print(" 2 - Resultados:", r2_menor)
    print(" 3 - Resultados:", r3_porc)
    print(" 4 - Resultados:", r4_cumplen)


if __name__ == '__main__':
    principal()

