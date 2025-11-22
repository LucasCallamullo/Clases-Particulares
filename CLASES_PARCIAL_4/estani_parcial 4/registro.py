
class Equipo:
    # numero_insc INT, nombre STR, edad INT (12, 17), nivel INT (0,2), monto FLOAT
    def __init__(self, numero_insc, nombre, edad, nivel, monto, campeon):
        self.numero_insc = numero_insc
        self.nombre = nombre
        self.edad = edad
        self.nivel = nivel
        self.monto = monto
        self.campeon = campeon

    def __str__(self):
        # self.nivel(5, 7) 5-5         6-5           7
        # indices           0           1           2
        tupla_niveles = ("Bajo", "Intermedio", "Avanzado")

        if self.campeon:
            mensaje = "Es campeon"
        else:
            mensaje = "No es campeon"

        cadena = "Num Inscr: " + str(self.numero_insc)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Edad: " + str(self.edad)
        cadena += " | Nivel: " + tupla_niveles[self.nivel]
        cadena += " | Monto: " + str(self.monto)
        cadena += " | Campeon: " + mensaje
        return cadena