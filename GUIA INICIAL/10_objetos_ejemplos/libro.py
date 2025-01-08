

 # Libro: Define una clase Libro con atributos como título, género(0, 4), el precio es mayor a 0,
 # autor es un valor entre 1, 19

 # 1 ) cargar arreglo con una cantidad n de libros donde n es un valor ingresado por teclado
 # 2 ) Mostrar los datos ordenados por autor de mayor a menor, pero solo aquellos datos que superen un importe t
 #      donde t es un valor ingresado por teclado


import random


# registro/ clase/ objeto
class Libro:
    # genero(0,4)   ,  precio > 0           ; autor (1, 19)
    def __init__(self, titulo, genero, precio, autor):
        self.titulo = titulo            # ctrl + d
        self.genero = genero
        self.precio = precio
        self.autor = autor

    def __str__(self):
        cadena = "Titulo: " + self.titulo          # ctrl + d
        cadena += " | Genero: " + str(self.genero)
        cadena += " | Precio: " + str(self.precio)
        cadena += " | Autor: " + str(self.autor)
        return cadena


# Opcion 1
def validar_n():
    n = int(input("Ingresar cantidad de libros a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de libros a cargar(debe ser positivo): "))
    return n


def cargar_arreglo(v_libro, n):

    # genero(0,4)   ,  precio > 0           ; autor (1, 19)
    # def __init__(self, titulo, genero, precio, autor):
    titulos = ("A", "B", "C", "D")
    for i in range(n):
        titulo = random.choice(titulos)
        genero = random.randint(0, 4)
        # random para numeros flotantes
        precio = round(random.uniform(0.1, 10), 2)
        autor = random.randint(1, 19)
        lib = Libro(titulo, genero, precio, autor)
        # agregar elementos a la lista
        v_libro.append(lib)
        #
        # v_libro = [ L, L, L, L, L ]


# Opcion 2
def ordenar(v_libro):
    n = len(v_libro)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_libro[i].autor < v_libro[j].autor:
                v_libro[i], v_libro[j] = v_libro[j], v_libro[i]


def mostrar_datos(v_libro, t):
    # v_libro = [ L, L, L, L, L ]
    # for i in range(len(v_libro)):
         # 0, 1, 2, 3, 4
    #    if v_libro[i].precio > t:
    #        print(v_libro[i])

    # print("=" * 50)

    # v_libro = [ L, L, L, L, L ]
    for i in v_libro:
        # i = L
        if i.precio > t:
            print(i)


def menu():
    print("=" * 50)
    print(" 1 - Cargar arreglo."
          # alt + 92 = \        ; ctrl + d
          "\n 2 - Mostrar datos."
          "\n 3 - "
          "\n 4 - "
          "\n 0 - Salir.")
    return int(input("Ingresar una opcion: "))


def main():

    # vector/arreglo/lista principal con la que vamos a trabajar.
    v_libro = []                # list()

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_libro, n)

        elif op == 2:
            ordenar(v_libro)
            t = float(input("Ingresar importe a comparar: "))
            mostrar_datos(v_libro, t)

        elif op == 3:
            pass

        elif op == 4:
            pass

        #  funciones que creamos para cooroborar que vamos haciendo bien las cosas
        elif op == 6:
            for i in v_libro:
                print(i)


# main
if __name__ == '__main__':
    main()
