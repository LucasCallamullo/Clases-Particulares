
class Libro:
    # isbn 13 digitos INT, titulo STR, autor STR, idioma(1, 5), importe FLOAT, categoria(13, 15)

    def __init__(self, isbn, titulo, autor, idioma, importe, categoria):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.idioma = idioma
        self.importe = importe
        self.categoria = categoria

    def __str__(self):
        # idioma(1, 5)      1-1           2           3           4           5
        # indices           0           1           2           3           4
        tupla_idiomas = ("Español", "Inglés", "Portugués", "Francés", "Italiano")

        cadena = "ISBN: " + str(self.isbn)
        cadena += " | Titulo: " + self.titulo
        cadena += " | Autor: " + self.autor
        cadena += " | Idioma: " + tupla_idiomas[self.idioma - 1]
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Categoria: " + str(self.categoria)
        return cadena
