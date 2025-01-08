'''
    Enunciado:
    Ingresar por teclado una cadena de caracteres la misma debe terminar en punto.
    Se pide un menu que permita realizar las siguientes acciones:
    Verificar cuantas palabras tiene la cadena, cuantas vocales hay en la cadena, cuantas consonantes hay en
    la palabra, si la palabra tiene alguna mayuscula.
'''


def menu():
    print("1 - Mostrar Resultados.")
    return int(input("Ingresar una opcion: "))


# Opcion 1
def cant_palabras(cad):
    cant = 0
    palabra_nueva = False
    # cad = "hola."
    for i in cad:
        if i == " " or i == ".":
            if palabra_nueva:
                cant += 1
            palabra_nueva = False
        else:
            palabra_nueva = True

    return cant


# opcion 2
def cant_vocales(cad):
    cant = 0
    vocales = "aeiou"
    # holA
    for i in cad:
        if i != " " or i != ".":
            # .lower() es para tomar a la letra como minuscula.
            if i.lower() in vocales:
                cant += 1
    return cant


# Opcion3
def cant_consonantes(cad):
    cant = 0
    consonantes = "BCDFGHJKLMNPQRSTVWXYZ"
    for i in cad:
        if i != " " or i != ".":
            # .upper() es para tomar la letra como mayuscula.
            if i.upper() in consonantes:
                cant += 1
    return cant


# opcion 4
def cant_mayus(cad):
    cant = 0
    mayus = "BCDFGHJKLMNPQRSTVWXYZ"
    for i in cad:
        if i != " " or i != ".":
            if i in mayus:
                cant += 1
    return cant




def main():

    cad = input("Ingresar una cadena: ")

    op = -1

    while op != 0:
        print("=" * 50)
        op = menu()

        if op == 1:
            cant = cant_palabras(cad)
            print("Cantidad de palabras:", cant)

        # elif op == 2:
            vocales = cant_vocales(cad)
            print("Cantidad de vocales:", vocales)

        # elif op == 3:
            consonantes = cant_consonantes(cad)
            print("Cantidad de consonantes:", consonantes)

        # elif op == 4:
            mayus = cant_mayus(cad)
            print("Cantidad de mayus:", mayus)



if __name__ == '__main__':
    main()
