

# registro clase objeto
class Estudiante:
    # Legajo , Nombre (str) , Carrera ( 1, 4 ), cuota importe > 0 ( float )
    def __init__(self, legajo, nombre, carrera, importe):         # funcion constructor o inicializadora de la clase
        # ctrl + d
        self.legajo = legajo
        self.nombre = nombre
        self.carrera = carrera
        self.importe = importe

    def __str__(self):
        # alt + 92
        # indices              0        1           2            3
        # valores              1        2           3            4
        tupla_carreras = ("Sistemas", "Civil", "Industrial", "Quimica")

        # cadena = (f"Legajo: {self.legajo} | "
        #          f"Nombre: ")
        cadena = "Legajo: " + str(self.legajo)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Carrera: " + tupla_carreras[self.carrera-1]
        cadena += " | Importe: " + str(self.importe)
        return cadena
