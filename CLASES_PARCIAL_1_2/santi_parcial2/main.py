


def es_vocal(car):
    return car.lower() in "aeiou"   # return True or False


def es_digito(ult_car):
    return "0" <= ult_car <= "9"     # return True or False


def es_mayuscula(car):
    return "A" <= car <= "Z"     # return True or False   no incluye ñ


def es_minuscula(car):
    return "a" <= car <= "z"     # return True or False   no incluye ñ


def es_consonante(car):
    return car.lower() in "qwrtypsdfghjklñzxcvbnm"  # return True or False   no incluye ñ


def validar_vocales(car):
    # retorna True si es vocal, False si no lo es
    if car.lower() in "aeiou":
        return True
    else:
        return False


def principal():

    m = open("entrada.txt")     #
    cadena = m.read()       # m.read()
    m.close()

    # 1. Determinar la cantidad de palabras que terminan con un dígito pero no tienen ninguna mayúscula.
    r1 = 0      # cantidad de palabras que cumplan
    ult_car = ""
    r1_tiene_mayus = False

    # 2. Determinar la longitud de la palabra más larga entre aquellas que tienen un solo dígito impar,
    # y la longitud sea par.
    r2 = None       # r2 hace referencia a la longitud mas larga
    indice = 0
    r2_cont_digito_impares = 0

    # 3. Determinar el promedio entero caracteres por palabra entre las palabras que tengan todas letras minusculas
    # pero tienen por lo menos tres consonantes.

    # promedio = sumatoria de caracteres / cantidad de palabras que sumaste
    r3 = 0      # promedio
    r3_acum_carac = 0       # += indice
    r3_cant_palabras = 0    # += 1

    r3_todas_minus = True
    r3_cont_cons = 0


    for car in cadena:

        # estas fuera de la palabra/ termino una palabra
        if car in " .":

            # Punto 1
            if es_digito(ult_car) and not r1_tiene_mayus:   # r1_tiene_mayus is False
                r1 += 1

            # Punto 2
            # tienen un solo dígito impar y la longitud (indice) sea par.
            if r2_cont_digito_impares == 1 and indice % 2 == 0:
                # la longitud de la palabra más larga
                if r2 is None or r2 < indice:
                    r2 = indice     # r2 = 8

            # Punto 3
            if r3_cont_cons >= 3 and r3_todas_minus:    # r3_todas_minus  == True
                r3_acum_carac += indice
                r3_cant_palabras += 1

            # resetear banderas / contadores

            # Punto 1
            ult_car = ""
            r1_tiene_mayus = False
            # Punto 2
            indice = 0
            r2_cont_digito_impares = 0
            # Punto 3
            r3_todas_minus = True
            r3_cont_cons = 0


        # estas dentro de la palabra
        else:

            # Punto 1
            ult_car = car

            if es_mayuscula(car):
                r1_tiene_mayus = True

            # Punto 2
            indice += 1
            if car in "13579":     # para saber si es un digito impar
                r2_cont_digito_impares += 1

            # Punto 3
            if not es_minuscula(car):       # return False
                r3_todas_minus = False

            if es_consonante(car):
                r3_cont_cons += 1

    #
    # calcular promedio
    prom = 0
    if r3_cant_palabras != 0:
        prom = r3_acum_carac // r3_cant_palabras
    r3 = prom

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    # print("Cuarto resultado:", r4)


if __name__ == "__main__":
    principal()



