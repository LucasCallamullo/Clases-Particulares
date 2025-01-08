

# clase - registro - objetos
class Figurita:

    # funcion constructora o inicializadora
    # posiciones = ("Arquero", "Defensor", "Mediocampista", "Delantero")
    # pais(1, 32) , num_jug(1, 19), nombre STR, posicion(1, 4), importe > 0
    def __init__(self, pais, num_jug, nombre, posicion, importe):
        # ctrl + d
        self.pais = pais
        self.num_jug = num_jug
        self.nombre = nombre
        self.posicion = posicion
        self.importe = importe

    #
    def __str__(self):

        # posicion(1, 4)    1-1             2-1             3-1         4-1
        # indices               0           1               2           3
        tupla_posiciones = ("Arquero", "Defensor", "Mediocampista", "Delantero")

        cadena = "Pais: " + str(self.pais)
        cadena += " | Num Jug: " + str(self.num_jug)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Posicion: " + tupla_posiciones[self.posicion-1]
        cadena += " | Importe: " + str(self.importe)
        return cadena