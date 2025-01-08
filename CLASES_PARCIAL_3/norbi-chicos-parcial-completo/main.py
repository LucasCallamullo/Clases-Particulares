


# clase - registro . objetos
class Figurita:
    # tupla_posiciones = ("Arquuero", "Defensor", "Volante", "Delantero")
    # pais (1, 32), num_jug(1, 19), nombre STR, posicion(1, 4), importe > 0 FLOAT

    # funcion constructora o inicializadora
    def __init__(self, pais, num_jug, nombre, posicion, importe):
        # ctrl + d
        self.pais = pais
        self.num_jug = num_jug
        self.nombre = nombre
        self.posicion = posicion
        self.importe = importe

    # funcion de print para nuestro objeto
    def __str__(self):
        cadena = "Pais: " + str(self.pais)
        cadena += " | Num_Jug: " + str(self.num_jug)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Posicion: " + str(self.posicion)
        cadena += " | Importe: " + str(self.importe)
        return cadena


def principal():
    figu1 = Figurita(1, 1, "1", 1, 1)
    figu2 = Figurita(2, 2, "1", 1, 1)
    print(figu1)
    print(figu2)

    figu1.pais = 25
    print()
    print(figu1)
    print(figu2)


def principal2():
    # vector - arreglo , listas, arrays

    # crear una lista vacia
    v_lista = []        # list()

    # .append() # anexar/agregar elementos al final de la lista, pero conservando el contenido anterior
    v_lista.append(50)
    v_lista.append(70)
    v_lista.append(80)

    # indices     0   1  2
    # v_lista = [50, 70, 80]

    v_lista[1] += 10
    # v_lista = [50, 80, 80]

    len(v_lista)    # --> nos devuelve/nos dice el tamaño de la lista, que esta dado por la cantidad elementos


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Vector de Conteo/Acum.")
    print("4 - Busqueda Secuencial.")
    print("0 - Salir.")
    op = int(input("Ingresar una opcion: "))    # 3

    return op   # devolver o retornar algun valor


def principal2():

    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingreso al ciclo

        # si una variable esta igualada a una funcion es porque espero que la funcino devuelva algo
        op = menu()     # lo que retorna menu es un 3

        if op == 1:
            pass

        elif op == 2:
            pass




if __name__ == '__main__':
    principal()


