# función para determinar si un caracter es un digito.
def es_digito(car):
    return "0" <= car <= "9"


# función para determinar si un caracter es una vocal.
def es_vocal(car):
    return car in "aeiouáéíóúAEIOUÁÉÍÓÚ"


# función para determinar si un caracter es una consonante...
def es_consonante(car):
    return car.lower() in "bcdfghjklmnñpqrstvwxyz"


# función para calcular el promedio entero entre sus parámetros...
def calcular_promedio(a, c):
    promedio = 0
    if c > 0:
        promedio = a // c
    return promedio


# función principal del programa.
def principal():
    # inicialización de variables de resultados..
    r1 = r3 = r4 = 0
    r2 = None

    # contador de letras en una palabra...
    cl = 0

    # item 1: variable para el caracter anterior...
    ant = " "

    # item 2: flag de inclusión de digito par y flag de mayuscula...
    sdp, smy = False, False

    # item 3: acumuladores, contadores y flags para r3...
    acr3, cpr3, sr3 = 0, 0, False

    # item 4: flags para m, mo y digito...
    sm, smo, sd = False, False, False

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # texto = "Saben que vienen muchos y penan y gritan por ello."
    # texto = "Las piezas X2a7jpRq y ca97 pueden usarse en lugar de c5d4V7g o K55td."
    # texto = "Pararon todos los profesores de arranque y luego saltaron."
    # texto = "Amo el movimiento del mar en el sector fMo45 y Momo que es mio."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if cl > 0:
                # item 1...
                if ant in "nN" and cl <= 5:
                    r1 += 1

                # item 2...
                if sdp and smy:
                    if r2 is None or cl < r2:
                        r2 = cl

                # item 3...
                if sr3:
                    cpr3 += 1
                    acr3 += cl

                # item 4...
                if smo and not sd:
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            cl = 0

            # item 1...
            ant = " "

            # item 2...
            sdp, smy = False, False

            # item 3...
            sr3 = False

            # item 4...
            sm, smo, sd = False, False, False

        else:
            # caracter dentro de la palabra... contarlo...
            cl += 1

            # item 1...
            ant = car

            # item 2...
            if es_digito(car) and int(car) % 2 == 0:
                sdp = True
            elif car.isupper():
                smy = True

            # item 3...
            if car in "rR" and cl <= 3:
                sr3 = True

            # item 4...
            if car in "mM":
                sm = True
            else:
                if sm and car in "oóOÓ":
                    smo = True
                sm = False

            if es_digito(car):
                sd = True

    # cálculo del porcentaje para r3...
    r3 = calcular_promedio(acr3, cpr3)

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()
