# clase , registro , objeto
class Parlante:

    # colores = ("Negro", "Blanco", "Azul")
    # Numero id de produccion > 0, Marca, Color(1, 3), Precio > 0

    # funcion constructora o inicializadora
    def __init__(self, id, marca, color, importe):
        # ctrl + d
        self.id = id
        self.marca = marca
        self.color = color
        self.importe = importe

    def __str__(self):
        # self.color  1-1       2-1      3-1
        # indices      0        1        2
        colores = ("Negro", "Blanco", "Azul")

        # format <20:
        cadena = "ID: " + str(self.id)
        cadena += " | Marca: " + self.marca
        cadena += " | Color: " + colores[self.color-1]
        cadena += " | Importe: " + str(self.importe)
        return cadena