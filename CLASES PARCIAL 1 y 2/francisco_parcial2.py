

# r3
def calcular_promedio(r3_cont_total, r3_acum_total):
    prom = 0
    if r3_cont_total > 0:
        prom = r3_acum_total // r3_cont_total
    return prom


# r2
def validar_digitos_impares(i):
    if i in "13579":
        return True
    else:
        return False


# r1
def validar_consonantes(i):
    # B -> b, .lower() transforma al caracter en minuscula,
    if i.lower() in "bcdfghjklmnpqrstvwxyz":  # si i esta en "aeiou"
        return True
    else:
        return False


def validar_vocales(i):
    # A -> a, .lower() transforma al caracter en minuscula,
    if i.lower() in "aeiou":  # si i esta en "aeiou"
        return True
    else:
        return False


def principal():

    fd = "entrada.txt"      # file description ; nombre del archivo
    m = open(fd, "rt")      # read text ; leer texto
    linea = m.readline()        # te recupera un str

    #                     1234567801  11223435
    ''' 1 - Determinar la cantidad de palabras cuya longitud sea par, y que estén conformadas por 
    vocales y consonantes en partes iguales (minúsculas o mayúsculas) '''
    r1_cumplen = 0      # Hace referencia a las palabras que cumplan las condiciones
    r1_cont_caracteres = 0
    r1_cont_consosnantes = 0
    r1_cont_vocales = 0

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que
tienen al menos un dígito impar y no tienen una "p" '''
    r2_mayor = None
    r2_cont_caracteres = 0
    r2_tiene_digito_impar = False
    r2_tiene_p = False

    #       Ast astds.
    ''' 3 - Determinar el promedio entero de caracteres por palabra entre las palabras que empiezan con 
vocal y tienen una "t" en la tercera posicion de la palabra, pero incluyen una o más veces una "s" '''
    # Promedio = Una sumatoria de cosas ( acumulador ) / cantidad de cosas que sumamos ( contador )
    # Promedio = ( 5 + 8 + 9 ) / 3
    r3_prom = 0
    r3_acum_total = 0
    r3_cont_total = 0
    r3_cont_caracteres = 0
    r3_empieza_vocal = False
    r3_tiene_t_pos3 = False
    r3_tiene_s = False

    # ra               para pare rapido paz.
    ''' 4 - Determinar cuántas palabras incluyen la expresión "ra" (con cualquiera de sus letras en 
minúscula o mayúscula) pero de tal forma que la palabra termine en una vocal '''
    r4_cumplen = 0
    r4_tiene_r = False
    r4_tiene_ra = False
    r4_ult_letra_vocal = None
    es_palabra = False

    # 1234 123
    # Hola Mundo
    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":
            es_palabra = True

            # r1
            r1_cont_caracteres += 1

            es_vocal_r1 = validar_vocales(i)   # return True si es vocal, return False si no lo es
            if es_vocal_r1:
                r1_cont_vocales += 1

            es_consonante_r1 = validar_consonantes(i)   # return True si es cons o false si no lo es
            if es_consonante_r1:
                r1_cont_consosnantes += 1

            # r2
            r2_cont_caracteres += 1

            es_digito_r2 = validar_digitos_impares(i)   # return True si es digito, y flase si no loes
            if es_digito_r2:
                r2_tiene_digito_impar = True

            if i.lower() == "p":
                r2_tiene_p = True

            # r3
            r3_cont_caracteres += 1

            es_vocal_r3 = validar_vocales(i)
            if r3_cont_caracteres == 1 and es_vocal_r3:
                r3_empieza_vocal = True

            if r3_cont_caracteres == 3 and i.lower() == "t":
                r3_tiene_t_pos3 = True

            if i.lower() == "s":
                r3_tiene_s = True

            # r4
            if r4_tiene_r and i.lower() == "a":
                r4_tiene_ra = True
            elif i.lower() == "r":
                r4_tiene_r = True
            else:
                r4_tiene_r = False

            r4_ult_letra_vocal = i.lower()

        # Estoy fuera de la palabra / Termino una palabra
        else:
            if es_palabra:
                # r1
                if r1_cont_caracteres % 2 == 0 and r1_cont_consosnantes == r1_cont_vocales:
                    r1_cumplen += 1

                # r2
                if r2_tiene_digito_impar and not r2_tiene_p:
                    if r2_mayor is None or r2_cont_caracteres > r2_mayor:
                        r2_mayor = r2_cont_caracteres

                # r3
                if r3_empieza_vocal and r3_tiene_t_pos3 and r3_tiene_s:
                    r3_acum_total += r3_cont_caracteres
                    r3_cont_total += 1

                # r4
                es_vocal_r4 = validar_vocales(r4_ult_letra_vocal)
                if r4_tiene_ra and es_vocal_r4:
                    r4_cumplen += 1


            # APAGAR LAS BANDERAS , REINICIAR CONTADORES ETC ETC
            # r1
            r1_cont_caracteres = 0
            r1_cont_consosnantes = 0
            r1_cont_vocales = 0

            # r2
            r2_cont_caracteres = 0
            r2_tiene_digito_impar = False
            r2_tiene_p = False

            # r3
            r3_cont_caracteres = 0
            r3_empieza_vocal = False
            r3_tiene_t_pos3 = False
            r3_tiene_s = False

            # r4
            r4_tiene_r = False
            r4_tiene_ra = False
            r4_ult_letra_vocal = None

            es_palabra = False

    # Estoy Fuera de ciclo for
    m.close()

    r3_prom = calcular_promedio(r3_cont_total, r3_acum_total)

    print("1 - Resultados:", r1_cumplen)
    print("2 - Resultados:", r2_mayor)
    print("3 - Resultados:", r3_prom)
    print("4 - Resultados:", r4_cumplen)


if __name__ == "__main__":
    principal()
    # main()

