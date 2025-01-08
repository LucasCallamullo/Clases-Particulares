import random

from registro import *


# =====================================================================
#                           Opcion 1
# =====================================================================
def validar_n():
    n = int(input("Ingresar la cantidad de juicios a cargar: "))    # 3
    while n <= 0:   # mientras n sea igual o menor a cero
        n = int(input("Ingresar la cantidad de juicios a cargar: "))

    return n    # 3


def cargar_arreglo(v_juicios, n):
    # codigo > 0 INT , descripcion STR, tipo(1, 15) INT, nombre STR, importe > 0 FLOAT
    for i in range(n):      # 3
        # i = 0, 1, 2
        codigo = random.randint(1, 10)  # INT   1
        descripcion = random.choice("ABCDEF")   # STR   "B"
        tipo = random.randint(1, 15)  # INT
        nombre = random.choice("ABCDEF")  # STR
        importe = round(random.uniform(0.1, 10), 2)   # FLOAT

        juicio_objeto = Juicio(codigo, descripcion, tipo, nombre, importe)
        v_juicios.append(juicio_objeto)
        # v_juicios = [J1, J2, J3]
    print("Se cargaron los", n, "juicios.")


# =====================================================================
#                           Opcion 2
# =====================================================================
def ordenar_arreglo(v_juicios):
    # Metodo de ordenamiento por seleccion directa

    # indices        0      1       2
    # v_juicios = [ J3,     J1,     J2]
    # codigo         2      4       3
    n = len(v_juicios)  # nos dice/nos devuelve el tamaño del vector, que esta dado por la cantidad de elementos

    for i in range(n-1):    # range(2)
        # i = 0,    1

        for j in range(i+1, n):     #range(
            # j = 1,    2
            # i = 0

            # la boquita define si esta ordenado de menor a mayor o mayor a menor
            if v_juicios[i].codigo > v_juicios[j].codigo:

                v_juicios[i], v_juicios[j] = v_juicios[j], v_juicios[i]


def mostrar_arreglo(v_juicios, t):

    # Indicar al final el promedio de importes de los juicios que se mostraron
    # promedio = acumulado(de importes) / cantidad
    acum = 0
    cont = 0

    # indices        0      1       2
    # v_juicios = [ J1,     J2,     J3]
    # importe         2      4       3
    for i in v_juicios:
        # i = J1 , J2, J3

        if i.importe > t:
            print(i)
            acum += i.importe
            cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los importes mostrados es:", prom)


# =====================================================================
#                           Opcion 3
# =====================================================================
def generar_vector_conteo(v_juicios, x):

    # generar vector de conteo/acum
    v_conteo = [0] * 15     # tipo(1000, 1014) 15 contadores

    # tipo         1-1  2   3   4   5   6                         15
    # indices       0   1   2   3   4 --> los indices hacen referencia a cada posible "tipo de juicio"
    # v_conteo = [  2,  1,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #

    # rellenar el vector de conteo/Acum
    # indices        0      1       2
    # v_juicios = [ J1,     J2,     J3]
    # tipo           1      2       1
    for i in v_juicios:
        # i = J1,       J2,     J3
        v_conteo[i.tipo-1] += 1
        # v_acum[i.tipo-1] += i.importe

    # mostrar el vector de conteo/acum
    for i in range(len(v_conteo)):  # range(15)
        # i = 0,    1, 2, ..., 14 --> los indices hacen referencia a cada posible "tipo de juicio"

        # Solo mostrar los contadores que superan una cantidad "x"
        if v_conteo[i] > x:
            print("Tipo de juicio:", i+1, "Tiene la cantidad de:", v_conteo[i])

        # Solo mostrar los contadores que superan una cantidad 0
        if v_conteo[i] > 0:
            pass

        # Solo mostrar los tipo de juicios que sean mayores o iguales a 3  "x"
        if i+1 >= 3:
            pass


# =====================================================================
#                           Opcion 4
# =====================================================================
def busqueda_secuencial(v_juicios, desc, cod):  # desc = Z
    # indices        0      1       2
    # v_juicios = [ J1,     J2,     J3]
    # descripcion    A      B       F
    pos = -1
    for i in range(len(v_juicios)):
        # i = 0,    1,  2
        if v_juicios[i].descripcion == desc and v_juicios[i].codigo == cod:
            pos = i
            break   # romper ciclos

    return pos  # 0 o + SI EXISTE / -1 NO EXISTE


def menu():
    # ctrl + d
    print(" 1 - Cargar Arreglo.")
    print(" 2 - Mostrar Arreglo.")
    print(" 3 - Vector de Conteo/acum.")
    print(" 4 - Busqueda Secuencial en el Arreglo.")
    print(" 0 - Salir.")
    op = int(input("Ingresar opcion: "))        # 2
    return op       # devolver o retornar op


def principal():

    # crear una lista / vector / arreglo de trabajo
    v_juicios = []

    op = -1
    while op != 0:          # mientras op sea distinto de cero, ingresar al ciclo

        # si una variable esta igualada a una funcion es porque espero que es funcion
        # me devuelva un resultado
        op = menu()     # 1

        if op == 1:
            n = validar_n()     # 3
            cargar_arreglo(v_juicios, n)

        elif op == 2:
            """ 
            2 - Mostrar los juicios ordenados por codigo de menor a mayor.
            Solo Mostrar los importes que superen un valor "t" que se ingresa por teclado
            
            """
            if len(v_juicios) > 0:
                ordenar_arreglo(v_juicios)

                t = float(input("Ingresar importe a superar: "))
                mostrar_arreglo(v_juicios, t)

            else:
                print("Debe ingresar a la opcion 1.")

        elif op == 3:
            """
            3 - Determinar y mostrar la cantidad de juicios por cada posible tipo de juicio(1, 15)
            15 contadores vector de conteo,
            - Solo mostrar los contadores que superen una cantidad "x" que se carga por teclado
            """
            if len(v_juicios) > 0:
                x = int(input("Ingresar cantidad a superar: "))
                generar_vector_conteo(v_juicios, x)

            else:
                print("Debe ingresar a la opcion 1.")

        elif op == 4:
            """
            4- Determinar si existe algun juicio con una descripcion "desc" y un codigo "cod"
            que se cargan por teclado.
            - si existe ---
            - Si no existe informar con el siguiente mensaje "No existe ese juicio"
            - detener al primer resultado encontrado
            """
            if len(v_juicios) > 0:
                desc = input("Ingresar descripcion a buscar: ")
                cod = int(input("Ingresar codigo a buscar: "))

                pos = busqueda_secuencial(v_juicios, desc, cod)

                if pos >= 0:
                    # si existe modificar su importe por un valor "imp" que se carga por teclado y luego
                    # mostrar su datos modificados.
                    print("Datos Sin Modificar:", v_juicios[pos])

                    imp = float(input("Ingresar nuevo importe: "))
                    v_juicios[pos].importe = imp

                    print("Datos Modificados:", v_juicios[pos])

                    # aumentar su importe por un 10%
                    v_juicios[pos].importe += v_juicios[pos].importe * 0.1

                    # Solo mostrar su nombre y su importe
                    print("Nombre:", v_juicios[pos].nombre, "y su importe:", v_juicios[pos].importe)

                    # si existe mostrar sus datos
                    print(v_juicios[pos])

                else:
                    print("No existe ese juicio")

            else:
                print("Debe ingresar a la opcion 1.")








if __name__ == '__main__':
    principal()