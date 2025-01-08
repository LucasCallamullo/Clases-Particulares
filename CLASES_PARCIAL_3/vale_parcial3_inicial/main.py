


# clase / registro / objeto

class Tele:
    # num id de fabricacion, marca, precio, pulgadas,

    # funcion constructora o inicializadora
    def __init__(self, id, marca, importe, pulgadas):
        # ctrl + d
        self.id = id
        self.marca = marca
        self.importe = importe
        self.pulgadas = pulgadas

    # funcion de print
    def __str__(self):
        cadena = "ID: " + str(self.id)
        cadena += " | Marca: " + self.marca
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Pulgadas: " + str(self.pulgadas)
        return cadena


def principal():
    tele1 = Tele(1, "Hitachi", 100.5, 42)
    tele2 = Tele(2, "LG", 100.5, 42)

    print(tele1)
    print(tele2)

    tele1.id = 20
    print()
    print(tele1)
    print(tele2)


def principal2():

    # listas / arreglos / arrays / vectores

    # se genera una lista vacia
    v_listas = []           # list()

    # .append()     # anexar o agregar elementos al final de  la lista, pero conservando su contenido anterior
    v_listas.append(15)
    v_listas.append(25)
    v_listas.append(50)


    # indices      0   1   2
    # v_listas = [15, 25, 50]

    # v_listas[1] += 15
    # v_listas = [15, 40, 50]

    # v_listas[0] = "Lucas"
    # v_listas = ["Lucas", 25, 50]

    #
    #
    # indices      0   1   2
    # v_listas = [15, 25, 50]

    # leer el contenido de mi lista
    for i in v_listas:      # 3
        # i = 15, 25, 50
        print(i)

    #
    #
    # indices      0   1   2  3
    # v_listas = [20, 30, 50, 100]

    # len(v_listas) --> nos devuelve/nos dice cual es el tamaño de la lista, y su tamaño esta dado por la cantidad
    #                   de elementos que contenga

    for i in range(len(v_listas)):      # range(3)
        # i = 0, 1, 2, 3                   # para que la i tome valores de indice
        v_listas[i] += 5


















def menu():

    # ctrl + d
    print("1 - Op1")
    print("2 - Mostrar Arreglo.")
    print("3 - Op1")
    print("4 - Op1")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))        # 2
    return op       # 2



def principal3():



    op = -1
    while op != 0:      # mientras op sea distinto de cero

        # que si una variable esta igualada a una funcion es porque espero que esa funcion me devuelva algo
        op = menu()     # 2

        if op == 1:
            pass

        elif op == 2:
            print("Toco el 2")

        elif op == 3:
            pass


if __name__ == '__main__':
    principal()

