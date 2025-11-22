




def es_consonante(caracter):
    if caracter.lower() in "qwrtypsdfghjklñzxcvbnm":
        return True

    return False



def es_vocal(caracter):     # H - > h
    # pasamos los parametros necesarios para que trabaje nuestra funcion como tal

    # .lower() transforma una mayuscula a miniscula
    if caracter.lower() in "aeiou":
        return True

    return False


def principal():

    # contador de vocales
    cont_vocales = 0

    # contador consonantes
    cont_consonantes = 0

    cadena = "Hola mundo."

    for caracter in cadena:
        # caracter = "H", "o", "l", "a", " ", "m", ..., "."

        # Dentro de una palabra
        if caracter != " " and caracter != ".":     # SI O SI ES UN AND

            # siempre que una variable se iguala a funcion es porque espera que la funcion retorne algo
            vocal = es_vocal(caracter)      # vocal = True

            if vocal is True:   # if vocal:    # if vocal == 1
                cont_vocales += 1

            cons = es_consonante(caracter)
            if cons is True:    # if cons:      # if cons == 1
                cont_consonantes += 1

        # Fuera de una palabra
        else:
            # terminamos de leer una palabra
            pass



        print(caracter)

    print("sali del ciclo for")
    print("cantidad de vocales:", cont_vocales)




    for i in range(10):
        # i = 0, 1, 2, 3, 4, ..., 9
        pass


if __name__ == '__main__':
    principal()
