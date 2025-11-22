

class Equipo:
    def __init__(self, nombre, jugadores, rango, puntaje, region, descripcion):
        self.nombre = nombre
        self.jugadores = jugadores
        self.rango = rango
        self.puntaje = puntaje
        self.region = region
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.nombre:<20} - Jugadores: {self.jugadores:>1} - Rango {self.rango:>1} " \
               f"- Puntaje: {self.puntaje:>4} - Región {self.region:>1}"
