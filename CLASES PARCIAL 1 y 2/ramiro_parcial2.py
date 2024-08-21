

# r6
def calcular_promedio(r6_total_acum, r6_total_cant):
    prom = 0
    if r6_total_cant != 0:
        prom = r6_total_acum // r6_total_cant
    return prom


def validar_vocales(letra):
    return letra.lower() in "aeiou"


# r1
def validar_mayusculas(i):
    if "A" <= i <= "Z":
        return True
    return False


def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    return False


# r3
def validar_vocales_sin_u(i):
    # .lower() transformar los caracteres en minusculas
    if i.lower() in "aeio":
        return True
    return False



# r5
def validar_digitos_impares(i): # 3
    # return i in "13579"
    if i in "13579":            # si la i esta en "13579"
        return True
    else:
        return False


def principal():

    m = open("entrada.txt", "rt")   # read Text , leer texto
    linea = m.readline()            # recupera un str o un string

    ''' 1 - Determinar la cantidad de palabras que tienen un dígito en la segunda y 
en la cuarta posición, pero de tal forma que el resto de sus caracteres son letras 
mayúsculas. '''
    r1 = 0
    r1_cont_caracteres = 0
    r1_todas_mayusculas = True
    r1_cumple_digitos = True

    # r1_tiene_digito_pos2 = False
    # r1_tiene_digito_pos4 = False

    # r1_cont_digitos = 0

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más corta 
entre aquellas que comienzan con una "t" (minúscula o mayúscula) '''
    r2 = None
    r2_cont_caracteres = 0
    r2_empieza_t = False

    ''' 3 - Determinar cuántas palabras están conformadas solo por vocales (minúsculas 
o mayúsculas), pero no contienen ninguna "u" (minúscula o mayúscula). '''
    r3 = 0
    r3_todas_vocales_sin_u = True

    ''' 4 - Determinar cuántas palabras incluyen la expresión "di" (con cualquiera de 
sus letras en minúscula o mayúscula) pero de tal forma que a su vez no comiencen con
la expresión "di". 

    DS AS FG
'''
    r4 = 0
    r4_cont_caracteres = 0
    r4_tiene_d = False
    r4_tiene_di = False
    r4_tiene_di_primera_letra = False

    ''' 5 - determinar la cantidad de palabras que empiezen con digito impar y contenga al 
menos una "s" (mayuscula o minuscula) en la posicion 3, pero no contenga ninguna "p".'''
    r5 = 0      # hace referencia a la respuesta
    r5_cont_caracteres = 0
    r5_empieza_digito_impar = False
    r5_tiene_s_pos3 = False
    r5_tiene_p = False

    ''' 6 - determinar el promedio de caracteres de las palabras que terminan con vocal.
    y contenga al menos dos "t"
        # Promedoi = suma de cosas ( acumulador de caracteres ) / cantidad de cosas que acumule
    '''
    r6 = 0
    r6_total_acum = 0
    r6_total_cant = 0
    r6_cont_caracteres = 0
    r6_ultima_letra = ""
    r6_cont_t = 0

    for i in linea:

        # =====================================================
        #   Estoy dentro de una palabra
        # =====================================================
        if i != " " and i != ".":

            # r1
            r1_cont_caracteres += 1

            if r1_cont_caracteres == 2 or r1_cont_caracteres == 4:
                es_digito = validar_digitos(i) # return True si es digito, False si no l oes
                if not es_digito:
                    r1_cumple_digitos = False

            else:
                es_mayuscula = validar_mayusculas(i)
                if not es_mayuscula:
                    r1_todas_mayusculas = False

            # r2
            r2_cont_caracteres += 1
            if r2_cont_caracteres == 1 and i.lower() == "t":
                r2_empieza_t = True

            # r3
            es_vocal_sin_u = validar_vocales_sin_u(i)   # return True si "aeio", False si no loes
            if not es_vocal_sin_u:  # esta en False
                r3_todas_vocales_sin_u = False

            # r4
            r4_cont_caracteres += 1

            if r4_tiene_d and i.lower() == "i":
                r4_tiene_di = True
                if r4_cont_caracteres == 2:
                    r4_tiene_di_primera_letra = True
            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

            ''' que tenga una "s" despues de la sigla
            if i.lower() == "s" and r4_tiene_di:
                r4_tiene_s = True
            que tenga una "s" antes de la sigla
            if i.lower() == "s" and not r4_tiene_di:
                r4_tiene_s = True
            '''

            # r5
            r5_cont_caracteres += 1     # 4

            es_digito_impar_r5 = validar_digitos_impares(i)     # return True si es digito impaor, False si no lo es
            if r5_cont_caracteres == 1 and es_digito_impar_r5:  # es_digito_impar_r5 esta diciend True
                r5_empieza_digito_impar = True

            if r5_cont_caracteres == 3 and i.lower() == "s":
                r5_tiene_s_pos3 = True

            if i.lower() == "p":
                r5_tiene_p = True

            # r6
            r6_cont_caracteres += 1
            r6_ultima_letra = i
            if i.lower() == "t":
                r6_cont_t += 1

        # =====================================================
        #   Estoy fuera de una palabra / Termino una palabra
        # =====================================================
        else:
            # r1
            if r1_todas_mayusculas and r1_cumple_digitos:
                r1 += 1

            # r2
            if r2_empieza_t:
                if r2 is None or r2_cont_caracteres < r2:
                    r2 = r2_cont_caracteres

            # r3
            if r3_todas_vocales_sin_u:
                r3 += 1

            # r4
            if r4_tiene_di and not r4_tiene_di_primera_letra:
                r4 += 1

            # r5
            if r5_empieza_digito_impar and r5_tiene_s_pos3 and not r5_tiene_p:
                r5 += 1

            # r6
            es_vocal_ultima_letra = validar_vocales(r6_ultima_letra)
            if r6_cont_t >= 2 and es_vocal_ultima_letra:
                r6_total_acum += r1_cont_caracteres
                r6_total_cant += 1

            # =====================================================
            #       Apagar banderas y reiniciar contadores
            # =====================================================

            # r1
            r1_cont_caracteres = 0
            r1_todas_mayusculas = True
            r1_cumple_digitos = True

            # r2
            r2_cont_caracteres = 0
            r2_empieza_t = False

            # r3
            r3_todas_vocales_sin_u = True

            # r4
            r4_cont_caracteres = 0
            r4_tiene_d = False
            r4_tiene_di = False
            r4_tiene_di_primera_letra = False

            # r5
            r5_cont_caracteres = 0
            r5_empieza_digito_impar = False
            r5_tiene_s_pos3 = False
            r5_tiene_p = False

            # r6
            r6_cont_caracteres = 0
            r6_ultima_letra = ""
            r6_cont_t = 0

    # Termino el ciclo
    m.close()

    r6 = calcular_promedio(r6_total_acum, r6_total_cant)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)
    print("Quinto resultado:", r5)
    print("Sexto resultado:", r6)


if __name__ == "__main__":
    principal()
