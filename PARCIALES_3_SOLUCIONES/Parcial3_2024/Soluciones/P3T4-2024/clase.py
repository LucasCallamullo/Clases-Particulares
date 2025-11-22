class Pintura:
    def __init__(self, cod, tip, met, imp):
        self.codigo = cod
        self.tipo = tip
        self.metros = met
        self.precio = imp

    def __str__(self):
        r = ""
        r = "{:<20}".format("Codigo: " + str(self.codigo))
        r += "{:<10}".format(" - Tipo: " + str(self.tipo))
        r += "{:25}".format(" - Metros de rinde: " + str(self.metros))
        r += "{:<17}".format(" - Precio: " + str(self.precio))
        return r
