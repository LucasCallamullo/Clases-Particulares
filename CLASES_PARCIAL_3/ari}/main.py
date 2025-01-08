

# clases , registros,               objetos
class Tablet:

    # id, pulgadas, marca, precio, peso
    # funcion constructora o inicializadora
    def __init__(self, id, pulgadas, marca, importe, peso):
        # ctrl + d  ; ctrl + c ; ctrl + v
        self.id = id
        self.pulgadas = pulgadas
        self.marca = marca
        self.importe = importe
        self.peso = peso

    # Nuestra funcion para ver los datos del objeto / clase / registro
    def __str__(self):

        cadena = "ID: " + str(self.id)                # ID: Cadena
        cadena += " | Pulgadas: " + str(self.pulgadas)
        cadena += " | Marca: " + self.marca
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Peso: " + str(self.peso)
        return cadena


def principal2():
    tablet1 = Tablet(1, 10, "Samsung", 100.5, 0.5)
    tablet2 = Tablet(2, 12, "LG", 90.5, 0.4)

    tablet1.id = 5

    print(tablet1)
    print(tablet2)


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de conteo/Acum.")
    print("4 - Busqueda Secuencial.")
    print("0 - Salir.")

    op = int(input("Ingresar su opcion: "))  # 4
    return op               # retornar, devolver, 4


def principal():

    # listas / arreglos / arrays / vectores
    # Lista vacía
    listas = [15]         # o list()

    tuplas = ()

    # la funcion .append() , agregar elementos al final de la lista, conservando su contenido
    listas.append(5)
    # listas = [ 15, 5 ]
    listas.append("Lucas")
    # listas = [ 15, 5, "Lucas" ]
    listas.append(10.5)
    # listas = [ 15, 5, "Lucas", 10.5 ]

    # Indices  0   1   2
    listas = [15, 25, 30]

    # listas[0] == 15
    # listas[1] == 25

    listas[1] += 25
    # listas = [15, 50, 30]

    # listas = [15, 50, 30]
    for i in listas:
        # i = 15, 50, 30
        print(i)
        # 15
        # 50
        # 30

    # indices    0   1   2
    # listas = [15, 50, 30]
    n = len(listas)     # Tamaño de la lista esta dado por su cantidad de elementos
    for i in range(n):      # 3     0, 1, 2
        # i = 0, 1, 2
        print(listas[i])
        # 15
        # 50
        # 30

    op = -1
    while op != 0:      # mientras op sea distinta de cero

        # Cuando igualas una variable a un funcion es porque esperas que esa funcion te devuelva algo
        op = menu()     # 4

        if op == 1:
            print("Selecciono el 1")

        elif op == 2:
            print("Selecciona el 2")

        elif op == 3:
            pass

        elif op == 4:
            pass

        elif op == 0:
            print("Gracias por usar el menu.")


if __name__ == '__main__':
    principal2()

