



# clases - objetos - registros
# es una plantilla base o un diseño base a partir del cual nosotros vamos a crear muchos objetos
# la plantilla iba a definir los atributos de nuestros objetos
class Figurita:
    # tuplas_posiciones = ("Arquero", "Defensor", "Volante", "Delantero")
    # pais (1, 32) INT, num_jug(1, 19), nombre STR, posicion(1, 4), importe > 0 FLOAT

    # funcion constructora o inicializadora
    def __init__(self, pais, num_jug, nombre, posicion, importe):
        # ctrl + d
        self.pais = pais
        self.num_jug = num_jug
        self.nombre = nombre
        self.posicion = posicion
        self.importe = importe

    # funcion de print para mi objeto figurita
    def __str__(self):
        cadena = "Pais: " + str(self.pais)
        cadena += " | Num Jug: " + str(self.num_jug)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Posicion: " + str(self.posicion)
        cadena += " | Importe: " + str(self.importe)
        return cadena



def principal():

    figu1 = Figurita(1, 1, "A", 1, 1)
    figu2 = Figurita(2, 2, "B", 1, 1)



    print(figu1)
    print(figu2)

    figu1.pais = 5
    print()
    print(figu1)
    print(figu2)




def principal2():

    # arreglos - lista - vector - array
    # crear una lista vacía
    v_lista = []        # list()

    # .append() anexar/ agregar elementos al final de la lista, pero conservando el contenido anterior
    v_lista.append(50)
    v_lista.append(100)
    v_lista.append(150)

    # indices    0    1     2
    # v_lista = [50, 100, 150]

    # len(v_lista) --> nos devuelve o nos dice, el tamaño de la lista, que esta dado por la cantidad de elementos

    for i in range(len(v_lista)):   # range(3)  --> lo hacemos si queremos modificar algo en la lista
        # i = 0, 1, 2   --> la "i" vale como indices
        v_lista[i] += 10

        print(v_lista[i])
    # v_lista = [60, 110, 160]

    #
    for i in v_lista:       # --> leer el contenido de neustro arreglo
        # i = 60, 110, 160
        print(i)



def menu():
    # ctrl + d
    print(" 1 - ")
    print(" 2 - ")
    print(" 3 - ")
    print(" 4 - ")
    print(" 0 - Salir.")
    op = int(input("Ingresar opcion: "))    # 1
    return op   # retornar, devolver algo


def principal2():

    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingresa al ciclo while

        # si una variable esta igualada a una funcion, que espera que la funcion me retorne algo
        op = menu()  # 1 - > o sea lo que devuelva menu

        if op == 1:
            pass

        elif op == 2:
            pass

        elif op == 3:
            pass

        elif op == 4:
            pass




if __name__ == '__main__':
    principal()

