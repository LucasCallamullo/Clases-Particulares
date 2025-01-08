

class Error:
    # hora (0 23)    cod_errror entre 1000 y 5000
    def __init__(self, cod_error, num_sist, mensaje, hora, segundos):
        self.cod_error = cod_error
        self.num_sist = num_sist
        self.mensaje = mensaje
        self.hora = hora
        self.segundos = segundos

    def __str__(self):

        # str(self.num_sist)  1:windows 2:Mac 3:linux
        variable = num_str(self.num_sist)

        cadena = "Cod Error: " + str(self.cod_error)
        cadena += " | num_sist: " + variable
        cadena += " | mensaje: " + self.mensaje
        cadena += " | hora: " + str(self.hora)
        cadena += " | segundos: " + str(self.segundos)
        return cadena


# 1:windows 2:Mac 3:linux
def num_str(num_sist):
    # num_sist(1, 3)

    #              1-1      2-1       3-1
    #               0           1       2
    sistemas_op = ["Windows", "Mac", "Linux"]
    variable = sistemas_op[num_sist-1]      #
    return variable
