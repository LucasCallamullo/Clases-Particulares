import os.path
import pickle
import random
from registro import *


# ================= Opcion 1 ==========================
def validar_n():
    n = int(input("Ingresar cantidad de Televisores a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de Televisores a cargar(Debe ser positivo): "))
    return n


def cargar_arreglo(v_tele, n):
    marcas = "ABCDEF"
    for i in range(n):
        marca = random.choice(marcas)
        size = random.randint(30, 40)
        resolucion = random.randint(1, 3)
        importe = round(random.uniform(0.1, 10), 2)
        tele = Televisor(marca, size, resolucion, importe)
        add_in_order(v_tele, tele)


def add_in_order(v_tele, tele):
    izq, der = 0, len(v_tele) - 1

    while izq <= der:
        c = (izq + der) // 2
        if v_tele[c].marca == tele.marca:
            pos = c
            break
        elif v_tele[c].marca > tele.marca:          # si se come al vector esta de menor a mayor
            der = c - 1                             # se se come al objeto esta de mayor a menor
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_tele[pos:pos] = [tele]


# ================= Opcion 2 ==========================
def mostrar_datos(v_tele, t):
    # v_tele = [ T1, T2, T3 ... ]
    for i in v_tele:
        # T1
        if i.importe > t:
            print(i)


# ================= Opcion 4 ==========================
def cargar_archivo(fd, v_tele, x):
    m = open(fd, "wb")  # write binary, crea el archivo, si existe borra su contenido y lo reescribe
    # m = open(fd, "ab")  # append binary, crea el archivo, si existe agregarlo al final.

    cont = 0
    for i in v_tele:
        if i.size >= x and (i.resolucion == 1 or i.resolucion == 2):
            pickle.dump(i, m)
            m.flush()
            cont += 1

    # print("La cantidad de televisores que se guardaron fue:", cont)
    m.close()   # SI ES NECESARIO


# ================= Opcion 5 ==========================
def mostrar_archivo(fd):
    if os.path.exists(fd):          # pregunta si el archivo existe

        m = open(fd, "rb")  # read binary, modo de solo lectura
        tam = os.path.getsize(fd)   # el tamaño bytes del archivo. 300

        #             0   1   2
        # v_tele = [ T1, T2, T3 ]

        # fd = [ T1         T2      T3 ]
        #      0     100        200     300

        cont = 0
        acum = 0

        while m.tell() < tam:
            tele = pickle.load(m)
            print(tele)

            if tele.resolucion == 1:
                cont += 1
                acum += tele.importe

        if cont > 0:
            prom = acum / cont
            print("El costo promedio por resolucion 720P es:", prom)

        m.close()

    else:
        print("El archivo no existe, por favor ingrese primero por la opcion 4.")


# ================= Opcion 6 ==========================
def busqueda_binaria(v_tele, mar):
    izq, der = 0, len(v_tele) - 1

    while izq <= der:
        c = (izq + der) // 2
        if v_tele[c].marca == mar:
            return c        # 0, 1, 2, ...,
        elif v_tele[c].marca > mar:          # si se come al vector esta de menor a mayor
            der = c - 1                      # se se come al objeto esta de mayor a menor
        else:
            izq = c + 1
    return -1


def menu():
    print("=" * 50)
    print(" 1 - Cargar arreglo"
          "\n 2 - Mostrar dats"
          "\n 3 - Matriz"
          "\n 4 - Generar Archivo"
          "\n 5 - Mostrar Archivo"
          "\n 6 - Busqueda binaria.")

    return int(input("Ingresar opcion: "))


def principal():

    # arreglo / vector / lista principal
    v_tele = []            # list()


    # una variable que contenga el nombre de nuestro archivo
    fd = "teles.dat"            # file descripction


    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_tele, n)

        elif op == 2:
            t = float(input("Ingresar precio a superar: "))
            mostrar_datos(v_tele, t)


        elif op == 4:
            x = int(input("Ingresar cantidad de pulgadas a superar o igualar para guardar en archivo: "))
            cargar_archivo(fd, v_tele, x)

        elif op == 5:
            mostrar_archivo(fd)

        elif op == 6:
            mar = input("Ingresar marca a buscar (A,F): ")
            pos = busqueda_binaria(v_tele, mar)

            if pos >= 0:
                # mostrar todos sus datos
                print(v_tele[pos])

                # modificar el precio por un valor x
                x = float(input("Ingrese nuevo valor de precio para cambiar: "))
                v_tele[pos].importe = x

                # por ejemplo si te pide un aumento del 10%
                # v_tele[pos].importe = v_tele[pos].importe + v_tele[pos].importe * 0.1

                # si te pidieran que si es de resolucion 1080 o 4K muestre un mensaje adicional
                # dicienado "opcion HD"
                if v_tele[pos].resolucion == 2 or v_tele[pos].resolucion == 3:
                    print("Opcion HD!")

                # mostrar solo algunos atributos en este caso solo resolucion y precio
                # desc_resoluciones = ("720P", "1080P", "4K")
                # print("Resolucion:", desc_resoluciones[v_tele[pos].resolucion-1], "Precio:", v_tele[pos].importe)

            else:
                print("No se encontro la marca buscada.")


if __name__ == '__main__':
    principal()
