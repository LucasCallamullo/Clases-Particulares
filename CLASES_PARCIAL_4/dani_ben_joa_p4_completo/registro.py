
class Libro:

    # isbn 13 digitos INT, autor STR, titulo STR, idioma(1, 5), importe FLOAT, categoria(13, 17)
    def __init__(self, isbn, autor, titulo, idioma, importe, categoria):
        # ctrl + d
        self.isbn = isbn
        self.autor = autor
        self.titulo = titulo
        self.idioma = idioma
        self.importe = importe
        self.categoria = categoria

    def __str__(self):

        # idioma(1, 5)     1-1          2           3           4           5
        # indices           0           1           2           3           4
        tupla_idiomas = ("Español", "Inglés", "Portugués", "Francés", "Italiano")

        cadena = "ISBN: " + str(self.isbn)
        cadena += " | autor: " + self.autor
        cadena += " | titulo: " + self.titulo
        cadena += " | idioma: " + tupla_idiomas[self.idioma - 1]        # 1
        cadena += " | importe: " + str(self.importe)
        cadena += " | categoria: " + str(self.categoria)
        return cadena       # RETORNAR LA CADENA
