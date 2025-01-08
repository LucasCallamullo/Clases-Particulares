

from funciones import *


# =================================================================
#                   Opcion 3
# =================================================================
def generar_matriz(v_vehiculos):
    """
    el primer valor hace referencia a las columnas "c" y el segundo a las filas "f"
    """
    # crear la matriz
    c = 5   # c = tipo(5, 9)        # lim_superior - lim_inferior + 1 = 5
    f = 4   # f = tam(1, 4)
    matriz = [ [0] * c for i in range(f) ]

    # c     --> tipo   5-5, 6-5, 7,  8,  9
    # indices           0   1   2   3   4

    # f     --> tam     1-1 2   3   4
    # indices           0   1   2   3

    # [ [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0] ]

    # rellenar la matriz
    # v1 tam = 2, tipo 5
    for i in v_vehiculos:
        # i = V1, V2, V3
        # matriz[f][c]      # los indices son al reves a como lo creamos
        matriz[i.tam-1][i.tipo-5] += i.importe
        # matriz[i.tam-1][i.tipo-5] += 1

    # mostrar la matriz
    tupla_tams = ("Subcompacto", "Compacto", "Mediano", "Grande")
    tuplas_tipo = ("Nafta", "Gasoil", "GNC", "Eléctrico", "Hidrógeno")

    for f in range(len(matriz)):    # esta dado por la cantidad de filas, 4, porque tiene 4 listas
        # f = 0, 1, 2, 3

        for c in range(len(matriz[0])): # range(5), esta dado por la cantidad de columnas 5
            # c = 0, 1, 2, 3, 4

            # solo mostrar los tipo de motores 5, 6, 7 ( Nafta, Gasoil, GNC )
            if 5 <= c+5 <= 7:
                # print("Para el tamaño:", f+1, "y el tipo de motor:", c+5)
                print("Para el tamaño:", tupla_tams[f], "y el tipo de motor:", tuplas_tipo[c])
                print("Tiene el acumulado de:", matriz[f][c])
                print()

            # Solo mostrar los que tengo un contador/acumulador que sea superior a 0 o "letra"
            if matriz[f][c] > 0:        # if matriz[f][c] > "letra":
                pass


# =================================================================
#                   Opcion 6
# =================================================================
def busqueda_binaria(v_vehiculos, x):   # x = 5
    # indices           0   1   2   3   4
    # v_vehiculos = [   V1, V2, V3, V4, V5 ]
    # id                2   3   4   5   6

    izq, der = 0, len(v_vehiculos) - 1
    # izq = 3
    # der = 4

    while izq <= der:       # mientrass izq sea menor o igual a cero , ingreso al ciclo

        c = (izq + der) // 2        # c = centro    = 2, 3

        # if v_vehiculos[c].id == auto.id:
        if v_vehiculos[c].id == x:
            # pos = c
            # break
            return c    # 3
        # elif v_vehiculos[c].id > auto.id:
        elif v_vehiculos[c].id > x:
            der = c - 1
        else:
            izq = c + 1

    return -1


def menu():
    print("1 - Cargar Arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar Matriz.")
    print("4 - Generar Archivo Binario.")
    print("5 - Mostrar Archivo Binario.")
    print("6 - Busqueda Binaria.")
    print("0 - Salir.")
    return int(input("Ingresar una opcion: "))


def main():

    # vector/arreglo/lista de trabajo
    v_vehiculos = []

    # nombre del archivo binario
    fd = "vehiculos.dat"           # file description, nombre del archivo

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            """
            1 - cargar arReglo bla BLA
            - cada vez que se ingresa a esta opcion debe crear nuevamente el arreglo
            """
            n = validar_n()
            v_vehiculos = []
            cargar_arreglo(v_vehiculos, n)

        elif op == 2:
            """
            2 - solo mostrar los que tengan importes entre "s1" y "s2"
            """
            if len(v_vehiculos) > 0:
                s1 = float(input("Importe a superar: "))
                s2 = float(input("Importe a ser menor: "))
                mostrar_arreglo(v_vehiculos, s1, s2)
            else:
                print("El arreglo no esta cargado, ingrese a la opcion 1")

        elif op == 3:
            """
            3 - Generar Matriz
            Calcular los importes acumulados por cada tamaño de vehiculo y tipo de motor posible
            - 
            """
            if len(v_vehiculos) > 0:
                generar_matriz(v_vehiculos)
            else:
                print("El arreglo no esta cargado, ingrese a la opcion 1")

        elif op == 4:
            """
            4 - solo guardar los que superan un importe "t"
            """
            if len(v_vehiculos) > 0:
                t = float(input("Ingresar importe a superar para guardar: "))
                generar_archivo_binario(v_vehiculos, fd, t)

            else:
                print("El arreglo no esta cargado, ingrese a la opcion 1")

        elif op == 5:
            """
            5 - Mostrar archivo binario
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """
            Buscar un vehículo por identificador. Si existe mostrar todos sus datos y si, además, 
            el tipo de motor es GNC, Eléctrico o Hidrógeno entonces mostrar el mensaje “Opción ecológica!”. 
            Si el vehículo no existe informar con
            un mensaje
            """
            if len(v_vehiculos) > 0:
                x = int(input("Ingresar numero id a buscar: "))
                pos = busqueda_binaria(v_vehiculos, x)
                if pos >= 0:
                    print(v_vehiculos[pos])

                    if 7 <= v_vehiculos[pos].tipo <= 9:
                        print("Opcion Ecologica!")

                else:
                    print("No existe.")
            else:
                print("El arreglo no esta cargado, ingrese a la opcion 1")


if __name__ == '__main__':
    main()