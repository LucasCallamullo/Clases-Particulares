import random

from registro import *

def validar_n():
    n = int(input("Ingresar cantidad a cargar: "))  # 0
    while n <= 0:
        n = int(input("Ingresar cantidad a cargar(DEBE SER POSITIVO): ")) # 3
    return n


def cargar():
    n = validar_n()
    v_juicios = []
    # codigo INT, descripcion STR, tipo(1, 15) , nombre STR, importe FLOAT
    for i in range(n):
        codigo = random.randint(1, 10)  # INT
        descripcion = random.choice("ABCDEF")   # STR
        tipo = random.randint(1, 15)    # INT
        nombre = random.choice("ABCDEF")      # STR
        importe = round(random.uniform(0.1, 10), 2)   # FLOAT

        j = Juicio(codigo, descripcion, tipo, nombre, importe)
        v_juicios.append(j)
        # v_juicios = [ J1, J2, J3 ]

    print("Se cargaron los juicios.")
    return v_juicios


# Opcion 2
def mostrar(v_juicios):
    # Ordenar el arreglo
    n = len(v_juicios)
    for i in range(n-1):
        for j in range(i+1, n):

            # la > es lo que determinar si esta de menor a mayor o mayor a menor
            if v_juicios[i].codigo > v_juicios[j].codigo:
                v_juicios[i], v_juicios[j] = v_juicios[j], v_juicios[i]

    # Solo mostrar los mayores a un importe "t" que se carga por teclado
    t = float(input("Ingresar un importe a superar: "))

    # Al final del listado indique cuantos objetos se mostraron
    cont = 0

    # indices       0   1   2
    # v_juicios = [ J1, J2, J3 ]
    #
    for i in range(len(v_juicios)):
        # i = 0, 1, 2
        if v_juicios[i].importe > t:
            print(v_juicios[i])
            cont += 1
            # acum += i.importe

    print("Se mostraron la cantidad de contadores:", cont)


# Opcion 3:
def generar_vector_conteo(v_juicios):
    # generar el vector de conteo/acum
    v_conteo = [0] * 15     # tipo(1, 15) 15 contadores

    # tipo         1-1 2-1  3   4
    # indices       0   1   2   3  4 --> los indices hacen referencia a cada tipo posible
    # v_conteo = [  1,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # rellenar el vector de conteo
    # indices       0   1   2
    # v_juicios = [ J1, J2, J3 ]
    # tipo          1   2   1
    for i in range(len(v_juicios)):
        # i = 0,    1, 2
        indice = v_juicios[i].tipo - 1
        v_conteo[indice] += 1
        # v_acum[indice] += v_juicios[i].importe

    #
    # Solo mostrar los contadores que superen una cantidad "m" que se carga por teclado
    m = int(input("Ingresar la cantidad a superar: "))

    # mostrar el vector de conteo
    for i in range(len(v_conteo)):
        # i = 0,    1, 2, 3, --> los indices hacen referencia a cada tipo posible

        if v_conteo[i] > m:
            print("Tipo de juicio:", i+1, "tiene la cantidad de:", v_conteo[i])

        # Solo mostrar los contadores que superen a 0
        if v_conteo[i] > 0:
            pass

        # Solo mostrar el tipo de juicio 3
        if i+1 == 3:
            pass


# Opcion 4
def buscar(v_juicios):

    nom = input("Ingresar nombre cliente a buscar: ")
    cod = int(input("Ingresar codigo a buscar: "))

    for i in range(len(v_juicios)):
        # i = 0, 1, 2
        if v_juicios[i].nombre == nom and v_juicios[i].codigo == cod:
            # si existe modificar su importe por un valor "imp" que se cargar por teclado
            # luego mostrar sus datos modificados
            print("Datos sin actualizar:", v_juicios[i])

            imp = float(input("Ingresar un nuevo importe: "))
            v_juicios[i].importe = imp

            print("Datos actualizados:", v_juicios[i])

            # aumentar 10% su importe
            v_juicios[i].importe += v_juicios[i].importe * 0.1

            # Solo mostrar el importe y la descripcion
            print("Descripción:", v_juicios[i].descripcion, " - Importe:", v_juicios[i].importe)

            # solo mostrar sus datos
            print(v_juicios[i])
            return

    print("No existe")


def menu():
    # ctrl + d
    print(" 1 - Cargar Arreglo.")
    print(" 2 - Mostrar arreglo.")
    print(" 3 - Vector Conteo Acum.")
    print(" 4 - Busqueda seucuencial.")
    print(" 5 - Salir.")
    op = int(input("Ingresar una opcion: "))    # 3
    return op


def principal():
    v_juicios = []

    op = -1
    while op != 5:  # mientras op sea distinto de cero, quiero que ingrese al ciclo while

        # si una variable es igual a una funcion significa que espera que la funcion devuelva algo
        op = menu()     # 3

        if op == 1:
            """
            1 - pedir n y validar n, y cargar arreglo
            """
            v_juicios = cargar()

        elif op == 2:
            """
            2 - mostrar el arreglo ordenado de menor a mayor por codigo
            """
            if len(v_juicios) > 0:
                mostrar(v_juicios)
            else:
                print("El vector no esta cargado")

        elif op == 3:
            """
            3 - Determinar y mostrar la cantidad de juicios que hay por cada "tipo de juicio"
            posible , 15 contdares
            """
            if len(v_juicios) > 0:
                generar_vector_conteo(v_juicios)
            else:
                print("El vector no esta cargado")

        elif op == 4:
            """
            4 - Determinar si existe un juicio cuyo nombre del cliente sea "nom", y cuyo codigo
            sea "cod" ambos se cargan por teclaod
            - Si existe- modificar
            - Si no existe - Informar
            - Detener la busqueda al primer resultado
            """
            if len(v_juicios) > 0:
                buscar(v_juicios)
            else:
                print("El vector no esta cargado")

        elif op == 5:
            print("Nos vemos")


if __name__ == '__main__':
    principal()