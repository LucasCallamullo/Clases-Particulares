import random
from reg import *


def validar():
    n = int(input("Ingrese la cantidad de estudiantes a cargar: "))
    while n <= 0:
        n = int(input("Ingrese la cantidad de estudiantes a cragar: "))
    return n

def cargar_arreglo(v, n):

    for i in range(n):
        legajo = random.randint(400000, 460000)
        nombre = random.choice(["Simona", "Laura", "Amelie", "Lourdes", "Selene"])
        curso = random.randint(1, 17)
        aula = random.randint(540, 555)
        cuest_aprobados = random.randint(1, 32)

        estud = Estudiante(legajo, nombre, curso, aula, cuest_aprobados)
        add_in_order(v, estud)

    print("Se cargo el arreglo.")


def add_in_order(v, estud):

    izq, der = 0, len(v) - 1

    while izq <= der:
        c = (izq + der) // 2

        if v[c].legajo == estud.legajo:
            pos = c
            break

        elif v[c].legajo > estud.legajo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [estud]



def menu():
    print("------------------------------")
    print("1- Cargar arreglo. ")
    print("2- Mostrar arreglo. ")
    print("3- Cantidad de alumnos. ")
    print("4- Generar archivo binario. ")
    print("5- Mostrar archivo binario. ")
    op = int(input("Ingrese una opcion: "))
    return op

def principal():

    v = []

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar()
            cargar_arreglo(v, n)

        elif op == 2:
            for i in v:
                print(i)

        elif op == 3:
            pass

        elif op == 4:
            pass

        elif op == 5:
            pass



if __name__ == '__main__':
    principal()