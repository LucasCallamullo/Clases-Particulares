import os.path
import pickle

from registro import *


# Opcion 1
def cargar_arreglo(fdcsv, v_series):

    m = open(fdcsv, "r", encoding="utf-8")    # read

    primera_linea = False

    for linea in m:

        if primera_linea is False:
            primera_linea = True

        else:
            # [ https://m.media-amazon.com/images/M/MV5BYTRiNDQwYzAtMzVlZS00NTI5LWJjYjUtMzk2AL_.jpg,
            # "Game of Thrones", "(2011–2019)",A;"["57", "min"]";Adventure;9,3;
            # Nine nnia.;Emilia Clarke;Peter Dinklage;Kit Harington;Lena Headey;1773458 ]

            lista_linea = linea.strip().split(";")

            if len(lista_linea[4]) != 0:
                # def __init__(self, poster, title, years, certificate, time_episodes, genre, imdb, overwiew, no_of_vote):

                time = lista_linea[4].split(" ")    # ["57", "min"]

                poster = lista_linea[0]
                title = lista_linea[1]
                years = lista_linea[2]
                certificate = lista_linea[3]
                time_episodes = int(time[0])
                genre = lista_linea[5]
                imdb = lista_linea[6]
                overwiew = lista_linea[7]
                no_of_vote = int(lista_linea[12])

                serie = Serie(poster, title, years, certificate, time_episodes, genre, imdb, overwiew, no_of_vote)

                add_in_order(v_series, serie)


def add_in_order(v_series, serie):

    izq, der = 0, len(v_series) - 1

    while izq <= der:

        c = (izq + der) // 2

        if v_series[c].no_of_vote == serie.no_of_vote:
            pos = c
            break

        elif v_series[c].no_of_vote > serie.no_of_vote:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_series[pos:pos] = [serie]


# Opcion 2
def mostrar_arreglo(v_series, m1, m2, archivo_csv):

    # calcular promedio = acumulado de duracion / la cantidad de veces que acumule
    acum = 0
    cont = 0

    cadena = ""

    for i in v_series:

        if m1 < i.time_episodes < m2:
            print(i)

            acum += i.time_episodes
            cont += 1

            cadena += str(i.poster) + ";"
            cadena += str(i.title) + ";"
            cadena += str(i.years) + ";"
            cadena += str(i.certificate) + ";"
            cadena += str(i.time_episodes) + ";"
            cadena += str(i.genre) + ";"
            cadena += str(i.imdb) + ";"
            cadena += str(i.overwiew) + ";"
            cadena += str(i.no_of_vote) + "\n"

    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio del listado es: ", round(prom, 2))

    generar_csv(cadena, archivo_csv)


def generar_csv(cadena, archivo_csv):

    op = input("Desea almacenar el listado en un archivo csv (S/N)?: ")

    if op.lower() == "s":
        m = open(archivo_csv, "w", encoding="utf-8")
        m.write(cadena)


# opcion 3
def opcion3(v_series, v_generos):

    for i in v_series:
        if i.genre not in v_generos:
            v_generos.append(i.genre)


# opcion 4
def opcion4(v_series, v_generos):

    v_conteo = [0] * len(v_generos)

    for i in v_series:

        for j in range(len(v_generos)):
            # 0, 1, 2, 3

            if i.genre == v_generos[j]:
                v_conteo[j] += 1
                break

    #
    for i in range(len(v_generos)):
        # i = 0, 1, 2, 3, 4,
        print("Genero:", v_generos[i], " - Cantidad:", v_conteo[i])

    return v_conteo


# opcion 5
def opcion5(v_conteo, v_generos, fd_op5):

    m = open(fd_op5, "wb")

    for i in range(len(v_conteo)):
        nombre = v_generos[i]
        numero = i
        cantidad = v_conteo[i]
        genre = Genero(nombre, numero, cantidad)

        pickle.dump(genre, m)
        m.flush()

    print("Se genero el archivo", fd_op5, "correctamente.")
    m.close()


# opcion 6
def opcion6(fd_op5):

    if not os.path.exists(fd_op5):
        print("No existe el archivo:", fd_op5)
        return

    m = open(fd_op5, "rb")
    tam = os.path.getsize(fd_op5)

    while m.tell() < tam:
        genre = pickle.load(m)
        print(genre)

    m.close()


# opcion 7
def opcion7(v_series, tit):
    pos = -1
    for i in range(len(v_series)):

        if v_series[i].title == tit:
            pos = i
            break

    return pos


# menu
def menu():
    print("aca iria un menu")


    print(" 0 - Salir.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # opcion 1
    v_series = []
    fdcsv = "series_aed.csv"

    # opcion 2
    archivo_csv = "opcion2.csv"

    # opcion 3
    v_generos = []

    # opcion 4
    v_conteo = []

    # opcion 5
    fd_op5 = "opcion5.dat"

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            cargar_arreglo(fdcsv, v_series)


        elif op == 2:
            if len(v_series) > 0:
                m1 = int(input("Ingresar duracion a superar: "))
                m2 = int(input("Ingresar duracion a ser menor: "))
                mostrar_arreglo(v_series, m1, m2, archivo_csv)

            else:
                print("Ingrese primero a la opcion 1.")

        #
        elif op == 3:
            if len(v_series) > 0:
                opcion3(v_series, v_generos)

            else:
                print("Ingrese primero a la opcion 1.")

        #
        elif op == 4:
            if len(v_generos) > 0:
                v_conteo = opcion4(v_series, v_generos)

            else:
                print("Ingrese primero a la opcion 3.")

        #
        elif op == 5:
            if len(v_conteo) > 0:
                opcion5(v_conteo, v_generos, fd_op5)

            else:
                print("Ingrese primero a la opcion 3.")

        #
        elif op == 6:
            opcion6(fd_op5)

        #
        elif op == 7:
            if len(v_series) > 0:
                tit = input("Ingresar titulo a buscar: ")
                pos = opcion7(v_series, tit)

                if pos >= 0:
                    print("datos sin actualizar: ", v_series[pos])
                    v_series[pos].no_of_vote += 1
                    print("datos actualizados: ", v_series[pos])

                else:
                    print("No existe ese serie con ese titulo.")

            else:
                print("Ingrese primero a la opcion 1.")

        #
        elif op == 0:
            print("Gracias por usar el programa.")


if __name__ == '__main__':
    principal()





