

from funciones import *


# Opcion 3:
def generar_vector_conteo(v_parlantes, x):

    # generar vector de conteo
    v_conteo = [0] * 21     # peso(1, 21) 21 * contadores

    # peso         1-1  2-1 3-2 4-3
    # indices       0   1   2   3   4   --> los indices tienen que referenciar a cada "peso" posible
    # v_conteo = [  2,  1,  0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # rellenar el vector
    # indices         0     1       2
    # v_parlantes = [P1,    P2,     P3]
    # peso            1      2       1
    for i in v_parlantes:
        # i = P1,   P2, P3
        v_conteo[i.peso-1] += 1
        # v_acum[i.peso-1] += i.importe

    # Mostrar el vector de conteo/acum

    # Calcular la mayor cantidad e indicar cual fue el peso con esa mayor cantidad
    mayor = None
    peso = None

    for i in range(len(v_conteo)):      # 21
        # i = 0,    1, 2, 3, ..., 20   --> los indices tienen que referenciar a cada "peso" posible

        # solo mostrar los contadores mayores a "x"
        if v_conteo[i] > x:
            print("El peso:", i+1, "Tiene la cantidad de parlantes de:", v_conteo[i])

        # solo mostrar los contadores mayores a 0
        if v_conteo[i] > 0:
            pass

        # solo mostrar los pesos mayores o iguales a 3  o a "x"
        if i+1 >= 3:
            pass

        #
        if mayor is None or v_conteo[i] > mayor:
            mayor = v_conteo[i]
            peso = i+1

    print("El mayor peso es:", peso, "con:", mayor)


# Opcion 4:
def busqueda_secuencial(v_parlantes, id, desc): # id = 2
    pos = -1
    # indices         0     1       2
    # v_parlantes = [P1,    P2,     P3]
    # id            1      2       3
    for i in range(len(v_parlantes)):
        # i = 0, 1, 2
        if v_parlantes[i].id == id and v_parlantes[i].descripcion == desc:
            pos = i
            break   # romper ciclos

    return pos  # 0 o + SI EXISTE  / -1 NO EXISTE


def menu():
    # ctrl + d
    print("1- Cargar Arreglo.")
    print("2- Mostrar Arreglo.")
    print("3- Vector Conteo/Acum.")
    print("4- Busqueda Secuencial.")
    print("0- Salir.")

    x = int(input("Ingresa la opcion: "))  # 2
    return x          # devolver o retornar


def principal():

    # crear nuestra lista vacia con la que vamos a trabajar
    v_parlantes = []

    op = -1

    while op != 0:      # mientras op sea distinto de cero, ingresar al ciclo

        # si una variable esta igualada a una funcion es porque espera que le devuelva algun resultado
        op = menu()         # 2

        if op == 1:
            n = validar_n()     # 3
            """
            1 - Cada vez que se ingrese a esta opcion debe generar nuevamente el arreglo
            """
            v_parlantes = []
            cargar_arreglo(v_parlantes, n)

        elif op == 2:
            """
                - Mostrar el arreglo Ordenado por ID
                - Solo muestres los que se encuentran entre un importe "t1" y "t2" que secargarn por teclado
            """

            ordenar_arreglo(v_parlantes)

            t1 = float(input("Ingrese el valor a superar: "))
            t2 = float(input("Ingrese el valor al que deba ser menor: "))
            mostrar_arreglo(v_parlantes, t1, t2)

        elif op == 3:
            """
                Determinar y mostrar la cantidad de parlantes que hay por cada tipo de peso posible
                # Peso(200, 220) * 21 contadores
                - Solo mostremos los contadores que tengan una cantidad mayor a "x" que se carga por teclado
                
            """
            x = int(input("Ingresar cantidad a superar: "))
            generar_vector_conteo(v_parlantes, x)

        elif op == 4:
            """
            4 - Determinar si existe un parlante cuyo id "id" y descripcion "desc" ambos valores
            que se cargan por teclado
            - Si existe modificar su precio por un valor "imp" que se carga por teclado, y despues
            mostrar su datos modificados
            - Si no existe, informar    
            - Deternerse al primer resultado
            """
            id = int(input("Ingresar Id a buscar: "))
            desc = input("Ingresar desc a buscar: ")
            pos = busqueda_secuencial(v_parlantes, id, desc)

            if pos >= 0:
                print("Datos No Modificados:", v_parlantes[pos])

                imp = float(input("Ingresar nuevo precio: "))
                v_parlantes[pos].importe = imp

                print("Datos Modificados:", v_parlantes[pos])

                # Aumentar el importe un 10%
                v_parlantes[pos].importe += v_parlantes[pos].importe * 0.1

                # SOlo mostrar su peso y su marca
                print("Peso:", v_parlantes[pos].peso, "y su marca es:", v_parlantes[pos].marca)

            else:
                print("No existe.")


if __name__ == '__main__':
    principal()
