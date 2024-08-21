

# r1
def validar_minusculas(i):
    if "a" <= i <= "z":
        return True
    else:
        return False


def validar_digitos_impares(i):
    if i in "13579":
        return True
    else:
        return False


# r3
def calcular_promedio(r3_acum_total_caract, r3_cont_total_palabras):
    prom = 0
    if r3_cont_total_palabras > 0:
        prom = r3_acum_total_caract // r3_cont_total_palabras
    return prom


def validar_consonantes(i):
    # if "a" <= i.lower() <= "z" and not i.lower() in "aeiou":
    if i.lower() in "bcdfghjklmnpqrstvwxyz":
        return True
    else:
        return False


def validar_vocales(letra):         # A -> a
    # .lower() transforma caracteres a minuscula / .upper() transforma a mayusculas
    if letra.lower() in "aeiou":  # si i esta en "aeiou"
        return True
    else:
        return False


def principal():

    archivo = "entrada.txt"
    m = open(archivo, "rt")     # read text , leer texto
    linea = m.readline()        # str

    ''' 1 - Determinar la cantidad de palabras comienzan con un dígito impar, 
pero tales que el resto de sus caracteres son letras en minúsculas. '''
    # 12
    # 3asdasd
    r1_cumplen = 0
    r1_cont_caracter = 0
    r1_empieza_digito_impar = False
    r1_todas_minusculas = True

    #       123456              123456780123
    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre 
aquellas que comienzan con una vocal y contenga al menos una letra "b" (mayúscula o minúscula)
    mayor = None
    '''
    r2_mayor = None
    r2_cont_caracteres = 0
    r2_empieza_vocal = False
    r2_tiene_b = False

    #       1122343546
    ''' 3 - Determinar el promedio entero de caracteres por palabra entre las palabras que tienen más
consonantes que vocales, pero no contienen ninguna "m" ni tampoco ninguna "a" 
    # Promedio = Una suma de notas (acumulador) / cantidad de notas que sumamos ( contador )
    promedio = (3+ 6 +9) / 3
'''
    r3_prom = 0
    r3_acum_total_caract = 0
    r3_cont_total_palabras = 0
    r3_cont_caracteres = 0
    r3_cont_consonantes = 0
    r3_cont_vocales = 0
    r3_tiene_m_a = False

    # da de di do du        HC SC       incluyen
    ''' 4 - Determinar cuántas palabras incluyen dos o más veces la expresión que conforman la 
letra "d" mas una vocal (con cualquiera de sus letras en minúscula o mayúscula) pero de tal 
forma que la palabra termine además con una vocal. '''
    r4_cumplen = 0
    r4_tiene_d = False
    r4_tiene_d_vocal = False
    r4_cont_d_vocal = 0
    r4_ultima_letra = " "

    # linea = Hola Mundo.
    for i in linea:

        # Estoy Dentro de una palabra
        if i != " " and i != ".":

            # r1
            r1_cont_caracter += 1
            es_digito_impar_r1 = validar_digitos_impares(i)
            if r1_cont_caracter == 1 and es_digito_impar_r1:
                r1_empieza_digito_impar = True

            es_minuscula_r1 = validar_minusculas(i)
            if not es_minuscula_r1 and r1_cont_caracter > 1:
                r1_todas_minusculas = False

            # r2
            r2_cont_caracteres += 1

            es_vocal_r2 = validar_vocales(i)        # True si es vocal, False si no lo es

            if r2_cont_caracteres == 1 and es_vocal_r2:
                r2_empieza_vocal = True

            if i.lower() == "b":
                r2_tiene_b = True

            # r3
            r3_cont_caracteres += 1

            es_vocal_r3 = validar_vocales(i)    # True si era vocal, Falso si no lo era
            if es_vocal_r3:
                r3_cont_vocales += 1

            es_consonante_r3 = validar_consonantes(i)   # True si era consonante y en False si no lo es
            if es_consonante_r3:
                r3_cont_consonantes += 1

            if i.lower() == "m" or i.lower() == "a":
                r3_tiene_m_a = True

            # r4
            es_vocal_r4 = validar_vocales(i)

            if r4_tiene_d and es_vocal_r4:
                r4_tiene_d_vocal = True
            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

            if r4_tiene_d_vocal:
                r4_cont_d_vocal += 1
                r4_tiene_d_vocal = False

            r4_ultima_letra = i

        # Estoy fuera de una palabra o que termino una palabra
        else:

            # r1
            if r1_empieza_digito_impar and r1_todas_minusculas:
                r1_cumplen += 1

            # r2
            if r2_empieza_vocal and r2_tiene_b:
                if r2_mayor is None or r2_cont_caracteres > r2_mayor:
                    r2_mayor = r2_cont_caracteres

            # r3
            if r3_cont_consonantes > r3_cont_vocales and not r3_tiene_m_a:
                r3_acum_total_caract += r3_cont_caracteres
                r3_cont_total_palabras += 1

            # r4
            es_vocal_r4_ult = validar_vocales(r4_ultima_letra)
            if r4_cont_d_vocal >= 2 and es_vocal_r4_ult:
                r4_cumplen += 1

            # Apagar Banderas , Reiniciar contadores
            # r1
            r1_cont_caracter = 0
            r1_empieza_digito_impar = False
            r1_todas_minusculas = True

            # r2
            r2_cont_caracteres = 0
            r2_empieza_vocal = False
            r2_tiene_b = False

            # r3
            r3_cont_caracteres = 0
            r3_cont_consonantes = 0
            r3_cont_vocales = 0
            r3_tiene_m_a = False

            # r4
            r4_tiene_d = False
            r4_tiene_d_vocal = False
            r4_cont_d_vocal = 0
            r4_ultima_letra = " "


    # Estoy fuera del ciclo for
    m.close()

    r3_prom = calcular_promedio(r3_acum_total_caract, r3_cont_total_palabras)

    print(" 1 - Resultados:", r1_cumplen)
    print(" 2 - Resultados:", r2_mayor)
    print(" 3 - Resultados:", r3_prom)
    print(" 4 - Resultados:", r4_cumplen)


if __name__ == '__main__':
    principal()