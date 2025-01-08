

class Error:
    # tupla_errores = ("Error 404", "Error 500", "Error 600")
    # codigo (1000, 5000) INT, mensaje STR, Hora ( 1 , 24 ), num_error(1, 3) , importe FLOAT

    def __init__(self, codigo, mensaje, hora, num_error, importe):
        self.codigo = codigo
        self.mensaje = mensaje
        self.hora = hora
        self.num_error = num_error
        self.importe = importe

    def __str__(self):
        # num_error(1, 3)  1-1         2-1          3-1
        # indices           0           1           2
        tupla_errores = ("Error 404", "Error 500", "Error 600")

        cadena = "Codigo: " + str(self.codigo)
        cadena += " | Mensaje: " + self.mensaje
        cadena += " | Hora: " + str(self.hora)
        cadena += " | Num_error: " + tupla_errores[self.num_error-1]
        cadena += " | Importe: " + str(self.importe)
        return cadena
