

'''
    # Dado el archivo.txt se desea analizar la cadena de la tercera linea del archivo

    1) Cantidad palabras de la frase    ( corrobar que no hay dos espacios en blanco )
    2) Verificar cuantas palabras empiezan con Vocal ( minus o mayus )
    3) Contar la cantidad de palabras que tienen mas vocales que consonantes
        # r3_contador_palabras cumplen
        # cont_vocales_por_palabra = 0
        # cont_consonantes_por_palabra = 0

    4) Determinar cuántas palabras incluyen la expresión “pa” (con cualquiera de sus letras
    enminúscula o en maúscula) pero no contienen al mismo tiempo una “t”. Por ejemplo, en el
    texto: “La patada hizo que el tiro raspara el palo.” Hay dos palabras que cumplen: “raspara”
     y “palo”. La palabra “patada” no cuenta porque si bien tiene “pa”, incluye también una
     “t”.Criterios generales de evaluación.
        #
            r4_contador = 0
            tiene_p = False
            tiene_pa = False
            tiene_t = False

    5) 3.Determinar cuántas palabras empiezan y terminan con el mismo caracter (si es letra, en
    minúscula o en mayúscula en forma indistinta). Por ejemplo, en el texto “Sabes que ese oso
    es pardo y malo.” Hay 4palabras que cumplen: “Sabes”, “ese”, “oso”, “y”. Notar que la palabra
    “y” solo contiene un carácter, pero cumple en forma trivial con la condición.
        #
            r5_contador_cumplan = 0
            indice = 0
            primera_letra = None
            ultima_letra = None

    6)  2.Determinar el promedioenterode caracteres por palabra, de las palabras que tienen una o
    más veces una ‘s’ o una o más veces una ‘n’ o una o más veces una ‘p’ (minúsculas o mayúsculas).
     Por ejemplo, en el texto: “La pelota sirve apenas.” hay tres palabras que cumplen el criterio
     (“pelota”, “sirve”, “apenas”). Entre las tres suman 17 caracteres, por lo que el promedio enteropedido
      es 5 caracteres por palabra.
        # promedioenterode = Suma de cosas // la cantidad de cosas que sumaste
        #
            tiene_nsp = False
            r5_long_palabra = 0
            r5_cont_prom = 0
            r5_acum_prom = 0






'''


#r6
def calcular_promedio(r5_cont_prom, r5_acum_prom):
    prom = 0
    if r5_cont_prom > 0:
        prom = r5_acum_prom // r5_cont_prom
    return prom


# r2
def validar_consonantes(i):
    consonantes = "bcdfghijklmnpqrstvwxyzñ"
    i = i.lower()  # aca lo hice minuscula
    if i in consonantes:  # aca compara a la i, con las letras de la cadena consonantes
        return True  # si esta dentro de la cadena devuelve True ( o sea es consonantes )
    else:
        return False  # si no esta dentro de la cadena devuelve False ( o sea no es consonantes )


# r1
def validar_vocales(i):
    i = i.lower()           # aca lo hice minuscula
    vocales = "aeiou"       # declare una cadena
    if i in vocales:        # aca compara a la i, con las letras de la cadena vocales
        return True         # si esta dentro de la cadena devuelve True ( o sea es vocal )
    else:
        return False        # si no esta dentro de la cadena devuelve False ( o sea no es vocal )


def main():
    # Como abrir el archivo
    archivo = "archivo.txt"
    m = open(archivo, "r")          # r = read = leer el archivo

    # Como evitar la segunda linea o más
    cont_lineas = 0

    # r1
    r1_cont_palabras = 0
    es_palabra = False

    # r2
    r2_cont_palabras = 0
    indice = 0

    # r3
    r3_contador_palabras_cumplen = 0
    cont_vocales_por_palabra = 0
    cont_consonantes_por_palabra = 0

    # r4
    r4_contador = 0
    tiene_p = False
    tiene_pa = False
    tiene_t = False

    # r5
    r5_contador_cumplan = 0
    # indice = 0
    primera_letra = None
    ultima_letra = None

    # r6
    tiene_nsp = False
    r6_long_palabra = 0
    r6_cont_prom = 0
    r6_acum_prom = 0


    for linea in m:
        cont_lineas += 1

        if cont_lineas > 2:

            linea = "Sabes Que ese Oso y pardo malo."

            for i in linea:
                # Que estamos dentro de una palabra
                if i != " " and i != ".":

                    # r1
                    es_palabra = True

                    # r2
                    # 1234567890120123450
                    # Empanadas de carne.
                    indice += 1

                    # if i.lower() in "aeiou" and indice == 1:
                    #    r2_cont_palabras += 1
                    es_vocal = validar_vocales(i)       # return True o False segun corresponda
                    if es_vocal and indice == 1:
                        r2_cont_palabras += 1

                    # r3
                    es_vocal = validar_vocales(i)       # return True o False segun corresponda
                    if es_vocal:
                        cont_vocales_por_palabra += 1

                    es_consonante = validar_consonantes(i)  # return True o False segun corresponda
                    if es_consonante:
                        cont_consonantes_por_palabra += 1

                    # r4
                    # raspar aprat
                    if i.lower() == "t":
                        tiene_t = True

                    if i.lower() == "p":
                        tiene_p = True

                    elif i.lower() == "a" and tiene_p:
                        tiene_pa = True

                    else:
                        tiene_p = False

                    # r5
                    # oso de
                    if indice == 1:
                        primera_letra = i.lower()   # que se guarde en minuscula
                        ultima_letra = i.lower()
                    else:
                        ultima_letra = i.lower()

                    # r6
                    r6_long_palabra += 1
                    if i.lower() in "nsp":
                        tiene_nsp = True



                # Aca termino una palabra
                else:
                    # r1
                    if es_palabra:
                        r1_cont_palabras += 1

                    # r3
                    if cont_vocales_por_palabra > cont_consonantes_por_palabra:
                        r3_contador_palabras_cumplen += 1

                    # r4
                    if tiene_pa and not tiene_t:        # not tiene_t, py lo lee como un False
                        r4_contador += 1

                    # r5
                    if primera_letra == ultima_letra and es_palabra:
                        r5_contador_cumplan += 1

                    # r6
                    if tiene_nsp:
                        # pelota
                        r6_cont_prom += 1                   # suma 1 palabra cumple
                        r6_acum_prom += r6_long_palabra     # suma seis letras



                    # Apagues las banderas, reiniciar contadores, indices etc
                    # r1
                    es_palabra = False

                    # r2
                    indice = 0

                    # r3
                    cont_vocales_por_palabra = 0
                    cont_consonantes_por_palabra = 0

                    # r4
                    tiene_pa = False
                    tiene_p = False
                    tiene_t = False

                    # r5
                    primera_letra = None
                    ultima_letra = None

                    # r6
                    tiene_nsp = False
                    r6_long_palabra = 0

    m.close()

    # Resultados ..
    print("La cantidad de palabras r1:", r1_cont_palabras)
    print("La cantidad de palabras r2:", r2_cont_palabras)
    print("La cantidad de palabras r3:", r3_contador_palabras_cumplen)
    print("La cantidad de palabras r4:", r4_contador)
    print("La cantidad de palabras r5:", r5_contador_cumplan)

    prom_r6 = calcular_promedio(r6_cont_prom, r6_acum_prom)

    print("La cantidad de palabras r6:", prom_r6)


if __name__ == '__main__':
    main()