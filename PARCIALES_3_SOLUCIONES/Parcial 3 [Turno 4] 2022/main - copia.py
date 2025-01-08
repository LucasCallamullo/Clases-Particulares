import random


class Figurita:
    # pais (1, 32)   ; num_j (1, 19)    ; pos 0 4       ; valor = int
    def __init__(self, pais, num_j, nombre, pos, valor):
        self.pais = pais
        self.num_j = num_j
        self.nombre = nombre
        self.pos = pos
        self.valor = valor

    def __str__(self):
        # 0: arquero ; 1:defensa ; 2:volante ; 3:delantero
        new_pos = pos_to_str(self.pos)

        cadena = "Pais: " + str(self.pais)
        cadena += " | Num J: " + str(self.num_j)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Posicion: " + new_pos
        cadena += " | Valor: " + str(self.valor)
        return cadena


def pos_to_str(pos):
    # pos ( 0 , 3)
    # pos

    # ind           0              1        2           3
    posiciones = ["Arquero", "Defensa", "Volante", "Delantero"]
    return posiciones[pos]


# Opcion 1
def validar_n():
    n = int(input("INgresar cantidad de Figuritas a cargar: "))
    while n <= 0:
        n = int(input("INgresar cantidad de Figuritas a cargar(Ingrese un valor positvo): "))
    return n


def cargar_arreglo(v_figu, n):
    # pais (1, 32)   ; num_j (1, 19)    ; pos 0 4       ; valor = int
    # def __init__(self, pais, num_j, nombre, pos, valor):
    nombres = "ABCDE"
    for i in range(n):
        pais = random.randint(1, 32)
        num_j = random.randint(1, 19)
        nombre = random.choice(nombres)
        pos = random.randint(0, 3)
        valor = random.randint(1, 10)
        figu = Figurita(pais, num_j, nombre, pos, valor)
        v_figu.append(figu)


# opcion 2
def ordenar(v_figu):
    n = len(v_figu)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_figu[i].nombre > v_figu[j].nombre:
                v_figu[i], v_figu[j] = v_figu[j], v_figu[i]


def mostrar_datos(v_figu, v):
    cont = 0
    for i in v_figu:
        if i.valor > v:
            print(i)
            cont += 1

    print("La cantidad de figuritas que se mostraron fueron:", cont)


# opcion 3
def completar_v_conteo(v_figu):
    # pais(1, 32)

    #        1  2  3  4  ....                                                                            32
    # ind    0  1  2  3    . ...                                                                          31
    #       [5, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    v_conteo = [0] * 32

    for i in v_figu:
        v_conteo[i.pais-1] += 1
    return v_conteo


def mostrar_contador_op3(v_conteo, c):
    for i in range(len(v_conteo)):
        # i = 0, 1, 2, 3 ....
        if v_conteo[i] > c:
            print("La cantidad de figuritas del pais", i+1, "Son:", v_conteo[i])


# opcion 4
def busqueda_lineal(v_figu, p, j):
    for i in range(len(v_figu)):
        # i = 0, 1, 2, 3 ....
        if v_figu[i].pais == p and v_figu[i].num_j == j:
            return i
    return -1


def menu():
    print("=" * 50)
    print(" 1 - Cargar Arreglo."
          "\n 2 - Mostrar dats"
          "\n 3 - Contadores op 3"
          "\n 2 - "
          "\n 0 - Salir.")
    return int(input("Ingresar opcion: "))


def main():

    v_figu = []

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_figu, n)

        elif op == 2:
            ordenar(v_figu)
            v = int(input("Ingresar valor a superar: "))
            mostrar_datos(v_figu, v)

        elif op == 3:
            v_conteo = completar_v_conteo(v_figu)
            c = int(input("Ingresar una cantidad para superar en los contadores: "))
            mostrar_contador_op3(v_conteo, c)

        elif op == 4:
            p = int(input("Ingresar pais a buscar (1, 32): "))
            j = int(input("Ingresar num j a buscar(1, 19): "))

            pos = busqueda_lineal(v_figu, p, j)

            if pos >= 0:
                valor = int(input("Ingresar nuevo valor: "))

                # modificar valores en atributos
                v_figu[pos].valor = valor

                print(v_figu[pos])

            else:
                print("No encontramos la figurita buscada.")


        elif op == 6:
            for i in v_figu:
                print(i)


if __name__ == '__main__':
    main()
