

class Termo:

    # marca, capacidad(1,3), precio > 0, diametro(10cm, 30), id produccion > 0

    # funcion constructora o inicializadora
    def __init__(self, marca, capacidad, importe, diametro, id):
        # ctrl + d
        self.marca = marca
        self.capacidad = capacidad
        self.importe = importe
        self.diametro = diametro
        self.id = id

    def __str__(self):
        cadena = "Marca: " + self.marca
        cadena += " | Capacidad: " + str(self.capacidad)
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Diametro: " + str(self.diametro)
        cadena += " | ID: " + str(self.id)
        return cadena
