class Taxi:
    def __init__(self, cod, dni, mar, tar):
        self.codigo = cod
        self.dni = dni
        self.marca = mar
        self.tarifa = tar

    def __str__(self):
        r = ""
        r = "{:<15}".format("Codigo: " + str(self.codigo))
        r += "{:<20}".format(" - DNI: " + str(self.dni))
        r += "{:<25}".format(" - Marca: " + str(self.marca))
        r += "{:<17}".format(" - Tarifa: " + str(self.tarifa))
        return r
