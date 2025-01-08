# clase - registro - objetos
# es un diseño o una plantilla base a partir de la cual nosotros vamos a construir muchos objetos

class Figurita:

    # pais(1, 32) INT, num_jug (1, 19) INT, nombre STR, posicion(0, 3) INT, importe > 0 FLOAT

    # funcion constructora o inicializadora
    def __init__(self, pais, num_jug, nombre, posicion, importe):
        # ctrl + d
        self.pais = pais
        self.num_jug = num_jug
        self.nombre = nombre
        self.posicion = posicion
        self.importe = importe

    # reemplazar el print del objeto por defecto
    def __str__(self):
        cadena = "Pais: " + str(self.pais)
        cadena += " | Num Jug: " + str(self.num_jug)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Posicion: " + str(self.posicion)
        cadena += " | Importe: " + str(self.importe)
        return cadena



def principal():
    figu1 = Figurita(1, 1, "Lautaro", 3, 5.5)
    figu2 = Figurita(2, 2, "Lisandro", 2, 5.5)

    print(figu1)
    print(figu2)

    figu1.nombre = "Cuti"
    print()
    print(figu1)
    print(figu2)



def principal2():
    # listas - arreglo - vector - array

    # listas es un nuevo tipo de variable del tipo List
    # del tipo mutable, es decir que se pueden modificar a lo largo del programa

    # crear una lista vacia
    v_lista = []  # list()

    # .append()     # anexar/agregar elementos al final de la lista, conservando todo su contenido anterior
    v_lista.append(50)
    v_lista.append(70)
    v_lista.append(100)

    # indices    0   1     2
    # v_lista = [50, 70, 100]

    # v_lista[1] += 15
    # v_lista = [50, 85, 100]

    # v_lista[0] = "Lucas"
    # v_lista = ["Lucas", 85, 100]

    # indices    0   1     2
    # v_lista = [50, 70, 100]
    for i in v_lista:  # solo lectura, solo para leer el contenido del arreglo
        # i = 50, 70, 100
        print(i)  # la "i" adopta el valor de los elementos de la lista
        # 50
        # 70
        # 100

    # len(v_lista) --> nos devuelve/nos dice el tamaño de la lista, que esta dado por la cantidad de elementos
    # indices    0   1     2
    # v_lista = [50, 70, 100]
    for i in range(len(v_lista)):  # range(3)
        # i = 0, 1, 2           # la "i" adopta valores de indice
        if i != 2:
            v_lista[i] += 10
    # v_lista = [60, 80, 100]


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de Conteo.")
    print("4 - Busqueda Secuencial.")
    print("0 - Salir.")

    op = int(input("Ingresar opcion: "))  # 2
    return op


def principal3():
    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingresar al ciclo

        # si una variable esta igualada a una funcion, significa que espera la funcion retorne algo
        op = menu()

        if op == 1:
            pass

        elif op == 2:
            pass


if __name__ == '__main__':
    principal()
