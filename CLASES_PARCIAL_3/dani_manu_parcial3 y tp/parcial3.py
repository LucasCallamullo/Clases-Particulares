

from funciones import *


# Opcion 3
def generar_vector_conteo(v_mascotas, x):
    # generar vector conteo acum
    v_conteo = [0] * 10     # edad(1, 10) 10 contadores

    #
    # edad(1,10)    1-1 2-1 3   4
    # indices       0   1   2   3   4  --> los indices hacen referencia a cada posible edad
    # v_conteo = [  1,  1,  0,  0,  0,  0,  0,  0, 0, 0]

    # rellenar el vector de conte/acum
    # indices           0       1       2
    # v_mascotas = [    M1,     M2,     M3]
    # edad              1       2       1
    for i in v_mascotas:
        # i = M1,   M2, M3
        v_conteo[i.edad-1] += 1
        # v_acum[i.edad-1] += i.importe

    # Al final de este listado mostrar cual fue la edad que tuvo la mayor cantidad de mascotas
    mayor = None
    edad = None

    # mostrar el vector de conteo/acum
    for i in range(len(v_conteo)):  # range(10)
        # i = 0,    1, 2, 3, .. --> --> los indices hacen referencia a cada posible edad

        # Solo mostrar los contadores que superen una cantidad "x"
        if v_conteo[i] > x:
            print("Edad:", i+1, "tiene la cantidad de:", v_conteo[i])

        # Solo mostrar los contadores que superen una cantidad 0
        if v_conteo[i] > 0:
            pass

        # Solo mostrar las edades superiores o iguales a 3
        if i+1 >= 3:
            pass

        if mayor is None or v_conteo[i] > mayor:
            mayor = v_conteo[i]
            edad = i+1

    print("Edad:", edad, "tuvo la mayor cantidad con:", mayor)


# Opcion 4
def busqueda_secuencial(v_mascotas, e, nom):    # e = 2
    # indices           0       1       2
    # v_mascotas = [    M1,     M2,     M3]
    # edad              1       2       1
    pos = -1
    for i in range(len(v_mascotas)):
        # i = 0, 1, 2
        if v_mascotas[i].edad == e and v_mascotas[i].nombre == nom:
            pos = i
            break   # rompe ciclos

    return pos     # 0 o + SI EXISTE    / -1 NO EXISTE


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar Arreglo.")
    print("3 - ")
    print("4 - ")
    print("0 - Salir.")

    op = int(input("Ingresar opcion: "))  # 2
    return op       # devolver o retornar op


def principal():

    # nuestra lista con la que vamos a trabajar
    v_mascotas = []

    op = -1
    while op != 0:      # mientras op sea distinto de cero, ingrese al ciclo while

        # si una variable esta igualada a una funcion es porque espero que la funcion me devuelva algun valor
        op = menu()         # 2

        if op == 1:
            n = validar_n()
            """
            1 - 
            - cada vesz que se ingrese a esta opcion cargar nuevamente el arreglo
            """
            v_mascotas = []
            cargar_arreglo(v_mascotas, n)

        elif op == 2:
            """
                2 - Mostrar el arreglo ordenado de menor a mayor por ID, 
                Solo muestre aquellos que superan un importe "t" donde t se ingresa por teclado
            """
            ordenar_arreglo(v_mascotas)

            t = float(input("Ingresar importe a superar: "))
            mostrar_arreglo(v_mascotas, t)

        elif op == 3:
            """
                3 - Determinar y mostrar la cantidad de mascotas por cada edad posible (edad 1,10) 
                10 contadores, 
                - Solo mostrar los contadores que superen una cantidad "x" que se ingresa por teclado
            """
            if len(v_mascotas) > 0:
                x = int(input("Ingresar cantidad a superar: "))
                generar_vector_conteo(v_mascotas, x)
            else:
                print("Ingrese a la opcion 1")

        elif op == 4:
            """
            4 - Determinar si existe una mascota cuya edad sea igual "e" y tenga un nombre "nom" ambos valores
            se ingresan por teclado, 
            - Si existe modifque su importe por un valor "imp" que se carga por teclado, y luego mostrar los
            datos modificados
            - Si No existe, Informar
            - Detener la busqueda al primer resultado
            """
            if len(v_mascotas) > 0:

                e = int(input("Ingresar edad a buscar: "))
                nom = input("Ingresar nombre a buscar: ")
                pos = busqueda_secuencial(v_mascotas, e, nom)

                if pos >= 0:
                    print("Datos sin modificar:", v_mascotas[pos])

                    imp = float(input("Ingresar nuevo importe: "))
                    v_mascotas[pos].importe = imp

                    print("Datos modificados:", v_mascotas[pos])

                    # aumentar un 10% el importe
                    v_mascotas[pos].importe += v_mascotas[pos].importe * 0.1

                    # solo mostrar su id y su importe
                    print("ID:", v_mascotas[pos].id, "y su importe:", v_mascotas[pos].importe)

                else:
                    print("No existe.")


if __name__ == '__main__':
    principal()


