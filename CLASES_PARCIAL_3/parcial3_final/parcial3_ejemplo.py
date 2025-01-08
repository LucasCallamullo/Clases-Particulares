

from funciones import *


# =========================================================================
#                       Opcion 3
# =========================================================================
def generar_vector_conteo(v_figuritas, t):
    # generar vector de conteo/acum
    # pais(0, 3)
    v_conteo = [0] * 4

    # pais       1-1   2-1     3-1     4-1
    # indices     0     1       2       3   .... --> estos indices representan en realidad a un pais                     31
    # v_conteo = [1,    0,      0,      0 ]

    # rellenar el vector de conteo/acum
    # este paso rellena el vector de conteo a partir de los datos de las figuritas

    # indices         0   1   2
    # v_figuritas = [ F1, F2, F3 ]
    # pais            1    3   1
    for i in v_figuritas:
        # i = F1, F2,        F3
        v_conteo[i.pais-1] += 1
        # v_acum[i.pais-1] += i.importe

    #
    # Mostrar el vector de conteo / acum
    for i in range(len(v_conteo)):      # range(4)
        # i = 0,        1, 2, 3

        if v_conteo[i] > t:
            print("Para el pais:", i+1, "existen la cantidad de figuritas de:", v_conteo[i])

        # Solo muestren los pais 2 y 3
        if i+1 == 2 or i+1 == 3:
            pass

        # solo mostrar un pais "p" que se ingresa por teclado
        # if i+1 == p:
        #    pass


# =========================================================================
#                       Opcion 4
# =========================================================================
def busqueda_secuencial(v_figuritas, p):    # p = 3
    # indices         0   1   2
    # v_figuritas = [ F1, F2, F3 ]
    # pais            1    3   2

    pos = -1
    for i in range(len(v_figuritas)):
        # i = 0, 1, 2, ...
        if v_figuritas[i].pais == p and (v_figuritas[i].posicion == 1 or v_figuritas[i].posicion == 2):
            pos = i     # 1
            break   # para romper ciclos

    return pos      # 1   (0 o más)     /    -1




def menu():
    # ctrl + d
    print("1 - Cargar Arreglo ")
    print("2 - Ordenar y Mostrar el arreglo ")
    print("3 - Vector De conteo/Acum")
    print("4 - Busqueda Secuencial")
    print("0 - ")
    op = int(input("Ingresar opcion: "))  # 3
    return op


def principal():

    # arreglo / vector / lista
    v_figuritas = []        # list()

    op = -1
    while op != 0:          # mientras op sea distinto de cero que ingrese al ciclo

        # Si yo igualo una variable a una funcion es porque estoy esperando que me retorne algun valor
        op = menu()     # 3

        if op == 1:
            """
                1. Cada vez que se ingrese a esta opcion, se debe generar un arreglo nuevo desde cero.
            """
            v_figuritas = []
            n = validar_n()
            cargar_arreglo(v_figuritas, n)

        elif op == 2:
            """
                2. Ordenar el arreglo por nombre de menor a mayor y luego mostrarlo a razon de un por linea, solo
                debe mostrar las figuritas que 'superen un importe "x"', al final debe mostrar el promedio de los 
                importes de las figuritas mostradas
            """
            ordenar_arreglo(v_figuritas)

            x = float(input("Importe a superar: "))
            mostrar_datos(v_figuritas, x)

        elif op == 3:
            """
                3 - Determianr la cantidad de figuritas por cada poisible pais
                - Solo mostrar los que superen una cantidad de figuritas "t" que se ingresa por teclado
                - 
            """
            t = int(input("Ingresar cantidad a superar: "))
            generar_vector_conteo(v_figuritas, t)

        elif op == 4:
            """
                4 - Determinar si existe una Figurita con un pais "p" que se ingresa por teclado y que juega
                en la posicion de "Arquero" o "Defensor"
            """

            p = int(input("Ingresar pais a buscar (1, 4):"))

            pos = busqueda_secuencial(v_figuritas, p)       # 1

            if pos >= 0:

                # Mostrar los datos
                print("Datos Viejos:", v_figuritas[pos])

                # Modificar el importe de esa figurita por un valor "imp" que se ingresa por teclado
                imp = float(input("INgresar nuevo valor: "))
                v_figuritas[pos].importe = imp

                print("Datos Actualizados:", v_figuritas[pos])

                # Aumenta el importe de esa Figurita por un 10%
                v_figuritas[pos].importe += 0.1 * v_figuritas[pos].importe

                # Mostrar solo el Pais, y el Nombre
                print("Pais:", v_figuritas[pos].pais, "Nombre:", v_figuritas[pos].nombre)

            else:       # cuando pos es -1
                print("No se encontro una Figurita")



        elif op == 0:
            pass


if __name__ == '__main__':
    principal()
