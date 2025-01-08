import random


class Tele:
    # ID: valor positivo, Marca = ("Hitachi", "LG", "Samsung"), Precio: flotante, pulgadas: (32-50)
    # Funcion constructor, inicializador
    def __init__(self, id, marca, precio, pulgadas):
        # ctrl + d
        self.id = id
        self.marca = marca
        self.precio = precio
        self.pulgadas = pulgadas

    def __str__(self):
        cadena = "ID: " + str(self.id)   # str + str , el más concatena
        cadena += " | Marca: " + self.marca
        cadena += " | Precio: " + str(self.precio)
        cadena += " | Pulgadas: " + str(self.pulgadas)
        return cadena


# ===========================================================================
#               Opcion 1
# ===========================================================================
def validar_n():
    n = int(input("Cantidad de teles a cargar: "))
    while n <= 0:       # mientras la n sea igual o menor a cero
        n = int(input("Ingrese un valor positivo a cargar: "))
    return n


def cargar_arreglo(n, v_teles):

    marcas = ("Hitachi", "LG", "Samsung")

    for i in range(n):       # 5
        id = random.randint(1, 10)          # Int
        marca = random.choice(marcas)           # Str
        precio = round(random.uniform(0.1, 10), 2)    # Float
        pulgadas = random.randint(32, 50)
        tv = Tele(id, marca, precio, pulgadas)
        v_teles.append(tv)

        # v_teles = [tv0, tv1, tv2, tv3, tv4]


# ===========================================================================
#               Opcion 2
# ===========================================================================
def ordenar_arreglo(v_teles):
    n = len(v_teles)        # 5

    #              0    1    2    3    4
    # v_teles = [tv2, tv0, tv1, tv3, tv4]

    # id = 3, id = 4, id= 5, id= 10, id= 7


    for i in range(n-1):     # 4
        # 0, 1       2, 3

        #        range(start, stop)
        for j in range(i+1, n):     # 5
            # 2, 3, 4
                                                        # si la i se come a la j, es de menor a mayor
                                                        # si la j se come a la i, es de mayor a menor

            if v_teles[i].id > v_teles[j].id:           # la orientacion de la boquita

                v_teles[i], v_teles[j] = v_teles[j], v_teles[i]



def mostrar_datos(v_teles):
    for i in v_teles:   # lista
        # i = tv0, tv1, tv2, tv3, tv4
        print(i)


def menu():
    # ctrl + d
    print()
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar el Arreglo.")
    print("3 - Vector de conteo o acumulacion.")
    print("4 - Busqueda secuencial o binaria.")
    print("0 - Salir.")
    print()
    op = int(input("Ingresar la opcion: "))     # 3
    return op


def principal():

    v_teles = []        # list()

    op = -1
    while op != 0:      # mientras op sea distinto de cero ejecuto el ciclo while

        op = menu()     # 3

        if op == 1:
            n = validar_n()
            cargar_arreglo(n, v_teles)

        elif op == 2:

            ordenar_arreglo(v_teles)
            mostrar_datos(v_teles)


        elif op == 3:
            pass
        elif op == 4:
            print("alguna cosa 2")
        elif op == 5:
            print("alguna cosa 2")


        elif op == 0:
            print("gracioas por usar el programa ")



    print("Termino el programa")




def print_hi():

    tuplas = ("lucas", "azul", "matias")

    # como crear una lista, vector, arreglo
    v_lista = []    # list()           # lista vacía


    #           0,   1,   2
    # listas = [Est1, Est2, Est3]     # len(listas) = 3

    listas = ["lucas", "azul", "matias"]
    listas.append("juli")

    # listas = ["lucas", "azul", "matias", "juli"]

    for i in listas:
        # i = "lucas", "azul" "matias", "juli"
        print(i)


    for i in range(len(listas)):    # 4
        # i = 0, 1, 2, 3
        print(i)
        print(listas[i])


if __name__ == '__main__':
    principal()
