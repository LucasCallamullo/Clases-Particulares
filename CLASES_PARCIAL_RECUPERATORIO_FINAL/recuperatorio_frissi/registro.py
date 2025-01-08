
class Proyecto:
    # codigo INT, titulo STR "termina en .", importe FLOAT, cant_inv INT, disponible BOOL,
    # laboratorio(3, 5), zona(10, 13)

    def __init__(self, codigo, titulo, importe, cant_inv, disponibilidad, laboratorio, otro):
        self.codigo = codigo
        self.titulo = titulo
        self.importe = importe
        self.cant_inv = cant_inv
        self.disponibilidad = disponibilidad
        self.laboratorio = laboratorio
        self.otro = otro

    def __str__(self):
        # si esta en true diga "Habilitado" si esta en false "No Habilitado"
        if self.disponibilidad is True:     # True
            hab = "Habilitado"
        else:
            hab = "No Habilitado"

        cadena = "Codigo: " + str(self.codigo)
        cadena += " | titulo: " + self.titulo
        cadena += " | importe: " + str(self.importe)
        cadena += " | cant_inv: " + str(self.cant_inv)
        cadena += " | disponibilidad: " + hab
        cadena += " | laboratorio: " + str(self.laboratorio)
        cadena += " | otro: " + str(self.otro)
        return cadena
