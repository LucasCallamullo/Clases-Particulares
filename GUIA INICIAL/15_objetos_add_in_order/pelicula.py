

# Película: Define una clase Película con atributos como título, duración minutos(1, 59), genero(1, 4)
# # ( 1:Drama 2:Comedia 3:Romantico 4:Accion ), presupuesto sea mayor a 0
# 1 : cargar los registros en un arreglo ordenados por alguna atributo, en este caso titulo

# 2 : mostrar los datos a razon de uno por linea, pero mostrar las palabras correspondientes
# a cada valor en vez del genero, y que supere un importe t ingresado por telcado

# 3: determinar cuantas peliculas tienen una duracion tienen cada pelicula por genero, no debe mostrar
# los valores que sean iguales a 0, tambien debe solo mostrar los valores los minutos entre
# 92 y 96 incluidos ambos


# 4 : Generar un archivo binario que contenga a todas las peliculas que superen un presupuesto t
# iungresado por el usuario.

# 5 : Mostrar el archivo generado en el punto anterior indicando al final el promedio de los presupuestos
# acumulados de las peliculas grabadas en el archivo binario


# 7 : realizar una busqueda por titulo, si existe mostrar el registro y si el genero es drama o comedia
# tambien debe mostrar "opcion recomendada", si no existe informar al usuario

# 8 : Realizar una busqueda por genero, si existe mostrar si no existe ionformar al usuario

# 10: generar una matriz que acumule los presupuestos por duracion y genero.
import os.path
import pickle
import random


class Pelicula:
    # constructor de la clase
    # minutos(90, 99), genero(1,4 ) , importe > 0
    def __init__(self, titulo, genero, minutos, importe):
        self.titulo = titulo        # ctrl + d
        self.genero = genero
        self.minutos = minutos
        self.importe = importe

    # la funcion de print para mostrar nuestro objeto
    def __str__(self):
        genero_str = genero_to_str(self.genero)
        cadena = "Titulo: " + self.titulo
        cadena += " | Genero: " + genero_str
        cadena += " | Minutos: " + str(self.minutos)
        cadena += " | Importe: " + str(self.importe)
        return cadena


def genero_to_str(genero):      # 1 2 3 4   540 541 542 543
    #           540-540    541      542            543
    # genero      1-1     2-1         3-1         4-1
    # indices =    0        1           2           3
    genders = ["Drama", "Comedia", "Romantico", "Accion"]
    gen = genders[genero-1]         # gen = "Accion"
    return gen


# ====================================================================
#                   Opcion 1
# ====================================================================
def validar_n():
    n = int(input("Ingrese cantidad de Peliculas a cargar: "))
    while n <= 0:       # mientras n sea igual o menor a 0 (cero), que ingrese al ciclo while
        n = int(input("Ingrese cantidad de Peliculas a cargar (Un valor positivo): "))
    return n


def cargar_arreglo(v_peli, n):  # n = 5
    # minutos(90, 180), importe > 0
    # def __init__(self, titulo, minutos, importe):
    titulos = "ABCDE"
    for i in range(n):
        titulo = random.choice(titulos)         # strings
        minutos = random.randint(90, 99)       # enteros
        genero = random.randint(1, 4)       # enteros
        importe = round(random.uniform(0.1, 10), 2)
        peli = Pelicula(titulo, genero, minutos, importe)
        add_in_order(v_peli, peli)


# ====================================================
#               Opcion Alternativa CSV
# ====================================================
def cargar_desde_csv(v_consumo, name_csv="peliculas.csv"):
    archivo = open(name_csv, 'rt')
    pelis = archivo.readlines()

    cont = 0
    for i in pelis:
        cont += 1
        if cont > 2:
            #           0           1           2           3
            # linea = [ "id 12345", "titulo", "tipovehigculo", "cabina"..
            linea = i.split(",")
            id = int(linea[0])

            titulo = linea[1]

            importe = float(linea[2])
            minutos = int(linea[3])
            genero = int(linea[4])

            peli = Pelicula(titulo, genero, minutos, importe)

            add_in_order(v_consumo, peli)

    archivo.close()



def add_in_order(v_peli, peli):
    # v_peli = len(v_peli) = 0 ,  # primera vuelta  peli.titulo = B     peli.titulo = A
    # v_peli = len(v_peli) = 1 ,  # segunda vuelta  peli.titulo = A     peli.titulo = B
    izq, der = 0, len(v_peli) - 1

    while izq <= der:       # mientras izq sea menor o igual a derecha
        c = (izq + der) // 2
        if v_peli[c].titulo == peli.titulo:
            pos = c
            break
        elif v_peli[c].titulo > peli.titulo:        #   v[c] > es de menor a mayor
            der = c - 1                             #   v[c] < es de mayor a menor
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_peli[pos:pos] = [peli]


# ====================================================================
#                   Opcion 2
# ====================================================================
def mostrar_datos(v_peli, t):
    # v_peli = [P , P , P , P ]
    for i in v_peli:
        # i = P, P, P, P
        if i.importe > t:
            print(i)


# ====================================================================
#                   Opcion 3
# ====================================================================
# minutos(90, 99), genero(1,4 )
def generar_matriz(v_peli, num):

    # crear la matriz inicializada en 0
                        #   90-90
    columnas = 10       #   0       1       2       ....    9
                        #   1-1    2-1       3       4
    filas = 4           #   0       1       2       3
    matriz = [[0] * columnas for i in range(filas)]

    # v_peli = [P , P ,P ..
    for i in v_peli:
        # i = P
        matriz[i.genero-1][i.minutos-90] += 1


    # Mostrar la matriz
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):     #   0   1   2   3   4   5   6   7   8   9
            # 92 y 96 incluidos
            # if matriz[f][c] > 0 and 2 <= c <= 6:
            if matriz[f][c] > 0 and c+90 >= num:
                print("La cantidad de peliculas para el genero", genero_to_str(f+1), "y los minutos:", c+90)
                print("La cantidad total:", matriz[f][c])
                print("=" * 50)


# ====================================================================
#                   Opcion 4
# ====================================================================
def generar_archivo_binario(v_peli, fd, t):
    m = open(fd, "wb")
    se_creo_nuevo_archivo = False
    for i in v_peli:
        # i = P, P, P, P
        if i.importe > t:
            pickle.dump(i, m)
            se_creo_nuevo_archivo = True
            m.flush()

    if se_creo_nuevo_archivo:
        print("Se genero un archivo con peliculas que superan el importe:", t)
    else:
        print("No se genero un archivo nuevo en esta oportunidad.")
    m.close()


# ====================================================================
#                   Opcion 5
# ====================================================================
def mostrar_archivo_binario(v_peli, fd):
    if os.path.exists(fd):
        m = open(fd, "rb")
        tam = os.path.getsize(fd)       # len(v_peli) 100

        # crear promedio
        cant, acum = 0, 0

        # [ binary   binary  binary     binary         ]
        #   25          50     75       100
        while m.tell() < tam:
            peli = pickle.load(m)
            print(peli)
            cant += 1
            acum += peli.importe
        m.close()

        prom = 0
        if cant > 0:
            prom = acum / cant
        print("El promedio del presupuesto de las Peliculas en el archivo es:", prom)

    else:
        print("Primero debe ingresar por la opcion 4.")


# ====================================================================
#                   Opcion 7
# ====================================================================
def busqueda_binaria(v_peli, tit):      # E
    # v_peli         = [ P  P  P   P   P  P ]   # 6 pelis, # len(v_peli = 6 )
    #        Titulos   [ A  A  A   B   C  D ]
    #                          2       4
    izq, der = 0, len(v_peli) - 1
    # izq = 3 , 5
    while izq <= der:
        c = (izq + der) // 2
        if v_peli[c].titulo == tit:
            return c

        if v_peli[c].titulo > tit:
            der = c - 1
        else:
            izq = c + 1
    return -1


def busqueda_secuencial(v_peli, gen):
    for i in range(len(v_peli)):
        # i = 0 1 2 3 etc
        if v_peli[i].genero == gen:
            return i
    return -1


# ====================================================================
#                   Opcion 10
# ====================================================================
def genarar_matriz_op10(v_peli):
    columnas = 10       #   0       1       2       ....    9
                        #   1-1    2-1       3       4
    filas = 4           #   0       1       2       3
    matriz = [[0] * columnas for i in range(filas)]

    # v_peli = [P , P ,P ..
    for i in v_peli:
        # i = P
        matriz[i.genero-1][i.minutos-90] += i.importe

    # Mostrar la matriz
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):     #   0   1   2   3   4   5   6   7   8   9
            # 92 y 96 incluidos
            # if matriz[f][c] > 0 and 2 <= c <= 6:
            if matriz[f][c] > 0 and c+90 >= 92:
                print("La cantidad de peliculas para el genero", genero_to_str(f+1), "y los minutos:", c+90)
                print("La cantidad total:", matriz[f][c])
                print("=" * 50)


def menu():
    print("=" * 50)
    # alt + 92 = \
    print("1 - Cargar arreglo."
          "\n 2 - Mostrar arregl"
          "\n 3 - "
          "\n 4 - Generar Archivo Binario"
          "\n 5 - Leer Archivo Binario, Mostrar Promedio"
          "\n 0 - Salir.")
    x = int(input("Ingresar una opcion: "))
    return x


def principal():
    # Vector / Lista / Arreglo principal
    v_peli = []         # list()

    # Archivo binario con el que vamos a trabajar
    fd = "datos.dat"

    # validar que paso por la opcion 1
    validar_op1 = False

    op = -1
    while op != 0:

        op = menu()

        if not validar_op1:
            if op == 1:
                n = validar_n()
                cargar_arreglo(v_peli, n)
                validar_op1 = True
            else:
                print("Debe pasar primero por la opcion 1.")

        else:
            if op == 1:
                n = validar_n()
                cargar_arreglo(v_peli, n)

            elif op == 2:
                t = float(input("Importe a superar: "))
                mostrar_datos(v_peli, t)

            elif op == 3:
                num = int(input("Ingresar minutos a superar (90, 99): "))
                generar_matriz(v_peli, num)

            elif op == 4:
                t = float(input("Presupuesto a superar: "))
                generar_archivo_binario(v_peli, fd, t)

            elif op == 5:
                mostrar_archivo_binario(v_peli, fd)

            elif op == 7:
                tit = input("Ingresar Titulo a buscar: ")
                pos = busqueda_binaria(v_peli, tit)

                if pos >= 0:
                    print(v_peli[pos])

                    recomendados = [1, 2]
                    if v_peli[pos].genero in recomendados:
                        pass

                    if v_peli[pos].genero == 1 or v_peli[pos].genero == 2:
                        print("Opcion recomendada")
                else:
                    print("No se encontro el titulo buscado.")

            elif op == 8:
                gen = int(input("Ingrese un valor del (1, 4): "))
                pos = busqueda_secuencial(v_peli, gen)

                if pos >= 0:
                    print(v_peli[pos])

                    # remplazes su presupuesto actual por un valor x ingresado por teclado.
                    x = float(input("Nuevo importe para reemplazar: "))
                    v_peli[pos].importe = x

                    # que tenga una aumento del 10%
                    # v_peli[pos].importe = v_peli[pos].importe + v_peli[pos].importe * 0.1

                    print(v_peli[pos])
                else:
                    print("No se encontro el genero buscado.")

            elif op == 10:
                genarar_matriz_op10(v_peli)

            elif op == 6:
                for i in v_peli:
                    print(i)


if __name__ == '__main__':
    principal()
