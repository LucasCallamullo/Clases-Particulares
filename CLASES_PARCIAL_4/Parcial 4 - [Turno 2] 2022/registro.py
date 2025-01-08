

class Vehiculo:
    # size ( 1 , 4 ) ,  tipo ( 0 , 4 )
    def __init__(self, id, size, tipo, importe):
        self.id = id
        self.size = size
        self.tipo = tipo
        self.importe = importe

# el tamaño del vehículo (1: Subcompacto, 2: Compacto,
# 3: Mediano, 4: Grande), el tipo de motor (0: Nafta, 1: Gasoil, 2: GNC, 3: Eléctrico, 4: Hidrógeno) y
    def __str__(self):

        # size(1,4)     1-1             2-1         3-1         4-1
        # ind           0               1           2           3
        desc_size = ["Subcompacto", "Compacto", "Mediano", "Grande"]

        #               0           1       2       3           4
        desc_motor = ["Nafta", "Gasoil", "GNC", "Electrico", "Hidrogeno"]


        cad = "ID: " + str(self.id)
        cad += " | Tamaño: " + desc_size[self.size-1]
        cad += " | Tipo: " + desc_motor[self.tipo]
        cad += " | Importe: " + str(self.importe)
        return cad
