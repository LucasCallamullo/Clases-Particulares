

# clases / registros / objetos
class Mascota:
    # edad, nombre, tipo(conejo, gato, perro), precio

    # funcion constructora o inicializadora
    def __init__(self, edad, nombre, tipo, precio):
        # ctrl + d, doble click, ctrl + c, ctrl + v
        self.edad = edad
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

    def __str__(self):
        cadena = "Nombre: " + self.nombre
        return cadena


def principal():

    mascota1 = Mascota(3, "Coco", "Perro", 10.5)
    mascota2 = Mascota(3, "Michi", "Gato", 15.5)

    print(mascota1)
    print(mascota2)

    mascota1.nombre = "Dante"
    print()
    print(mascota1)
    print(mascota2)





def principal2():

    # listas / arreglos / arrays / vectores
    # Como se hace una lista vacía
    v_lista = []        # list()

    # .append()     Agrega elementos al final de la lista, conservando el contenido anterior
    v_lista.append(35)
    v_lista.append(50)
    v_lista.append(100)

    # indices =    0   1   2
    # v_lista = [ 35, 50, 100 ]

    # print(v_lista)

    v_lista[1] = 75
    # v_lista = [ 35, 75, 100 ]
    v_lista[0] += 5
    # v_lista = [ 40, 75, 100 ]

    # indices =    0   1   2
    # v_lista = [ 40, 75, 100 ]
    for i in v_lista:
        # i = 40, 75, 100
        print(i)


    n = len(v_lista)   # 3  # el tamaño de la lista esta dado por la cantidad de elementos que contenga
    # indices =    0   1   2
    # v_lista = [ 40, 75, 100 ]
    for i in range(n):      # 3
        # i = 0, 1, 2
        if i != 2:
            v_lista[i] = v_lista[i] * 2
            print(v_lista[i])       # 80, 150















def principal3():



    op = -1
    while op != 0:          # mientras op sea distinto de cero, ingreso al ciclo while

        # ctrl + d
        print("1 - Cargar Arreglo. ")
        print("2 - ")
        print("3 - Mostrar Datos. ")
        print("5 - Busqueda Secuencial")
        print("0 - Salir. ")

        op = int(input("Ingresar opcion: "))

        if op == 1:
            pass

        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 0:
            print("Gracias por usar el menu.")
        else:
            print("INgrese un numero valido.")








if __name__ == '__main__':
    principal()






