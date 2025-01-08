import os.path
import pickle
import random
from registro import *


# =========================================================================
#                       OPCION 1
# =========================================================================
def validar_n():
    n = int(input("Ingresar cantidad de estudiantes a cargar: "))       # 0
    while n <= 0:   # mientras n sea menor o igual a cero
        n = int(input("Ingresar cantidad de estudiantes a cargar (DEBE SER POSITIVO): ")) # 3
    return n        # 3


def cargar_arreglo(v_estudiantes, n):
    tupla_nombre = ("Lucas", "Lauti", "Lula")

    # legajo INT > 0 , nombre STR, curso INT (1, 17), aula (540, 555), importe FLOAT
    for i in range(n):      # 3 vueltas
        # i = 0, 1
        legajo = random.randint(1, 10)    # INT
        nombre = random.choice("ABCDEF")        # STR
        curso = random.randint(1, 17)
        aula = random.randint(540, 555)
        importe = round(random.uniform(0.1, 10), 2) # Float con dos decimales
        documento = random.randint(1, 2)

        est = Estudiante(legajo, nombre, curso, aula, importe, documento)
        add_in_order(v_estudiantes, est)

    print("Se cargo el arreglo.")


def add_in_order(v_estudiantes, est):
    # E1 Legajo = 3
    # E2 legajo = 1
    # v_estudiantes = [E1, ]        # 1

    izq, der = 0, len(v_estudiantes) - 1

    # izq = 0
    # der = -1

    while izq <= der:
        c = (izq + der) // 2    # 0

        if est.legajo == v_estudiantes[c].legajo:
            pos = c
            break

        # si esta ordenado de menor a mayor o mayor a menor es la boquita
        elif est.legajo < v_estudiantes[c].legajo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # indices           0   1   2
    # v_estudiantes = [ E2, E1, ]
    v_estudiantes[pos:pos] = [est]          # no te olvides los corchetes


# =========================================================================
#                       OPCION 2
# =========================================================================
def mostrar_arreglo(v_estudiantes):

    # indices           0   1   2
    # v_estudiantes = [ E1, E2, E3]
    for i in v_estudiantes: # leer contenido del arreglo
        # i = E1,    E2, E3          # la "i" toma el valor de cada elemento del arreglo

        # solo mostrar los que superan un importe "x"
        # if i.importe > x:
        print(i)


# =========================================================================
#                       OPCION 4
# =========================================================================
def generar_archivo_binario(v_estudiantes, fd, t):
    m = open(fd, "wb")  # write binary, sobreescribe tod0 el contenido del archivo, crea el archivo si no existiera

    # indices           0   1   2
    # v_estudiantes = [ E1, E2, E3]
    for i in v_estudiantes: # leer el contenido
        # i = E1, E2, E3
        if i.importe > t:
            # primer parametro = lo que queremos guardar
            # segundo parametro = donde se guarda
            pickle.dump(i, m)
            m.flush()       # esto es opcional

    print("se genero el archivo binario.")
    m.close()   # esto es obligatorio


# =========================================================================
#                       OPCION 5
# =========================================================================
def mostrar_archivo_binario(fd):

    if os.path.exists(fd):      # pregunta si existe el archivo binario como tal

        tam = os.path.getsize(fd)    # tamaño/size, nos dice/nos devuelve el tamaño en bytes del archivo binario
        m = open(fd, "rb")  # read binary , leer archivo binario, modo solo lectura

        # indices          0    1   2   3
        # v_estudiantes = [E1,  E2, E3, E4]

        # estudiantes.dat = [E1,    E2,     E3,     E4] 1000 bytes
        # m.tell()          0  250    500      750     1000

        # mostrar el archivo binario pero al final del listado mostrar el promedio de los importes
        # de los archivos binarios que se guardaron

        # promedio = acumulado ( de importes ) / cantidad
        acum = 0
        cont = 0

        while m.tell() < tam:
            est = pickle.load(m)    # recibe por parametro a la variable que hace referencia al archivo o sea "m"

            # solo mostrar los que estan entre el curso 1k1 y 1k10
            # if est.curso >= 1 and est.curso <= 10:
            if 1 <= est.curso <= 10:
                print(est)
                cont += 1
                acum += est.importe

        # calcular promedio
        prom = 0
        if cont > 0:
            prom = acum / cont
        print("El promedio de los importes mostrados fue:", prom)

        m.close()       # es obligatorio

    else:
        print("No existe el archivo binario:", fd, "ingrese primero a la opcion 4")


# =========================================================================
#                       OPCION 3
# =========================================================================
def generar_matriz(v_estudiantes, x):

    # Crear la matriz
    f = 17      # f = filas = curso(1, 17) = lim_superior - lim_inferior + 1 = 17 - 1 + 1 = 17
    c = 16      # c = columnas = aula(540, 555) = lim_superior - lim_inferior + 1 = 555 - 540 + 1 = 16
    matriz = [ [0] * c for i in range(f) ]

    # curso(1, 17)     1-1 2-1   ...         17
    # fila_indices      0   1   2   ...     16

    # aula(540, 555) 540-540 541 542 543 ... 555
    # columnas_indices  0   1   2   3   ... 15

    # matriz[f][c] --> se accede al reves a como lo creamos
    # [ [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   ...,
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    ]

    #
    # rellenar la matriz
    # indices           0   1   2
    # v_estudiantes = [E1, E2, E3]
    for i in v_estudiantes:
        # i = E1,   E2,     E3
        # matriz[f][c]
        matriz[i.curso - 1][i.aula - 540] += 1
        # matriz[i.curso - 1][i.aula - 540] += i.importe

    #
    # mostrar la matriz
    for f in range(len(matriz)):    # range(17)
        # f = 0, 1, 2, ..., 16

        for c in range(len(matriz[0])): # range(16)
            # c = 0, 1, 2, ..., 15

            # o comparen con el aula o con el curso
            if c+540 > x and matriz[f][c] > 0:
                print("Aula:", c+540, "| Curso:", f+1, "| Cantidad:", matriz[f][c])

            # solo mostrar los contadores/acumuladores que tengan un valor significativo o distinto de cero
            if matriz[f][c] > 0:
                pass    # print( )


# =========================================================================
#                       OPCION 6
# =========================================================================
def busqueda_binaria(v_estudiantes, leg):   # leg = 5

    # indices           0       1       2
    # v_estudiantes = [ E1  ,   E2,     E3 ]
    # legajo            3       4       5

    izq, der = 0, len(v_estudiantes) - 1
    # izq = 2
    # der = 2

    while izq <= der:
        c = (izq + der) // 2  # c = centro del arreglo = 2

        # if est.legajo == v_estudiantes[c].legajo:
        if leg == v_estudiantes[c].legajo:
            pos = c     # pos = c = 2
            # break
            return pos      # pos = 2   v_estudiantes[pos]  >= 0 Existe

        # elif est.legajo < v_estudiantes[c].legajo:
        elif leg < v_estudiantes[c].legajo:
            der = c - 1

        else:
            izq = c + 1

    return -1       # retorna -1 cuando no existe un objeto que cumpla mi criterio de busqueda



def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - Generar Matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Leer archivo Binario.")
    print("0 - Salir.")
    x = int(input("Ingresar la opcion: "))      #  1
    return x    # 1



def principal():

    # vector - Arreglo - lista de trabajo
    v_estudiantes = []      # list()

    # archivo binario
    fd = "estudiantes.dat"       # file description ; nombre del archivo

    op = -1
    while op != 0:
        # si una variable esta igualada a una funcion es porque espero que la funcion devuelva algo
        op = menu()     # 1

        if op == 1:
            n = validar_n()     # 3
            cargar_arreglo(v_estudiantes, n)

        elif op == 2:
            if len(v_estudiantes) > 0:
                mostrar_arreglo(v_estudiantes)
            else:
                print("El vector no esta cargado.")

        elif op == 3:
            """
            3 - Determinar cuántos alumnos rinden por curso y por aula. Mostrar únicamente 
            los conteos que correspondan a las aulas mayores o iguales a "x".
            """
            if len(v_estudiantes) > 0:
                x = int(input("Ingresar aula a superar: (540, 555): "))
                generar_matriz(v_estudiantes, x)
            else:
                print("El vector no esta cargado.")

        elif op == 4:
            """
            4 - generar archivo binario
            solo guardar los que superen un importe "t" que se carga por teclado
            
            - Generar archivo pero cada vez que se genere debe crearlo nuevamente "wb"
            - Generar archivo pero si ya esta creado agregar los nuevos objetos "ab"
            
            """
            if len(v_estudiantes) > 0:
                t = float(input("Importe a superar: "))
                generar_archivo_binario(v_estudiantes, fd, t)
            else:
                print("El vector no esta cargado.")

        elif op == 5:
            """
            5 - Mostrar el archivo del punto anterior
            
            - solo mostrar los que estan entre el curso 1k1 y 1k10
            """

            mostrar_archivo_binario(fd)

        elif op == 6:
            """ 
            6 - Buscar por legajo "leg" un estudiante y si su documento era "Pasaporte" realizarle un descuento
            del 22% mostrar sus datos antes y despues de la actualizacion, si no existe mostrar el mensaje
            "No existe un estudiante con el legajo <LEG>"
            """

            if len(v_estudiantes) > 0:
                leg = int(input("Ingresar legajo a buscar: "))
                pos = busqueda_binaria(v_estudiantes, leg)

                if pos >= 0:
                    print("Datos sin actualizar:", v_estudiantes[pos])

                    if v_estudiantes[pos].documento == 1:
                        # descuento
                        v_estudiantes[pos].importe -= v_estudiantes[pos].importe * 0.22

                    print("Datos actualizados:", v_estudiantes[pos])

                else:   # cuando pos es -1
                    print("No existe un estudiante con el legajo", leg)

            else:
                print("El vector no esta cargado.")


if __name__ == '__main__':
    principal()

