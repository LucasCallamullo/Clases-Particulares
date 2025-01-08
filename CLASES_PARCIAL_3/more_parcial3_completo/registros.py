

# registros / clase / objetos
class Estudiante:
    # carreras = ("Sistemas", "Civil", "Industrial", "Quimica")
    # legajo INT > 0, nombre STR, carrera(1, 4) INT, cuota a pagar - importe FLOATS > 0

    # funcion constructora o inicializadora
    def __init__(self, legajo, nombre, carrera, importe):
        self.legajo = legajo
        self.nombre = nombre
        self.carrera = carrera
        self.importe = importe

    def __str__(self):
        # carreras      1           2       3           4
        # indices       0          1          2             3
        carreras = ("Sistemas", "Civil", "Industrial", "Quimica")

        # f"{20<: }  "
        cadena = "Legajo: " + str(self.legajo)
        cadena += " | Nombre:" + self.nombre
        cadena += " | Carrera:" + carreras[self.carrera-1]
        cadena += " | Importe:" + str(self.importe)
        return cadena
