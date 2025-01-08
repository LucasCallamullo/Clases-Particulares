

# clase es una plantilla base que define los atributos con los cuales vamos a crear objetos a partir de esta plantill
class Paquete:

    # tipo = ("Europa", "Asia", "Oceanía", "America"

    # id > 0 INT, descripcion STR, tipo(10, 13), cantidad INT, importe FLOAT

    # funcion constuctora
    def __init__(self, id, descripcion, tipo, cantidad, importe):
        self.id = id
        self.descripcion = descripcion
        self.tipo = tipo
        self.cantidad = cantidad
        self.importe = importe

    def __str__(self):

        # tipo(10, 13)    10-10    11-10      12          13
        # indices           0       1       2           3
        tupla_tipos = ("Europa", "Asia", "Oceanía", "America")

        cadena = "ID: " + str(self.id)
        cadena += " | Descripcion: " + self.descripcion
        cadena += " | Tipo: " + tupla_tipos[self.tipo-10]
        cadena += " | Cantidad: " + str(self.cantidad)
        cadena += " | Importe: " + str(self.importe)
        return cadena