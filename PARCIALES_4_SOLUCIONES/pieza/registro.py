

class Pieza:
    # tipo(1: TIPO1, 2: TIPO2, 3:TIPO3)
    # id INT > 0 , descripcion STR, tipo(1, 3), sector, (10, 25), stock INT, importe FLOAT

    def __init__(self, id, descripcion, tipo, sector, stock, importe):
        # ctrl + d
        self.id = id
        self.descripcion = descripcion
        self.tipo = tipo
        self.sector = sector
        self.stock = stock
        self.importe = importe

    def __str__(self):
        # tipo(1, 3)    1-1      2-1         3-1
        # indices       0           1           2
        tupla_tipos = ("TIPO1", "TIPO2", "TIPO3")

        cadena = "ID: " + str(self.id)
        cadena += " | Descripcion: " + self.descripcion
        cadena += " | Tipo: " + tupla_tipos[self.tipo - 1]  #
        cadena += " | Sector: " + str(self.sector)
        cadena += " | Stock: " + str(self.stock)
        cadena += " | Importe: " + str(self.importe)
        return cadena
