class Estudiante:
    # legajo > 0 , curso ( 1, 17), aula  (540, 555),
    # (Nombre (1, 4)    1:Lucas 2: Matias 3:Tomas 4:Jere
    def __init__(self, legajo, curso, aula, cuestionarios, nombre):
        self.legajo = legajo
        self.curso = curso
        self.aula = aula
        self.cuestionarios = cuestionarios
        self.nombre = nombre

    def __str__(self):

        # nombre=   540-540                        543
        # nombre=   1-1         2-1       3-1       4-1
        # indices=  0           1           2       3
        nombres = ["Lucas", "Matias", "Tomas", "Jere"]

        cad = "Legajo: " + str(self.legajo)
        cad += " | Curso: " + "1K" + str(self.curso)
        cad += " | Aula: " + str(self.aula)
        cad += " | Cuestionarios: " + str(self.cuestionarios)
        cad += " | Nombre: " + nombres[self.nombre-1]
        return cad
