

class Televisor:
    # (size, entre 30 y 40)        ; Resolución (1, 3)
    def __init__(self, marca, size, resolucion, importe):
        self.marca = marca
        self.size = size
        self.resolucion = resolucion
        self.importe = importe

    def __str__(self):

        #  1:720p, 2:1080p, 3:4K)
        # self.resolucion ( 1, 3)

        #                    1-1        2-1     3-1
        # indices               0       1       2
        desc_resoluciones = ("720P", "1080P", "4K")

        cad = "Marca: " + self.marca
        cad += " | Tamaño: " + str(self.size)
        cad += " | Resolucion: " + desc_resoluciones[self.resolucion-1]
        cad += " | Importe: " + str(self.importe)
        return cad
