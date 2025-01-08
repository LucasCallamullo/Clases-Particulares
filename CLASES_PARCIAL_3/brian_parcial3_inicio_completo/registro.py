

class Estudiante:

    # nos crea la clase estudiante
    # ctrl + d
    def __init__(self, nombre, edad, legajo, carrera, cuota_importe):
        self.nombre = nombre
        self.edad = edad
        self.legajo = legajo
        self.carrera = carrera
        self.cuota_importe = cuota_importe

    def __str__(self):
        # carreras (1, 4) ( "Sistemas", "Civil", "Industrial", "Quimica")
        tupla_carreras = ("Sistemas", "Civil", "Industrial", "Quimica")

        cadena = "Nombre: " + self.nombre
        cadena += " | Edad: " + str(self.edad)   # int
        cadena += " | Legajo: " + str(self.legajo)   # int
        cadena += " | Carrera: " + tupla_carreras[self.carrera-1]
        cadena += " | cuota_importe: " + str(self.cuota_importe)
        return cadena
