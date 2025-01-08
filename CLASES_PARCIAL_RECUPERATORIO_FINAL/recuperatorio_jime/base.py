from registro import *


# ===========================================================================
#                           Opcion 1
# ===========================================================================
def cargar_arreglo(v_series, file_csv):

    m = open(file_csv, "r", encoding="utf-8")
    cont = 0

    for linea in m:
        cont += 1

        if cont >= 2:
            # data = [ "https://m.media-amazon.com/images/M/MV5BYTRiNDQwYzAtMzVlZS00NTI5LWJjYjUtMzkwNTUzMWMxZTllXkEyXkFqcGdeQXVyNDIzMzcwNjc@._V1_UY98_CR2,0,67,98_AL_.jpg";
            # "Game of Thrones", "(2011–2019)", A, "57 min" ;Adventure;9,3;Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.;Emilia Clarke;Peter Dinklage;Kit Harington;Lena Headey;1773458

            lista_data = linea.strip().split(";")

            time = validar_time_episode(lista_data[4])

            if time is not None:

                poster = lista_data[0]
                title = lista_data[1]
                runtime_series = lista_data[2]
                certificate = lista_data[3]
                runtime_episode = time
                genre = lista_data[5]
                imdb = lista_data[6]
                overview = lista_data[7]
                votes = int(lista_data[12])

                serie = Serie(poster, title, runtime_series, certificate, runtime_episode, genre, imdb, overview, votes)

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
    if len(time_min) == 0:
        return None

    else:
        data = time_min.split(" ")
        time = int(data[0])
        return time


def menu():
    print("1 - Cargar arreglo.")

    op = int(input("Ingresar opción: "))
    return op


def principal():

    # file_csv = "prueba.csv"
    file_csv = "series_aed.csv"

    v_series = []

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            cargar_arreglo(v_series, file_csv)

        elif op == 2:
            pass


if __name__ == "__main__":
    principal()