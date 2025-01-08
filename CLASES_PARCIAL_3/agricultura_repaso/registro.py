

class Trabajo:
    def __init__(self, id, desc, tipo, importe, cant_personas):
        self.id = id                    # ctrl + d
        self.desc = desc
        self.tipo = tipo
        self.importe = importe
        self.cant_personas = cant_personas


    def __str__(self):
        cadena = "Id: " + str(self.id) + \
                "\n Descripcion:" + self.desc + \
                "\n tipo:" + str(self.tipo) + \
                "\n importe:" + str(self.importe) + \
                "\n personas:" + str(self.cant_personas)
        return cadena
