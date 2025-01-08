

# Clases , Registros , Objetos
class Figurita:
    # tupla_posicion = ("Arquero", "Defensor", "Mediocampista", "Delantero")

    # pais jugador (1, 32), numero jugador ( 1, 19), nombre, posicion (1, 4), importe > 0

    # Funcion constructora o inicializadora
    def __init__(self, pais, num_jugador, nombre, posicion, importe):
        self.pais = pais
        self.num_jugador = num_jugador
        self.nombre = nombre
        self.posicion = posicion
        self.importe = importe

    def __str__(self):

        # self.posicion  =      1-1         2-1        3 -1            4-1
        # indices        =      0           1           2               3
        tupla_posiciones = ("Arquero", "Defensor", "Mediocampista", "Delantero")

        cadena = "Pais: " + str(self.pais)
        cadena += " | Num Jugador: " + str(self.num_jugador)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Posicion: " + tupla_posiciones[self.posicion-1]
        cadena += " | Importe: " + str(self.importe)
        return cadena
