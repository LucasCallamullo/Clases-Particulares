
# r1
def validar_consonantes(i):
    car = i.lower()
    if "a" <= car <= "z" and car not in "aeiou":
        return True
    return False


def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    return False


# r2
def calcular_porcentaje(r2_total_cumplen, r2_total_palabras):
    porc = 0
    if r2_total_palabras != 0:
        porc = r2_total_cumplen * 100 // r2_total_palabras
    return porc


# r3
def validar_vocales(i):
    if i.lower() in "aeiou":
        return True
    else:
        return False


def principal():

    fd = "entrada.txt"
    m = open(fd, "rt")
    linea = m.readline()

    ''' 1- Determinar la cantidad de palabras que tienen un dígito en la segunda o en la tercera posición 
y además incluyen dos o más consonantes pero a partir de la cuarta posición, incluida la cuarta (en
minúscula o mayúscula) '''
    r1 = 0  # hace referencia a la respuesta
    r1_cont_caracteres = 0
    r1_tiene_digito_pos2_pos3 = False
    r1_cont_consonantes_pos4mas = 0

    ''' 2 - Determinar el porcentaje entero de palabras (con respecto al total de palabras del texto), 
de las palabras que tienen al menos una vocal (en minúscula o mayúscula) y finalizan con un dígito. '''
    r2 = 0
    r2_total_palabras = 0
    r2_total_cumplen = 0
    r2_tiene_vocal = False
    r2_ultimo_caracter = ""

    ''' 3- Determinar cuántas palabras tienen cuatro caracteres o más pero en las primeras tres posiciones solo
tienen vocales (en minúscula o mayúscula, y sin importar si luego aparecen otras vocales más atrás). '''
    r3 = 0  # hace referencia a la respuesta
    r3_cont_caracteres = 0
    # la logica va a ser yo afirmo que son todas vocales hasta la pos3 si no se llegara a cumplir y toca
    # alguna consonante/digito/lo que sea, lo voy a cambiar a False, entonces para que se cumpla la condicion
    # esta bandera deberia llegar a True cuando termino una palabra
    r3_solo_vocales_hasta_pos3 = True

    '''4- Determinar cuántas palabras incluyen la expresión "de" (con cualquiera de sus letras en minúscula o
mayúscula) pero de tal forma que después de ella aparezca una "t" (minúscula o mayúscula) en cualquier
lugar. '''
    r4 = 0      # hace referencia a la respuesta
    r4_tiene_d = False
    r4_tiene_de = False
    r4_tiene_t = False

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # ===================================================================
            #                       Punto 1
            # ===================================================================
            r1_cont_caracteres += 1

            es_digito_r1 = validar_digitos(i)
            if (r1_cont_caracteres == 2 or r1_cont_caracteres == 3) and es_digito_r1:
                r1_tiene_digito_pos2_pos3 = True

            es_consonante_r1 = validar_consonantes(i)
            if r1_cont_caracteres >= 4 and es_consonante_r1:
                r1_cont_consonantes_pos4mas += 1

            # ===================================================================
            #                       Punto 2
            # ===================================================================
            es_vocal_r2 = validar_vocales(i)
            if es_vocal_r2:
                r2_tiene_vocal = True

            r2_ultimo_caracter = i

            # ===================================================================
            #                       Punto 3
            # ===================================================================
            r3_cont_caracteres += 1

            # si esta bandera se pone en false ante de la pos 3 significa que no me toco una vocal entonces
            # cambio el valor de la bandera a False porque ya no se cumple mi condicion
            es_vocal_r3 = validar_vocales(i)
            if r3_cont_caracteres <= 3 and not es_vocal_r3:
                r3_solo_vocales_hasta_pos3 = False

            # ===================================================================
            #                       Punto 4
            # ===================================================================
            if r4_tiene_d and i.lower() == "e":
                r4_tiene_de = True
            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

            # en este caso la bandera "r4_tiene_de" en True nos indica que ya encontramos la sigla por lo
            # tanto logicamente significa que solo vamos a encontrar una "t" despues de la sigla
            if i.lower() == "t" and r4_tiene_de:
                r4_tiene_t = True

        # Termino una palabra
        else:

            # r1
            if r1_cont_consonantes_pos4mas >= 2 and r1_tiene_digito_pos2_pos3:
                r1 += 1

            # r2
            r2_total_palabras += 1

            es_digito_r2_ultimo = validar_digitos(r2_ultimo_caracter)
            if r2_tiene_vocal and es_digito_r2_ultimo:
                r2_total_cumplen += 1

            # Punto 3
            # si r3_solo_vocales se mantuvo en True durante la palabra significa que esa palabra cumple
            # si se cambio es porque alguno delos primers 3 caracteres no era una vocal
            if r3_solo_vocales_hasta_pos3 and r3_cont_caracteres >= 4:
                r3 += 1

            # r4
            if r4_tiene_de and r4_tiene_t:
                r4 += 1

            # Apagar Banderas / Reiniciar Contadores , etc
            # r1
            r1_cont_caracteres = 0
            r1_tiene_digito_pos2_pos3 = False
            r1_cont_consonantes_pos4mas = 0

            # r2
            r2_tiene_vocal = False
            r2_ultimo_caracter = ""

            # r3
            r3_cont_caracteres = 0
            r3_solo_vocales_hasta_pos3 = True

            # r4
            r4_tiene_d = False
            r4_tiene_de = False
            r4_tiene_t = False

    # Fuera del ciclo
    m.close()

    # r2
    r2 = calcular_porcentaje(r2_total_cumplen, r2_total_palabras)


    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()