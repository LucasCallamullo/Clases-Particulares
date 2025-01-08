

# clases - registros - objetos

class Juicio:

    # tupla_clientes = ( "CLIENTE 1" , "CLIENTE 2", "CLIENTE 3
    # codigo INT , descripcion STR, tipo (1, 15), cliente(1, 3), importe FLOAT

    # funcion constructora o incializadora
    def __init__(self, codigo, descripcion, tipo, cliente, importe):
        self.codigo = codigo
        self.descripcion = descripcion
        self.tipo = tipo
        self.cliente = cliente
        self.importe = importe

    def __str__(self):
        cadena = "Codigo: " + str(self.codigo)
        cadena += " | Descripcion: " + self.descripcion
        cadena += " | tipo: " + str(self.tipo)
        cadena += " | cliente: " + str(self.cliente)
        cadena += " | importe: " + str(self.importe)
        return cadena


def principal():

    juicio1 = Juicio(1, "1", 1, 1, 1.0)
    juicio2 = Juicio(2, "1", 1, 2, 1)

    print(juicio1)
    print(juicio2)

    juicio1.codigo = 5
    print()
    print(juicio1)
    print(juicio2)



def principal2():
    # listas - vector- arreglos- array
    # crear una lista vacía
    v_lista = []       # list()

    # .append()     agregar o anexar elementos al final de la lista conservando el contenido anterior
    v_lista.append(50)
    v_lista.append(100)
    v_lista.append(150)

    # indices    0     1    2
    # v_lista = [50, 100, 150]

    # len(v_lista) --> nos dice o nos devuelve el tamaño del vector, que esta dado por la cantidad de elementos
    for i in range(len(v_lista)):   # range(3)
        # i = 0,     1, 2       --> la "i" toma los valores de indice

        if i < 2:
            v_lista[i] += 10
        else:
            v_lista[i] = "Palabra"

    # v_lista = [60, 110, "Palabra"]

    #
    # indices    0     1    2
    # v_lista = [60, 110, "Palabra"]
    for i in v_lista:                   # leer el contenido del arreglo
        # i = 60, 110, "Palabra"        --> la "i" vale como cada elemento de la lista
        print(i)
        # 60
        # 110
        # Palabra


def menu():
    # ctrl + d
    print("1 - ")
    print("2 - ")
    print("3 - ")
    print("4 - ")
    print("0 - ")
    op = int(input("Ingresar un valor: "))  # 3
    return op   # 3     # devolver valores


def principal2():


    op = -1
    while op != 0:  # mientras op sea distinto de cero, ingresa al ciclo

        # si una variable esta igualada a una funcion es porque espera que la funcion nos devuelva algo
        op = menu()

        if op == 1:
            pass

        elif op == 2:
            pass









if __name__ == '__main__':
    principal()

