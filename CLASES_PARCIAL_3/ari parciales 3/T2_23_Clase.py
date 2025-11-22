class Ticket:
    def __init__(self, codigo, ide, destino, asiento, importe):
        self.codigo = codigo
        self.ide = ide
        self.destino = destino
        self.asiento = asiento
        self.importe = importe

    def __str__(self):
        cadena = "| Codigo: " + self.codigo
        cadena += "| Identificacion: " + str(self.ide)
        cadena += "| Destino: " + str(self.destino)
        cadena += "| Asiento: " + str(self.asiento)
        cadena += "| Importe: " + str(self.importe)
        return cadena