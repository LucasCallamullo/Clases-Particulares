

# clases / registros / objetos
class Tele:

    # lotes = ("Deposito 1", "Deposito 2", "Deposito 3")
    # numero identificacion produccion > 0 , marca STR, pulgadas(32, 50), precio > 0, lote(1, 3)

    # funcion constructora o inicializadora
    def __init__(self, id, marca, pulgadas, importe, lote):
        # ctrl + d
        self.id = id
        self.marca = marca
        self.pulgadas = pulgadas
        self.importe = importe
        self.lote = lote

    # funcion de print
    def __str__(self):

        # lote(1, 3) 1-1
        # indices      0            1               2
        lotes = ("Deposito 1", "Deposito 2", "Deposito 3")

        cadena = "ID: " + str(self.id)
        cadena += " | Marca: " + self.marca
        cadena += " | Pulgadas: " + str(self.pulgadas)
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Lote: " + lotes[self.lote-1]
        return cadena
