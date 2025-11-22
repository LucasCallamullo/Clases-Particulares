class Articulo:
    def __init__(self, cod, des, sec, vol, imp):
        self.codigo = cod
        self.descripcion = des
        self.seccion = sec
        self.volumen = vol
        self.precio = imp

    def __str__(self):
        r = ""
        r = "{:<20}".format("Codigo: " + str(self.codigo))
        r = "{:<30}".format("Descripcion: " + str(self.descripcion))
        r += "{:<10}".format(" - Tipo: " + str(self.seccion))
        r += "{:<20}".format(" - Volumen: " + str(self.volumen))
        r += "{:<17}".format(" - Precio: " + str(self.precio))
        return r
