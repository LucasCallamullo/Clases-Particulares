

# clase - objeto - registro
class Figurita:
    # tupla_posiciones = ("Arquero", "Defensor", "Mediocampista", "Delantero")
    # pais (1, 32), num_jug (1, 19) INT, nombre STR, posicion(1, 4), importe > 0 FLOAT

    # funcion constructora o inicializadora
    def __init__(self, pais, num_jug, nombre, posicion, importe):
        # ctrl + d
        self.pais = pais
        self.num_jug = num_jug
        self.nombre = nombre
        self.posicion = posicion
        self.importe = importe

    # funcion de print para nuestro objetos
    def __str__(self):
        cadena = "Pais: " + str(self.pais)
        cadena += " | Num Jug: " + str(self.num_jug)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Posicion: " + str(self.posicion)
        cadena += " | Importe: " + str(self.importe)
        return cadena



def principal():
    figu1 = Figurita(1, 1, "A", 1, 1)
    figu2 = Figurita(1, 1, "D", 1, 1)

    print(figu1)
    print(figu2)






def principal2():

    # listas - vectores - arreglos - arrays

    # crear una lista vacía
    v_lista = []        # list()

    # .append()     anexar / agregar elementos al final de la lista, pero conservando su contenido anterior
    v_lista.append(50)
    v_lista.append(20)
    v_lista.append(10)

    # indices    0   1   2
    # v_lista = [50, 20, 10]

    v_lista[1] += 10
    # v_lista = [50, 30, 10]

    v_lista[0] = 100
    # v_lista = [100, 30, 10]

    # len(v_lista)      que nos devuelve o nos dice el tamaño de la lista, que estas dado por la cantidad de elementos

    #
    # indices    0   1   2
    # v_lista = [50, 20, 10]
    for i in range(len(v_lista)):   # range(3)
        # i = 0, 1, 2   --> la "i" toma valores de indices, o tambien que empieza desde el cero
        v_lista[i] += 1
        # v_lista = [51, 21, 10]

    #
    # indices    0   1   2
    # v_lista = [50, 20, 10]
    for i in v_lista:   # --> leer el contenido del arreglo
        # i = 50, 20, 10     --> la i toma el valor de cada elemento de la lista
        print(i)

def menu():
    # ctrl + d
    print("1 - Cargar Arreglo")
    print("2 - Mostrar Arreglo")
    print("3 - Vector de conteo/acum")
    print("4 - Busqueda Secuencial")
    print("0 - Salir.")
    x = int(input("Ingresar una opcion: "))     # 1
    return x        # devolver, retornar algun valor


def principal2():

    op = -1

    while op != 0:      # mientras op sea distinto de cero, ingreso al ciclo

        # si una variable esta igualada a una funcion, es porque espero que la funcino me devuelva algo
        op = menu()     # vale lo que retorna menu = 1

        if op == 1:
            pass

        elif op == 2:
            pass

        elif op == 3:
            pass





if __name__ == '__main__':
    principal()




