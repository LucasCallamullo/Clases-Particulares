

# una clase es un boceto o un diseño que abarca distintos atributos o comportamientos comunes de objetos
class Teclado:

    # el metodo constructor
    def __init__(self, peso, marca, precio, tamanio):
        self.peso = peso
        self.marca = marca
        self.precio = precio
        self.tamanio = tamanio

    # el metodo str
    def __str__(self):
        cadena = "Peso: " + str(self.peso)
        cadena += " | Marca: " + str(self.marca)
        cadena += " | Precio: " + str(self.precio)
        cadena += " | Tamanio: " + str(self.tamanio)
        return cadena


def objetos():
    teclado1 = Teclado(5, "Redragon", 10, 10)
    teclado2 = Teclado(4, "Logitech", 10, 10)

    print(teclado1)
    print(teclado2)
    print()

    # acceder a los atributos
    teclado1.precio = 20
    print(teclado1)
    print(teclado2)


def listas():
    lista = []      # list()
    lista.append(3)

    # indice    0
    # lista = [ 3 ]

    lista.append(5)
    # indice    0   1
    # lista = [ 3,  5 ]

    print(lista)    # [ 3,  5 ]

    print(lista[0])     # 3
    print(lista[1])     # 5


    # iterar sobre la listas
    # lista = [ 3,  5 ]
    for i in lista:
        # i = 3, 5
        print(i)        # 3
                        # 5

    # len(lista) --> el tamaño de una lista esta dado por la cantidad de elementos
    n = len(lista)  # 2
    for i in range(n):
        # i = 0,    1
        print(i)        #   0
                        #   1
        print(lista[i])     # 3
                            # 5


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de conteo.")
    print("4 - Busqueda secuencial.")
    print("0 - Salir.")
    x = int(input("Ingresar opcion: "))        # 3
    return x   # 3


def principal():


    op = -1
    while op != 0:

        op = menu()         # op = el retorno


        if op == 1:
            pass

        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass

        elif op == 0:
            print("Termino el programa.")




if __name__ == "__main__":
    # principal()
    # listas()
    objetos()
