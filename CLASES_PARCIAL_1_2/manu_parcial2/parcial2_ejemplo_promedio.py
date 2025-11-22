


def validar_vocales(caracter):
    if caracter.lower() in "aeiou":
        return True
    return False


def validar_consonantes(caracter):
    if caracter.lower() in "qwrtypsdfghjklñzxcvbnm":
        return True
    return False


def principal():

    m = open("archivo.txt", "rt")
    linea = m.readline()
    m.close()

    """ 
    #    1221
    #      0
    1- ) el promedio de caracteres de las palabras que contengan mas consonantes que vocales.
    
    promedio = sumatoria de los caracteres de las palabras que cumplan // cantidad de veces que sume o acumule
    """
    r1 = 0
    r1_acum_car = 0
    r1_cont_car = 0

    indice = 0
    r1_cont_cons = 0
    r1_cont_vocales = 0

    for caracter in linea:

        # dentro de la palabra
        if caracter != " " and caracter != ".":

            # verificar condiciones que nos pida palabra
            indice += 1

            # si una variable esta igualada a una funcion es porque espera algun retorno
            es_cons = validar_consonantes(caracter)     # return True or False

            if es_cons is True:         # if es_cons
                r1_cont_cons += 1

            es_vocal = validar_vocales(caracter)    # return True or False
            if es_vocal is True:        # if es_vocal
                r1_cont_vocales += 1

        # fuera de la palabra
        else:
            # 12344
            # Hola a todos mundo.
            # indice = 4
            # cont_vocales = 2
            # cont_cons = 2
            if r1_cont_cons > r1_cont_vocales:
                r1_acum_car += indice
                r1_cont_car += 1

            #
            # reiniciar contadores
            indice = 0
            r1_cont_cons = 0
            r1_cont_vocales = 0

    # fuera del ciclo for
    if r1_cont_car > 0:
        r1 = r1_acum_car // r1_cont_car

    print("promedio r1:", r1)



if __name__ == '__main__':
    principal()




