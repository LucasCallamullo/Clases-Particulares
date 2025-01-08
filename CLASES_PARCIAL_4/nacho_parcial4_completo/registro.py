

class Pantalon:
    # codigo INT, nombre STR, talle_largo(30, 50), talle_cintura(30, 50), tela(1, 3), stock INT
    # importe FLOAT

    def __init__(self, codigo, nombre, talle_largo, talle_cintura, tela, stock, importe):
        self.codigo = codigo
        self.nombre = nombre
        self.talle_largo = talle_largo
        self.talle_cintura = talle_cintura
        self.tela = tela
        self.stock = stock
        self.importe = importe

    def __str__(self):
        # tela(1,3)   1-1           2           3
        # indices       0           1           2
        tupla_telas = ("Jean", "Gabardina", "Denim")

        cadena = "Codigo: " + str(self.codigo)
        cadena += " | Nombre: " + str(self.nombre)
        cadena += " | Talle_largo: " + str(self.talle_largo)
        cadena += " | Talle_cintura: " + str(self.talle_cintura)
        cadena += " | Tela: " + tupla_telas[self.tela - 1]
        cadena += " | Stock: " + str(self.stock)
        cadena += " | Importe: " + str(self.importe)
        return cadena
