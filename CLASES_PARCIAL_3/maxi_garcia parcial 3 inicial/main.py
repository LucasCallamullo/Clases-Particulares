

# clase , registro , objeto
class Parlante:

    # colores = ("Negro", "Blanco", "Azul")
    # Numero id de produccion > 0, Marca, Color(1, 3), Precio > 0

    # funcion constructora o inicializadora
    def __init__(self, id, marca, color, importe):
        # ctrl + d
        self.id = id
        self.marca = marca
        self.color = color
        self.importe = importe

    # funcion
    def __str__(self):
        cadena = "ID: " + str(self.id)
        cadena += " | Marca: " + self.marca
        cadena += " | Color: " + str(self.color)
        cadena += " | Importe: " + str(self.importe)
        return cadena


def principal():

    parlante1 = Parlante(5, "JBL", 1, 500.20)
    parlante2 = Parlante(4, "Redragon", 2, 400.20)

    print(parlante1)
    print(parlante2)
    parlante1.id = 1
    print(parlante1)
    print(parlante2)

def principal2():

    # Arreglos, Arrays, Listas, Vectores
    v_listas = []
    # v_listas = list()

    # .append()   y se conserva contenido de la lista
    v_listas.append(15)
    v_listas.append(50)
    v_listas.append(35)

    # Indices       0   1   2
    # v_listas = [ 15, 50, 35 ]

    v_listas[1] += 10
    # Indices       0   1   2
    # v_listas = [ 15, 60, 35 ]

    v_listas[2] = 40
    # Indices       0   1   2
    # v_listas = [ 15, 60, 40 ]

    # Indices       0   1   2
    # v_listas = [ 15, 60, 40 ]
    for i in v_listas:
        # i = 15, 60, 40
        # leer los datos del arreglo
        i += 10
        print(i)

    # pára cuando queres hacer modificaciones o reliazar modificaciones o encontrar una posicion dentro del arreglo
    # len(v_listas) Nos devuelve el tamaño de la lista que esta dado por la cantidad de elementos que tenga

    # Indices       0   1   2
    # v_listas = [ 15, 60, 40 ]
    n = len(v_listas)   # 3
    for i in range(n):  # 3
        # i = 0, 1, 2

        if i != 2:
            v_listas[i] += 10

    # Indices       0   1   2
    # v_listas = [ 25, 70, 40 ]




def menu():
    # ctrl + d
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))    # 2
    return op           # retornar o devolver op


def principal2():

    op = -1
    while op != 0:

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
            print("Gracias por usar el menu.")






if __name__ == "__main__":
    principal()
