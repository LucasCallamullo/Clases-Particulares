'''
    Solo leer la tercera linea del archivo
    1) Determianr la cantidad de palabras que tiene la frase
    2) Determinar cuantas palabras empiezan con vocal
    3) Cuantas palabras tienen mas consonantes que vocales
    4) El porcentaje que reepresenta la cantidad total de vocales sobre el total de letras
        #           cant letras   --> 100
        #           cant vocales  --> X = cant vocales * 100 // cant letras

    5) Promedio de la longitud de las palabras de la frase
        # Promedio = Suma de algo // Cantidad de cosas que sumamos

    6) Cantidad de palabras que tengan la sigla consecutiva de "MP", o

    7) Cantidad de veces que aparece la tercera letra de la primera palabra en las siguiente palabras
        # ejemplo "Hola" Bola ases
'''


def calcular_promedio_r5(cont_palabras_r5, cont_letras_total_r5):
    prom = 0
    if cont_palabras_r5 > 0:
        prom = cont_letras_total_r5 // cont_palabras_r5
    return prom


# ==================================================================
#                           Respuesta 4
# ==================================================================
def calcular_porcentaje_r4(letras, vocal):
    x = 0
    if letras > 0:
        x = vocal * 100 // letras
    return x


# ==================================================================
#                           Respuesta 3
# ==================================================================
def validar_consonante(i):
    consonantes = "bcdfghjklmnpqrstvwxyzñ"
    if i.lower() in consonantes:                 # si i esta en "bcdfghjklmnpqrstvwxyzñ"
        return True
    else:
        return False


# ==================================================================
#                           Respuesta 2
# ==================================================================
def validar_vocales(i):
    # s, a, A
    i = i.lower()       # transforma a minuscula cualquier caracter
    vocales = "aeiou"
    if i in vocales:                 # si i esta en "aeiou"
        return True
    else:
        return False


def principal():

    # bandera
    primera_linea = True

    # contadores
    cont_linea = 0

    # 1
    r1_cont_palabras = 0
    es_palabra = False

    # 2
    r2_cont_palabras = 0
    indice = 0
    cumple_r2 = False

    # 3
    r3_cont_palabras = 0
    cont_vocales = 0
    cont_consonantes = 0

    # 4
    cont_vocales_total = 0
    cont_letras_total = 0

    # 5
    cont_letras_total_r5 = 0
    cont_palabras_r5 = 0

    # 6
    r6_cont_palabras = 0
    tiene_m = False
    tiene_mp = False

    # 7
    r7_cont_palabras = 0
    primera_palabra = True
    r7_caracter = None

    archivo = "archivito.txt"
    m = open(archivo, "r", encoding="utf-8")      # read

    for linea in m:

        # linea = "Primera Linea No  Va."
        # linea = "Segunda Linea No  Va."
        cont_linea += 1

        if cont_linea == 3:
            print(linea, end="")

            # analisis de cadena
            for i in linea:
            # linea = Soy responsable de mi propia  felicidad

                # podemos afirmar que estamos dentro de una palabra
                # if i not in " .!?":
                if i != " " and i != "." and i != "!" and i != "?":
                    # 1
                    es_palabra = True

                    # 2
                    indice += 1
                    es_vocal = validar_vocales(i)           # True
                    if indice == 1 and es_vocal:
                        cumple_r2 = True

                    # 3
                    es_consonante = validar_consonante(i)
                    if es_vocal:
                        cont_vocales += 1

                    if es_consonante:
                        cont_consonantes += 1

                    # 4
                    if es_vocal or es_consonante:
                        cont_letras_total += 1
                    if es_vocal:
                        cont_vocales_total += 1

                    # 5
                    cont_letras_total_r5 += 1

                    # 6
                    # empanada montaña
                    if i.lower() == "m":
                        tiene_m = True

                    elif i.lower() == "p" and tiene_m:
                        tiene_mp = True

                    else:
                        tiene_m = False

                    # 7
                    if primera_palabra and indice == 3:
                        r7_caracter = i         # "p"

                    if not primera_palabra and indice == 3 and r7_caracter == i:
                        r7_cont_palabras += 1

                # Termine de leer una palabra
                else:

                    # respuesta 1
                    if es_palabra:
                        r1_cont_palabras += 1

                    # respouesta 2
                    if cumple_r2:
                        r2_cont_palabras += 1

                    # respuesta 3
                    if cont_consonantes > cont_vocales:
                        r3_cont_palabras += 1

                    # respuesta 5
                    if es_palabra:
                        cont_palabras_r5 += 1

                    # respuesta 6
                    if tiene_mp:
                        r6_cont_palabras += 1

                    # respuesta 7
                    if es_palabra:
                        primera_palabra = False

                    # apagar banderas / contadores / acumuladores lo que sea
                    # 1
                    es_palabra = False

                    # 2
                    cumple_r2 = False
                    indice = 0

                    # 3
                    cont_consonantes = 0
                    cont_vocales = 0

                    # 6
                    tiene_m = False
                    tiene_mp = False

    # Salimos del ciclo for
    # Repuesta 4
    porc = calcular_porcentaje_r4(cont_letras_total, cont_vocales_total)

    # Respuesta 5
    prom = calcular_promedio_r5(cont_palabras_r5, cont_letras_total_r5)

    # ==================================================================
    #                           Respuesta
    # ==================================================================
    print()
    # con ctrl + d copias la linea en la que esta el cursor
    print("La cantidad de palabras es r1:", r1_cont_palabras)
    print("La cantidad de palabras es r2:", r2_cont_palabras)
    print("La cantidad de palabras es r3:", r3_cont_palabras)

    # print("letras:", cont_letras_total, "vocales:", cont_vocales_total)
    print("El porcentaje de r4:", porc)
    print("El promedio de r5:", prom)
    print("La cantidad de palabras que tienen MP de r6:", r6_cont_palabras)

    print("La cantidad de palabras de r7:", r7_cont_palabras)


if __name__ == '__main__':
    principal()
