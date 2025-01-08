
class Lote:

    # nombre STR, manzana(1, 35), num_lote(1, 20), orientacion(1, 4), superficie FLOAT, importe FLOAT
    def __init__(self, nombre, manzana, num_lote, orientacion, superficie, importe):
        self.nombre = nombre
        self.manzana = manzana
        self.num_lote = num_lote
        self.orientacion = orientacion
        self.superficie = superficie
        self.importe = importe

    def __str__(self):
        # orientacion(1, 4)   1-1     2-1     3-1       4-1
        # indices               0       1       2       3
        tupla_orientaciones = ("Norte", "Sur", "Este", "Oeste")

        cadena = "Nombre: " + str(self.nombre)
        cadena += " | Manzana: " + str(self.manzana)
        cadena += " | Num_lote: " + str(self.num_lote)
        cadena += " | Orientacion: " + tupla_orientaciones[self.orientacion - 1]
        cadena += " | Superficie: " + str(self.superficie)
        cadena += " | Importe: " + str(self.importe)
        return cadena
