



# clase / objeto / registro
class Tele:

    # id de fabricacion, marca, cantidad de pulgadas, precio

    # funcion constructora o inicializadora
    def __init__(self, id, marca, pulgadas, importe):
        # ctrl + d
        self.id = id
        self.marca = marca
        self.pulgadas = pulgadas
        self.importe = importe

    # reemplaza la funcion de print
    def __str__(self):

        cadena = "ID: " + str(self.id)
        cadena += " | Marca: " + self.marca
        cadena += " | Pulgadas: " + str(self.pulgadas)
        cadena += " | Importe: " + str(self.importe)
        return cadena


def principal():

    tele1 = Tele(1, "Samsung", 42, 10.0)
    tele2 = Tele(2, "Hitachi", 32, 15.0)



    print(tele1)
    print(tele2)
    print()
    tele1.id = 15
    print(tele1)
    print(tele2)

def principal2():

    # listas - arreglos - vectores- arrays
    # son un tipo de variable del tipo list()
    # son variables mutables, o sea que se modifican a lo largo del programa

    # crear una lista vacía
    v_lista = []        # list()

    # .append()   -  anexar o agregar al final de la lista un elemento, conservando el contenido anterior
    v_lista.append(15)
    v_lista.append(25)
    v_lista.append(50)

    # indices     0   1   2
    # v_lista = ["asd", 35, 50]

    # v_lista[1] += 10
    # v_lista[0] = "asd"

    #
    # indices     0   1   2
    # v_lista = [15, 25, 50]

    for i in v_lista:       # leer el contenido del arreglo
        # i = 15, 25, 50
        print(i)
        # 15
        # 25
        # 50

    # len(v_lista) --> Nos dice o nos devuelve el tamaño de la lista, que esta dado por la cantidad d elementos
    #
    # indices     0   1   2
    # v_lista = [20, 30, 50]
    for i in range(len(v_lista)):       # range(3)  # este ciclo nos permite realizar modificaciones
        # i = 0,    1,  2           # i toma valores de indice
        v_lista[i] += 5



def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar")
    print("3 - Vector de conteo")
    print("4 - Busqueda Secuencial")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))  # 1
    return op     # devolver retornar algun valor


def principal3():

    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingreso al ciclo while

        # si una variable esta igualada a una funcion es porque espero que la funcion me devuelva algo
        op = menu() # 1

        if op == 1:
            print("Toco el 1")

        elif op == 2:
            pass


if __name__ == "__main__":
    principal()



