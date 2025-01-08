

# clase - registro - objeto
class Juicio:

    # codigo INT, descripcion STR, tipo(1, 15) , nombre STR, importe FLOAT

    # funcion constrcutora o inicializadora
    def __init__(self, codigo, descripcion, tipo, nombre, importe):
        self.codigo = codigo
        self.descripcion = descripcion
        self.tipo = tipo
        self.nombre = nombre
        self.importe = importe

    # nuestra funcion de print
    def __str__(self):
        cadena = "Codigo: " + str(self.codigo)
        cadena += " | Descripcion: " + self.descripcion
        cadena += " | Tipo: " + str(self.tipo)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Importe: " + str(self.importe)
        return cadena
