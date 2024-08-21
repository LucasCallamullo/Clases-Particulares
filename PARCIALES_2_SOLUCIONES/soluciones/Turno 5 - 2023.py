

# r3
def calcular_porcentaje(r2_total_cumplen, r2_total_palabras):
    porc = 0
    if r2_total_palabras != 0:
        porc = r2_total_cumplen * 100 // r2_total_palabras
    return porc


def validar_vocal_consonante(i):
    # solamente para mostrarle unir dos posibles resultados en una sola funcion
    if i.lower() in "aeiou":
        return "VOCAL"
    else:
        if i.lower in "bcdfghjklmnpqrstvwxyz":
            return "CONSONANTE"
    return "NADA"


# r4
def validar_digitos(i):
    return "0" <= i <= "9"


def validar_letras(i):
    if "a" <= i.lower() <= "z":
        return True
    else:
        return False


def validar_digitos_pares(i):
    if i in "02468":
        return True
    else:
        return False


def principal():

    fd = "entrada.txt"
    m = open(fd, "rt")
    linea = m.readline()

    ''' 1 - Determinar la cantidad de palabras de más de dos caracteres, que tienen letras (minúsculas o 
mayúsculas) en las primeras dos posiciones, y luego solo siguen caracteres que representen dígitos pares 

# en este caso la logica aplicada es que yo voy a decir que todas mis condiciones se cumplen hasta que yo 
demuestre lo contrario en este caso, al menos me sirve hacerlo con una sola bandera pero pueden hacerlo con dos
(ejemplo r1_empieza_letras=True y r1_resto_digitos_pares=True) y aplicar la misma logica de decir que se 
cumplen hasta que demuestren los contrarios, al final de la palabra ambas banderas deberian manterse prendidas
en este caso voy a usar solo una 
'''
    r1 = 0  # hace referencia a la respuesta
    r1_cont_caracteres = 0
    r1_cumple_condiciones = True

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más corta entre aquellas que 
tienen más de tres caracteres de largo.  '''
    r2 = None
    r2_cont_caracteres = 0

    ''' 3 - Determinar el porcentaje entero (respecto del total de palabras del texto) de las 
palabras que tienen más vocales que consonantes '''
    r3 = 0  # hace referencia a la respuesta
    r3_total_palabras = 0
    r3_total_cumplen = 0
    r3_cont_vocales = 0
    r3_cont_consonantes = 0

    ''' 4 - Determinar cuántas palabras incluyen la expresión "tu" (con cualquiera de sus letras en minúscula o
mayúscula) pero de tal forma que la palabra no tenga además ninguna ninguna "b" (minúscula o
mayúscula) ni ningún dígito.'''
    r4 = 0      # hace referencia a la respuesta
    r4_tiene_t = False
    r4_tiene_tu = False
    r4_tiene_b = False
    r4_tiene_digito = False

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":
            # ===================================================================
            #                       Punto 1
            # ===================================================================
            r1_cont_caracteres += 1
            # nos indica que son los dos primeros caracteres
            if r1_cont_caracteres <= 2:
                es_letra = validar_letras(i)
                # si no fuera una letra le digo que ya no cumple mis condiciones
                if not es_letra:
                    r1_cumple_condiciones = False

            # este else toma cuando el contador de caracteres fuera 3 o más, osea el resto
            else:
                es_digito_par = validar_digitos_pares(i)
                # si no fuera un digito par le digo que ya no cumple mis condiciones
                if not es_digito_par:
                    r1_cumple_condiciones = False

            # r2
            r2_cont_caracteres += 1

            # r3
            es_vocal_o_cons = validar_vocal_consonante(i)

            if es_vocal_o_cons == "VOCAL":
                r3_cont_vocales += 1
            elif es_vocal_o_cons == "CONSONANTE":
                r3_cont_consonantes += 1

            # r4
            if r4_tiene_t and i.lower() == "u":
                r4_tiene_tu = True
            elif i.lower() == "t":
                r4_tiene_t = True
            else:
                r4_tiene_t = False

            if i.lower() == "b":
                r4_tiene_b = True

            es_digito_r4 = validar_digitos(i)
            if es_digito_r4:
                r4_tiene_digito = True

        # Termino una palabra
        else:
            # r1
            if r1_cumple_condiciones and r1_cont_caracteres > 2:
                r1 += 1

            # r2
            if r2_cont_caracteres >= 3:
                if r2 is None or r2_cont_caracteres < r2:
                    r2 = r2_cont_caracteres

            # r3
            r3_total_palabras += 1
            if r3_cont_vocales > r3_cont_vocales:
                r3_total_cumplen += 1

            # r4
            if r4_tiene_tu and not r4_tiene_b and not r4_tiene_digito:
                r4 += 1

            # Apagar Banderas / Reiniciar Contadores , etc
            # r1
            r1_cont_caracteres = 0
            r1_cumple_condiciones = True

            # r2
            r2_cont_caracteres = 0

            # r3
            r3_cont_vocales = 0
            r3_cont_consonantes = 0

            # r4
            r4_tiene_t = False
            r4_tiene_tu = False
            r4_tiene_b = False
            r4_tiene_digito = False

    # Fuera del ciclo
    m.close()

    # r3
    porc = calcular_porcentaje(r3_total_cumplen, r3_total_palabras)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()