
class Libro:
    # isbn 13digitos INT , titulo STR, autor(2, 7),
    # idioma(1, 5) (1: Español, 2: Inglés, 3: Portugués, 4: Francés, 5: Italiano), importe FLOAT
    def __init__(self, isbn, titulo, autor, idioma, importe):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.idioma = idioma
        self.importe = importe

    def __str__(self):
        # idioma(1, 5)   1-1          2           3           4           5
        # indices           0           1           2           3           4
        tupla_idiomas = ("Español", "Inglés", "Portugués", "Francés", "Italiano")

        cadena = "ISBN: " + str(self.isbn)
        cadena += " | Titulo: " + self.titulo
        cadena += " | Autor: " + str(self.autor)
        cadena += " | Idioma: " + tupla_idiomas[self.idioma - 1]
        cadena += " | Importe: " + str(self.importe)
        return cadena
