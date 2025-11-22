

# r3
def contiene_vocal(caracter):
    if caracter.lower() in "aeiou":
        return True
    return False


# r2
def contiene_p(caracter):
    if caracter.lower() in "p":
        return True
    return False


# r1
def contiene_digito(caracter):
    if caracter in "0123456789":
        return True
    return False


def contiene_mayuscula(caracter):
    if caracter in "QWERTYUIOPASDFGHJKLÑZXCVBNM":
        return True
    return False


def principal():

    m = open("archivo.txt", "rt")
    linea = m.readline()
    m.close()

    """ 
    #   123456789 0120123 
    1 - Determinar la cantidad de palabras que comienzan con mayúscula y tienen 
    un dígito en la cuarta posición. 
    """
    r1 = 0
    indice = 0
    r1_comienza_mayus = False
    r1_tiene_digito_pos4 = False

    """ 
    #   123456789
    
    # "al menos una" habla de que tiene o no tiene, es no importa la cantidad
    # "tiene una" esta hablando cantidad -> necesitas un contador para verificar la cantidad
    
    2 - Determina la longitud de la palabra más larga entre las que tienen una "p" o una "n".
    """
    r2 = None      # buscar la mayor longitud
    r2_cont_p = 0
    r2_cont_n = 0

    """ 
        
    3 - Determinar el promedio entero de caracteres por palabra entre las que tienen dos o 
    más veces un dígito en cualquier lugar y además tienen una vocal en cualquier lugar.
    
    promedio = sumatoria de caracteres de las palabras que cumplen // cantidad de veces que sumaste
    """
    r3 = 0      # promedio
    r3_acum_caracter = 0
    r3_cont_palabras = 0

    r3_cont_2oMas_digitos = 0
    r3_cont_vocal = 0

    """ 
    # estados -> comienza o no comienza, tiene o no tiene, es o no es, son o no son, --> banderas
    
    4 - Determinar cuántas palabras incluyen la expresión "fa" (con cualquiera de sus letras 
    en minúscula o mayúscula) pero de tal forma que además comiencen con una vocal. 
    """
    r4 = 0
    r4_tiene_f = False
    r4_tiene_fa = False
    r4_comienza_vocal = False

    """ 
    5 - DETERMINAR la cantidad de palabras que no tiene un dígito en la segunda o tercera posicion
    pero el resto de sus caracteres son mayusculas.
    """
    r5 = 0
    r5_tiene_digito_pos2_pos3 = False     # if tienedigito is True   -->> tiene digito is  False
    r5_todas_mayusculas = True              #


    for caracter in linea:
        # caracter = "H", "o", "l", ...

        # dentro de la palabra
        if caracter != " " and caracter != ".":

            # r1
            indice += 1

            es_mayus = contiene_mayuscula(caracter)     # return True or False
            if es_mayus is True and indice == 1:
                r1_comienza_mayus = True

            es_digito = contiene_digito(caracter)       # return True or False
            if es_digito is True and indice == 4:
                r1_tiene_digito_pos4 = True

            # r2
            # es_p = contiene_p(caracter)
            if caracter.lower() == "p":
                r2_cont_p += 1

            if caracter.lower() == "n":
                r2_cont_n += 1

            # r3
            es_digito = contiene_digito(caracter)       # return True or False
            if es_digito is True:
                r3_cont_2oMas_digitos += 1

            es_vocal = contiene_vocal(caracter)
            if es_vocal is True:
                r3_cont_vocal += 1

            # r4
            if r4_tiene_f is True and caracter.lower() == "a":
                r4_tiene_fa = True
            elif caracter.lower() == "f":
                r4_tiene_f = True
            else:
                r4_tiene_f = False

            es_vocal = contiene_vocal(caracter)
            if es_vocal is True and indice == 1:
                r4_comienza_vocal = True

            # r5
            es_digito = contiene_digito(caracter)
            if indice == 2 or indice == 3:
                if es_digito is True:
                    r5_tiene_digito_pos2_pos3 = True

            else:   # no es posicion 2 ni 3
                es_mayus = contiene_mayuscula(caracter)  # return True or False
                if es_mayus is False:
                    r5_todas_mayusculas = False

        #
        # fuera de la palabra
        else:
            # r1_comienza_mayus = True
            # r3_cont_2oMas_digitos = 3

            # si se cumplen las condiciones de comienza mayuscula y digito en la posicion 4
            if r1_comienza_mayus is True and r1_tiene_digito_pos4 is True:
                r1 += 1            # sumar en tu contador de palabras

            # r2
            # que la longitud sea impar
            if (r2_cont_p == 1 or r2_cont_n == 1) and indice % 2 == 1:
                if r2 is None or r2 > indice:
                    r2 = indice         # aca se guarda la longitud

            # r3
            if r3_cont_2oMas_digitos >= 2 and r3_cont_vocal == 1:
                r3_acum_caracter += indice
                r3_cont_palabras += 1

            # r4
            if r4_tiene_fa is True and r4_comienza_vocal is True:
                r4 += 1

            # r5
            if r5_tiene_digito_pos2_pos3 is False and r5_todas_mayusculas is True:
                r5 += 1

            #
            # reiniciar banderas / contadores

            # r1
            indice = 0
            r1_comienza_mayus = False
            r1_tiene_digito_pos4 = False

            # r2
            r2_cont_p = 0
            r2_cont_n = 0

            # r3
            r3_cont_2oMas_digitos = 0
            r3_cont_vocal = 0

            # r4
            r4_tiene_f = False
            r4_tiene_fa = False
            r4_comienza_vocal = False

            # r5
            r5_tiene_digito_pos2_pos3 = False
            r5_todas_mayusculas = True

            #
    # calcular promedio
    if r3_cont_palabras > 0:
        r3 = r3_acum_caracter // r3_cont_palabras

    #
    # resultados fuera del for
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)
    print("Quinto resultado:", r5)


if __name__ == '__main__':
    principal()