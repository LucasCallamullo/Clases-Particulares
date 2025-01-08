import random


class Trabajo:
    def __int__(self, nombre, legajo, importe, marca, num):
        pass

    def __str__(self):
        # marca = transformar_marca(marca)
        pass


# def transformar_marca(marca):
#     marcas = ("Peugeot", "Fiat")
#    return marcas[marca]


def crear_lista(v1):
    # 5 vueltas
    nombres = ("Lucas", "Matias", "Tomas")
    for i in range(5):
        nombre = random.choice(nombres)
        legajo = random.randint(100, 100)
        # importe
        # nota
        num = random.randint(1, 5)
        # trabajito = Trabajo(nombre, legajo, importe, nota, num)
        v1.append(num)


# Busqueda Secuencial o Lineal
# v = mi lista/vector ; x = parametro a buscar ; x = 3
# [1, 4, 7, 10, 15]
def linear_search(v, x):
    #  0  1  2  3  4
    # [5, 5, 3, 3, 4]                    x = 6
    # busqueda secuencial...
    for i in range(len(v)):
        # i = 0  a 4
        if x == v[i]:
            return i
    return -1


# Busqueda binaria               #            #  v1[i].nombre v1.nota v1.prom
# v = mi lista ; x = parametro a buscar
#        2  3   4


        # Op 1 = Cargar arreglo
        # op 2 = Mostrar ordenado por legajo

        # Op 3 = Busqueda de legajo

        # op 4 = Busqueda por nombre

# [1, 4, 7, 10, 15]
#
#  v.legajo= 1 ;  v.nombre = ZOE
#  v.legajo= 4 ;  v.nombre = AZUL
#  v.legajo= 7 ;  v.nombre = Carlos


def binary_search(v, x):
    # busqueda binaria...
    # izq = 5          ; der = 4
    # c = 4        x = 16
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1
    return -1


# funcion necesaria para la busqueda binaria ordenar el algoritmo
# va a ser de forma ascendente o descendente dependiendo de como pongamos el < ó >
# > = ascendente        ; < = descendente
def sort_v(v):
    n = len(v)
    #i    1  2  3
    #j       2  3  4
    # [2, 4, 5, 3, 3]

    #
    for i in range(n-1):
        # i = 2
        #  3, 5        range(i+1, 5, 1)
        for j in range(i+1, n):
            # i = 1
            # j = 4
            if v[i] > v[j]:
                # 4    3      3     4
                v[i], v[j] = v[j], v[i]

    print(v)


def main():

    # crear lista/vector
    v1 = list()     # []
    crear_lista(v1)
    print(v1)

    v1 = [5, 5, 3, 3, 4]

    # Menu busquedas
    # estudiante ( legajo y notas)
    # oordenas por legajo
    # buscar legajo busqueda binaria; si esta ordenado
    #
    # busqueda secuencial

    op = -1
    while op != 0:
        print("=" * 50)
        op = int(input("Ingresar opcion: "))

        # Busqueda secuencial  / lineal
        #
        if op == 1:
            num = int(input("Numero a buscar: "))
            pos = linear_search(v1, num)

            if pos >= 0:
                print(" Se encontro el numero! en la posicion:", pos,
                      "\n El valor encontrado fue:", v1[pos])
            else:
                print("No se encontro el numero ingresado")



        # Busqueda binaria
        elif op == 2:
            sort_v(v1)

            num = int(input("Numero a buscar: "))
            pos = binary_search(v1, num)
            if pos >= 0:
                print(" Se encontro el numero! en la posicion:", pos,
                      "\n El valor buscado fue:", v1[pos])
            else:
                print("No se encontro el numero ingresado")



if __name__ == '__main__':
    main()
