


# clase / registro / objetos
class Termo:

    # marca, capacidad(1,3), precio, diametro(10cm, 30)

    # funcion constructora o inicializadora
    def __init__(self, marca, capacidad, importe, diametro):
        # ctrl + d
        self.marca = marca
        self.capacidad = capacidad
        self.importe = importe
        self.diametro = diametro

    def __str__(self):
        cadena = "Marca: " + self.marca
        cadena += " | Capacidad: " + str(self.capacidad)
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Diametro: " + str(self.diametro)
        return cadena


def principal():

    termo1 = Termo("A", 1, 10.5, 15)
    termo2 = Termo("B", 1, 20.5, 15)

    termo1.marca = "C"

    print(termo1)
    print(termo2)



def principal3():

    # listas / arreglos / arrays / vectores

    # como crear una lista vacia
    v_listas = []               # list()

    # la funcion .append() , agrega elementos a la lista, conservando todoo el contenido anterior
    v_listas.append(15)
    v_listas.append(25)
    v_listas.append(35)

    # indices      0   1   2
    # v_listas = [15, 25, 35]

    # v_listas[1] += 15
    # v_listas = [15, 40, 35]

    # v_listas[0] = 20
    # v_listas = [20, 40, 35]

    # len(v_listas) : nos devuelve el tamaño de la lista, y el tamaño esta dado por la cantidad de elementos
    # de la lista

    # indices      0   1   2
    # v_listas = [15, 25, 35]
    # para hacer modificaciones o acceder a indices
    for i in range(len(v_listas)):   # range(3)
        # i = 0, 1,  2
        if i != 2:
            v_listas[i] += 5

    # v_listas = [20, 30, 35]


    # Este ciclo for nos sirve para leer el contenido del arreglo
    # v_listas = [20, 30, 35]
    for i in v_listas:
        # i = 20, 30, 35
        print(i)




def menu():
    # ctrl + d
    print("1 - Cargar arreglo")
    print("2 - Mostrar arreglo")
    print("3 - Vector de Conteo / Acum ")
    print("4 - Busqueda Secuencial")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))  # 2
    return op


def principal2():


    op = -1
    while op != 0:      # mientras op sea distinto de cero, ingreso al ciclo while

        # si una variable esta igualada a una funcion es porque espero que me devuelva algun valor
        op = menu()     # 2

        if op == 1:
            pass

        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 0:
            pass






if __name__ == '__main__':
    principal()







