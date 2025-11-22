

class Figurita:
    # pais (1, 32), num_jug (1, 19), nombre STR, posicion (0, 3), importe FLOAT
    def __init__(self, pais, num_jug, nombre, posicion, importe):
        self.pais = pais
        self.num_jug = num_jug
        self.nombre = nombre
        self.posicion = posicion
        self.importe = importe

    def __str__(self):

        # posicion(5,8)         5-5         6-5         7-5             8-5

        # posicion(0,3)         0           1           2               3
        # indices               0           1           2               3
        tupla_posiciones = ("Arquero", "Defensor", "Mediocampista", "Delantero")

        cadena = "Pais: " + str(self.pais)
        cadena += " | num_jug: " + str(self.num_jug)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Posicion: " + tupla_posiciones[self.posicion]
        cadena += " | Importe: " + str(self.importe)
        return cadena

