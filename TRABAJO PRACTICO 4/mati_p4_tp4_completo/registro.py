

class Vehiculo:

    # id INT > 0, tamanio(1, 4), tipo(0, 5), importe FLOAT, marca(3, 7), anio(2000, 2020)

    def __init__(self, id, tamanio, tipo, importe, marca, anio):
        self.id = id
        self.tamanio = tamanio
        self.tipo = tipo
        self.importe = importe
        self.marca = marca
        self.anio = anio

    def __str__(self):
        # tamanio(1, 4)     1           2           3           4
        # indices           0           1           2           3
        tupla_tams = ("Subcompacto", "Compacto", "Mediano", "Grande")

        # tipo(0, 4)    0       1           2       3           4
        # indices       0       1           2       3           4
        tupla_tipos = ("Nafta", "Gasoil", "GNC", "Eléctrico", "Hidrógeno")

        cadena = "ID: " + str(self.id)
        cadena += " | Tamaño: " + tupla_tams[self.tamanio - 1]
        cadena += " | tipo: " + tupla_tipos[self.tipo]
        cadena += " | importe: " + str(self.importe)
        cadena += " | marca: " + str(self.marca)
        cadena += " | anio: " + str(self.anio)
        return cadena
