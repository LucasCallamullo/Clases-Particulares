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



if __name__ == '__main__':
    main()
