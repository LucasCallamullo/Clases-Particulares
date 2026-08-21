class Equipo:
    def __init__(self, num, nom, edad, niv, monto):
        self.numero = num
        self.nombre = nom
        self.edad = edad
        self.nivel = niv
        self.monto = monto

    def __str__(self):
        niveles = ("Bajo", "Intermedio", "Avanzado")
        cadena = "Numero: " + str(self.numero)
        cadena += " - Nombre: " + self.nombre
        cadena += " - Edad: " + str(self.edad)
        cadena += " - Nivel: " + niveles[self.nivel]
        cadena += " - Monto: $" + str(self.monto)
        return cadena


if __name__ == "__main__":
    e = Equipo(100, "Equipo 1", 15, 2, 2548.3)
    print(e)

