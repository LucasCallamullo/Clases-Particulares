

class Error:
    # errores ( 1:"Error 404", 2:"Error 500", 3:"Error 505"
    # codigo (1000, 5000) INT, mensaje STR, hora(1, 24), importe, errores(1, 3)
    def __init__(self, codigo, mensaje, hora, importe, errores):
        self.codigo = codigo
        self.mensaje = mensaje
        self.hora = hora
        self.importe = importe
        self.errores = errores

    def __str__(self):
        # errores(1, 3)   1-1             2-1         3-2
        # indices           0               1           2
        tupla_errores = ("Error 404", "Error 500", "Error 505")

        cadena = "Codigo: " + str(self.codigo)
        cadena += " | Mensaje: " + self.mensaje
        cadena += " | Hora: " + str(self.hora)
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Errores: " + tupla_errores[self.errores-1]
        return cadena
