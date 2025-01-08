

# Clases , Registros , Objetos
class Figurita:
    # tupla_posicion = ("Arquero", "Defensor", "Mediocampista", "Delantero")

    # pais jugador (1, 32), numero jugador ( 1, 19), nombre, posicion (1, 4), importe > 0

    # Funcion constructora o inicializadora
    def __init__(self, pais, num_jugador, nombre, posicion, importe):
        self.pais = pais
        self.num_jugador = num_jugador
        self.nombre = nombre
        self.posicion = posicion
        self.importe = importe

    def __str__(self):
        cadena = "Pais: " + str(self.pais)
        cadena += " | Num Jugador: " + str(self.num_jugador)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Posicion: " + str(self.posicion)
        cadena += " | Importe: " + str(self.importe)
        return cadena


def principal():
    figurita1 = Figurita(1, 1, "a", 2, 5000)
    figurita2 = Figurita(1, 2, "b", 2, 5500)

    print(figurita1)
    print(figurita2)

    figurita1.pais = 15

    print(figurita1)
    print(figurita2)




def principal2():
    # LISTA / ARREGLO / ARRAY / VECTOR

    # Crear lista vacia
    v_lista = []        # list()

    # La funcion append, agrega un elemento al final de la lista conservando el contenido anterior
    v_lista.append(15)
    v_lista.append(35)
    v_lista.append(50)
    # v_lista = [ 15, 35, 50 ]

    # INDICES      0   1   2
    # v_lista = [ 15, 35, 50 ]

    # El tamaño del vector
    len(v_lista) # por su cantidad de elementos, 3

    print(v_lista[0])       # 15
    print(v_lista[2])       # 50

    v_lista[0] += 10
    # INDICES      0   1   2
    # v_lista = [ 25, 35, 50 ]

    # si solo queres leer el contenido del arreglo
    for i in v_lista:
        # i = 25 , 35, 50
        print(i)

    # si queres modificar algo en el arreglo
    for i in range(len(v_lista)):       # range(3)
        # i = 0, 1, 2
        if i != 2:
            v_lista[i] = v_lista[i] * 2

    # INDICES      0   1   2
    # v_lista = [ 50, 70, 50 ]


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo ")
    print("2 - Ordenar y Mostrar el arreglo ")
    print("3 - Vector De conteo/Acum")
    print("4 - Busqueda Secuencial")
    print("0 - ")
    op = int(input("Ingresar opcion: "))  # 3
    return op


def principal3():


    op = -1
    while op != 0:          # mientras op sea distinto de cero que ingrese al ciclo

        # Si yo igualo una variable a una funcion es porque estoy esperando que me retorne algun valor
        op = menu()     # 3

        if op == 1:
            print("Selecciona la op 1")

        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 0:
            pass


if __name__ == '__main__':
    principal()
