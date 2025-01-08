
# r5
def validar_minusculas(i):
    if "a" <= i <= "z":
        return True
    return False


# r1
def validar_mayusculas(i):
    # return "A" <= i <= "Z"
    if "A" <= i <= "Z":
        return True
    return False


def validar_digitos(i):
    # if i in "0123456789":
    if "0" <= i <= "9":
        return True
    else:
        return False


def validar_digitos_impares(i):
    # if i in "13579":
    if "0" <= i <= "9":
        if int(i) % 2 != 0:
            return True
    return False


# r3
def calcular_porcentaje(r3_total_palabras, r3_total_cumplen):
    porc = 0
    if r3_total_palabras != 0:
        porc = r3_total_cumplen * 100 // r3_total_palabras
    return porc


def es_n(i):
    if i.lower() in "n":
        return True
    else:
        return False


def validar_vocales(i): # o
    # .lower() transforma al caracter a minuscula
    if i.lower() in "aeiou":  # si la i esta en "aeiou"
        return True
    else:
        return False        # retornar devovler


def principal():

    m = open("entrada.txt", "rt")   # read text ; leer texto
    linea = m.readline()        # recuperarnos la primera linea del archivo como un str

    ''' 1 - Determinar la cantidad de palabras que tienen un dígito en la segunda y en la
cuarta posición, pero de tal forma que el resto de sus caracteres son letras mayúsculas.  '''
    r1 = 0
    r1_cont_caracteres = 0
    r1_todas_mayusculas = True
    r1_todos_digitos_pos2_pos4 = True

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más corta entre 
aquellas que comienzan con una "t" (minúscula o mayúscula) pero tambien debe tener una longitud par. '''
    r2 = None
    r2_cont_caracteres = 0
    r2_empieza_t = False

    ''' 3 - Determinar el porcentaje entero de palabras (sobre el total de palabras) que tienen 
exactamente una "n" antes de la tercera posicion y que termine con una vocal. 
    # Porcentaje
        Total Palabras ----- 100%
        palabras_cumplen ---- porc = palabras_cumplen * 100 // Total Palabras
'''
    r3 = 0
    r3_total_palabras = 0
    r3_total_cumplen = 0
    r3_cont_caracteres = 0
    r3_cont_n = 0
    r3_ultima_letra = ""

    ''' 4 -  Determinar cuántas palabras incluyen la expresión "di" (con cualquiera de sus 
letras en minúscula o mayúscula) pero de tal forma que a su vez no comiencen con la expresión 
"di". '''
    r4 = 0
    r4_tiene_d = False
    r4_tiene_di = False
    r4_cont_caracteres = 0
    r4_comienza_di = False

    ''' 5 - Determinar la cantidad de palabras que tienen un solo dígito y además todo 
el resto de sus caracteres son minúsculas. '''
    r5 = 0
    r5_todas_minusculas = True
    r5_cont_digitos = 0

    for i in linea:

        # Estoy dentro de la palabra
        if i != " " and i != ".":

            # r1
            r1_cont_caracteres += 1

            if r1_cont_caracteres == 2 or r1_cont_caracteres == 4:
                es_digito_r1 = validar_digitos(i)   # return True si es un digito, False si no lo es
                if not es_digito_r1:    # "es_digito_r1" esta en False
                    r1_todos_digitos_pos2_pos4 = False

            else:
                es_mayuscula_r1 = validar_mayusculas(i) # return True si mayus, si toca FAlse
                if not es_mayuscula_r1:
                    r1_todas_mayusculas = False

            # r2
            r2_cont_caracteres += 1

            if r2_cont_caracteres == 1 and i.lower() == "t":
                r2_empieza_t = True

            # r3
            r3_cont_caracteres += 1

            if 1 <= r3_cont_caracteres <= 3 and i.lower() == "n":
                r3_cont_n += 1

            r3_ultima_letra = i

            # r4
            r4_cont_caracteres += 1

            if r4_tiene_d and i.lower() == "i":
                r4_tiene_di = True

                if r4_cont_caracteres == 2:
                    r4_comienza_di = True

            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

            ''' Encontrar la "t" antes de la sigla'''
            if i.lower() == "t" and not r4_tiene_di:
                pass

            ''' Encontrar la "t" despues de la sigla'''
            if i.lower() == "t" and r4_tiene_di:
                pass

            # r5

            if validar_digitos(i):      # devuelve True
                r5_cont_digitos += 1

            else:
                es_minuscula = validar_minusculas(i)
                if not es_minuscula:
                    r5_todas_minusculas = False


        # Termino la palabra / estoy fuera de la palabra
        else:
            # r1
            if r1_todas_mayusculas and r1_todos_digitos_pos2_pos4:
                r1 += 1

            # r2
            if r2_empieza_t and r2_cont_caracteres % 2 == 0:
                if r2 is None or r2_cont_caracteres < r2:
                    r2 = r2_cont_caracteres     # 4

            # r3
            r3_total_palabras += 1

            es_vocal_r3 = validar_vocales(r3_ultima_letra)  # return True si era vocal, False si no lo es
            if r3_cont_n == 1 and es_vocal_r3:
                r3_total_cumplen += 1

            # r4
            if r4_tiene_di and not r4_comienza_di:
                r4 += 1

            # r5
            if r5_todas_minusculas and r5_cont_digitos == 1:
                r5 += 1

            # Reiniciar contadores / Banderas
            # r1
            r1_cont_caracteres = 0
            r1_todas_mayusculas = True
            r1_todos_digitos_pos2_pos4 = True

            # r2
            r2_cont_caracteres = 0
            r2_empieza_t = False

            # r3
            r3_cont_caracteres = 0
            r3_cont_n = 0
            r3_ultima_letra = ""

            # r4
            r4_tiene_d = False
            r4_tiene_di = False
            r4_cont_caracteres = 0
            r4_comienza_di = False

            # r5
            r5_todas_minusculas = True
            r5_cont_digitos = 0

    # Termino el ciclo
    m.close()

    r3 = calcular_porcentaje(r3_total_palabras, r3_total_cumplen)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()




