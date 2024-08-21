

def calcular_promedio(acum, cont):
    prom = 0
    if cont > 0:
        prom = acum // cont
    return prom


def validar_digito(i):
    if "0" <= i <= "9":
        return True
    return False
    # return "0" <= i <= "9"


def validar_consonantes(i):
    consonantes = "bcdfghjklmnpqrstvwxyz"
    if i in consonantes:
        return True
    return False


def validar_vocales(i):     # A
    # .lower() transforma si puede en una minuscula / .upper() transforma si puede en una mayuscula
    if i.lower() in "aeiou":            # si la i esta en aeiou
        return True
    return False
    # return i in "aeiou"


def principal():

    fd = "entrada.txt"
    # m = open(fd, "rt", encoding="utf-8")      # read text , leer texto
    m = open(fd, "rt")      # read text , leer texto
    linea = m.readline()


    ''' 1 - Determinar la cantidad de palabras cuya longitud sea par, y que estén conformadas por vocales y
consonantes en partes iguales (minúsculas o mayúsculas) '''
    #                         8
    #                 123456780120120123
    r1 = 0          # contador de la cantidad de palabras que cumplen
    r1_cont_letras = 0      # determinar la longitud
    r1_cont_vocales = 0
    r1_cont_consonantes = 0

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que
tienen al menos un dígito en la tercera posicion de la palabra y no tienen una "p" (mayúscula o minúscula). '''
    r2 = None           # referencia a la palabra con mayor longitud, calcular el mayor
    r2_cont_caracteres = 0
    r2_tiene_digito_pos3 = False
    r2_tiene_p = False

    ''' 3 - Determinar el promedio entero de caracteres por palabra entre las palabras que tienen más de
dos caracteres pero incluyen una o más veces una "s". 
    # Promedio = suma de cosas / la cantidad de cosas que sumamos
    '''
    r3 = 0      # hace referencia al promedio
    r3_acum_caracteres_cumplen = 0
    r3_cont_palabras_cumplen = 0
    r3_cont_caracteres = 0
    r3_tiene_s = False

    ''' 4 - Determinar cuántas palabras incluyen la expresión "ra" (con cualquiera de sus letras en minúscula
o mayúscula) pero de tal forma que la palabra además tenga una vocal (mayúscula o minúscula)
entre sus dos primeros caracteres. y que ademas tiene que aparecer una p antes de la sigla ra '''
    # "TA"
    r4 = 0          # contador de la cantidad de palabras que cumplen
    r4_cont_caracteres = 0
    r4_tiene_r = False
    r4_tiene_ra = False
    r4_tiene_vocal_pos1_pos2 = False
    r4_tiene_p = False

    ''' 5 - Determinar cuántas palabras empiezan y terminan con el mismo caracter '''
    r5 = 0
    r5_cont_letras = 0
    r5_primera_letra = None
    r5_ultima_letra = None


    # Hace falta coraje para saltar de ese punto.
    for i in linea:
        # i = H, a
        # estabas dentro de una palabra
        if i != " " and i != ".":

            # Punto 1
            r1_cont_letras += 1             # 1
            es_vocal_r1 = validar_vocales(i)        #
            es_consonante_r1 = validar_consonantes(i)
            if es_vocal_r1:
                r1_cont_vocales += 1
            if es_consonante_r1:
                r1_cont_consonantes += 1

            # Punto 2
            r2_cont_caracteres += 1
            es_digito_r3 = validar_digito(i)

            if es_digito_r3 and r2_cont_caracteres == 3:
                r2_tiene_digito_pos3 = True

            if i.lower() == "p":
                r2_tiene_p = True

            # Punto 3
            r3_cont_caracteres += 1
            if i.lower() == "s":
                r3_tiene_s = True

            # Punto 4
            r4_cont_caracteres += 1
            es_vocal_r4 = validar_vocales(i)
            if es_vocal_r4 and r4_cont_caracteres <= 2:
                r4_tiene_vocal_pos1_pos2 = True

            if r4_tiene_r and i.lower() == "a":
                r4_tiene_ra = True
            elif i.lower() == "r":
                r4_tiene_r = True
            else:
                r4_tiene_r = False

            if i.lower() == "p" and not r4_tiene_ra:
                r4_tiene_p = True

            # Punto 5
            r5_cont_letras += 1
            r5_ultima_letra = i.lower()
            if r5_cont_letras == 1:
                r5_primera_letra = i.lower()


        # estoy fuera de una palabra o que termino una palabra
        else:
            # Punto 1
            if r1_cont_letras % 2 == 0 and r1_cont_vocales == r1_cont_consonantes:
                r1 += 1

            # Punto 2
            if r2_tiene_digito_pos3 and not r2_tiene_p:
                if r2 is None or r2_cont_caracteres > r2:
                    r2 = r2_cont_caracteres

            # Punto 3
            if r3_tiene_s and r3_cont_caracteres > 2:
                r3_cont_palabras_cumplen += 1
                r3_acum_caracteres_cumplen += r3_cont_caracteres

            # Punto 4
            if r4_tiene_ra and r4_tiene_vocal_pos1_pos2 and r4_tiene_p:
                r4 += 1

            # Punto 5
            if r5_ultima_letra == r5_primera_letra:
                r5 += 1


            # Apagar banderas, reinciar contadores etc
            # Punto 1
            r1_cont_letras = 0
            r1_cont_vocales = 0
            r1_cont_consonantes = 0

            # Punto 2
            r2_cont_caracteres = 0
            r2_tiene_digito_pos3 = False
            r2_tiene_p = False

            # Punto 3
            r3_cont_caracteres = 0
            r3_tiene_s = False

            # Punto 4
            r4_cont_caracteres = 0
            r4_tiene_r = False
            r4_tiene_ra = False
            r4_tiene_vocal_pos1_pos2 = False
            # Sabes que ese oso es pardo y malo.
            # Punto 5
            r5_cont_letras = 0
            r5_primera_letra = None
            r5_ultima_letra = None

    # Fuera del ciclo for
    m.close()

    r3 = calcular_promedio(r3_acum_caracteres_cumplen, r3_cont_palabras_cumplen)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)
    print("Quinto resultado:", r5)


if __name__ == '__main__':
    principal()

    # forma abrir mas lineas
    # for linea in m:
    #    for i in linea:
