

# definir clases u objetos
class Monitor:
    # definimos como parametros todos nuestros atributos de nuestro objeto

    # funcion constructora o inicializadora
    def __init__(self, marca, cant_pulgadas, precio):
        # ctrl + d
        self.marca = marca
        self.cant_pulgadas = cant_pulgadas
        self.precio = precio

    def __str__(self):
        cadena = "MARCA: " + self.marca
        cadena += " | CANT PULGADAS: " + str(self.cant_pulgadas)
        cadena += " | PRECIO: " + str(self.precio)
        return cadena


def principal():

    monitor1 = Monitor("LG", 22, 1499.99)   # return OBJETO
    monitor2 = Monitor("SAMSUNG", 22, 1499.99)   # return OBJETO
    # ahora monitor1 queda almacenado con un objeto unico

    print(monitor1.marca)

    # print(monitor1)
    # print(monitor2)

    listas = []

    listas.append(monitor1)
    listas.append(monitor2)

    # indices     0   1
    # listas = [ M1, M2 ]
    for i in listas:
        # i = M1,   M2
        print(i)        # print M1, M2


    for i in range(len(listas)):        # range(2)
        # i = 0, 1

        # buscar la marca samsung
        if listas[i].marca == "SAMSUNG":
            print(listas[i])        # print M1, M2










def principal2():

    # crear una lista
    listas = []     # list()     # o []

    # agregar elementos   - INT, STR, FLOAT, LISTAS, OBJETOS
    listas.append(5)
    # [5]
    listas.append(3)
    # [5, 3]
    listas.append(2)

    print(listas)

    # indices para permitirnos acceder directamente a un elemento dentro de una posicion en la lista
    # indices        0      1       2
    # listas =      [5,     3,      2]
    print(listas[0])        # 5
    print("=" * 50)

    # nos indica el tamaño de la lista como tasl
    # el tamaño es la cantidad de celdas/ casilleros que contenga
    # las celdas son los elementos por asi decirlo
    n = len(listas)     # return EL TEMAÑO com INT

    # como iterar listas
    for i in range(len(listas)):        # for i in range(3)
        # i = 0, 1, 2
        print(listas[i])
        # 5
        # 3
        # 2

    print()
    # listas =      [5,     3,      2]
    for i in listas:
        # en este caso la "i" vale cada vuelta de ciclo como un elemento distinto dentro de la lista
        # i = 5, 3, 2
        print(i)
        # 5
        # 3
        # 2












if __name__ == '__main__':
    principal()

