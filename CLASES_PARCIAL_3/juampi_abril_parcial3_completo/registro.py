

class Juicio:

    # codigo > 0 INT , descripcion STR, tipo(1, 15) INT, nombre STR, importe > 0 FLOAT

    # funcion constructora o inicializadora
    def __init__(self, codigo, descripcion, tipo, nombre, importe):
        # ctrl + d
        self.codigo = codigo
        self.descripcion = descripcion
        self.tipo = tipo
        self.nombre = nombre
        self.importe = importe

    # funcion de print
    def __str__(self):
        cadena = "Codigo: " + str(self.codigo)
        cadena += " | Descripcion: " + self.descripcion
        cadena += " | Tipo: " + str(self.tipo)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Importe: " + str(self.importe)
        return cadena
