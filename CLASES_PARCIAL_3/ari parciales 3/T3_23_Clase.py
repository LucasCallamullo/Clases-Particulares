
class Servicio:
    def __init__(self, ide, nombre, tipo, importe):
        self.ide = ide
        self.nombre = nombre
        self.tipo = tipo
        self.importe = importe
    def __str__(self):
        cadena = "| Identificacion: " + str(self.ide)
        cadena += "| Nombre: " + self.nombre
        cadena += "| Tipo: " + str(self.tipo)
        cadena += "| Importe: " + str(self.importe)
        return cadena









