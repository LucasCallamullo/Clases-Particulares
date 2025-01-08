def validar_mayusculas(i):
    if "A" >= i <= "Z":
        return True
    return False


def validar_consonantes(i):
    consonantes = "qwrtypsdfghjklzxcvbnm"
    if i.lower() in consonantes:
        return True
    return False


def validar_impares(i):
    impares = "13579"
    if i in impares:
        return True
    return False


def validar_vocales(i):
    vocales = "aeiou"
    if i.lower() in vocales:
        return True
    return False


def principal():
    fd = "texto.txt"
    m = open(fd, "rt")
    linea = m.readline()

    '''1-determinar la cantidad de palabras que empiezen con digito impar y contenga al menos una "s"
     (mayuscula o minuscula) en la posicion 3, pero no contenga ninguna "p"'''
    r1 = 0  # Cantidad de palabras que cumplen
    r1_contador_caracteres = 0
    r1_comienza_impar = False
    r1_tiene_s = False
    r1_contiene_s_pos_3 = False
    r1_cont_p = 0

    '''2 - calcular la longitud en cantidad de caracteres de la menor palabra que contenga en su 
     ultima letra una vocal, y contenga al menos dos "t"'''
    r2 = None  # Respuesta
    r2_cont_caracteres = 0
    r2_cont_t = 0
    r2_tiene_vocal_ult_letra = False
    r2_ultima_letra = ""

    '''3 - calcular el porcentaje entero de las palabras (sobre el total de palabras) que contengan mas 
    vocales que consonantes, pero tales que el resto de sus caracteres son letras en minúsculas'''
    r3 = 0  # porcentaje entero...  #Total_palabras ----- 100 %
    # palabras_cumplen ---- porc = palabras_cumplen * 100 // Total_palabras
    r3_cont_total_palabras = 0
    r3_cont_vocales = 0
    r3_cont_consonantes = 0
    r3_todas_minusculas = True
    r3_palabras_cumplen = 0

    '''4 - determinar la cantidad de palabras que contengan dos mayúsculas seguidas pero ademas 
    contenga un digito antes de encontrar la sigla'''
    r4 = 0  # Cantidad de palabras que cumplen
    r4_tiene_1mayuscula = False
    r4_tiene_2mayuscula = False
    r4_tiene_digito_antes = False
    r4_dos_mayusculas_seguidas = False

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # r1
            r1_contador_caracteres += 1
            tiene_digito_impar = validar_impares(i)
            if r1_contador_caracteres == 1 and tiene_digito_impar:
                r1_comienza_impar = True
            if i.lower() == "s":
                r1_tiene_s = True
            if r1_contador_caracteres == 3 and r1_tiene_s:
                r1_contiene_s_pos_3 = True
            if i.lower() == "p":
                r1_cont_p += 1

            # r2
            es_vocal = validar_vocales(i)
            r2_ultima_letra = i.lower()
            if es_vocal and r2_ultima_letra:
                r2_tiene_vocal_ult_letra = True
            if i.lower() == "t":
                r2_cont_t += 1

            # r3
            es_consonante = validar_consonantes(i)
            tiene_mayusculas = validar_mayusculas(i)
            if es_vocal:
                r3_cont_vocales += 1
            if es_consonante:
                r3_cont_consonantes += 1
            if tiene_mayusculas:
                r3_todas_minusculas = False

            # r4
            if r4_tiene_1mayuscula and r4_tiene_2mayuscula:
                r4_dos_mayusculas_seguidas = True
            elif tiene_mayusculas:
                r4_tiene_1mayuscula = True



        # Estoy fuera de una palabra
        else:
            # r1
            if r1_comienza_impar and r1_contiene_s_pos_3 and r1_cont_p == 0:
                r1 += 1
            # r2
            if r2_tiene_vocal_ult_letra and r2_cont_t >= 2:
                r2_cont_caracteres += 1
                if r2 is None or r2_cont_caracteres < r2:
                    r2 = r2_cont_caracteres
            # r3
            r3_cont_total_palabras += 1
            if r3_cont_vocales > r3_cont_consonantes and r3_todas_minusculas:
                r3_palabras_cumplen += 1

            # APAGAR BANDERAS,REINICIAR CONTADORES,ETC.
            # r1
            r1_contador_caracteres = 0
            r1_comienza_impar = False
            r1_contiene_s_pos_3 = False
            r1_cont_p = 0
            # r2
            r2_cont_caracteres = 0
            r2_cont_t = 0
            r2_tiene_vocal_ult_letra = False
            # r3
            r3_cont_vocales = 0
            r3_cont_consonantes = 0
            r3_todas_minusculas = True
            r3_palabras_cumplen = 0

    # Fuera del ciclo for
    m.close()

    # r3-Porcentaje
    r3 = 0
    if r3_cont_total_palabras != 0:
        r3 = (r3_palabras_cumplen * 100) // r3_cont_total_palabras

    print("1 - Respuesta:", r1)
    print("2 - Respuesta:", r2)
    print("3 - Respuesta:", r3)
    # print("4 - Respuesta:", r4)


if __name__ == '__main__':
    principal()
