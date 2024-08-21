

# r5
def calcular_promedio(acum, cant):
    prom = 0
    if cant != 0:
        prom = acum // cant
    return prom


def validar_consonantes(i):
    if i in "bcdfghjklmnpqrstvwxyz":
        return True
    return False
    # if i in "qwrtypsdfghjklzxcvbnm


# r1
def validar_mayusculas(i):
    if "A" <= i <= "Z":
        return True
    return False


def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    return False


# r2
def validar_digitos_impares(i):
    '''
    if "0" <= i <= "9":
        if int(i) % 2 != 0:
            return True
    return False
    '''
    if i in "13579":
        return True
    return False


# r3
def validar_vocales(i): # A -> a
    # i.lower() transforma al caracter a minuscula
    if i.lower() in "aeiou":  # si la i esta en "aeiou"
        return True
    else:
        return False


def principal():

    m = open("entrada.txt", "rt")   # read text , leer texto
    linea = m.readline()            # nos trae un str
    print(linea)

    ''' 1 - Determinar la cantidad de palabras que tienen un dígito en la segunda y en la
cuarta posición, pero de tal forma que el resto de sus caracteres son letras mayúsculas. '''
    r1 = 0
    r1_cont_caracteres = 0
    r1_tiene_digitos_pos2_pos4 = True
    r1_todas_mayusculas = True

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más corta de 
aquellas que tienen exactamente un dígito impar y que su longitud sea par.'''
    r2 = None
    r2_cont_caracteres = 0
    r2_cont_digitos_impares = 0

    ''' 3 - Determinar cuántas palabras empiezan con una vocal y terminan con una vocal 
pero distinta de la primera (ambas en minúscula o en mayúscula en forma indistinta). '''
    r3 = 0
    r3_cont_caracteres = 0
    r3_empieza_vocal = False
    r3_primera_letra = ""
    r3_ultima_letra = ""

    ''' 4 - Determinar cuántas palabras incluyen la expresión "di" (con cualquiera de 
sus letras en minúscula o mayúscula) pero de tal forma que a su vez no comiencen con 
la expresión "di". '''
    r4 = 0
    r4_tiene_d = False
    r4_tiene_di = False
    r4_cont_caracteres = 0
    r4_empieza_di = False

    ''' 5 - Determinar el promedio entero de caracteres por palabra, de las palabras que 
tienen solo una vez una 'r' y dos o más veces una consonante (ambas en minúsculas o mayúsculas).
    Promedio = Una suma de cosas (acumulador) // cantidad de cosas que sumamos ( contador ) 
'''
    r5 = 0
    r5_total_acum = 0
    r5_total_cant = 0
    r5_cont_caracteres = 0
    r5_cont_r = 0
    r5_cont_cons = 0

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # r1
            r1_cont_caracteres += 1

            if r1_cont_caracteres == 2 or r1_cont_caracteres == 4:
                es_digito_r2 = validar_digitos(i)   # return True si es digito, False si no lo es
                if not es_digito_r2:    # es_digito es False
                    r1_tiene_digitos_pos2_pos4 = False

            else:
                es_mayuscula_r1 = validar_mayusculas(i)
                if not es_mayuscula_r1:
                    r1_todas_mayusculas = False

            # r2
            r2_cont_caracteres += 1
            es_digito_impar_r2 = validar_digitos_impares(i) # return True si es digito impar, False si no l oes
            if es_digito_impar_r2:
                r2_cont_digitos_impares += 1

            # r3
            r3_cont_caracteres += 1

            es_vocal_r1 = validar_vocales(i)    # return True si es vocal, False si no lo es
            # es_vocal = True
            if r3_cont_caracteres == 1 and es_vocal_r1:
                r3_empieza_vocal = True
                r3_primera_letra = i.lower()

            r3_ultima_letra = i.lower()

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

            ''' enuentr una "t" antes de la sigla '''
            if i.lower() == "t" and not r4_tiene_di:
                pass

            ''' enuentr una "t" despues de la sigla '''
            if i.lower() == "t" and r4_tiene_di:
                pass

            # r5
            r5_cont_caracteres += 1

            if i.lower() == "r":
                r5_cont_r += 1

            es_consonante_r5 = validar_consonantes(i)
            if es_consonante_r5:
                r5_cont_cons += 1

        # Termino una palabra / estoy fuera de una palabra
        else:
            # r1
            if r1_todas_mayusculas and r1_tiene_digitos_pos2_pos4:
                r1 += 1

            # r2
            if r2_cont_digitos_impares == 1 and r2_cont_caracteres % 2 == 0:
                if r2 is None or r2_cont_caracteres < r2:
                    r2 = r2_cont_caracteres

            # r3
            es_vocal_ultima_r3 = validar_vocales(r3_ultima_letra)
            if r3_empieza_vocal and r3_primera_letra != r3_ultima_letra and es_vocal_ultima_r3:
                r3 += 1

            # r4
            if r4_tiene_di and not r4_empieza_di:
                r4 += 1

            # r5
            if r5_cont_r == 1 and r5_cont_cons >= 2:
                r5_total_acum += r5_cont_caracteres
                r5_total_cant += 1

            # Reiniciar contadores, banderas
            # r1
            r1_cont_caracteres = 0
            r1_tiene_digitos_pos2_pos4 = True
            r1_todas_mayusculas = True

            # r2
            r2_cont_caracteres = 0
            r2_cont_digitos_impares = 0

            # r3
            r3_cont_caracteres = 0
            r3_empieza_vocal = False
            r3_primera_letra = ""
            r3_ultima_letra = ""

            # r4
            r4_tiene_d = False
            r4_tiene_di = False
            r4_cont_caracteres = 0
            r4_empieza_di = False

            # r5
            r5_cont_caracteres = 0
            r5_cont_r = 0
            r5_cont_cons = 0

    # Termino el ciclo
    m.close()

    # r5
    r5 = calcular_promedio(r5_total_acum, r5_total_cant)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)
    print("Quinto resultado:", r5)


if __name__ == '__main__':
    principal()