
# r1
def es_digito(caracter):    # 5
    if caracter in "0123456789":
        return True
    return False


# r2
def es_mayuscula(caracter):
    if caracter in "QWRTYPSDFGHJKLÑZXCVBNMAEIOU":
        return True
    return False


# r3
def es_vocal_sin_u(caracter):
    if caracter.lower() in "aeio":
        return True
    return False


# r1
def validar_vocales(caracter):
    if caracter.lower() in "aeiou":
        return True
    return False


def validar_digitos(caracter):
    if caracter in "0123456789":
        return True
    return False


def validar_digitos_impar(caracter):
    if caracter in "13579":
        return True
    return False




def principal():

    m = open('archivo.txt', 'rt')       # read o read text

    linea = m.readline()        # obtiene la primera linea de texto

    # indice = 123401
    # linea = "Hola Mundo."
    m.close()

    """  
    #   123456789         
    1 - Determina la cantidad de palabras que tienen exactamente seis caracteres de largo e incluyen una o dos
    vocales (en mayúscula o minúscula) y uno o más dígitos de la posicion 3 a la 7.
    """
    r1 = 0
    indice = 0
    r1_cont_vocales = 0
    r1_tiene_digito = False


    """ 
    #   123456789
    2 - Determina el promedio entero de caracteres por palabra, de las palabras que tienen solo una vez una 'r' y
dos o más veces una 'e' (ambas en minúsculas o mayúsculas). 

tiene al menos una letra e, --> bandera  TRUE o FALSE
tiene dos o mas letras e --> contador de letras "e" y con eso podes verificar la cantidad

    # Promedio 
    prom = sumatoria de caracteres / cantidad de palabras
    """
    r2 = 0      # promedio
    r2_acum = 0
    r2_cont = 0

    r2_cont_r = 0
    r2_cont_e = 0

    """
    # ultima        
    #   Determina         p       
    3 - Determina cuántas palabras empiezan con una vocal y terminan con una vocal pero distinta de la primera
(ambas en minúscula o en mayúscula en forma indistinta)
    """
    r3 = 0
    r3_empieza_vocal = False
    ultima = ""
    primera = ""

    """
    4 - Determinar cuántas palabras incluyen la expresión "fi" (con cualquiera de sus letras en minúscula o en
mayúscula) y también contienen una "n" o una "t" y ademas la sigla aparezca antes de una "p".
    """
    r4 = 0
    r4_tiene_f = False
    r4_tiene_fi = False
    r4_tiene_n_or_t = False

    r4_tiene_p = False

    #
    for caracter in linea:
        # caracter = "H", "o", ..., "."

        # Estoy dentro de una palabra
        if caracter != " " and caracter != ".":

            # r1
            indice += 1

            es_vocal = validar_vocales(caracter)
            if es_vocal is True:    # if es_vocal:
                r1_cont_vocales += 1

            es_digito = validar_digitos(caracter)   # return True or False
            # if es_digito is True and 3 <= indice and indice <= 7:
            if es_digito is True and 3 <= indice <= 7:

                r1_tiene_digito = True

            # r2
            if caracter.lower() == "e":
                r2_cont_e += 1

            if caracter.lower() == "r":
                r2_cont_r += 1


            # r3
            es_vocal = validar_vocales(caracter)
            if indice == 1 and es_vocal is True:
                r3_empieza_vocal = True

            if indice == 1:
                primera = caracter

            ultima = caracter

            # r4
            if caracter.lower() == "p":
                r4_tiene_p = True

            # if caracter.lower() == "i" and r4_tiene_f and r4_tiene_p is False:  # antes de la p
            if caracter.lower() == "i" and r4_tiene_f and r4_tiene_p is True:  # despues de la p
                r4_tiene_fi = True

            elif caracter.lower() == "f":
                r4_tiene_f = True

            else:
                r4_tiene_f = False

            if caracter.lower() == "n" or caracter.lower() == "t":
                r4_tiene_n_or_t = True

        #
        # Fuera de una palabra
        else:
            # indice = 8
            # ultima = "a"

            # r1
            if r1_tiene_digito and r1_cont_vocales <= 2 and indice == 6:
                r1 += 1

            # r2
            if r2_cont_e >= 2 and r2_cont_r == 1:
                r2_acum += indice
                r2_cont += 1

            # r3
            es_vocal = validar_vocales(ultima)
            if r3_empieza_vocal is True and primera.lower() != ultima.lower() and es_vocal is True:
                r3 += 1

            # r4
            if r4_tiene_n_or_t and r4_tiene_fi:
                r4 += 1

            # Reiniciar contadores / banderas

            # r1
            indice = 0
            r1_cont_vocales = 0
            r1_tiene_digito = False

            # r2
            r2_cont_r = 0
            r2_cont_e = 0

            # r3
            r3_empieza_vocal = False
            ultima = ""
            primera = ""

            # r4
            r4_tiene_f = False
            r4_tiene_fi = False
            r4_tiene_n_or_t = False

    #
    # r2 - calcular promedio
    if r2_cont > 0:
        r2 = r2_acum // r2_cont

    # resultados
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()

