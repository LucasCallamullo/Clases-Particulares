

# clases / registros / objetos
class Tele:

    # funcion constructora o inicializadora
    # id > 0 INT, marca STR, pulgadas (32, 50) INT, importe > 0 FLOAT
    def __init__(self, id, marca, pulgadas, importe):
        # ctrl + d
        self.id = id
        self.marca = marca
        self.pulgadas = pulgadas
        self.importe = importe

    def __str__(self):
        cadena = "ID: " + str(self.id)
        cadena += " | Marca: " + str(self.marca)
        cadena += " | Pulgadas: " + str(self.pulgadas)
        cadena += " | Importe: " + str(self.importe)
        return cadena