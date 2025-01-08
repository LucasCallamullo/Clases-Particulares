import os.path
import pickle
import random
from registro import *


# ============== Opcion 1 ============================
def validar_n():
    n = int(input("Ingresar cantidad de Estudiantes a cargar en el arreglo: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de Estudiantes a cargar en el arreglo(debe ser positivo): "))
    return n


def cargar_arreglo(v_est, n):
    for i in range(n):  # n = 3         0           1       2
        legajo = random.randint(1, 15)
        curso = random.randint(1, 17)
        aula = random.randint(540, 555)
        cuestionarios = random.randint(1, 20)
        nombre = random.randint(1, 4)
        est = Estudiante(legajo, curso, aula, cuestionarios, nombre)
        add_in_order(v_est, est)


def add_in_order(v_est, est):       #
    izq, der = 0, len(v_est) - 1    # len(v_est) = 0
                                    # segunda vuelta
                                    # v_est = [ E1 ] E1.legajo = 5      E2.legajo = 3

    while izq <= der:
        c = (izq + der) // 2
        if v_est[c].legajo == est.legajo:
            pos = c
            break
        elif v_est[c].legajo > est.legajo:      # si se come al vector > es menor a mayor
            der = c - 1                         # si se come al objeto > es mayor a menor
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    #           0    1
    # v_est = [ E2, E1 ]
    v_est[pos:pos] = [est]


# ============ opcion 2
def mostrar_datos(v_est):
    for i in v_est:
        # v_vest = [ E, E, E ]
        # i = E, E, E
        print(i)


# ================== opcion 3
def generar_matriz(v_est):

    filas = 17      # curso ( 1, 17)    17 - 1 + 1 = 17
    columnas = 16   # aula  (540, 555)  555 - 540 + 1 = 16

    # generar la matriz
    matriz = [[0] * columnas for i in range(filas)]

    # completar la cantidad la matriz.
    for i in v_est:
        # i = E , E, E
        matriz[i.curso-1][i.aula-540] += 1
        # matriz[i.curso-1][i.aula-540] += i.cuestionarios

    return matriz


def mostrar_matriz(matriz):
    # Mnostrar matriz
    for f in range(len(matriz)):    # f = cursos =  0, 1, 2, ..., 16
        for c in range(len(matriz[0])):         # c = aulas = 0, 1, 2, ..., 15
            if matriz[f][c] > 0 and c+540 >= 545:
                curso = "1K" + str(f+1)
                print("La cantidad de alumnos del curso", curso, "Y el aula", c+540)
                print("La cantidad es:", matriz[f][c])
                print("=" * 50)


# ================== opcion 4
def generar_archivo(fd, v_est, x):

    m = open(fd, "wb")  # write binary  escribiendo sobre el archivo binario

    # que les pida mostrar la cantidad de estudiantes que se guardaron en el archivo:
    cont = 0

    for i in v_est:
        # i = E1 , E2, E3
        # if i.cuestionarios >= 10:
        if i.cuestionarios > x:
            pickle.dump(i, m)
            m.flush()           # no es necesario
            cont += 1

    print("La cantidad de estudiantes cargados en el archivo es:", cont)

    m.close()           # SI VA SI O SI


# ================== opcion 5
def mostrar_archivo(fd):

    if os.path.exists(fd):      # si existe el archivo
        m = open(fd, "rb")      # read binary abrir el archivo en modo lectura
        tam = os.path.getsize(fd)   # obtiene el tamaño real del archivo en bytes  = 70 bytes

        # vector = [ E , E, E ]

        # f d   = [ E1       E2           E3 ]
        #         0     25       50          70
        cont, acum = 0, 0
        while m.tell() < tam:
            est = pickle.load(m)
            print(est)

            # if est.curso == 13:
            acum += est.cuestionarios
            cont += 1

        if cont > 0:
            prom = acum / cont
            print("El promedio de los alumnos en el archivo es:", prom)

        m.close()


    else:               # el camino de no existe
        print("El archivo no existe, ingrese primero por la opcion 4.")


def busqueda_binaria(v_est, leg):
    izq, der = 0, len(v_est) - 1

    while izq <= der:
        c = (izq + der) // 2
        if v_est[c].legajo == leg:
            return c            # 0 1 2 3 4 5...
        elif v_est[c].legajo > leg:      # si se come al vector > es menor a mayor
            der = c - 1                  # si se come al objeto > es mayor a menor
        else:
            izq = c + 1
    return -1       # no existe


def busqueda_secuencial(v_est, nombre):
    for i in range(len(v_est)):
        if v_est[i].nombre == nombre:
            return i
    return -1


def menu():
    print("=" * 50)
    print(" 1 - Cargar arreglo."
          "\n 2 - Mostrar datos."
          "\n 3 - Matriz."
          "\n 4 - Generar archivo."
          "\n 5 - Mostrar archivo."
          "\n 6 - Busqueda secuencial."
          "\n 7 - Busqueda binaria.")

    return int(input("Ingresar la opcion: "))


def main():


    # vector/arreglo principal
    v_est = []

    # nombre del archivo binario
    fd = "estudiantes.dat"

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_est, n)

        elif op == 2:
            mostrar_datos(v_est)

        elif op == 3:
            matriz = generar_matriz(v_est)
            mostrar_matriz(matriz)

        elif op == 4:
            # supongamos que nos piden guardar los que tengan una cantidad x o mas de cuestionarios aprobados
            # donde x se carga por teclado
            x = int(input("Cantidad de cuestionarios aprobados a superar: "))
            generar_archivo(fd, v_est, x)

        elif op == 5:
            mostrar_archivo(fd)

        elif op == 7:
            # buscar por legajo leg, un estudiante que cumpla con ese legajo, si existe modifcar su cantidad
            # de cuestionarios aprobados por 15 y mostrar todos sus datos si no existe informar con un mensaje.
            leg = int(input("Ingresar legajo a buscar: "))
            pos = busqueda_binaria(v_est, leg)
            if pos >= 0:
                # mostrar todos los datos
                print(v_est[pos])

                # modificar algun atributo
                # v_est[pos].cuestionarios = 15

                if v_est[pos].cuestionarios > 10:
                    print("Aprobado")
                else:
                    print("Desaprobado")


                # si tuvieramos un precio con un recargo del 10%
                # v_est[pos].precio = v_est[pos].precio + v_est[pos].precio * 0.1

                # por ahi les pide mostrar solo los atributos
                # print(v_est[pos].cuestionarios)

            else:
                print("No existe el estudiante buscado por ese legajo.")



if __name__ == '__main__':
    main()
