import os.path
import pickle
import random
from registro import *


#       =====================       Opcion 1            =================================
def validar_n():
    n = int(input("Cantidad de vehiculos a cargar: "))
    while n <= 0:
        n = int(input("Cantidad de vehiculos a cargar(debe ser positivo el valor): "))
    return n


def cargar_arreglo(v_vehiculo, n):
    for i in range(n):      # n = 3         0           1       2
        id = random.randint(1, 9)
        size = random.randint(1, 4)
        tipo = random.randint(0, 4)
        importe = round(random.uniform(0.1, 10), 2)
        vehi = Vehiculo(id, size, tipo, importe)
        add_in_order(v_vehiculo, vehi)


def add_in_order(v_vehiculo, vehi):                     # v1.id = 6
    izq, der = 0, len(v_vehiculo) - 1                   # v2.id = 4

    while izq <= der:
        c = (izq + der) // 2
        if v_vehiculo[c].id == vehi.id:
            pos = c
            break
        elif v_vehiculo[c].id > vehi.id:                # menor a mayor ; v_vector[c] >
            der = c - 1                                 # mayor a menu  ;               <     objeto
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # vuelta 0  = v_vehiculo[ V1 ]
    # vuelta 1  = v_vehiculo[ V2,  V1 ]
    v_vehiculo[pos:pos] = [vehi]


#       =====================       Opcion 2            =================================
def mostrar_datos(v_vehiculo):
    # v_vehiculo = V V V
    for i in v_vehiculo:
        # i = V V
        print(i)


#       =====================       Opcion 3            =================================
def busqueda_binaria(v_vehiculo, num):
    izq, der = 0, len(v_vehiculo) - 1                   # v2.id = 4

    # id = [ 5 4 3 2 1 ]
    # num = 5
    while izq <= der:
        c = (izq + der) // 2
        if v_vehiculo[c].id == num:
            return c
        elif v_vehiculo[c].id > num:                # menor a mayor ; v_vector[c] >
            der = c - 1                               # mayor a menu  ;               <     objeto
        else:
            izq = c + 1

    return -1


#       =====================       Opcion 4            =================================
def generar_archivo(v_vehiculo, fd):
    m = open(fd, "wb")
    cont = 0
    for i in v_vehiculo:
        if i.size == 3 or i.size == 4:
            pickle.dump(i, m)
            m.flush()           # no es necesario,
            cont += 1
    print("Se cargaron", cont, "vehiculos")
    m.close()                   # SI ES NECESARIO,


#       =====================       Opcion 5            =================================
def mostrar_archivo(fd):

    if not os.path.exists(fd):
        print("El archivo no existe, debe pasar primero por la opcion 4.")

    else:
        m = open(fd, "rb")
        tam = os.path.getsize(fd)       # te devuelve un valor en bytes que esle tamañao del archivo

        # bytes0  20    25      25      = 70 bytes
        # fd = [ V      V       V ]
        #       0   20      45      70

        # prom = acum / cont
        acum, cont = 0, 0

        while m.tell() < tam:
            vehi = pickle.load(m)
            print(vehi)
            if vehi.tipo == 3:
                cont += 1
                acum += vehi.importe

        if cont > 0:
            prom = acum / cont
            print("El promedio de los importes de los autos electricos fue:", prom)
        else:
            print("No se encontraron autos electricos en el archivo.")

        m.close()   # SI ES NECESARIO


#       =====================       Opcion 6            =================================
def busqueda_secuencial(v_vehiculo, t):
    # promedio
    cont, acum = 0, 0
    for i in range(len(v_vehiculo)):
        if v_vehiculo[i].importe > t:
            print(v_vehiculo[i])
            cont += 1
            acum += v_vehiculo[i].importe

    if cont > 0:
        prom = acum / cont
        print("El promedio de los importes de los autos electricos fue:", prom)


#       =====================       Opcion 7          =================================
def generar_matriz(v_vehiculo):
    # Calcular cuantos autos existen por tipo de motor y tamaño vehiculo
    # Tamaño ( 1, 4 )       ; Tipo (0, 4)
    # Mostrar solo los que sean mayores a 0.
    # mostrar solo tipos de motor gnc, electrico, hidrogeno (2, 3, 4)
    # mostrar solo los tamaños mediano y grande ( 3 y 4 )

    # generar una matriz
    filas = 4
    columnas = 5
    matriz = [[0] * columnas for i in range(filas)]

    matriz_2 = [[0] * columnas for i in range(filas)]

    # rellenar la matriz
    for i in v_vehiculo:
        matriz[i.size-1][i.tipo] += 1
        matriz_2[i.size-1][i.tipo] += i.importe

    # printear la matriz
    # size(1,4)     1-1             2-1         3-1         4-1
    # ind           0               1           2           3
    desc_size = ["Subcompacto", "Compacto", "Mediano", "Grande"]

    #               0           1       2       3           4
    desc_motor = ["Nafta", "Gasoil", "GNC", "Electrico", "Hidrogeno"]

    for f in range(len(matriz)):        # 0 1 2 3

        for c in range(len(matriz[0])):

            # if matriz[f][c] > 0 and 2 <= c <= 4:
            # if matriz[f][c] > 0 and (c == 2 or c == 3 or c == 4):
            # if f+1 == 3 or f+1 == 4:
            if matriz[f][c] > 0:


                # print("En el tamaño de vehiculo:", f+1, "y el Tipo de motor:", c)
                print("En el tamaño de vehiculo:", desc_size[f], "y el Tipo de motor:", desc_motor[c])
                print("La cantidad es:", matriz[f][c])
                print("el importe acumulado es:", matriz_2[f][c])
                print("=" * 50)




    # [[0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0]]





def menu():
    print("=" * 50)
    # alt 92
    print(" 1 - Cargar Arreglo."
          "\n 2 - Mostrar datos."
          "\n 3 - Busqueda Binaria."
          "\n 4 - Generar archivo."
          "\n 5 - Mostrar archivo."
          "\n 0 - Salir.")

    return int(input("Ingresar opcion del usuario: "))


def main():

    # arreglo principal
    v_vehiculo = []

    # archivo principal
    fd = "vehiculos.dat"

    # validar opcion 1
    validar_op1 = False

    op = -1
    while op != 0:

        op = menu()

        if not validar_op1:
            if op == 1:
                n = validar_n()
                cargar_arreglo(v_vehiculo, n)
                validar_op1 = True
            else:
                print("Primero debe ingresar a la opcion 1.")

        else:
            if op == 1:
                n = validar_n()
                cargar_arreglo(v_vehiculo, n)

            elif op == 2:
                mostrar_datos(v_vehiculo)

            elif op == 3:
                num = int(input("Ingresar id a buscar: "))
                pos = busqueda_binaria(v_vehiculo, num)
                if pos >= 0:
                    print(v_vehiculo[pos])

                    # if 2 <= v_vehiculo[pos].tipo <= 4:
                    if v_vehiculo[pos].tipo == 2 or v_vehiculo[pos].tipo == 3 or v_vehiculo[pos].tipo == 4:
                        print("Opción ecologica.")

                    # modificar valor del importe por unvalor x del usuario.
                    x = float(input("Ingrese nuevo importe del vehiculo: "))
                    v_vehiculo[pos].importe = x

                    # modificar valor del importe con un 10% de recargo
                    recargo = 10 / 100 * v_vehiculo[pos].importe
                    v_vehiculo[pos].importe = v_vehiculo[pos].importe + v_vehiculo[pos].importe * 0.1
                    print(v_vehiculo[pos])

                else:
                    print("No se encontro el id buscado.")


            elif op == 4:
                generar_archivo(v_vehiculo, fd)

            elif op == 5:
                mostrar_archivo(fd)

            elif op == 6:
                # que muestres el promedio de todos los importe que superen un valor t
                t = float(input("Importe a superar"))
                busqueda_secuencial(v_vehiculo, t)

            elif op == 7:
                generar_matriz(v_vehiculo)




if __name__ == '__main__':
    main()
