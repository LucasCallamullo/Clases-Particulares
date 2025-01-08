

# r5
def es_mayus(i):
    return "A" <= i <= "Z"


# r4
def es_consonante(i):
    if "b" <= i.lower() <= "z" and i not in "eiou":
        return True
    return False
    # return i.lower() in "bcdfghjklmnpqrstvwxyz"


# r2
def es_digito_impar(i):
    if "0" <= i <= "9":
        if int(i) % 2 != 0:
            return True
    return False
    # return i in "13579"


# r1
def es_minusculas(i):
    return "a" <= i <= "z"


def validar_digitos(i):
    return "0" <= i <= "9"


def principal():

    m = open("entrada.txt", "rt")   # read text ; leer texto
    linea = m.read()                # nos trae un str o string
    m.close()

    ''' 1 - Determinar la cantidad de palabras que tienen un solo dígito y además todo el 
resto de sus caractres son minúsculas '''
    r1 = 0
    r1_cont_digitos = 0
    r1_todas_minusculas = True

    ''' 2 Determinar la longitud (en cantidad de caracteres) de la palabra más corta de 
aquellas que tienen al menos un dígito impar y su longitud sea par. '''
    r2 = None
    r2_cont_caracteres = 0
    r2_tiene_digito_impar = False

    ''' 3 - Determinar cuántas palabras tienen tienen exactamente dos "n" en cualquier lugar (seguidas o no,
mayúsculas o minúsculas) y al menos una "a" (mayúscula o minúscula) pero de forma que esa "a" esté
entre los cuatro primeros caracteres. '''
    r3 = 0
    r3_cont_n = 0
    r3_tiene_a = False

    ''' 4 - Determinar cuántas palabras incluyen la expresión "se" (con cualquiera de sus letras en 
minúscula o mayúscula) pero de tal forma que la palabra comience con esa expresión y termine con 
una consonante cualquiera (en minúscula o mayúscula). '''
    r4 = 0
    r4_tiene_s = False
    r4_tiene_se = False
    r4_ultima_letra = ""

    ''' 5 - Determinar la cantidad de palabras que tienen un dígito en la segunda y en la 
cuarta posición, pero de tal forma que el resto de sus caracteres son letras mayúsculas. '''
    r5 = 0
    r5_cont_caracteres = 0
    r5_todas_mayusculas = True
    r5_todos_digitos = True

    for i in linea:

        # Estoy dentro de la palabra
        if i != " " and i != ".":

            # r1
            es_digito = validar_digitos(i)              # return True
            if es_digito:
                r1_cont_digitos += 1

            else:
                es_minus = es_minusculas(i)     # return True si es minus, False si no lo es
                if es_minus is False:
                    r1_todas_minusculas = False

            # r2
            r2_cont_caracteres += 1

            if es_digito_impar(i):
                r2_tiene_digito_impar = True

            # r3
            if i.lower() == "n":
                r3_cont_n += 1

            elif i.lower() == "a" and r2_cont_caracteres <= 4:
                r3_tiene_a = True

            # r4
            r4_ultima_letra = i

            if r4_tiene_s and i.lower() == "e":
                r4_tiene_se = True
            elif i.lower() == "s" and r2_cont_caracteres == 1:
                r4_tiene_s = True
            else:
                r4_tiene_s = False

            ''' 
            if tiene_una_mayus and es_mayus:
                tiene_dos_mayus = True
            elif es_mayus:
                tiene_una_mayus = True
            else:
                tiene_una_mayus = False
            '''

            # r5
            r5_cont_caracteres += 1

            if r5_cont_caracteres == 2 or r5_cont_caracteres == 4:
                if validar_digitos(i) is False:
                    r5_todos_digitos = False

            else:
                if es_mayus(i) is False:        # if not es_mayus(i)
                    r5_todas_mayusculas = False

        # Termino una palabra / estoy fuera de una palabra
        else:

            # R1
            if r1_cont_digitos == 1 and r1_todas_minusculas:
                r1 += 1

            # r2
            if r2_tiene_digito_impar and r2_cont_caracteres % 2 == 0:
                if r2 is None or r2_cont_caracteres < r2:
                    r2 = r2_cont_caracteres

            # r3
            if r3_tiene_a and r3_cont_n == 2:
                r3 += 1

            # r4
            if r4_tiene_se and es_consonante(r4_ultima_letra):
                r4 += 1

            # r5
            if r5_todas_mayusculas and r5_todos_digitos:
                r5 += 1

            # Reiniciar banderas / reiniciar contadores
            # r1
            r1_cont_digitos = 0
            r1_todas_minusculas = True

            # r2
            r2_cont_caracteres = 0
            r2_tiene_digito_impar = False

            # r3
            r3_cont_n = 0
            r3_tiene_a = False

            # r4
            r4_tiene_s = False
            r4_tiene_se = False
            r4_ultima_letra = ""

            # r5
            r5_cont_caracteres = 0
            r5_todas_mayusculas = True
            r5_todos_digitos = True

    # termino el ciclo
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    principal()

