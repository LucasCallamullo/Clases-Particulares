

class Empleo:

    # id > 0 INT, descripcion STR, tipo(11, 20), importe > 0 FLOAT

    # funcion constructora o inicializadora
    def __init__(self, id, descripcion, tipo, importe):
        self.id = id
        self.descripcion = descripcion
        self.tipo = tipo
        self.importe = importe

    # funcion que reemplaze el print por defecto
    def __str__(self):
        cadena = "ID: " + str(self.id)
        cadena += " | Descripcion: " + self.descripcion
        cadena += " | Tipo: " + str(self.tipo)
        cadena += " | Importe: " + str(self.importe)
        return cadena
