


class Serie:
    # poster_link: link del poster de la serie en Amazon.
    # • series_title: Título de la serie.
    # • runtime_of_series: año desde - año hasta de la serie, puede estar en blanco el año desde.
    # • certificate: Categoría de la serie, puede estar en blanco.
    # • runtime_of_episodes: tiempo promedio de los capítulos. Es un número seguido por la palabra “min”.
    # Este valor puede venir en blanco.
    # • genre: Género de la serie (una cadena).
    # • imdb_rating: Es el rating que va de 1 a 9,7.
    # • overwiew: Es un resumen de la serie.
    # • star1, star2, star3 y star4: Son los actores y actrices de la serie.
    # • no_of_vote: La cantidad de votos recibida.
    def __init__(self, poster, title, runtime_series, certificate, runtime_episode, genre, imdb, overview, votes):
        self.poster = poster
        self.title = title
        self.years = runtime_series
        self.certificate = certificate
        self.time_episode = runtime_episode
        self.genre = genre
        self.imdb = imdb
        self.overview = overview
        self.votes = votes

    def __str__(self):
        cadena = "Poster: " + str(self.poster)
        cadena += " | Title: " + str(self.title)
        cadena += " | runtime_series: " + str(self.years)
        cadena += " | certificate: " + str(self.certificate)
        cadena += " | runtime_episode: " + str(self.time_episode)
        cadena += " | genre: " + str(self.genre)
        cadena += " | imdb: " + str(self.imdb)
        cadena += " | overview: " + str(self.overview)
        cadena += " | votes: " + str(self.votes)
        return cadena


# Opcion 5
class Genero:
    def __init__(self, numero, nombre, cantidad):
        self.numero = numero
        self.nombre = nombre
        self.cantidad = cantidad


    def __str__(self):
        cadena = "Numero: " + str(self.numero)
        cadena += " | nombre: " + str(self.nombre)
        cadena += " | cantidad: " + str(self.cantidad)
        return cadena
