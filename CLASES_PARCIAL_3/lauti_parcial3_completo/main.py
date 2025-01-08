


# clase - registro - objeto
class Juicio:

    # codigo INT, descripcion STR, tipo(1, 15) , nombre STR, importe FLOAT

    # funcion constrcutora o inicializadora
    def __init__(self, codigo, descripcion, tipo, nombre, importe):
        self.codigo = codigo
        self.descripcion = descripcion
        self.tipo = tipo
        self.nombre = nombre
        self.importe = importe

    # nuestra funcion de print
    def __str__(self):
        cadena = "Codigo: " + str(self.codigo)
        cadena += " | Descripcion: " + self.descripcion
        cadena += " | Tipo: " + str(self.tipo)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Importe: " + str(self.importe)
        return cadena


def listas():
    juicio1 = Juicio(1, 1, 1,1 ,1,)
    print(juicio1)

    # lista - vector - arreglo - array
    # crear una lista vacia
    v_lista = []        # list()

    # .append() # anexar o agregar elementos al final de la lista, pero conservando el contenido anterior
    v_lista.append(50)
    v_lista.append(70)
    v_lista.append(80)

    # indices    0   1   2
    # v_lista = [50, 70, 80]

    # len(v_lista)  - Nos devuelve o nos dice el tamaño de la lista, que esta dado por la cantidad de arreglos
    for i in range(len(v_lista)):  # range(3)
        # i = 0,     1, 2  ->> la "i" toma el valor de indices
        v_lista[i] += 10
        # v_lista = [60, 80, 80]

        print(v_lista[i])
        # 50





def menu():
    # ctrl + d
    print(" 1 - Cargar Arreglo.")
    print(" 2 - Mostrar arreglo.")
    print(" 3 - Vector Conteo Acum.")
    print(" 4 - Busqueda seucuencial.")
    print(" 5 - Salir.")
    op = int(input("Ingresar una opcion: "))    # 3
    return op


def principal():

    op = -1
    while op != 5:  # mientras op sea distinto de cero, quiero que ingrese al ciclo while

        # si una variable es igual a una funcion significa que espera que la funcion devuelva algo
        op = menu()     # 3

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



