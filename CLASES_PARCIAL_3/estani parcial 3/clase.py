

class Empleo:

    # num_id INT ; descripcion STR ; tipo INT (13, 18) ; sueldo FLOAT
    def __init__(self, num_id, descripcion, tipo, sueldo):
        # ctrl + d
        self.num_id = num_id
        self.descripcion = descripcion
        self.tipo = tipo
        self.sueldo = sueldo

    def __str__(self):
        cadena = "Num ID: " + str(self.num_id)
        cadena += " | Descripcion: " + self.descripcion
        cadena += " | Tipo: " + str(self.tipo)
        cadena += " | Sueldo: " + str(self.sueldo)
        return cadena