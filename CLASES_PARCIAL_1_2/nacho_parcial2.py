

# r3
def validar_mayuscula(i):
    if "A" <= i <= "Z":
        return True
    return False


# r2
def calcular_porcentaje(cumplen, total):
    porc = 0
    if total > 0:
        porc = cumplen * 100 // total
    return porc


def validar_consonantes(i):
    consonantes = "bcdfghjklmnpqrstvxywzñ"
    if i.lower() in consonantes:
        return True
    else:
        return False


# r1
def validar_vocales(i):
    # .lower() transforma al caracter en minuscula, i.upper() transforma al caracter a mayuscula
    if i.lower() in "aeiou":        #
        return True
    else:
        return False


def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    else:
        return False


def principal():

    '''
    1 - Determinar la cantidad de palabras que empiezan con una vocal (mayúscula o minúscula) e
incluyen dos o más dígitos(numeros).
    '''
    r1 = 0      # la cantidad de palabras que cumplen con las condiciones
    r1_indice = 0
    r1_empieza_vocal = False
    r1_cont_digitos = 0

    '''
    2 - Determinar el porcentaje entero de palabras (con respecto al total de palabras del texto), de las
palabras que tienen al menos dos consonantes seguidas
    
    # Porcentaje
    # cant_ total _palabras ---- 100 %
    # cant_ palabras cumplen --- X = 
    '''
    r2 = 0      # hace referencia al porcentaje
    r2_cant_total_palabras = 0
    r2_cant_total_cumplen = 0
    r2_tiene_consonante = False
    r2_tiene_dos_consonante = False

    ''' Determinar cuántas palabras tienen más de dos caracteres pero menos de siete, y presentan una
vocal en la posición 3, una consonante en la posición 5 y una mayúscula cualquiera en la posición 6.
'''

    r3 = 0             # la cantidad de palabras que cumplen con las condiciones
    r3_indice_longitud = 0
    r3_tiene_vocal_3 = False
    r3_tiene_cons_5 = False
    r3_tiene_mayus_6 = False

    ''' Determinar cuántas palabras incluyen la expresión “so” (con cualquiera de sus letras en minúscula
o mayúscula) pero de tal forma que antes de esa expresión haya aparecido una ‘p’ en cualquier
lugar'''
    r4 = 0           # la cantidad de palabras que cumplen con las condiciones
    r4_tiene_s = False
    r4_tiene_so = False
    r4_tiene_p_antes_so = False

    # como leer el archivo
    archivo = "archivito.txt"
    m = open(archivo, "rt")         # read text , leer texto

    # forma 1
    linea = m.readline()
    # linea = HOLA MUNDO

    for i in linea:

        # Estamos dentro de una palabra
        if i != " " and i != ".":           # if not i in " .":     # if i in " .":
            # H
            # r1
            r1_indice += 1
            es_vocal_r1 = validar_vocales(i)
            if r1_indice == 1 and es_vocal_r1:
                r1_empieza_vocal = True

            es_digito_r1 = validar_digitos(i)

            if es_digito_r1:
                r1_cont_digitos += 1

            # r2
            es_consonante_r2 = validar_consonantes(i)
            if r2_tiene_consonante and es_consonante_r2:
                r2_tiene_dos_consonante = True

            elif es_consonante_r2:
                r2_tiene_consonante = True

            else:
                r2_tiene_consonante = False

            # r3
            r3_indice_longitud += 1
            es_vocal_r3 = validar_vocales(i)
            es_consonante_r3 = validar_consonantes(i)
            es_mayuscula_r3 = validar_mayuscula(i)
            if r3_indice_longitud == 3 and es_vocal_r3:
                r3_tiene_vocal_3 = True

            elif r3_indice_longitud == 5 and es_consonante_r3:
                r3_tiene_cons_5 = True

            elif r3_indice_longitud == 6 and es_mayuscula_r3:
                r3_tiene_mayus_6 = True

            # r4
            if r4_tiene_s and i.lower() == "o":
                r4_tiene_so = True

            elif i.lower() == "s":
                r4_tiene_s = True

            else:
                r4_tiene_s = False

            if i.lower() == "p" and not r4_tiene_so:
                r4_tiene_p_antes_so = True

        # Terminando una palabra
        else:
            # r1
            if r1_empieza_vocal and r1_cont_digitos >= 2:
                r1 += 1

            # r2
            r2_cant_total_palabras += 1
            if r2_tiene_dos_consonante:
                r2_cant_total_cumplen += 1

            # r3
            if r3_tiene_vocal_3 and r3_tiene_cons_5 and r3_tiene_mayus_6 and 2 < r3_indice_longitud < 7:
                r3 += 1

            # r4
            if r4_tiene_so and r4_tiene_p_antes_so:
                r4 += 1

            # Apagar banderas, reiniciar contadores
            r1_indice = 0
            r1_empieza_vocal = False
            r1_cont_digitos = 0

            # r2
            r2_tiene_dos_consonante = False
            r2_tiene_consonante = False

            # r3
            r3_tiene_vocal_3 = False
            r3_tiene_cons_5 = False
            r3_tiene_mayus_6 = False
            r3_indice_longitud = 0

            # r4
            r4_tiene_s = False
            r4_tiene_so = False
            r4_tiene_p_antes_so = False

    # Cuando salimos del ciclo for
    r2 = calcular_porcentaje(r2_cant_total_cumplen, r2_cant_total_palabras)


    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)



if __name__ == "__main__":
    principal()