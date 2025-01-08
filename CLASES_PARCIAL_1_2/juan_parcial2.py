


# r2
def calcular_porcentaje(r2_total_palabras, r2_palabras_cumplen):
    porc = 0
    if r2_total_palabras != 0:
        porc = r2_palabras_cumplen * 100 // r2_total_palabras
    return porc



def validar_vocales(i): # o
    # .lower() transforma el caracter a minuscula / .upper()
    if i.lower() in "aeiou":  # si la i esta en "aeiou"
        return True
    else:
        return False        # nos trae, nos retorna, nos devuelve un valor


# r1
def validar_consonantes(i):
    if i.lower() in "bcdfghjklmnpqrstvwxyz":
        return True
    else:
        return False


def validar_digitos(i):
    # return "0" <= i <= "9"
    if "0" <= i <= "9":
        return True
    else:
        return False


def validar_digitos_impares(i):
    if i in "13579":
        return True
    return False




def principal():

    m = open("entrada.txt", "rt")       # read text ; leer texto

    linea = m.readline()        # les recupera un str
    # linea = "Hola mundooooo." # str

    ''' 123456789 012012345678
    1 - Determinar la cantidad de palabras que tienen un dígito en la segunda o en la tercera posición y además
incluyen dos o más consonantes pero a partir de la cuarta posición, incluida la cuarta (en minúscula o
mayúscula).
    '''
    r1 = 0
    r1_cont_caracteres = 0
    r1_tiene_digito_pos2_pos3 = False
    r1_cont_consonantes = 0

    ''' 2 - Determinar el porcentaje entero de palabras (con respecto al total de palabras del texto), de 
las palabrasn que tienen al menos una vocal (en minúscula o mayúscula) y finalizan con un dígito. 
    # Porcentaje
        Total_palabras --- 100%
        Palabras_cumplen -- X = Palabras_cumplen * 100 // Total_palabras
'''
    r2 = 0
    r2_total_palabras = 0
    r2_palabras_cumplen = 0
    r2_tiene_vocal = False
    r2_ultima_caracter = ""

    #
    ''' 3 - Determinar cuántas palabras tienen cuatro caracteres o más pero en las primeras tres 
posiciones solo tienen vocales (en minúscula o mayúscula, y sin importar si luego aparecen otras 
vocales más atrás). '''
    r3 = 0
    r3_cont_caracteres = 0
    r3_todas_vocales_pos3 = True

    ''' 4 - Determinar cuántas palabras incluyen la expresión "de" (con cualquiera de sus letras en
minúscula o mayúscula) pero de tal forma que después de ella aparezca una "t" (minúscula o mayúscula) 
en cualquier lugar. 

DOS MAYUUS SEGUIDAS
SD DS MN MS
tiene_una_mayus = False
tiene_dos_mayus = False

'''
    r4 = 0
    r4_tiene_d = False
    r4_tiene_de = False
    r4_tiene_t = False

    ''' 5 - Determinar la longitud (en cantidad de caracteres) de la palabra más corta de aquellas 
que tienen al menos un dígito. '''
    r5 = None
    r5_cont_caracters = 0
    r5_tiene_digito = False

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # r1
            r1_cont_caracteres += 1

            if r1_cont_caracteres == 2 or r1_cont_caracteres == 3:

                es_digito_r1 = validar_digitos(i)       # return True si es digito, False si no lo es
                if es_digito_r1:
                    r1_tiene_digito_pos2_pos3 = True

            elif r1_cont_caracteres >= 4:
                es_consonante_r1 = validar_consonantes(i)   # return True si es consonante, False si no lo es
                if es_consonante_r1:
                    r1_cont_consonantes += 1

            # r2
            r2_ultima_caracter = i

            es_vocal_r2 = validar_vocales(i)
            if es_vocal_r2:
                r2_tiene_vocal = True

            # r3
            r3_cont_caracteres += 1

            if r3_cont_caracteres <= 3:
                es_vocal_r3 = validar_vocales(i)        # return True si es vocal, False si no lo es
                if not es_vocal_r3:
                    r3_todas_vocales_pos3 = False

            # r4
            if r4_tiene_d and i.lower() == "e":
                r4_tiene_de = True

            elif i.lower() == "d":
                r4_tiene_d = True

            else:
                r4_tiene_d = False

            if i.lower() == "t" and r4_tiene_de:
                r4_tiene_t = True

            # r5
            r5_cont_caracters += 1
            if validar_digitos(i):
                r5_tiene_digito = True

        # Estoy fuera de la palabra / Termino una palabra
        else:

            # r1
            if r1_tiene_digito_pos2_pos3 and r1_cont_consonantes >= 2:
                r1 += 1

            # r2
            r2_total_palabras += 1

            es_digito_r2 = validar_digitos(r2_ultima_caracter)  # Return True si es digito False si no lo es
            if r2_tiene_vocal and es_digito_r2:
                r2_palabras_cumplen += 1

            # r3
            if r3_todas_vocales_pos3 and r3_cont_caracteres >= 4:
                r3 += 1

            # r4
            if r4_tiene_de and r4_tiene_t:
                r4 += 1

            # r5
            if r5_tiene_digito:
                if r5 is None or r5_cont_caracters < r5:
                    r5 = r5_cont_caracters

            # Reiniciar contadores, banderas
            # r1
            r1_cont_caracteres = 0
            r1_tiene_digito_pos2_pos3 = False
            r1_cont_consonantes = 0

            # r2
            r2_tiene_vocal = False
            r2_ultima_caracter = ""

            # r3
            r3_cont_caracteres = 0
            r3_todas_vocales_pos3 = True

            # r4
            r4_tiene_d = False
            r4_tiene_de = False
            r4_tiene_t = False

            # r5
            r5_cont_caracters = 0
            r5_tiene_digito = False

    # Termino el ciclo

    r2 = calcular_porcentaje(r2_total_palabras, r2_palabras_cumplen)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()


