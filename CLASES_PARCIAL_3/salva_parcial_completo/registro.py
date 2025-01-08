

class Figurita:
    # tupla_posiciones = ("Arquero", "Defensor", "MedioCampista", "Delantero")
    # pais(1, 32) INT, num_jug (1, 19) INT, nombre STR, posicion(1, 4) INT, importe > 0 FLOAT

    # funcion constructora o inicializadora
    def __init__(self, pais, num_jug, nombre, posicion, importe):
        # ctrl + d
        self.pais = pais
        self.num_jug = num_jug
        self.nombre = nombre
        self.posicion = posicion
        self.importe = importe

    # reemplazar el print del objeto por defecto
    def __str__(self):
        # posicion(1, 4)        1-1        2-1          3-1            4-1
        # indices               0           1               2               3
        tupla_posiciones = ("Arquero", "Defensor", "MedioCampista", "Delantero")

        cadena = "Pais: " + str(self.pais)
        cadena += " | Num Jug: " + str(self.num_jug)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Posicion: " + tupla_posiciones[self.posicion-1]
        cadena += " | Importe: " + str(self.importe)
        return cadena