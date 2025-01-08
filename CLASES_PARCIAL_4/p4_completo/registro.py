

class Libro:
    # ibsn 13 digitos INT, titulo STR, autor(11, 17), idioma(1, 5), importe FLOAT
    def __init__(self, isbn, titulo, autor, idioma, importe):
        # ctrl + d
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.idioma = idioma
        self.importe = importe

    def __str__(self):

        # idioma(1, 5)      1-1      2-1         3           4           5
        # indices           0       1           2           3           4
        tupla_idiomas = ("Español", "Inglés", "Portugués", "Francés", "Italiano")

        cadena = "ISBN: " + str(self.isbn)
        cadena += " | Titulo: " + self.titulo
        cadena += " | Autor: " + str(self.autor)
        cadena += " | Idioma: " + tupla_idiomas[self.idioma - 1]    #
        cadena += " | Importe: " + str(self.importe)
        return cadena
