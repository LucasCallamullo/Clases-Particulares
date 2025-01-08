
class Libro:

    # isbn 13 digitos INT, titulo STR, autor STR, idioma(1, 5), categoria(13, 15), importe FLOAT
    def __init__(self, isbn, titulo, autor, idioma, categoria, importe):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.idioma = idioma
        self.categoria = categoria
        self.importe = importe

    def __str__(self):

        # idioma(1, 5)     1-1        2 -1         3-1         4-1         5-1
        # indices           0           1           2           3           4
        tupla_idiomas = ("Español", "Inglés", "Portugués", "Francés", "Italiano")

        cadena = "ISBN: " + str(self.isbn)
        cadena += " | Titulo: " + self.titulo
        cadena += " | Autor: " + self.autor
        cadena += " | Idioma: " + tupla_idiomas[self.idioma - 1]
        cadena += " | Categoria: " + str(self.categoria)
        cadena += " | Importe: " + str(self.importe)
        return cadena
