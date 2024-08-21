

# r3
def calcular_porcentaje(r3_cont_total_palabras, r3_cont_palabras_cumplen):
    porc = 0
    if r3_cont_total_palabras > 0:
        porc = r3_cont_palabras_cumplen * 100 // r3_cont_total_palabras
    return porc


def validar_consonantes(i):
    if i in "bcdfghjklmnpqrstvwxyz":
        return True
    else:
        return False


def validar_vocales(car):   # O -> o
    # .lower() transforma al caracter en minuscula  / .upper() transforma al caracter en mayuscula
    if car.lower() in "aeiou":  # si la letra esta in "aeiou" (vocales)
        return True         # return True
    else:
        return False


def principal():

    archivo = "entrada.txt"
    m = open(archivo, "rt")     # read text ; leer texto
    linea = m.readline()
    m.close()

    #                             8
    #                     123456780
    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que
contienen al menos una ‘c’. '''
    r2_mayor = None
    r2_cont_caracteres = 0
    r2_tiene_c = False

    ''' 3 - Determinar el porcentaje (sobre el total de palabras) de la cantidad de palabras que 
    tienen más consonantes que vocales, pero no contienen ninguna ‘m’ ni tampoco ninguna ‘a’ 
    # Porcentaje
    total_palabras --- 100%
    palabras_cumplen --- porc = palabras_cumplen * 100 / total_palabras
    '''
    r3_porc = 0
    r3_cont_total_palabras = 0
    r3_cont_palabras_cumplen = 0
    r3_cont_consonantes = 0
    r3_cont_vocales = 0
    r3_tiene_m_a = False

    ''' 4 - Determinar cuántas palabras incluyen una sola vez la expresión “se” (con cualquiera de sus letras
en minúscula o mayúscula) pero de tal forma que la palabra no tenga ninguna otra ‘s’ ni ninguna
otra ‘e’ que las requeridas en la única expresión ‘se’ permitida. '''
    r4_cont_palabras_cumplen = 0
    r4_tiene_s = False
    r4_tiene_se = False
    r4_cont_s = 0
    r4_cont_e = 0

    # linea = casa aca casas.
    for i in linea:

        # Estoy en una palabra
        if i != " " and i != ".":

            # r2
            r2_cont_caracteres += 1
            if i.lower() == "c":
                r2_tiene_c = True

            # r3
            es_vocal_r3 = validar_vocales(i)        # return True es Vocal , False No es vocal
            if es_vocal_r3:
                r3_cont_vocales += 1

            es_consonante_r3 = validar_consonantes(i)       # return True es consonante, False no es consonanten
            if es_consonante_r3:
                r3_cont_consonantes += 1

            if i.lower() == "m" or i.lower() == "a":
                r3_tiene_m_a = True

            # r4
            if r4_tiene_s and i.lower() == "e":
                r4_tiene_se = True
            elif i.lower() == "s":
                r4_tiene_s = True
            else:
                r4_tiene_s = False

            if i.lower() == "s":
                r4_cont_s += 1
            if i.lower() == "e":
                r4_cont_e += 1

        # Estoy fuera de una palabra / Termino una palabra
        else:
            # r2
            if r2_tiene_c:
                # 4, 3, 5
                if r2_mayor is None or r2_cont_caracteres > r2_mayor:
                    r2_mayor = r2_cont_caracteres       # r2_mayor = 4

            # r3
            r3_cont_total_palabras += 1
            if r3_cont_consonantes > r3_cont_vocales and not r3_tiene_m_a:
                r3_cont_palabras_cumplen += 1

            # r4
            if r4_tiene_se and r4_cont_s == 1 and r4_cont_e == 1:
                r4_cont_palabras_cumplen += 1


            # APAGAR BANDERAS , REINICIAR CONTADORES ETC
            # r2
            r2_cont_caracteres = 0
            r2_tiene_c = False

            # r3
            r3_cont_consonantes = 0
            r3_cont_vocales = 0
            r3_tiene_m_a = False

            # r4
            r4_tiene_s = False
            r4_tiene_se = False
            r4_cont_s = 0
            r4_cont_e = 0

    # Fuera del ciclo for
    r3_porc = calcular_porcentaje(r3_cont_total_palabras, r3_cont_palabras_cumplen)

    print(" 2 - Resultado:", r2_mayor)
    print(" 3 - Resultado:", r3_porc)
    print(" 4 - Resultado:", r4_cont_palabras_cumplen)



if __name__ == "__main__":
    principal()