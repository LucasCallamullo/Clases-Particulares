

class Serie:

    # poster_link, series_title, runtime_of_series, certificate, runtime_of_episodes,
    # genre, imdb_rating, overwiew, no_of_vote
    def __init__(self, poster, title, years, certificate, time_episodes, genre, imdb, overwiew, no_of_vote):
        self.poster = poster
        self.title = title
        self.years = years
        self.certificate = certificate
        self.time_episodes = time_episodes
        self.genre = genre
        self.imdb = imdb
        self.overwiew = overwiew
        self.no_of_vote = no_of_vote

    def __str__(self):
        cadena = "Poster: " + self.poster
        cadena += " | Title: " + self.title
        cadena += " | Years: " + self.years
        cadena += " | Certificate: " + self.certificate
        cadena += " | Time_episodes: " + str(self.time_episodes)
        cadena += " | Genre: " + self.genre
        cadena += " | Imdb: " + self.imdb
        cadena += " | Overwiew: " + self.overwiew
        cadena += " | No_of_vote: " + str(self.no_of_vote)
        return cadena


class Genero:
    def __init__(self, nombre, numero, cantidad):
        self.nombre = nombre
        self.numero = numero
        self.cantidad = cantidad

    def __str__(self):
        cadena = "Nombre: " + str(self.nombre)
        cadena += " | Numero: " + str(self.numero)
        cadena += " | Cantidad: " + str(self.cantidad)
        return cadena
