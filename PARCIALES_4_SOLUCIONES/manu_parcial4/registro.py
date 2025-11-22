

class Pantalon:

    # codigo > 0, modelo STR, talle_largo (30, 50), talle_ancho(30, 50)
    # tela(1, 3), stock INT, precio FLOAT

    # tipo de tela (1: Jean, 2:Gabardina, 3: Denim)
    def __init__(self, codigo, modelo, talle_largo, talle_ancho, tela, stock, precio):
        self.codigo = codigo
        self.modelo = modelo
        self.talle_largo = talle_largo
        self.talle_ancho = talle_ancho
        self.tela = tela
        self.stock = stock
        self.precio = precio        # importes

    def __str__(self):

        # tela(1, 3)   1-1         2-1          3-1
        # indices       0           1           2
        tupla_telas = ("Jean", "Gabardina", "Denim")

        cadena = "Codigo: " + str(self.codigo)
        cadena += " - modelo: " + str(self.modelo)
        cadena += " - talle_largo: " + str(self.talle_largo)
        cadena += " - talle_ancho: " + str(self.talle_ancho)
        cadena += " - tela: " + tupla_telas[self.tela - 1]
        cadena += " - stock: " + str(self.stock)
        cadena += " - precio: " + str(self.precio)
        return cadena