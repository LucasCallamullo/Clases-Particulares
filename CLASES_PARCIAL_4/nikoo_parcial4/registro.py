
# clases or objetos
class Pieza:

    # id INT > 0 ; descripcion STR; tipo (0, 19) ; sector (10, 12) ; stock INT ; precio FLOAT
    def __init__(self, id, descripcion, tipo, sector, stock, precio):
        self.id = id
        self.descripcion = descripcion
        self.tipo = tipo
        self.sector = sector
        self.stock = stock
        self.precio = precio

    def __str__(self):

        # en vez de mostrar el valor del sector, muestre su descipcion asociada
        # sector ( 10: Sector 1 ; 11: Sector 2 ; 12: Sector 3 )

        #
        # sector(10, 12)   10-10        11-10       12-10
        # indices           0           1           2
        tupla_sectores = ("Sector 1", "Sector 2", "Sector 3")

        cadena = "ID: " + str(self.id)
        cadena += " - Descripcion: " + self.descripcion
        cadena += " - Tipo: " + str(self.tipo)
        cadena += " - Sector: " + tupla_sectores[self.sector - 10]
        cadena += " - Stock: " + str(self.stock)
        cadena += " - Precio: " + str(self.precio)
        return cadena