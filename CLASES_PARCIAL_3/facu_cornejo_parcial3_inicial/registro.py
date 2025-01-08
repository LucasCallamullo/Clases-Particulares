

# clase / objeto / registro
class Tele:

    # id INT > 0, marca, pulgadas(32, 42), importe > 0

    # funcion constructora o inicializadora
    def __init__(self, id, marca, pulgadas, importe):
        # ctrl + d
        self.id = id
        self.marca = marca
        self.pulgadas = pulgadas
        self.importe = importe

    # reemplaza la funcion de print
    def __str__(self):
        cadena = "ID: " + str(self.id)
        cadena += " | Marca: " + self.marca
        cadena += " | Pulgadas: " + str(self.pulgadas)
        cadena += " | Importe: " + str(self.importe)
        return cadena
