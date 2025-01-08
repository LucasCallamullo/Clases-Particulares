import os.path
import pickle

from registro import *


# ===========================================================================
#                           Opcion 1
# ===========================================================================
def cargar_arreglo(v_series, file_csv):

    m = open(file_csv, "r", encoding="utf-8")     # read
    cont = 0

    for linea in m:
        cont += 1

        if cont >= 2:
            # data = [ "https://m.media-amazon.com/images/M/MV5BYTRiNDQwYzAtMzVlZS00NTI5LWJjYjUtMzkwNTUzMWMxZTllXkEyXkFqcGdeQXVyNDIzMzcwNjc@._V1_UY98_CR2,0,67,98_AL_.jpg";
            # "Game of Thrones", "(2011–2019)", A, "57 min" ;Adventure;9,3;Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.;Emilia Clarke;Peter Dinklage;Kit Harington;Lena Headey;1773458

            data = linea.strip().split(";")

            existe_time_episode = validar_time_episode(data[4])

            if existe_time_episode is not None:
                #  poster, title, years, certificate, time_episode, genre, imdb, overview, votes):
                poster = data[0]
                title = data[1]
                years = data[2]
                certificate = data[3]
                time_episode = existe_time_episode      # "57 min"
                genre = data[5]
                # imdb = float(data[6])
                imdb = data[6]
                overview = data[7]
                votes = int(data[12])

                serie = Serie(poster, title, years, certificate, time_episode, genre, imdb, overview, votes)

                add_in_order(v_series, serie)


def add_in_order(v_series, serie):
    izq, der = 0, len(v_series) - 1

    while izq <= der:
        c = (izq + der) // 2

        if v_series[c].votes == serie.votes:
            pos = c
            break

        # la boquita determina si esta de menor a mayor
        elif v_series[c].votes > serie.votes:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_series[pos:pos] = [serie]


def validar_time_episode(time_min):
    # la logica fue que si el tamaño de caracteres del valor que recupera como time_mion es 0 significa
    # que no tiene un tamaño real por lo tantao
    if len(time_min) == 0:
        return None

    else:
        # [ "57", "min" ]
        data = time_min.split(" ")
        minutos = int(data[0])
        return minutos


# ===========================================================================
#                           Opcion 2
# ===========================================================================
def mostrar_arreglo(v_series, m1, m2):
    # promedio de la duracion ? tiempo de minutos de los episodios
    # promedio = acumulacion ( de minutos )  / cantidad ( de veces que acumule )

    acum = 0
    cont = 0

    v_mostrado = []

    # v_series = [ S1, s2, S3, S4 ]
    for i in v_series:
        # i = S1, S2, S3, S4...

        # solo mostrar los que tienen una duracion de minutos entre m1 y m2

        if m1 < i.time_episode < m2:
            print(i)
            acum += i.time_episode
            cont += 1

            v_mostrado.append(i)

    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio es:", prom)

    return v_mostrado


def generar_archivo_csv(v_mostrado, file_op2):

    # menu
    print("¿ Desea Generar Archivo S/N?")
    op = input("Ingresar opcion: ")

    if op.lower() == "s":
        m = open(file_op2, "w", encoding="utf-8")     # write
        # __init__(self, poster, title, years, certificate, time_episode, genre, imdb, overview, votes):
        for i in v_mostrado:

            cadena = i.poster + "," + i.title + ","
            cadena += i.years + "," + i.certificate + ","
            cadena += str(i.time_episode) + "," + i.genre + ","
            cadena += str(i.imdb) + "," + i.overview + "," + str(i.votes) + "\n"

            m.write(cadena)

        m.close()


# ===========================================================================
#                           Opcion 3
# ===========================================================================
def obtener_generos_opcion3(v_series):
    v_generos = []

    # v_series = [ S1, s2, S3, S4 ]
    for i in v_series:
        # i =   S1, S2, S3, S4
        # i.genre = "Comedia", "Drama"

        # si el genero que toco esta vuelta de ciclo no esta en el vector generos
        if i.genre not in v_generos:
            v_generos.append(i.genre)

    return v_generos


# ===========================================================================
#                           Opcion 4
# ===========================================================================
def generar_vector_conteo(v_series, v_generos):

    v_conteo = [0] * len(v_generos)

    for i in v_series:

        for j in range(len(v_generos)):
            # j = 0, 1, 2, 3, 4,
            # Crime  == Crime
            if i.genre == v_generos[j]:
                v_conteo[j] += 1

    # mostrar los generos con vector de conteo
    for i in range(len(v_generos)):
        # i = 0, 1, 2, 3
        print("Genero:", v_generos[i], " - Cantidad:", v_conteo[i])

    return v_conteo


# ===========================================================================
#                           Opcion 5
# ===========================================================================
def generar_archivo_binario(v_generos, v_conteo, fd):
    m = open(fd, "wb")

    for i in range(len(v_generos)):
        # i = 0, 1, 2

        numero = i
        nombre = v_generos[i]
        cantidad = v_conteo[i]
        genre = Genero(numero, nombre, cantidad)

        pickle.dump(genre, m)
        m.flush()   # opcional

    m.close()       # OBLIGATORIOOOOOOOOOOO


# ===========================================================================
#                           Opcion 6
# ===========================================================================
def mostrar_archivo_binario(fd):

    if os.path.exists(fd) is False: # cuando no existe el archivo binario
        print("No existe el archivo:", fd)
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    # fd = [  G1         G2              G3  ]

    while m.tell() < tam:

        genre = pickle.load(m)

        # genre = G1, G2, G3
        print(genre)

    m.close()


# ===========================================================================
#                           Opcion 7
# ===========================================================================
def busqueda_secuencial(v_series, tit):     # B
    pos = -1

    # indices     0     1       2
    # v_series = S1,    S2,     S3
    # titulso     A      B       C


    for i in range(len(v_series)):
        # i = 0,    1,     2,   3
        if v_series[i].title == tit:
            pos = i
            break

    return pos


def menu():
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Generar matriz.")
    print("4 - Generar archivo binario.")
    print("5 - Mostrar archivo binario.")
    op = int(input("Ingresar opción: "))
    return op


def principal():

    # file_csv = "prueba.csv"
    file_csv = "series_aed.csv"

    # Opcion 2
    file_op2 = "salida.csv"

    # opcion 3
    v_generos = []

    # opcion 4
    v_conteo = []

    # opcion 5:
    fd = "generos.dat"

    v_series = []

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            cargar_arreglo(v_series, file_csv)

            for i in v_series:
                print(i)

            print("El tamaño del vector es:", len(v_series))

        elif op == 2:
            if len(v_series) > 0:
                m1 = int(input("Ingresar minutos a superar: "))
                m2 = int(input("Ingresar minutos a ser menor: "))

                v_mostrado = mostrar_arreglo(v_series, m1, m2)
                generar_archivo_csv(v_mostrado, file_op2)

            else:
                print("Primero debe pasar por la opcion 1.")

        elif op == 3:
            if len(v_series) > 0:
                v_generos = obtener_generos_opcion3(v_series)

            else:
                print("Primero debe pasar por la opcion 1.")


        elif op == 4:

            if len(v_generos) > 0:
                v_conteo = generar_vector_conteo(v_series, v_generos)

            else:
                print("Primero debe pasar por la opcion 3.")


        elif op == 5:
            if len(v_conteo) > 0:
                generar_archivo_binario(v_generos, v_conteo, fd)
            else:
                print("Primero debe pasar por la Opcion 4.")

        elif op == 6:
            mostrar_archivo_binario(fd)

        elif op == 7:
            tit = input("Ingresar titulo: ")
            pos = busqueda_secuencial(v_series, tit)

            if pos >= 0:
                # print("datos desactualizados:", v_series[pos])
                v_series[pos].votes += 1
                # print("datos actualizados:", v_series[pos])

            else:
                print("No existe el titulo:", tit)


if __name__ == "__main__":
    principal()



