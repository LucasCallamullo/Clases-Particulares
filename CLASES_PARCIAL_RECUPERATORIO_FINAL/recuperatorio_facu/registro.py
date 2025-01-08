
class Proyecto:
    # codigo INT, titulo STR que termina ".", importe FLOAT, cantidad INT, laboratorio(3, 5), calle(10, 15)
    def __init__(self, codigo, titulo, importe, cantidad, laboratorio, calle):
        # ctrl + d
        self.codigo = codigo
        self.titulo = titulo
        self.importe = importe
        self.cantidad = cantidad
        self.laboratorio = laboratorio
        self.calle = calle

    def __str__(self):
        cadena = "Codigo: " + str(self.codigo)
        cadena += " | titulo: " + self.titulo
        cadena += " | importe: " + str(self.importe)
        cadena += " | cantidad: " + str(self.cantidad)
        cadena += " | laboratorio: " + str(self.laboratorio)
        cadena += " | calle: " + str(self.calle)
        return cadena
