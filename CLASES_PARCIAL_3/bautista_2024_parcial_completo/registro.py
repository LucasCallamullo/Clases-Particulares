

# clase - registro - objeto
class Error:
    # tupla_errores = ("Error 404", "Error 502", "Error 600")
    # codigo (1000, 5000) INT, error_sist (1, 3), mensaje STR, hora(1, 24), importe FLOAT

    # funcion constructora o inicializadora
    def __init__(self, codigo, error_sist, mensaje, hora, importe):
        # ctrl + d
        self.codigo = codigo
        self.error_sist = error_sist
        self.mensaje = mensaje
        self.hora = hora
        self.importe = importe

    # funcion que reemplaze al print de los objetos
    def __str__(self):
        # error_sist(1, 3)  1-1             2-1         3-1
        # indices           0               1           2
        tupla_errores = ("Error 404", "Error 502", "Error 600")

        cadena = "Codigo: " + str(self.codigo)
        cadena += " | Error Sistema: " + tupla_errores[self.error_sist-1]
        cadena += " | Mensaje: " + self.mensaje
        cadena += " | Hora: " + str(self.hora)
        cadena += " | Importe: " + str(self.importe)
        return cadena
