

# r5
def validar_mayus(i):
    return "A" <= i <= "Z"


# r4
def validar_consonantes(i):
    # if "a" <= i.lower() <= "z" and i not in "aeiou":
    if i.lower() in "bcdfghjklmnpqrstvwxyz":
        return True
    return False
    # if i in "qwrtypsdfghjklzxcvbnm":


# r3
def calcular_promedio(r3_total_acum, r3_total_cont):
    prom = 0
    if r3_total_cont != 0:
        prom = r3_total_acum // r3_total_cont
    return prom


# r2
def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    return False


def validar_digitos_impares(i):
    '''
    if i in "13579":
        return True
    return False
    '''
    if "0" <= i <= "9":
        if int(i) % 2 != 0:
            return True
    return False


# r1
def validar_minusculas(i):
    if "a" <= i <= "z":
        return True
    return False


def validar_vocales(i): # o
    # .lower() transforma el caracter a minuscula
    if i.lower() in "aeiou":  # si la i esta en "aeiou"
        return True
    else:
        return False        # retornar devolver


def principal():

    m = open("entrada.txt", "rt")   # read text ; leer texto
    linea = m.readline()            # nos trae un str

    ''' 1- Determinar la cantidad de palabras que tienen un solo dígito y además todo el 
resto de sus caracteres son minúsculas 
'''
    r1 = 0
    r1_cont_digitos = 0
    r1_todas_minusculas = True

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más corta de 
aquellas que tienen dos dígitos, ademas que comienze con "p" (mayuscula o minuscula)
pero no tenga "t". '''
    r2 = None
    r2_cont_caracteres = 0
    r2_cont_digitos = 0
    r2_empieza_p = False
    r2_tiene_t = False

    #       123456
    ''' 3 - Determinar el promedio de caracteres de las palabras que tienen exactamente una "n" 
entre la posiciones 1 y 3, y al menos una "a" 
(mayúscula o minúscula) pero de forma que esa "a" esté entre los cuatro primeros caracteres. 
    # Promedio = un acumulador / un contador

'''
    r3 = 0
    r3_total_acum = 0
    r3_total_cont = 0
    r3_cont_caracteres = 0
    r3_cont_n_pos3 = 0
    r3_tiene_a_pos4 = False

    # HC SC            cuantas
    ''' 4 - Determinar cuántas palabras incluyen la expresión "se" (con cualquiera de sus letras en
minúscula o mayúscula) pero de tal forma que la palabra comience con esa expresión y termine con 
una consonante cualquiera (en minúscula o mayúscula). '''
    r4 = 0
    r4_tiene_s = False
    r4_tiene_se = False
    r4_cont_caracteres = 0
    r4_ultima_letra = ""

    ''' 5 - Determinar la cantidad de palabras que tienen un dígito en la segunda y en la 
cuarta posición, pero de tal forma que el resto de sus caracteres son letras mayúsculas. '''
    r5 = 0
    r5_cont_caracteres = 0
    r5_tiene_digito_pos2_pos4 = True
    r5_todas_mayusculas = True

    for i in linea:

        # Estoy dentro de la palabra
        if i != " " and i != ".":

            # r1
            es_digito_r1 = validar_digitos(i)

            if es_digito_r1:
                r1_cont_digitos += 1

            else:
                es_minuscula_r1 = validar_minusculas(i)
                if not es_minuscula_r1:
                    r1_todas_minusculas = False

            # r2
            r2_cont_caracteres += 1

            es_digito_r2 = validar_digitos(i)   # return True si es vocal, False si no lo es
            if es_digito_r2:
                r2_cont_digitos += 1

            if r2_cont_caracteres == 1 and i.lower() == "p":
                r2_empieza_p = True

            if i.lower() == "t":
                r2_tiene_t = True

            # r3
            r3_cont_caracteres += 1

            if 1 <= r3_cont_caracteres <= 3 and i.lower() == "n":
                r3_cont_n_pos3 += 1

            if 1 <= r3_cont_caracteres <= 4 and i.lower() == "a":
                r3_tiene_a_pos4 = True

            # r4
            r4_cont_caracteres += 1

            if r4_tiene_s and i.lower() == "e":
                r4_tiene_se = True
            elif i.lower() == "s" and r4_cont_caracteres == 1:
                r4_tiene_s = True
            else:
                r4_tiene_s = False

            r4_ultima_letra = i

            # encuentres la "t" antes de la sigla
            if i.lower() == "t" and not r4_tiene_se:
                pass

            # encuentres la "t" despues de la sigla
            if i.lower() == "t" and r4_tiene_se:
                pass

            # r5
            r5_cont_caracteres += 1

            if r5_cont_caracteres == 2 or r5_cont_caracteres == 4:
                es_digito_r5 = validar_digitos(i)
                if not es_digito_r5:
                    r5_tiene_digito_pos2_pos4 = False

            else:
                es_mayuscula = validar_mayus(i)
                if not es_mayuscula:
                    r5_todas_mayusculas = False

        # Estoy fuera de la palabra / Termine la palabra
        else:
            # r1
            if r1_todas_minusculas and r1_cont_digitos == 1:
                r1 += 1

            # r2
            if r2_cont_digitos == 2 and r2_empieza_p and not r2_tiene_t:
                if r2 is None or r2_cont_caracteres < r2:
                    r2 = r2_cont_caracteres

            # r3
            if r3_cont_n_pos3 == 1 and r3_tiene_a_pos4:
                r3_total_acum += r3_cont_caracteres
                r3_total_cont += 1

            # r4
            es_consonante_r4 = validar_consonantes(r4_ultima_letra) # return True si es cons o False si no lo es
            if r4_tiene_se and es_consonante_r4:
                r4 += 1

            # r5
            if r5_tiene_digito_pos2_pos4 and r5_todas_mayusculas:
                r5 += 1

            # Reiniciar ese contador, o esa bandera

            # r1
            r1_cont_digitos = 0
            r1_todas_minusculas = True

            # r2
            r2_cont_caracteres = 0
            r2_cont_digitos = 0
            r2_empieza_p = False
            r2_tiene_t = False

            # r3
            r3_cont_caracteres = 0
            r3_cont_n_pos3 = 0
            r3_tiene_a_pos4 = False

            # r4
            r4_tiene_s = False
            r4_tiene_se = False
            r4_cont_caracteres = 0
            r4_ultima_letra = ""

            # r5
            r5_cont_caracteres = 0
            r5_tiene_digito_pos2_pos4 = True
            r5_todas_mayusculas = True

    # Termino el ciclo
    m.close()

    # r3
    r3 = calcular_promedio(r3_total_acum, r3_total_cont)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)
    print("Quinto resultado:", r5)


if __name__ == '__main__':
    principal()
