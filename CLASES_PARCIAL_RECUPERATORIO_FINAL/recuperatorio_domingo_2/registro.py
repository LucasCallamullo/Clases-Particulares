
class Proyecto:

    # codigo INT, titulo STR, importe FLOAT, cant_inv INT, laboratorio(3, 5), zona(10, 15), disponible BOOL
    def __init__(self, codigo, titulo, importe, cant_inv, laboratorio, zona, disponible):

        self.codigo = codigo
        self.titulo = titulo
        self.importe = importe
        self.cant_inv = cant_inv
        self.laboratorio = laboratorio
        self.zona = zona
        self.disponible = disponible

    def __str__(self):

        # si esta disponible esta en true mostrar "Habilitado" y si esta en fFalse mostrar "No Habilitado"
        if self.disponible is True:
            cad_hab = "Habilitado"
        else:
            cad_hab = "No Habilitado"

        cadena = "Codigo: " + str(self.codigo)
        cadena += " | titulo: " + str(self.titulo)
        cadena += " | importe: " + str(self.importe)
        cadena += " | cant_inv: " + str(self.cant_inv)
        cadena += " | laboratorio: " + str(self.laboratorio)
        cadena += " | zona: " + str(self.zona)
        cadena += " | disponible: " + cad_hab
        return cadena