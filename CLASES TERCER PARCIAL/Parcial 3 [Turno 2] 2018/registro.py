

class Servicio:
    # tipo s = 0, 14        ; id > 0
    def __init__(self, id, desc, tipo_s, importe, cant_p):
        self.id = id
        self.desc = desc
        self.tipo_s = tipo_s
        self.importe = importe
        self.cant_p = cant_p

    def __str__(self):
        cadena = "ID: " + str(self.id)
        cadena += " | Desc: " + self.desc
        cadena += " | Tipo S: " + str(self.tipo_s)
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Cant_p: " + str(self.cant_p)
        return cadena
