class Tubo:
    def __init__(self, codigo, diametro, aplicacion, gramos, ignifugo):
        self.codigo = codigo
        self.diametro = diametro
        self.aplicacion = aplicacion
        self.gramos = gramos
        self.ignifugo = ignifugo

    def __str__(self):
        # self.ignifugo        1-1         2-1
        # indices               0           1
        tupla = ("Ignifugo", "No ignifugo")

        cadena = "Codigo: " + str(self.codigo)
        cadena += " | Diametro: " + str(self.diametro)
        cadena += " | Aplicacion: " + str(self.aplicacion)
        cadena += " | Gramos: " + str(self.gramos)
        cadena += " | Ignifugo: " + tupla[self.ignifugo - 1]
        return cadena