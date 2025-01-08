

class Pantalon:
    # codigo INT, nombre STR, largo(0, 6), cintura(1, 2), tela(1, 3), stock INT, importe FLOAT
    def __init__(self, codigo, nombre, largo, cintura, tela, stock, importe):
        # ctrl + d
        self.codigo = codigo
        self.nombre = nombre
        self.largo = largo
        self.cintura = cintura
        self.tela = tela
        self.stock = stock
        self.importe = importe

    def __str__(self):

        # tela(1, 3)   1-1     2-1          3-1
        # indices       0       1           2
        tupla_telas = ("Jean", "Gabardina", "Denim")

        cadena = "Codigo: " + str(self.codigo)
        cadena += " | Nombre: " + str(self.nombre)
        cadena += " | largo: " + str(self.largo)
        cadena += " | cintura: " + str(self.cintura)
        cadena += " | tela: " + tupla_telas[self.tela - 1]
        cadena += " | stock: " + str(self.stock)
        cadena += " | importe: " + str(self.importe)
        return cadena
