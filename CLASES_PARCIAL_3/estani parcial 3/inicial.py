



class Mesa:

    # funcion constructora o inicializadora
    def __init__(self, largo, ancho, altura, precio, marca):

        # ctrl + d
        self.largo = largo
        self.ancho = ancho
        self.altura = altura
        self.precio = precio
        self.marca = marca

    def __str__(self):
        cadena = "Largo: " + str(self.largo)     # Largo: 1 | Ancho: 1
        cadena += " | Ancho: " + str(self.ancho)
        cadena += " | altura: " + str(self.altura)
        cadena += " | precio: " + str(self.precio)
        cadena += " | marca: " + self.marca
        return cadena


def clases():

    # las clases son bocetos predefinidos que indican que atributos y comportamientos(metodos)
    # va a tener un objeto creado a partir de esta clase

    mesita1 = Mesa(1, 1, 1, 50.00, "Tablas")        # un objeto/registro creado a partir de la clase Mesa()
    mesita2 = Mesa(2, 2, 2, 100.00, "Tablas")        # un objeto/registro creado a partir de la clase Mesa()

    mesita1.marca = "Tablones"
    print(mesita1)
    print(mesita2)


def listas():
    # listas, vectores, arreglos, arrays

    # como crear una lista
    lista = []          # lista = list()

    # lista es una variable de tipo mutable ( porque se modifica los elementos )

    # funcion para agregar elementos al final de la lista
    lista.append(4)
    # lista = [ 4 ]
    #
    lista.append(5)
    # lista = [ 4,  5 ]

    # para acceder a esos elementos mediante indice
    # indice    =  0    1
    lista       = [4,   5]

    print(lista[0])     # 4
    lista[0] += 3       # 4 + 3 = 7
    print(lista[0])     # 7

    print(lista)    # [7,   5]

    #
    # como recorrer o leer las listas
    for i in lista:         #
        # i = 7,    5
        print(i)        # 7
                        # 5

    n = len(lista)      # el tamaño de la list esta dado por la cantidad de elementos
    # n = 2
    # indice   =   0    1
    #   lista  =  [3,   3]
    for i in range(n):      # range(2)
        # i = 0,         1

        lista[i] = 3
        print(lista[i])     # 3
                            # 3


def sumar(num1, num2):
    x = num1 + num2
    return x


def restar(num1, num2):
    x = num1 - num2
    return x


def principal():

    # menu de opciones
    op = -1     # op = opcion

    # 4 != 0
    while op != 0:          # mientras "op" sea distinto de cero, ingreso al ciclo while

        print("1 - Sumar dos números.")
        print("2 - Restar dos números.")
        print("0 - Salida.")
        op = int(input("Ingresar opción: "))        # "3" --> 3


        num1 = int(input("Ingresar numero 1: "))
        num2 = int(input("Ingresar numero 2: "))

        if op == 1:
            res = sumar(num1, num2)     # res = a lo que retorne funcion sumar( )
            print(res)

        elif op == 2:
            res = restar(num1, num2)      # res = a lo que retorne funcion restar( )
            print(res)

        elif op == 3:
            pass
        elif op == 4:
            pass
        # op = 4


if __name__ == '__main__':
    principal()
    # listas()
    # clases()