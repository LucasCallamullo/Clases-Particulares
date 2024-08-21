

# r5
def calcular_promedio(r5_acum_total, r5_cant_total):
    prom = 0
    if r5_cant_total != 0:
        prom = r5_acum_total // r5_cant_total
    return prom

def validar_consonantes(i):
    # if "a" <= i.lower() <= "z" and not i in "aeiou":
    if i.lower() in "bcdfghjklmnpqrstvwxyz":
        return True
    else:
        return False


# r1
def validar_mayusculas(i):
    if "A" <= i <= "Z":
        return True
    else:
        return False


def validar_digitos(i):
    if "0" <= i <= "9":         #
        return True
    else:
        return False


def validar_digitos_impares(i):
    if i in "13579":
        return True
    else:
        return False


# r3
def validar_vocales_sin_u(i):
    if i.lower() in "aeio":
        return True
    else:
        return False


def validar_vocales(i):
    # .lower() transforma el caracter a minuscula
    if i.lower() in "aeiou":  # si la i esta en "aeiou"
        return True
    else:
        return False        # retornar, devolver


def principal():

    m = open("entrada.txt", "rt")       # read text ; leer texto
    linea = m.readline()                # te recupera un str

    #       1234
    #  A3S4DSADaSDA
    ''' 1 - Determinar la cantidad de palabras que tienen un dígito en la segunda y en la cuarta 
posición, pero de tal forma que el resto de sus caracteres son letras mayúsculas. '''
    r1 = 0
    r1_cont_caracteres = 0
    r1_tiene_digito_pos2 = False
    r1_tiene_digito_pos4 = False
    r1_todas_mayusculas = True

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más corta entre aquellas 
que comienzan con una "t" (minúscula o mayúscula). 
'''
    r2 = None
    r2_cont_caracteres = 0
    r2_empieza_t = False

    ''' 3- Determinar cuántas palabras están conformadas solo por vocales (minúsculas o mayúsculas), 
pero no contienen ninguna "u" (minúscula o mayúscula). 
'''
    r3 = 0
    r3_todas_vocales = True

    # HC KJ MP         123456    sc cv bn nh
    ''' 4 - Determinar cuántas palabras incluyen la expresión "di" (con cualquiera de sus letras en 
minúscula o mayúscula) pero de tal forma que a su vez no comiencen con la expresión "di". '''
    r4 = 0
    r4_cont_caracteres = 0
    r4_tiene_d = False
    r4_tiene_di = False
    r4_empieza_di = False

    #       12132
    ''' 5 - promedio de caracteres de las palabras que tengan igual cantidad de vocales qeu consoantens 
    # Promedoi ( Acumulador / contador )
    '''
    r5 = 0
    r5_acum_total = 0
    r5_cant_total = 0
    r5_cont_caracteres = 0
    r5_cont_vocales = 0
    r5_cont_consonantes = 0

    for i in linea:
        # 12345
        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # r1
            r1_cont_caracteres += 1
            es_digito_r1 = validar_digitos(i)           # return True si es digito o Falñse si no lo es
            if r1_cont_caracteres == 2:
                if es_digito_r1:
                    r1_tiene_digito_pos2 = True

            elif r1_cont_caracteres == 4:
                if es_digito_r1:
                    r1_tiene_digito_pos4 = True

            else:
                es_mayuscula_r1 = validar_mayusculas(i)  # return True si es mayus sino false
                if not es_mayuscula_r1:
                    r1_todas_mayusculas = False

            # r2
            r2_cont_caracteres += 1     # 5
            if r2_cont_caracteres == 1 and i.lower() == "t":
                r2_empieza_t = True

            # r3
            es_vocal_sin_u = validar_vocales_sin_u(i)
            if not es_vocal_sin_u:
                r3_todas_vocales = False

            # r4
            r4_cont_caracteres += 1

            if r4_tiene_d and i.lower() == "i":
                r4_tiene_di = True

                if r4_cont_caracteres == 2:
                    r4_empieza_di = True

            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

            # r5
            r5_cont_caracteres += 1

            es_vocal_r5 = validar_vocales(i)
            if es_vocal_r5:
                r5_cont_vocales += 1

            es_consonante = validar_consonantes(i)
            if es_consonante:
                r5_cont_consonantes += 1

        # Estoy fuera de la palabra / Termino la palabra
        else:

            # r1
            if r1_todas_mayusculas and r1_tiene_digito_pos2 and r1_tiene_digito_pos4:
                r1 += 1

            # r2
            if r2_empieza_t:
                if r2 is None or r2_cont_caracteres < r2:
                    r2 = r2_cont_caracteres

            # r3
            if r3_todas_vocales:
                r3 += 1

            # r4
            if r4_tiene_di and not r4_empieza_di:
                r4 += 1

            # r5
            if r5_cont_vocales == r5_cont_consonantes:
                r5_acum_total += r5_cont_caracteres
                r5_cant_total += 1

            # Apagar banderas / Reiniciar las banderas
            # r1
            r1_cont_caracteres = 0
            r1_tiene_digito_pos2 = False
            r1_tiene_digito_pos4 = False
            r1_todas_mayusculas = True

            # r2
            r2_cont_caracteres = 0
            r2_empieza_t = False

            # r3
            r3_todas_vocales = True

            # r4
            r4_cont_caracteres = 0
            r4_tiene_d = False
            r4_tiene_di = False
            r4_empieza_di = False

            # r5
            r5_cont_caracteres = 0
            r5_cont_vocales = 0
            r5_cont_consonantes = 0

    # Termino un ciclo
    m.close()

    r5 = calcular_promedio(r5_acum_total, r5_cant_total)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)
    print("Quinto resultado:", r5)


if __name__ == "__main__":
    principal()

