

# r8
def calcular_porcentaje(vocales, letras):
    #   cant_ letras --- 100%
    #   cant_ vocales --- X = cant_vocales * 100 // cant_letras
    porc = 0
    if letras > 0:
        porc = vocales * 100 // letras
    return porc


def validar_letra(caracter):
    if "a" <= caracter.lower() <= "z":
        return True
    return False


# r7
def validar_digito(i):
    if "0" <= i <= "9":
        return True
    else:
        return False


# r6
def validar_consonantes(i):
    consonantes = "bcdfghjklmnpqrstvxywz"
    if i.lower() in consonantes:
        return True
    else:
        return False


def validar_vocales(i):
    if i.lower() in "aeiou":  # i.upper() a -> A
        return True
    return False


def main():
    # esta era la linea original = Hay muchas vocales en este escrito.
    archivo = "archivito.txt"
    m = open(archivo, "rt")  # read text     # leer texto

    '''
    1. Determinar la cantidad de palabras que tienen cuatro o más caracteres e incluyen tres o más
    vocales
    '''
    r1_cont_palabras_cumplen = 0
    cont_letras = 0
    cont_vocales = 0

    '''
    2. Determinar el promedio entero de caracteres por palabra, de las palabras que tienen una o
más veces una ‘s’ o una o más veces una ‘n’ o una o más veces una ‘p’ (minúsculas o
mayúsculas)
    # Promedio = (nota1 + nota2 + nota3) / 3
    # promedio = Una sumatoria de cosas / cantidad de cosas que sumamos
    '''
    cont_caracteres = 0
    acum_caracteres_palabras_cumplen_r2 = 0
    cant_palabras_cumple_r2 = 0
    tiene_nsp = False

    '''
    3. Determinar cuántas palabras empiezan y terminan con el mismo caracter (si es letra, en
minúscula o en mayúscula en forma indistinta).
    # 1234012345
    # hola mundo
    '''
    r3_palabras_cumplen = 0
    indice = 0
    primer_letra = None
    ult_letra = None

    ''' 
    4.Determinar cuántas palabras incluyen la expresión “pa”(con cualquiera de sus letras
enminúscula o en maúscula) pero no contienen al mismo tiempo una “t”.
    '''
    r4 = 0          # Cuantas palabras cumplen
    r4_tiene_p = False
    r4_tiene_pa = False
    r4_tiene_t = False


    '''
        5 -Otro caso: cantidad de palabras que hay en la linea analizada
    '''
    r5_cant_palabras = 0
    es_palabra = False

    '''
        6 - Caso: determinar la palabra de menor longitud que tenga mas vocales que consonantes
    '''
    r6 = None             # r6 hace referencia a la menor longitud que encontremos
    r6_cont_caracteres = 0
    r6_cont_vocales = 0
    r6_cont_consonantes = 0

    '''
        7 - Determinar cuantas digitos(numeros) habian en la palabras que su tercera letra era la letra "Z" y
        no tenian consonantes
    '''
    r7 = 0      # acumulador de la cantidad de digitos en las palabras que cumplan
    r7_indice = 0
    r7_tiene_Z = False
    r7_tiene_consonantes = False
    r7_cont_digitos = 0


    '''
        8 - Determinar el porcentaje entero(truncado) de vocales minusculas sobre el total de letras 
        (no incluye digitos u otros simbolos)
         #   cant_ letras --- 100% 
         #   cant_ vocales --- X = cant_vocales * 100 // cant_letras
    '''
    r8 = 0      # hace referencia al porcentaje
    r8_cant_letras = 0
    r8_cant_vocales = 0

    contador_lineas = 0

    for linea in m:

        # si me pidieran evitar 1, 2 o más lineas del archivo
        contador_lineas += 1
        if contador_lineas >= 3:

            # linea = La pelota sirve apenas.
            for i in linea:
                # i = H, a, y,  , m,

                # estamos en una palabra
                if i != " " and i != ".":

                    indice += 1
                    # punto 1
                    cont_letras += 1

                    es_vocal = validar_vocales(i)           # True si es vocal, False si no es vocal
                    if es_vocal:
                        cont_vocales += 1

                    # Punto 2
                    cont_caracteres += 1
                    if i.lower() in "nsp":
                        tiene_nsp = True

                    # Punto 3
                    if indice == 1:
                        primer_letra = i.lower()
                        ult_letra = i.lower()
                    # este else nos dice cuando el indice sea distinto de 1
                    else:
                        ult_letra = i.lower()

                    # Punto 5
                    es_palabra = True

                    # Punto 4
                    if i.lower() == "p":
                        r4_tiene_p = True
                    elif r4_tiene_p and i.lower() == "a":
                        r4_tiene_pa = True
                    else:
                        r4_tiene_p = False

                    if i.lower() == "t":
                        r4_tiene_t = True

                    # Punto 6
                    # Hola dsa
                    r6_cont_caracteres += 1
                    r6_es_vocal = validar_vocales(i)            # tiene True si es vocal y tiene False si no lo es
                    if r6_es_vocal:
                        r6_cont_vocales += 1

                    r6_es_consonante = validar_consonantes(i)
                    if r6_es_consonante:
                        r6_cont_consonantes += 1

                    # Punto 7
                    r7_indice += 1
                    if r7_indice == 3 and i == "Z":
                        r7_tiene_Z = True

                    r7_es_consonante = validar_consonantes(i)
                    if r7_es_consonante and r7_indice != 3:
                        r7_tiene_consonantes = True

                    r7_es_digito = validar_digito(i)
                    if r7_es_digito:
                        r7_cont_digitos += 1

                    # Punto 8
                    r8_es_letra = validar_letra(i)
                    r8_es_vocal = validar_vocales(i)
                    if r8_es_letra:
                        r8_cant_letras += 1

                    if r8_es_vocal:
                        r8_cant_vocales += 1


                # termine una palabra
                else:
                    # punto 1
                    if cont_letras >= 4 and cont_vocales >= 3:
                        r1_cont_palabras_cumplen += 1

                    # Punto 2
                    if tiene_nsp:
                        cant_palabras_cumple_r2 += 1
                        acum_caracteres_palabras_cumplen_r2 += cont_caracteres

                    # Punto 3
                    if primer_letra == ult_letra and es_palabra:
                        r3_palabras_cumplen += 1

                    # Punto 4
                    if r4_tiene_pa and not r4_tiene_t:
                        r4 += 1

                    # Punto 5
                    if es_palabra:
                        r5_cant_palabras += 1

                    # punto 6
                    if r6_cont_vocales > r6_cont_consonantes:
                        if r6 is None or r6_cont_caracteres < r6:
                            r6 = r6_cont_caracteres

                    # Punto 7
                    if r7_tiene_Z and not r7_tiene_consonantes:
                        r7 += r7_cont_digitos

                    # APAGAR BANDERAS, CONTADORES, INDICES; ETC
                    # punto 1
                    cont_vocales = 0
                    cont_letras = 0

                    # punto 2
                    cont_caracteres = 0
                    tiene_nsp = False

                    # Punto 3
                    indice = 0
                    primer_letra = None
                    ult_letra = None

                    # Punto 4
                    r4_tiene_p = False
                    r4_tiene_pa = False
                    r4_tiene_t = False

                    # Punto 5
                    es_palabra = False

                    # Punto 6
                    r6_cont_caracteres = 0
                    r6_cont_vocales = 0
                    r6_cont_consonantes = 0

                    # Punto 7
                    r7_indice = 0
                    r7_tiene_Z = False
                    r7_tiene_consonantes = False
                    r7_cont_digitos = 0


    # Todos los resultados fuera del ciclo for
    r8 = calcular_porcentaje(r8_cant_vocales, r8_cant_letras)

    # punto1
    print("Resultados 1:", r1_cont_palabras_cumplen)

    # punto 2
    prom = 0
    if cant_palabras_cumple_r2 > 0:
        prom = acum_caracteres_palabras_cumplen_r2 // cant_palabras_cumple_r2
    print("Resultados 2:", prom)

    # Punto 3
    print("Resultados 3:", r3_palabras_cumplen)

    # Punt4
    print("Resultados r4:", r4)

    # Punto 5
    print("Resultados Cantidad de palabras en el archivo:", r5_cant_palabras)

    # punto 6
    print("Resultados r6:", r6)

    # Punto 7
    print("Resultados r7: ", r7)

    # Punto 8
    print("Resultados r8: ", r8)





if __name__ == '__main__':
    main()
