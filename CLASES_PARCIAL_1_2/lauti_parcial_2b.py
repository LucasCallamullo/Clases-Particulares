
def validar_mayusculas(i):
    if "A" <= i <= "Z":
        return True
    else:
        return False


# r2
def calcular_porcentaje(r2_cont_total_palabras, r2_cont_palabras_cumplen):
    porc = 0
    if r2_cont_total_palabras != 0:
        porc = r2_cont_palabras_cumplen * 100 // r2_cont_total_palabras
    return porc


def validar_consonantes(i):
    # return i.lower() in "bcdfghjklmnpqrstvwxyz"
    # if "a" <= i.lower() <= "z" and not i in "aeiou":
    # if i in "qwrtypsdfghjklzxcvbnmñ":
    if i.lower() in "bcdfghjklmnpqrstvwxyz":
        return True
    else:
        return False


# r1
def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    else:
        return False


def validar_digitos_impares(i):
    if i in "13579":
        return True
    else:
        return False


def validar_vocales(i):
    # .lower() transformar el caracter a minuscula
    if i.lower() in "aeiou":  # si la i esta en "aeiou"
        return True
    else:
        return False


def principal():

    m = open("entrada.txt", "rt")   # read text ; leer texto
    linea = m.readline()            # nos recupera un str

    ''' 1 - Determinar la cantidad de palabras que tienen un dígito en la segunda o en la tercera 
posición y además incluyen dos o más consonantes pero a partir de la cuarta posición, incluida 
la cuarta (en minúscula o mayúscula)'''
    r1 = 0              # hace referencia a la respuesta
    r1_cont_caracteres = 0
    r1_tiene_digito_pos2_3 = False
    r1_cont_consonantes_pos4_mas = 0

    ''' 2 - Determinar el porcentaje entero de palabras (con respecto al total de palabras del texto),
de las palabras que tienen al menos una vocal (en minúscula o mayúscula) y finalizan con un dígito.
    # Porcentaje
        Total_Palabras ---- 100% 
        Palabras_cumplen --- X = Palabras_cumplen * 100 // Total_Palabras
'''
    r2 = 0
    r2_cont_total_palabras = 0
    r2_cont_palabras_cumplen = 0
    r2_tiene_vocal = False
    r2_ultima_caracter = ""

    ''' 3 - Determinar cuántas palabras tienen cuatro caracteres o más pero en las primeras tres 
posiciones solo tienen vocales (en minúscula o mayúscula, y sin importar si luego aparecen otras 
vocales más atrás). '''
    r3 = 0
    r3_cont_caracteres = 0
    r3_solo_vocales_pos3 = True

    ''' 4 - Determinar cuántas palabras incluyen la expresión "di" (con cualquiera de sus letras 
en minúscula o mayúscula) pero de tal forma que a su vez no comiencen con la expresión "di".
    
    # di            # DOS MAYUSCULAS SEGUIDAS
                    # DS AS
'''
    r4 = 0
    r4_cont_caracteres = 0
    r4_tiene_d = False
    r4_tiene_de = False
    r4_tiene_t = False

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":
            # r1
            r1_cont_caracteres += 1

            es_digito = validar_digitos(i)      # return True si es digito, False si no lo es
            if (r1_cont_caracteres == 2 or r1_cont_caracteres == 3) and es_digito:
                r1_tiene_digito_pos2_3 = True

            es_consonante = validar_consonantes(i)  # return True si es consonante, False si no lo es
            if r1_cont_caracteres >= 4 and es_consonante:
                r1_cont_consonantes_pos4_mas += 1

            # r2
            es_vocal = validar_vocales(i)   # return True si es vocal, False si no lo es
            if es_vocal:
                r2_tiene_vocal = True

            r2_ultima_caracter = i

            # r3
            r3_cont_caracteres += 1

            es_vocal_r3 = validar_vocales(i)    # return True si es vocal y un False si no lo es
            if r3_cont_caracteres <= 3 and not es_vocal_r3: # not es_vocal_r3 se refiere a que esta en False
                r3_solo_vocales_pos3 = False

            # r4
            r4_cont_caracteres += 1
            if r4_tiene_d and i.lower() == "e":
                r4_tiene_de = True
            # elif i.lower() == "d" and r4_cont_caracteres != 1:
            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

            ''' pero de tal forma que después de ella(la sigla) aparezca una "t" (minúscula o mayúscula) 
            en cualquier lugar. '''
            if i.lower() == "t" and r4_tiene_de:
                r4_tiene_t = True


        # Estoy fuera de una palabra / Termino una palabra
        else:

            # r1
            if r1_tiene_digito_pos2_3 and r1_cont_consonantes_pos4_mas >= 2:
                r1 += 1

            # r2
            r2_cont_total_palabras += 1

            es_digito_ultima = validar_digitos(r2_ultima_caracter)      # return True si es un digito False si no lo es
            if r2_tiene_vocal and es_digito_ultima:
                r2_cont_palabras_cumplen += 1

            # r3
            if r3_solo_vocales_pos3:        # "r3_solo_vocales_pos3" es True
                r3 += 1

            # r4
            if r4_tiene_de and r4_tiene_t:
                r4 += 1

            # Apagar banderas / reiniciar contadores
            # r1
            r1_cont_caracteres = 0
            r1_tiene_digito_pos2_3 = False
            r1_cont_consonantes_pos4_mas = 0

            # r2
            r2_tiene_vocal = False
            r2_ultima_caracter = ""

            # r3
            r3_cont_caracteres = 0
            r3_solo_vocales_pos3 = True

            # r4
            r4_cont_caracteres = 0
            r4_tiene_d = False
            r4_tiene_de = False
            r4_tiene_t = False

    # salgo del ciclo for
    m.close()

    r2 = calcular_porcentaje(r2_cont_total_palabras, r2_cont_palabras_cumplen)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    principal()

