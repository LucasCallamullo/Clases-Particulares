
class Proyecto:
    # codigo INT, titulo STR, importe FLOAT, cant_inv INT, laboratorio(1, 10), zona(15, 18), disponible BOOL
    def __init__(self, codigo, titulo, importe, cant_inv, laboratorio, zona, disponible):
        # ctrl + d
        self.codigo = codigo
        self.titulo = titulo
        self.importe = importe
        self.cant_inv = cant_inv
        self.laboratorio = laboratorio
        self.zona = zona
        self.disponible = disponible

    def __str__(self):
        # en vez de mostrar si el bool esta en true o false, debe reemplazar con la cadena "Habilitado" si esta entrue
        # y sino con "No habilitado" si esta en False

        if self.disponible is True:
            hab = "Habilitado"
        else:
            hab = "No Habilitado"

        cadena = "Codigo: " + str(self.codigo)
        cadena += " | titulo: " + self.titulo
        cadena += " | importe: " + str(self.importe)
        cadena += " | cant_inv: " + str(self.cant_inv)
        cadena += " | laboratorio: " + str(self.laboratorio)
        cadena += " | zona: " + str(self.zona)
        cadena += " | disponible: " + hab
        return cadena
