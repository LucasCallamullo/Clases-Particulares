class Lote:

    # nombre STR, manzana(1, 35), lote (1, 20),
    # orientacion(1, 4)  (1: Norte, 2: Sur, 3: Este, 4:Oeste), superficie INT, importe FLOAT
    def __init__(self, nombre, manzana, lote, orientacion, superficie, importe):
        self.nombre = nombre
        self.manzana = manzana
        self.lote = lote
        self.orientacion = orientacion
        self.superficie = superficie
        self.importe = importe

    def __str__(self):
        # orientacion(1, 4)    1-1     2-1     3-1       4
        # indices               0       1       2       3
        tupla_orientaciones = ("Norte", "Sur", "Este", "Oeste")

        cadena = "Nombre: " + self.nombre
        cadena += " | Manzana: " + str(self.manzana)
        cadena += " | Lote: " + str(self.lote)
        cadena += " | Orientacion: " + tupla_orientaciones[self.orientacion - 1]
        cadena += " | Superficie: " + str(self.superficie)
        cadena += " | Importe: " + str(self.importe)
        return cadena