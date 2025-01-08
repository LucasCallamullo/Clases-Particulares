

class Proyecto:
    # codigo INT, titulo STR, importe FLOAT, cantidad_inv INT, laboratorio(3, 7), encargado(5, 12)
    def __init__(self, codigo, titulo, importe, cantidad_inv, laboratorio, encargado):
        # ctrl + d
        self.codigo = codigo
        self.titulo = titulo
        self.importe = importe
        self.cantidad_inv = cantidad_inv
        self.laboratorio = laboratorio
        self.encargado = encargado

    def __str__(self):
        cadena = "Codigo: " + str(self.codigo)
        cadena += " | titulo: " + self.titulo
        cadena += " | importe: " + str(self.importe)
        cadena += " | cantidad_inv: " + str(self.cantidad_inv)
        cadena += " | laboratorio: " + str(self.laboratorio)
        cadena += " | encargado: " + str(self.encargado)
        return cadena
