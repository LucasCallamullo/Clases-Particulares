

class Beca:
    def __init__(self, d, nom, tip, car, mon):
        self.dni = d
        self.nombre = nom
        self.tipo = tip
        self.carrera = car
        self.monto = mon

    def __str__(self):
        cad = 'Dni: {:<10} | Nombre: {:<30} |  Tipo beca: {:<12} |  Carrera: {:<12} |  Monto: {:<10}'
        return cad.format(self.dni, self.nombre, self.tipo, self.carrera, self.monto)

