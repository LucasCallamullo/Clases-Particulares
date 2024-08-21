def es_dig(i):
    if "0" <= i <= "9":
        return True
    else:
        return False


def validar_mayusc(i):
    if i in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
        return True
    else:
        return False


def es_vocal(i):
    if i in "AEIOaeioáéíóÁÉÍÓ":
        return True
    else:
        return False




def principal():
    m = open("entrada.txt")
    linea = m.read()
    m.close()

    # inicializacion
    r1 = 0

    # r1
    '''Determinar la cantidad de palabras que tienen un dígito en la segunda y en la cuarta posición, pero de tal 
    forma que el resto de sus caracteres son letras mayúsculas.'''
    r1_cant_car = 0
    dig_2_pos = dig_4_pos = False
    cont_mayus = 0

    # r2

    '''Determinar la longitud (en cantidad de caracteres) de la palabra más corta entre aquellas que comienzan 
    con una "t" (minúscula o mayúscula)'''
    r2 = 0
    r2_cant_car = 0
    tiene_t, mas_corta_t = False, 0 # el 0 -->cant de letras de la palabra mas corta


    #r3
    '''Determinar cuántas palabras están conformadas solo por vocales (minúsculas o mayúsculas), pero no
    contienen ninguna "u" (minúscula o mayúscula).'''
    r3 = 0
    r3_cont_car = 0
    cont_vocales =0

    #r4
    '''Determinar cuántas palabras incluyen la expresión "di" (con cualquiera de sus letras en minúscula o 
    mayúscula) pero de tal forma que a su vez no comiencen con la expresión "di".'''
    r4 = 0
    r4_cont_car = 0
    tiene_d = tiene_di = empieza_di = False




    for i in linea: #i es cada letra

        if i != " " and i != ".":  # dentro de la palabra
            #r1
            r1_cant_car += 1
            if r1_cant_car == 2 and es_dig(i):
                dig_2_pos = True
            if r1_cant_car == 4 and es_dig(i):
                dig_4_pos = True
            if validar_mayusc(i):
                cont_mayus += 1

            #r2
            r2_cant_car += 1
            if r2_cant_car == 1 and i in "tT":
                tiene_t = True

            #r3
            r3_cont_car += 1
            if es_vocal(i):
                cont_vocales += 1

            #r4
            r4_cont_car += 1
            if tiene_d and i.lower() == "i":
                tiene_di = True
                if r4_cont_car == 2:
                    empieza_di = True
                ultima_pos = r4_cont_car
            elif i.lower() == "d":
                tiene_d = True
            else:
                tiene_d = False


        else:  # fuera de la palabra
            #r1
            if dig_4_pos and dig_2_pos and (r1_cant_car - cont_mayus == 2):
                r1 += 1


            #r2
            if tiene_t:
                if r2 == 0: #no conto ninguna palabra antes, no procese ninnguna palabra
                    r2 = r2_cant_car #si no twnfo ninguna pal, agarro la cant de letras q tiene en ese momento el r2_cant_car
                else:
                    if r2_cant_car < r2:
                        r2 = r2_cant_car

            #r3
            if r3_cont_car == cont_vocales:
                r3 += 1

            #r4
            if tiene_di and empieza_di is False:
                r4 += 1


            # reiniciar
            # r1
            r1_cant_car = 0
            dig_2_pos = dig_4_pos = False
            cont_mayus = 0

            #r2
            r2_cant_car = 0
            tiene_t = False

            #r3
            r3_cont_car = 0
            cont_vocales = 0

            #r4
            r4_cont_car = 0
            tiene_d = tiene_di = empieza_di = False


    # fuera del for
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()
