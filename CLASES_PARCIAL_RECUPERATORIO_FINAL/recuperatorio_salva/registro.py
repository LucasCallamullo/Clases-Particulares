
class Proyecto:
    # codigo INT, titulo UNA CADENA, importe FLOAT, cantidad INT
    def __init__(self, codigo, titulo, importe, cantidad):
        self.codigo = codigo
        self.titulo = titulo
        self.importe = importe
        self.cantidad = cantidad

    def __str__(self):
        cadena = "Codigo: " + str(self.codigo)
        cadena += " | Titulo: " + str(self.titulo)
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Cantidad: " + str(self.cantidad)
        return cadena
