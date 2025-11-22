


def validar_vocal(letra):
    if letra.lower() in "aeiou":
        return True
    return False


def validar_cons(i):
    # if "a" <= i <= "z":
    if i in "qwrtypsdfghjklñzxcvbnm":
        return True
    return False


# r1
def validar_digito(i):
    # return i in "0123456789"    # return True o False
    if i in "0123456789":
        return True
    return False


def validar_digito_impar(i):
    if i in "13579":
        return True
    return False


def validar_mayus(i):
    # if "A" <= i <= "Z":
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return True
    return False


def principal():


    m = open("entrada.txt", "rt")
    linea = m.readline()
    m.close()

    """ 
        1234
    1 - Determinar la cantidad de palabras que tienen un dígito en la segunda y en la cuarta posición, 
    pero de tal forma que el resto de sus caracteres son letras mayúsculas.
    """
    r1 = 0  # respuesta
    r1_indice = 0
    r1_cont_digitos_pos2_pos4 = 0
    r1_todas_mayus = True

    """ 
    1-b Determinar la cantidad de palabras que tienen un dígito en la primera posicion y todas las demas son
    consonantes
    """
    r1_indice = 0
    r1_tiene_digito_pos1 = 0
    r1_todas_cons = True

    #   Determinar
    """1- Determinar la cantidad de palabras que tienen ultima letra sea una vocal y ademas 
    sea igual a la primera """

    primera = ""
    ultima = ""

    """ 
    #                 12345678  
    2 - determinar la longitud de la palabra mas corta y que sea impar que empiece con vocal
    """
    r2 = None       # determinar el menor
    r2_empieza_vocal = False

    # smalltalk poo    , haskell pf    prolog p funcional

    """
    4 - Determinar cuántas palabras incluyen la expresión "d+vocal" (con cualquiera de sus letras en minúscula o
    mayúscula) pero de tal forma que a su vez no comiencen con la expresión "d+vocal".
    """
    r4 = 0
    r4_tiene_d = False
    r4_tiene_d_vocal = False
    r4_empieza_d_vocal = False


    """ 
    4 - b) Determinar cuántas palabras incluyen la expresión de dos mayusculas seguidas al menos dos veces
    y aparezca antes de la letra "p"
    """
    r4_tiene_una_mayus = False
    r4_cont_dos_mayus = 0
    # r4_tiene_dos_mayus = False

    r4_tiene_p = False



    for i in linea:

        # dentro de la palabra
        if i != " " and i != ".":

            r1_indice += 1

            if r1_indice == 2 or r1_indice == 4:
                es_digito = validar_digito(i)   # return True o False
                if es_digito:
                    r1_cont_digitos_pos2_pos4 += 1

            # if r1_indice != 2 and r1_indice != 4:
            else:
                es_mayus = validar_mayus(i)
                if not es_mayus:
                    r1_todas_mayus = False

            es_digito = validar_digito(i)
            if es_digito and r1_indice == 1:
                r1_tiene_digito_pos1 = True

            else:
                es_cons = validar_cons(i)
                if not es_cons:
                    r1_todas_cons = False

            # ultima letra guardarla
            if r1_indice == 1:
                primera = i

            ultima = i

            # r2
            if r1_indice == 1 and validar_vocal(i):
                r2_empieza_vocal = True

            # r4
            # 12
            # dios

            if validar_vocal(i) and r4_tiene_d:
                r4_tiene_d_vocal = True
                r4_tiene_d = False

                if r1_indice == 2:
                    r4_empieza_d_vocal = True

            elif i.lower() == "d":
                r4_tiene_d = True

            else:
                r4_tiene_d = False

            #
            # r4 mayusculas
            if i.lower() == "p":
                r4_tiene_p = True


            # DSS

            if validar_mayus(i) and r4_tiene_una_mayus and not r4_tiene_p:
                r4_cont_dos_mayus += 1      # 2

            elif validar_mayus(i):
                r4_tiene_una_mayus = True

            else:
                r4_tiene_una_mayus = False



        #
        # fuera de la palabra
        else:

            if r1_todas_mayus and r1_cont_digitos_pos2_pos4 == 2:
                r1 += 1

            if validar_vocal(ultima) and ultima.lower() == primera.lower():
                pass


            # r2
            if r2_empieza_vocal and r1_indice % 2 != 0:
                if r2 is None or r2 < r1_indice:
                    r2 = r1_indice

            # r4
            if r4_tiene_d_vocal and not r4_empieza_d_vocal:
                r4 += 1

            # r4 -b
            if r4_cont_dos_mayus >= 2:
                pass

            # reiniciar las banderas / contadores
            r1_indice = 0
            r1_cont_digitos_pos2_pos4 = 0
            r1_todas_mayus = True

            primera = ""
            ultima = ""

            # r4
            r4_tiene_d = False
            r4_tiene_d_vocal = False
            r4_empieza_d_vocal = False

            # r4
            r4_tiene_una_mayus = False
            r4_cont_dos_mayus = 0
            r4_tiene_p = False


    print("Primer resultado:", r1)
    # print("Segundo resultado:", r2)
    # print("Tercer resultado:", r3)
    # print("Cuarto resultado:", r4)





if __name__ == '__main__':
    principal()

