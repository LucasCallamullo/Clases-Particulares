




# clase / registro / objeto
class Mascota:

    # id  , nombre, tipo(1, 3), precio

    # funcion constructora o inicializadora
    def __init__(self, id, nombre, tipo, importe):
        # ctrl + d
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.importe = importe

    # funcion que reemplaza al print
    def __str__(self):
        cadena = "ID: " + str(self.id)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Tipo: " + str(self.tipo)
        cadena += " | Importe: " + str(self.importe)
        return cadena


def principal():

    mascota1 = Mascota(1, "Coco", 1, 10.5)
    mascota2 = Mascota(2, "Michi", 2, 10.5)

    print(mascota1)
    print(mascota2)

    mascota1.nombre = "Dante"
    print()
    print(mascota1)
    print(mascota2)




def principal2():

    """
    v_mascotas = []
    v_mascotas.append(mascota1)
    v_mascotas.append(mascota2)

    # indices        0    1
    # v_mascotas = [ M1 , M2 ]

    v_mascotas[1].nombre = "Dante"

    :return:
    """


    # listas / arreglos / arrays / vectores

    # crear una lista vacia
    v_lista = []        # list()

    # funcion .append() , anexar o agrega un elemento al final de la lista, conservando todo lo anterior
    v_lista.append(15)
    v_lista.append(30)
    v_lista.append(50)
    # v_lista = [15, 30, 50]

    #
    #
    # indices     0   1   2
    # v_lista = [15, 30, 50]

    # v_lista[1] += 5
    # v_lista = [15, 35, 50]

    # v_lista[0] = "Lucas"
    # v_lista = ["Lucas", 35, 50]


    #
    #
    # indices     0   1   2
    # v_lista = [15, 30, 50]

    # leer el contenido del arreglo
    for i in v_lista:
        # i = 15, 30, 50        # la i toma el valor de cada elemento
        print(i)


    # len(v_lista) --> Nos devuelve o nos dice, el tamaño de la lista, que esta dado por la cantidad
    #                   de elementos que tiene

    # indices     0   1   2
    # v_lista = [15, 30, 50]
    for i in range(len(v_lista)):       # range(3)
        # i = 0, 1, 2           # la i toma el valor de indices

        if i != 2:
            v_lista[i] += 10

        # v_lista = [25, 40, 50]


def menu():
    # ctrl + d
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("0 - Salir.")

    op = int(input("Ingresar opcion: "))  # 2
    return op       # devolver o retornar op



def principal3():


    op = -1
    while op != 0:      # mientras op sea distinto de cero, ingrese al ciclo while

        # si una variable esta igualada a una funcion es porque espero que la funcion me devuelva algun valor
        op = menu()         # 2

        if op == 1:
            pass

        elif op == 2:
            pass








if __name__ == '__main__':
    principal()


