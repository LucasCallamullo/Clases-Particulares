
# Libro: Define una clase Libro con atributos como título, género(1, 10), precio

# Se pide cargar el arreglo ordenado todo el tiempo por genero
# Se pide mostrar el arreglo
import pickle
import random


class Libro:
    # Constructor del objeto    # ctrl + c = copiar ; ctrl + v = pegar  ; ctrl + x = cortar
    def __init__(self, titulo, genero, precio, year):
        self.titulo = titulo        # ctrl + d
        self.genero = genero
        self.precio = precio
        self.year = year

    # es su funcion de print del objeto
    def __str__(self):
        # (531: Ficción, 532: Romantico, 533: Ciencia, 534: Misterio)

        # self.genero(1,4)
        #               531-531       532-531     533-531     534-531
        #                   1-1         2-1        3-1         4-1
        # indices           0           1           2           3       4       5       6   7   8
        desc_generos = ("Ficcion", "Romantico", "Ciencia", "Misterio")

        cadena = "Titulo: " + self.titulo
        cadena += " | Genero: " + desc_generos[self.genero-1]
        cadena += " | Precio: " + str(self.precio)
        cadena += " | Año: " + str(self.year)
        return cadena


# =============================================================================
#                       Opcion 1
# =============================================================================
def cargar_arreglo(v_libro, n):
    titulos = "ABCD"
    for i in range(n):      # n = 5
        # 0 1
        titulo = random.choice(titulos)
        genero = random.randint(1, 4)
        precio = round(random.uniform(0.1, 10), 2)
        year = random.randint(2000, 2020)
        librito = Libro(titulo, genero, precio, year)
        add_in_order(v_libro, librito)


def add_in_order(v_libro, librito):
    # len(v_libro) = 0      # primera vuelta    librito.genero = 5
    # len(v_libro) = 1      # segunda vuelta    librito.genero = 4

    izq, der = 0, len(v_libro) - 1

    while izq <= der:           # mientras
        c = (izq + der) // 2        #
        if v_libro[c].genero == librito.genero:
            pos = c
            break
        elif v_libro[c].genero > librito.genero:
            der = c - 1                     # der = -1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
                                            #       0                       1
    v_libro[pos:pos] = [librito]            # librito.genero = 4, primer librito.genero = 5


# =============================================================================
#                       Opcion 2
# =============================================================================
def mostrar_datos(v_libro):
    #            0  1  2  3  4
    # v_libro = [L, L, L, L, L]
    for i in v_libro:
        # i = L, L
        print(i)


# =============================================================================
#                       Opcion 4
# =============================================================================
def generar_archivo(fd, v_libro, x):
    m = open(fd, "wb")
    #            0  1  2  3  4
    # v_libro = [L1, L2, L3, L4, L5]
    for i in v_libro:
        # i = L1    ; L2    ; L3    ; L4    ; L5
        if i.year > x and (i.genero == 3 or i.genero == 4):
            pickle.dump(i, m)
            m.flush()    # No es necesaria
    m.close()





def menu():
    print("=" * 50)
    # alt + 92 = \
    print(" 1 - Cargar arreglo."
          "\n 2 - Mostrar Datos."
          "\n "
          "\n 4 - Generar Archivo Binario."
          "\n 5 - Mostrar Archivo Binario."
          "\n "
          "\n 0 - Salir.")

    op = int(input("Ingrese una opcion: "))
    return op


def principal():

    # nuestra vector/lista/arreglo
    v_libro = []    # tam = 0


    # archivo principal
    fd = "libros.dat"


    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = int(input("Ingrese cantidad de libros a cargar: "))
            cargar_arreglo(v_libro, n)


        elif op == 2:
            mostrar_datos(v_libro)

        elif op == 4:
            x = int(input("Ingresar año a superar: "))
            generar_archivo(fd, v_libro, x)

        elif op == 5:
            pass




if __name__ == '__main__':
    principal()
