

# clases - registros - objetos
class Celular:

    # num id de fabricacion > 0, Marca, pulgadas(5, 13), precio

    # id > 0, marca, pulgadas(5, 13), importe > 0

    # funcion constructora o inicializadora
    def __init__(self, id, marca, pulgadas, importe):
        self.id = id
        self.marca = marca
        self.pulgadas = pulgadas
        self.importe = importe

    # reemplazar el print de nuestro objeto
    def __str__(self):
        cadena = "ID: " + str(self.id)
        cadena += " | Marca: " + self.marca
        cadena += " | Pulgadas: " + str(self.pulgadas)
        cadena += " | Importe: " + str(self.importe)
        return cadena


def principal():

    celu1 = Celular(1, "Samsung",11, 100.5)     # Objetos
    celu2 = Celular(2, "Xiaomi",10, 120.5)      # Objetos

    celu1.id = 15

    print(celu1)
    print(celu2)


def principal2():
    # arreglo , lista, vector , array

    # lista es un nuevo tipo de variable del tipo List
    # lista es un tipo de variable mutable, es decir que se puede modificar a lo largo del programa

    # crear una lista vacía
    v_lista = []            # list()

    # .append()     # anexar o agregar elementos al final de la lista, conservando todoo su contenido anterior
    v_lista.append(25)
    v_lista.append(50)
    v_lista.append(100)

    # indices     0     1       2
    # v_lista = [25,    50,     100]

    # v_lista[1] += 10
    # v_lista[0] = "Lucas"

    #
    # indices     0     1       2
    # v_lista = [25,    50,     100]

    for i in v_lista:       # un lectura completa de arreglo
        # i = 25,   50, 100
        print(i)        # la "i" adopta el valor de los elementos
        # 25
        # 50
        # 100

    # len(v_lista) --> nos devuelve o nos dice, la longitud/tamaño de la lista, que esta
                    # dado por la cantidad de elementos que contenga
    #
    # indices     0     1       2
    # v_lista = [25,    50,     100]
    for i in range(len(v_lista)):   # range(3)
        # i = 0,    1,  2       # la "i" adopta el valor de los indices
        if i != 2:
            v_lista[i] += 5

    # v_lista = [30,    55,     100]



def menu():
    # ctrl + d
    print(" 1 - ")
    print(" 2 - ")
    print(" 3 - ")
    print(" 4 - ")
    print(" 0 - Salir.")

    op = int(input("Ingresar opcion: "))  # op = 2
    return op             # devolver / retornar


def principal3():
    op = -1

    while op != 0:      # mientras op sea distinto de 0, quiero que ingrese a mi ciclo

        # si una variable esta igulada a una funcion es porque espero que la funcion me retorne algo
        op = menu()     # 2

        if op == 1:
            pass

        elif op == 2:
            print("Toco el 2")


if __name__ == '__main__':
    principal()




