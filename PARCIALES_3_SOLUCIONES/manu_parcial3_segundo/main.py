

import random


from clase2 import *


# ==================================================================
#                   Opcion 1
# ==================================================================
def validar_n():
    n = int(input("Ingresar cantidad a trabajar: "))
    while n <= 0:
        n = int(input("Ingresar"))
    return n


def cargar_arreglo(v_tubos, n):

    # cod_prod (1, 5000) Entero, diametro_pulg(1, 200), tipo_apli (1, 20), gramaje(100, 300), ingnifugo(1, 2)
    for i in range(n):
        cod_prod = random.randint(1, 5000)
        diam_pulg = random.randint(1, 200)
        tipo_apli = random.randint(1, 20)
        # gramo = random.randint(100, 300)
        gramo = random.randint(1, 10)
        ignifugo = random.randint(1, 2)

        # campo booleano --> uno que guarda True or False
        # igni = random.choice((True, False))

        # aca definis tu objeto
        tubito = Tubo(cod_prod, diam_pulg, tipo_apli, gramo, ignifugo)

        v_tubos.append(tubito)

    print("se cargaron", n, "tubos")


# ==================================================================
#                   Opcion 2
# ==================================================================
def ordenar_arreglo(v):     # v --> v_tubos
    n = len(v)
    for i in range(n - 1):
        for j in range(i+1, n):
            # solo va a cambiar por el atributo que te pidan ordenar

            # la boquita ">" te indica si esta de menor a mayor o mayor a menor
            # str --> alfabeticamente
            if v[i].diam_pulg < v[j].diam_pulg:
                v[i], v[j] = v[j], v[i]


def mostrar_arreglo(v_tubos):

    # Al final del listado muestre la cantidad de gramos de PVC promedio que se utiliza para los tubos listados.
    # Promedio = sumatoria de la cantidad de gramos  //  cantidad de veces que sumaste
    acum = 0
    cont = 0

    # indices      0   1   2   3
    # v_tubos = [ T1, T2, T3, T4 ]
    for i in v_tubos:
        # i = T1,   T2,     T3,     T4

        # Mostrar los datos de todos los tubos ignífugos
        if i.igni == 1:
            print(i)
            acum += i.gramo
            cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio es:", prom)


# ==================================================================
#                   Opcion 3
# ==================================================================
def contar_tipo(v_tubos, a):

    # generar el vector de conteo
    # tipo_apli ( 1, 20 ) -> lim_superior - lim_inferior + 1 = 20 - 1 + 1 = 20
    v_conteo = 20 * [0]

    # tipo_apli(1, 20) 1  2  3  4                                                 20
    # indices          0  1  2  3  4 ..
    # v_conteo =      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # rellenar el vector
    for i in v_tubos:
        # i = T1,   T2,     T3

        # vector de conteo accedemos al indice segun el atributo que nos indican y le realizamos segun corresponda
        # o no un arreglo matematico
        v_conteo[i.tipo_apli - 1] += 1

    #
    # mostrar el vector
    for i in range(len(v_conteo)):
        # i = 0, 1, 2, 3, 4, ..., 19

        # v_conteo[i] --> contador / acumulador
        # i --> indices --> i + 1 --> corresponde al atributo ( "tipo_apli" )

        # Muestre solo aquellos acumuladores cuyo valor sea mayor un valor "a" que se carga por teclado
        if v_conteo[i] > a:
            print("Tipo Aplicacion:", i+1, " - Cantidad:", v_conteo[i])

        # Mostrar solos los tipo de aplicacion entre 1 y 10 ambos incluidos
        if i+1 >= 1 and i+1 <= 10:
            # print("Tipo Aplicacion:", i + 1, " - Cantidad:", v_conteo[i])
            pass

        #  Muestre solo los valores de los contadores cuyos valores finales sean mayores a cero y menores a tres.
        if v_conteo[i] > 0 and v_conteo[i] < 3:
            pass

# ==================================================================
#                   Opcion 4
# ==================================================================
def busqueda_secuencial(v_tubos, prod):

    # indices       0       1       2
    # v_tubos = [   T1,     T2,     T3 ]

    for i in range(len(v_tubos)):
        # i = 0,        1, 2,

        # en este caso v_tubos[i] apunta al objeto

        if v_tubos[i].cod_prod == prod:

            # Si se encuentra, mostrar el tipo de aplicación y su diámetro.
            print("Tipo de aplicacion: ", v_tubos[i].tipo_apli, "- Diametro:", v_tubos[i].diam_pulg)

            # si te pidieran mostrar todos sus datos
            # print(v_tubos[i])

            return  # Debe mostrar los datos del primero que encuentre y detener en ese momento
                    # la búsqueda (sin importar si hay más de un registro con el mismo código).

    # Si no se encuentra, indicar con un mensaje que no existe.
    print("No existe.")


def menu():
    print("1 - Cargar el vector.")
    print("2 - Mostrar Ordenado.")
    print("3 - Contar por tipo.")
    print("4 - Busqueda secuencial.")
    print("0 - Salir.")
    op = int(input("Ingresar una opcion: "))
    return op


def principal():

    v_tubos = []        # incias una lista vacia
    op = -1

    while op != 0:

        op = menu()

        if op == 1:
            # le cargas contenido a la lista
            n = validar_n()
            cargar_arreglo(v_tubos, n)

        elif op == 2:
            if len(v_tubos) == 0:
                print("El arreglo no esta cargado.")
            else:
                ordenar_arreglo(v_tubos)
                mostrar_arreglo(v_tubos)

        elif op == 3:
            if len(v_tubos) == 0:
                print("El arreglo no esta cargado.")
            else:
                a = int(input("Ingresar valor de contador a superar: "))
                contar_tipo(v_tubos, a)

        elif op == 4:
            if len(v_tubos) == 0:
                print("El arreglo no esta cargado.")
            else:
                # te pedian buscar el codigo de producto
                prod = int(input("Codigo de producto a buscar: "))
                busqueda_secuencial(v_tubos, prod)

        elif op == 6:
            # indices      0   1   2
            # v_tubos = [ T1, T2, T3 ]
            for i in v_tubos:
                # i = t1, t2, t3
                print(i)

        elif op == 0:
            print("gracias por usar el menu.")


if __name__ == '__main__':
    principal()

