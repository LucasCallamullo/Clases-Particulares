


def calcular_promedio(r3_acum_total, r3_cant_total):
    prom = 0
    if r3_cant_total > 0:
        prom = r3_acum_total // r3_cant_total
    return prom


def validar_consonantes(consonante):
    if consonante in "bcdfghjklmnñpqrstvwxyz":
        return True
    else:
        return False


# r2
def validar_vocales(car):           # si es vocal A
    if car.lower() in "aeiou":
        return True
    else:
        return False


# r1
def validar_minusculas(i):
    if "a" <= i <= "z":
        return True
    else:
        return False


def validar_digito_impar(i):
    if i in "13579":
        return True
    else:
        return False




def principal():

    fd = "entrada.txt"
    m = open(fd, "rt")      # , encoding="utf-8")
    linea = m.readline()        # sin la s
    #                   2
    #      123456789  120
    ''' 1- Determinar la cantidad de palabras comienzan con un dígito impar, pero tales que el resto de sus
caracteres son letras en minúsculas '''
    # 1asdaSd
    r1 = 0          # contador de palabras que cumplen las condiciones
    r1_cont_caracteres = 0
    r1_empieza_digito = False
    r1_todas_minusculas = True

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que
comienzan con una vocal y contenga al menos una letra "b" (mayúscula o minúscula). '''
    r2 = None           # hace referencia al mayor
    r2_cont_caracteres = 0
    r2_empieza_vocal = False
    r2_tiene_b = False

    ''' 3 - Determinar el promedio entero de caracteres por palabra entre las palabras que tienen más
consonantes que vocales, pero no contienen ninguna "m" ni tampoco ninguna "a". '''
    # promedio
    # acum = cont_caracters palabra que cumplen
    # cant = cantidad de palabras que cumplieron
    r3 = 0                          # hace referencia al promedio
    r3_acum_total = 0
    r3_cant_total = 0
    r3_cont_caracteres = 0
    r3_cont_cons = 0
    r3_cont_vocal = 0
    r3_tiene_m_a = False

    # da de di do du            # sd hc  SS DD DS
    ''' 4 - Determinar cuántas palabras incluyen dos o más veces la expresión que conforman la letra "d"
mas una vocal (con cualquiera de sus letras en minúscula o mayúscula) pero de tal forma que la
palabra termine además con una vocal. '''
    r4 = 0          # contador de palabras que cumplen las condiciones
    r4_tiene_d = False
    r4_tiene_d_vocal = False
    r4_cont_d_vocal = 0
    r4_ult_letra = None

    es_palabra = False

    for i in linea:

        # Estamos dentro de una palabra
        if i != " " and i != ".":
            es_palabra = True

            # r1
            r1_cont_caracteres += 1
            es_digito_impar_r1 = validar_digito_impar(i)            # es_digito

            if es_digito_impar_r1 and r1_cont_caracteres == 1:
                r1_empieza_digito = True

            es_minuscula_r1 = validar_minusculas(i)
            if not es_minuscula_r1 and r1_cont_caracteres >= 2:
                r1_todas_minusculas = False

            # r2
            r2_cont_caracteres += 1

            es_vocal_r2 = validar_vocales(i)        # return TRue o False
            if r2_cont_caracteres == 1 and es_vocal_r2:
                r2_empieza_vocal = True

            if i.lower() == "b":
                r2_tiene_b = True

            # r3
            r3_cont_caracteres += 1

            es_consonante_r3 = validar_consonantes(i)
            if es_consonante_r3:
                r3_cont_cons += 1

            es_vocal_r3 = validar_vocales(i)
            if es_vocal_r3:
                r3_cont_vocal += 1

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

            r4_ult_letra = i.lower()

        # Estoy fuera de una palabra / Termino una palabra
        else:

            # r1
            if r1_empieza_digito and r1_todas_minusculas:
                r1 += 1

            # r2
            if r2_empieza_vocal and r2_tiene_b:
                if r2 is None or r2_cont_caracteres > r2:
                    r2 = r2_cont_caracteres

            # r3
            if not r3_tiene_m_a and r3_cont_cons > r3_cont_vocal:
                r3_acum_total += r3_cont_caracteres
                r3_cant_total += 1

            # r4
            if es_palabra:
                es_vocal_r4 = validar_vocales(r4_ult_letra)
                if r4_cont_d_vocal >= 2 and es_vocal_r4:
                    r4 += 1

            # APAGAR BANDERAS , REINICIAR CONTADORES
            # r1
            r1_cont_caracteres = 0
            r1_empieza_digito = False
            r1_todas_minusculas = True

            # r2
            r2_cont_caracteres = 0
            r2_empieza_vocal = False
            r2_tiene_b = False

            # r3
            r3_cont_caracteres = 0
            r3_cont_cons = 0
            r3_cont_vocal = 0
            r3_tiene_m_a = False

            # r4
            r4_tiene_d = False
            r4_tiene_d_vocal = False
            r4_cont_d_vocal = 0
            r4_ult_letra = None

            es_palabra = False


    # Estoy fuera del ciclo
    m.close()

    # r3
    r3 = calcular_promedio(r3_acum_total, r3_cant_total)



    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()
