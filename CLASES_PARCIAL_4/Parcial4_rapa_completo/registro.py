

class Lote:

    # nombre STR , manzana (1, 35), num_lote(1, 20), orientacion(1, 4),
    # superficie FLOAT, importe FLOAT
    def __init__(self, nombre, manzana, num_lote, orientacion, superficie, importe):
        self.nombre = nombre
        self.manzana = manzana
        self.num_lote = num_lote
        self.orientacion = orientacion
        self.superficie = superficie
        self.importe = importe

    def __str__(self):
        # orientacion(1, 4)     1-1            2      3      4
        # indices               0           1       2       3
        tupla_orientaciones = ("Norte", "Sur", "Este", "Oeste")

        cadena = "Nombre: " + self.nombre
        cadena += " | manzana: " + str(self.manzana)
        cadena += " | num_lote: " + str(self.num_lote)
        cadena += " | orientacion: " + tupla_orientaciones[self.orientacion - 1]
        cadena += " | superficie: " + str(self.superficie)
        cadena += " | importe: " + str(self.importe)
        return cadena
