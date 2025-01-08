

# r5
def validar_mayusculas(i):
    # return "A" <= i <= "Z"
    if "A" <= i <= "Z":
        return True
    return False


# r4
def validar_minusculas(i):
    if "a" <= i <= "z":
        return True
    return False


def validar_digitos_impares(i):
    impares = "13579"
    if i in impares:
        return True
    else:
        return False


# r2
def validar_vocales(i):             # A
    if i.lower() in "aeiou":
        return True
    else:
        return False


def principal():

    ''' 1  - cantidad de palabras que comienzan y terminan con la misma letra, y su tercera letra
    no sea una t.'''
    r1 = 0          # la cantidad de palabras que cumplan las condiciones
    r1_cont_caracteres = 0
    r1_primera_letra = None
    r1_ultima_letra = None
    r1_tiene_t_pos3 = False

    es_palabra = False

    ''' 2 - la cantidad de palabras que comienzan y terminan con vocal. '''
    r2 = 0
    r2_empieza_vocal = False
    r2_ultima_letra = False

    ''' 3- la cantidad de palabras que comienza con la misma letra que termino la palabra anterior '''
    r3 = 0
    r3_ultima_letra = None

    ''' 4 - Determinar la cantidad de palabras que comienzan con un dígito impar, pero tales que el resto de sus
caracteres son letras en minúsculas. '''
    r4 = 0
    r4_empieza_digito = False
    r4_todas_minusculas = True

    ''' 5 - determinar la longitud de la menor palabra que contenga dos mayusculas seguidas '''
    r5 = None               # mayor
    r5_tiene_una_mayus = False
    r5_tiene_dos_mayus = False

    # da de di do du
    ''' 6 - Determinar cuántas palabras incluyen dos o más veces la expresión que conforman la letra "d"
mas una vocal (con cualquiera de sus letras en minúscula o mayúscula) pero de tal forma que la letra "p" 
aparezca antes de alguna de esas siglas'''
    # pedode  dopede
    r6 = 0
    r6_tiene_d = False
    r6_tiene_d_vocal = False
    r6_cont_d_vocal = 0
    r6_tiene_p = False

    m = open("archivo.txt", "rt")
    linea = m.readline()

    # linea = ese asa deidad jas kas lsk.
    for i in linea:
        # i =
        # Estoy dentro de una palabra
        if i != " " and i != ".":

            es_palabra = True

            # r1
            r1_cont_caracteres += 1
            r1_ultima_letra = i
            if r1_cont_caracteres == 1:
                r1_primera_letra = i

            if r1_cont_caracteres == 3 and i.lower() == "t":
                r1_tiene_t_pos3 = True

            # r2
            r2_ultima_letra = i
            es_vocal = validar_vocales(i)       # True si es vocal, False No sea vocal
            if r1_cont_caracteres == 1 and es_vocal:
                r2_empieza_vocal = True

            # r3
            if r1_cont_caracteres == 1 and i.lower() == r3_ultima_letra:
                r3 += 1

            r3_ultima_letra = i.lower()

            # r4
            es_digito_r4 = validar_digitos_impares(i)       # True si es digito, False no es digito
            if r1_cont_caracteres == 1 and es_digito_r4:
                r4_empieza_digito = True

            es_minuscula_r4 = validar_minusculas(i)     # True si es minuscula, return False si es mayuscula

            if not es_minuscula_r4 and r1_cont_caracteres > 1:
                r4_todas_minusculas = False

            # r5
            es_mayus = validar_mayusculas(i)        # return True si es mayuscula , false si no lo es
            if r5_tiene_una_mayus and es_mayus:
                r5_tiene_dos_mayus = True
            elif es_mayus:
                r5_tiene_una_mayus = True
            else:
                r5_tiene_una_mayus = False

            # r6
            es_vocal_r6 = validar_vocales(i)
            if r6_tiene_d and es_vocal_r6:
                r6_tiene_d_vocal = True
            elif i.lower() == "d":
                r6_tiene_d = True
            else:
                r6_tiene_d = False

            if i.lower() == "p" and r6_cont_d_vocal == 0:
                r6_tiene_p = True

            if r6_tiene_d_vocal:
                r6_cont_d_vocal += 1
                r6_tiene_d_vocal = False

        # estoy fuera de una palabra / termine una palabra
        else:
            # r1
            if r1_ultima_letra == r1_primera_letra and not r1_tiene_t_pos3 and es_palabra:
                r1 += 1

            # r2
            es_vocal_ult_letra = validar_vocales(r2_ultima_letra)
            if r2_empieza_vocal and es_vocal_ult_letra:
                r2 += 1

            # r4
            if r4_empieza_digito and r4_todas_minusculas:
                r4 += 1

            # r5
            if r5_tiene_dos_mayus:
                if r5 is None or r1_cont_caracteres < r5:
                    r5 = r1_cont_caracteres

            # r6
            if r6_cont_d_vocal >= 2 and r6_tiene_p:
                r6 += 1

            # Apagar las banderas , reiniciar contadores
            # r1
            r1_cont_caracteres = 0
            r1_primera_letra = None
            r1_ultima_letra = None
            r1_tiene_t_pos3 = False

            es_palabra = False

            # r2
            r2_empieza_vocal = False
            r2_ultima_letra = False

            # r4
            r4_empieza_digito = False
            r4_todas_minusculas = True

            # r5
            r5_tiene_una_mayus = False
            r5_tiene_dos_mayus = False

            # r6
            r6_tiene_d = False
            r6_tiene_d_vocal = False
            r6_cont_d_vocal = 0
            r6_tiene_p = False

    m.close()

    print("1 - Resultado:", r1)
    print("2 - Resultado:", r2)
    print("3 - Resultado:", r3) #
    print("4 - Resultado:", r4)
    print("5 - Resultado:", r5) #
    print("6 - Resultado:", r6)


if __name__ == '__main__':
    principal()
