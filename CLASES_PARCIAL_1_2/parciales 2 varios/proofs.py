


def validar_vocales(letra):
    if letra.lower() in "aeiou":
        return True

    return False

def validar_cons(i):
    if i.lower() in "bcdfghjklmnñopqrstvwxyz":
        return True
    return False


def validar_dig(i):
    if i in "0123456789":
        return True
    return False

def principal():
    m = open('entrada.txt', 'r')
    cadena = m.readline()  # str --> "Hola mundo."
    m.close()

    #               12012345678012012
    # 1. Determinar la cantidad de palabras que tienen una "x" en la segunda posición.
    r1 = 0              # tu contador de palabras que cumplen la condición
    indice = 0          # la posición
    tiene_x_pos2 = False    # si esta la x en la posición

    # 1.2. Determinar la cantidad de palabras que tienen una consonante en la tercera o en
    # la cuarta posición y además tienen dos o más dígito en cualquier parte.
    r1 = 0
    indice_2 = 0
    consonante_34 = False
    digito = 0

    # 1.3. Determinar la cantidad de palabras que comienzan con mayúscula y
    # tienen un dígito impar en la cuarta posición.
    r1 = 0
    cant_may = False
    dig_4 = False
    indice_3 = 0

    #    123456789 0120
    # 2.1 Determinar la longitud de la palabra más larga del texto.
    r2 = None       # la longitud de la palabra

    # 2.2 Determinar la longitud de la palabra más corta entre las que comienzan
    # con "s" (minúscula o mayúscula), no contenga ninguna "p" en ninguna parte.
    r2 = None
    com_s = False
    tiene_p = False


    # 2.3 Determinar la longitud de la palabra más larga entre las que terminen en vocal.
    r2 = None
    ult_car = ""



    for i in cadena:
        # i = H, o, l, a, .

        # dentro de una palabra
        if i != " " and i != ".":

            # punto 1
            indice += 1

            if i.lower() == "x" and indice == 2:
                tiene_x_pos2 = True

            # punto1.2
            indice_2 += 1

            es_cons = validar_cons(i)
            if es_cons and (indice_2 == 3 or indice_2 == 4):
                consonante_34 = True

            haydig = validar_dig(i)
            if haydig:
                digito += 1

             # punto 1.3
            indice_3 += 1

            if i in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" and indice_3 == 1:
                cant_may = True

            if i in "13579" and indice_3 == 4:
                dig_4 = True

            # Punto 2
            # ya usamos el indice del primero

            #punto 2.2
            if i.lower() == "s" and indice == 1:
                com_s = True

            if i.lower() == "p":
                tiene_p = True


            # PUNTO 2.3
            ult_car = i



        # fuera dela palabra
        else:
            # punto 1
            if tiene_x_pos2:
                r1 += 1

            # punto 1.2
            if consonante_34 and digito >= 2:
                r1 += 1

            # punto 1.3
            if cant_may and dig_4:
                r1 += 1

            # Punto 2
            # busca la longitud más larga
            if r2 is None or indice > r2:
                r2 = indice


            # punto 2.2
            if com_s and not tiene_p:
                if r2 is None or indice < r2:
                    r2 = indice

            # punto 2.3

            # longitud mas larga que termina en vocal
            # ult_car
            # if ult_car.lower() in "aeiou":
            if validar_vocales(ult_car):
                if r2 is None or indice < r2:
                    r2 = indice


            # reiniciar contadores y/o banderas

            # punto 1
            indice = 0
            tiene_x_pos2 = False
            # punto 1.2
            indice_2 = 0
            consonante_34 = False
            digito = 0
            # punto 1.3
            cant_may = False
            dig_4 = False
            indice_3 = 0
            #punto 2.2
            com_s = False

    print("Primer resultado:", r1)
    # print("Segundo resultado:", r2)
    # print("Tercer resultado:", r3)
    # print("Cuarto resultado:", r4)


if __name__ == "__main__":
    principal()