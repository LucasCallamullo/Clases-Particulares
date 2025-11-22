class Tubo:
    def __init__(self, cod, dia, tip, gra, imp):
        self.codigo = cod
        self.diametro = dia
        self.tipo = tip
        self.gramos = gra
        self.ignifugo = imp

    def __str__(self):
        r = ""
        r = "{:<17}".format("Codigo: " + str(self.codigo))
        r += "{:<20}".format(" - Diametro: " + str(self.diametro))
        r += "{:<20}".format(" - Tipo: " + str(self.tipo))
        r += "{:<17}".format(" - Gramos: " + str(self.gramos))
        r += "{:<17}".format(" - Ignifugo: " + str(self.ignifugo))
        return r
