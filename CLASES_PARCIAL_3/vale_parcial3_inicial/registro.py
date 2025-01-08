

# clase / registro / objeto
class Tele:
    # num id de fabricacion, marca, pulgadas, precio

    #                 1               2             3
    # depositos = ("Deposito A", "Deposito B", "Deposito C")

    # id > 0, marca STR, pulgadas(32, 50), importe > 0, deposito(1, 3)

    # funcion constructora o inicializadora
    def __init__(self, id, marca, pulgadas, importe, deposito):
        # ctrl + d
        self.id = id
        self.marca = marca
        self.importe = importe
        self.pulgadas = pulgadas
        self.deposito = deposito

    # funcion de print
    def __str__(self):

        # self.deposito         1-1             2             3
        # indices               0               1           2
        tupla_depositos = ("Deposito A", "Deposito B", "Deposito C")

        cadena = "ID: " + str(self.id)
        cadena += " | Marca: " + self.marca
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Pulgadas: " + str(self.pulgadas)
        cadena += " | Deposito: " + tupla_depositos[self.deposito-1]
        return cadena
