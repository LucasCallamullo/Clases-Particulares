
class Pantalon:

    # codigo INT > 0 , nombre STR, largo(30, 50), cintura(30, 50), tela(1, 3), stock INT, importe FLOAT
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

        # tela(1, 3)    1-1         2-1         3-1
        # indices       0         1           2
        tupla_telas = ("Jean", "Gabardina", "Denim")

        cadena = "Codigo: " + str(self.codigo)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Largo: " + str(self.largo)
        cadena += " | Cintura: " + str(self.cintura)
        cadena += " | Tela: " + tupla_telas[self.tela - 1]
        cadena += " | Stock: " + str(self.stock)
        cadena += " | Importe: " + str(self.importe)
        return cadena
