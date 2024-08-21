class Libro:
    # Constructor del objeto    # ctrl + c = copiar ; ctrl + v = pegar  ; ctrl + x = cortar
    def __init__(self, titulo, genero, precio, year):
        self.titulo = titulo        # ctrl + d
        self.genero = genero
        self.precio = precio
        self.year = year

    # es su funcion de print del objeto
    def __str__(self):
        # (531: Ficción, 532: Romantico, 533: Ciencia, 534: Misterio)

        # self.genero(1,4)
        #               531-531       532-531     533-531     534-531
        #                   1-1         2-1        3-1         4-1
        # indices           0           1           2           3       4       5       6   7   8
        desc_generos = ("Ficcion", "Romantico", "Ciencia", "Misterio")

        cadena = "Titulo: " + self.titulo
        cadena += " | Genero: " + desc_generos[self.genero-1]
        cadena += " | Precio: " + str(self.precio)
        cadena += " | Año: " + str(self.year)
        return cadena
