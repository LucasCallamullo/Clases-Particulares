class Pokemon:
    def __init__(self, nombre, numero, tipo, pc, nivel):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.pc = pc
        self.nivel = nivel

    def __str__(self):
        return f"{self.nombre:<15} - N° {self.numero:>4} - Tipo {self.tipo:>2} - PC: {self.pc:>6} - Nivel Evolución: {self.nivel:>2}"
