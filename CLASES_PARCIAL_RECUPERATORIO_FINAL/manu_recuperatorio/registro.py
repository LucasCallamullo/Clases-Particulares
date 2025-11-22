
class Proyecto:
    # codigo INT, titulo STR, importe FLOAT, cant_inv INT, disponible BOOL
    # laboratorio (3, 5), zona(10, 15)
    def __init__(self, codigo, titulo, importe, cant_inv, disponible, laboratorio, zona):
        # ctrl + d
        self.codigo = codigo
        self.titulo = titulo
        self.importe = importe
        self.cant_inv = cant_inv
        self.disponible = disponible
        self.laboratorio = laboratorio
        self.zona = zona

    def __str__(self):
        # si disponible esta en True mostrar la frase "Habilitado", si esta en false "No Habilitado"

        if self.disponible is True:
            hab = "Habilitado"
        else:
            hab = "No Habilitado"

        #
        cadena = "Codigo: " + str(self.codigo)
        cadena += " | titulo: " + str(self.titulo)
        cadena += " | importe: " + str(self.importe)
        cadena += " | cant_inv: " + str(self.cant_inv)
        cadena += " | disponible: " + hab
        cadena += " | laboratorio: " + str(self.laboratorio)
        cadena += " | zona: " + str(self.zona)
        return cadena
