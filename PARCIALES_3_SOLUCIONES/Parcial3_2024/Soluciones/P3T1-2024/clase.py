class Producto:
    def __init__(self, cod, des, cal, tip, imp):
        self.codigo = cod
        self.descripcion = des
        self.calorias = cal
        self.tipo = tip
        self.precio = imp

    def __str__(self):
        r = ""
        r = "{:<20}".format("Codigo: " + str(self.codigo))
        r += "{:<35}".format(" - Descripcion: " + self.descripcion)
        r += "{:<15}".format("Calorias: " + str(self.calorias))
        r += "{:<12}".format(" - Tipo: " + str(self.tipo))
        r += "{:<17}".format(" - Importe: " + str(self.precio))
        return r
