


def es_vocal(car):
    return car.lower() in "aeiou"   # return True or False


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

    # indice    12340123450
    # cadena = "Hola Mundo."

    # cantidad de palabras que tengan una vocal en la segunda posicion.
    r1 = 0
    indice = 0
    r1_tiene_vocal_pos2 = False     # esta bandera es la que cumple la condicion de tus palabras


    for car in cadena:

        # car = H, o, l, a,  , M

        # estas fuera de la palabra/ termino una palabra
        if car in " .":

            # Punto 1
            if r1_tiene_vocal_pos2:     # si tiene_vocal esta True
                r1 += 1

            # resetear banderas / contadores
            indice = 0
            r1_tiene_vocal_pos2 = False

        # estas dentro de la palabra
        else:

            # punto 1
            indice += 1

            if indice == 2 and validar_vocales(car):         # es_vocal == True
                r1_tiene_vocal_pos2 = True

    print("Primer resultado:", r1)
    # print("Segundo resultado:", r2)
    # print("Tercer resultado:", r3)
    # print("Cuarto resultado:", r4)


if __name__ == "__main__":
    principal()



