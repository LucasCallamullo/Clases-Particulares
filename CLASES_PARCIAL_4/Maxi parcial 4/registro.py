

class Consumo:
    # num_tel STR, hora (0, 23), tipo(1, 3), importe FLOAT > 0
    def __init__(self, num_tel, hora, tipo, importe):
        self.num_tel = num_tel
        self.hora = hora
        self.tipo = tipo
        self.importe = importe

    def __str__(self):
        # tipo          1-1    2-1         3-1
        # indices       0       1           2
        tuplas_tipo = ("SMS", "Llamada", "Uso de Datos")

        cadena = "Num Tel: " + self.num_tel
        cadena += " | Hora: " + str(self.hora)
        cadena += " | Tipo: " + tuplas_tipo[self.tipo-1]
        cadena += " | Importe: " + str(self.importe)
        return cadena