
class Libro:

    # isbn 13 digitos INT, autor STR, titulo STR, idioma(1, 5), importe FLOAT, categoria(13,15)

    def __init__(self, isbn, autor, titulo, idioma, importe, categoria):
        self.isbn = isbn
        self.autor = autor
        self.titulo = titulo
        self.idioma = idioma
        self.importe = importe
        self.categoria = categoria

    def __str__(self):

        # idioma(1, 5)   1-1         2-1         3-1         4-1         5-1
        # indices           0           1           2           3           4
        tupla_idiomas = ("Español", "Inglés", "Portugués", "Francés", "Italiano")

        cadena = "ISBN: " + str(self.isbn)
        cadena += " | Autor: " + self.autor
        cadena += " | Titulo: " + self.titulo
        cadena += " | Idioma: " + tupla_idiomas[self.idioma - 1]
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Categoria: " + str(self.categoria)
        return cadena

