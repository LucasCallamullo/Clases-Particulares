
class Estudiante:

    def __init__(self, legajo, nombre, curso, aula, cuest_aprobados):
        self.legajo = legajo
        self.nombre = nombre
        self.curso = curso
        self.aula = aula
        self.cuest_aprobados = cuest_aprobados

    def __str__(self):
        cadena = "Legajo: " + str(self.legajo)
        cadena += " - Nombre: " + self.nombre
        cadena += " - Curso: " + str(self.curso)
        cadena += " - Aula: " + str(self.aula)
        cadena += " - Cuestionarios aprobados: " + str(self.cuest_aprobados)
        return cadena
