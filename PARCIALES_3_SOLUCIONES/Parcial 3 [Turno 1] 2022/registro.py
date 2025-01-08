

class Paseo:
    # tipo (0 19)
    def __init__(self, id, name, tipo, importe):
        self.id = id
        self.name = name
        self.tipo = tipo
        self.importe = importe

    def __str__(self):
        cadena = "Id: " + str(self.id)
        cadena += " | Name: " + self.name
        cadena += " | Tipo: " + str(self.tipo)
        cadena += " | Importe: " + str(self.importe)
        return cadena
