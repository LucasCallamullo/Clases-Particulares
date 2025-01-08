

class Paquete:
    # tipo_p (0, 19)                ; id > 0

    # desc ( 1, 4) y que 1=A ; 2 = B ;  3 = C ; 4 = D pero por pantalla se debe mostrar el string que corresponda

    def __init__(self, id, desc, tipo_p, cant_dias, importe):
        self.id = id            # ctrl + d
        self.desc = desc
        self.tipo_p = tipo_p
        self.cant_dias = cant_dias
        self.importe = importe

    def __str__(self):

        desc_str = desc_to_str(self.desc)

        cadena = "ID: " + str(self.id)
        cadena += " | Descripcion: " + desc_str
        cadena += " | tipo_p: " + str(self.tipo_p)
        cadena += " | Cant Dias: " + str(self.cant_dias)
        cadena += " | importe: " + str(self.importe)
        return cadena


def desc_to_str(desc):
    descripciones = ["A", "B", "C", "D"]
    return descripciones[desc-1]
