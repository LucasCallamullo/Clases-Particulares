

class Equipo:
    # importe e id > 0   ;
    def __init__(self, id, desc, importe, cant_d):
        self.id = id
        self.desc = desc
        self.importe = importe
        self.cant_d = cant_d

    def __str__(self):
        cadena = "ID: " + str(self.id)
        cadena += " | Desc: " + self.desc
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Cant_d: " + str(self.cant_d)
        return cadena
