

class Estudiante:

    # legajo INT > 0 , nombre STR, curso INT (1, 17), aula (540, 555), importe FLOAT

    # 1: Pasaporte 2: DNI
    def __init__(self, legajo, nombre, curso, aula, importe, documento):
        self.legajo = legajo
        self.nombre = nombre
        self.curso = curso
        self.aula = aula
        self.importe = importe
        self.documento = documento

    def __str__(self):
        # curso(1, 17)    1-1   2-1   3 -1               4
        # indices          0     1    2
        tupla_cursos = ("1K1", "1K2", "1K3", ..., "1K17")

        # documento(1, 2)      1-1          2-1
        # indices               0           1
        tupla_documentos = ("Pasaporte", "DNI")

        cadena = "Legajo: " + str(self.legajo)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Curso: " + "1K" + str(self.curso)
        # cadena += " | Curso: " + tupla_cursos[self.curso-1]       # 2
        cadena += " | Aula: " + str(self.aula)
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Documento: " + tupla_documentos[self.documento - 1]
        return cadena
