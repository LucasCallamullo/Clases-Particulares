
class Proyecto:

    # codigo INT, titulo STR ".", importe FLOAT, cant_inv INT, disponible BOOL,
    # laboratorio(3, 5), zona(15, 18)

    def __init__(self, codigo, titulo, importe, cant_inv, disponible, laboratorio, zona):
        self.codigo = codigo
        self.titulo = titulo
        self.importe = importe
        self.cant_inv = cant_inv
        self.disponible = disponible
        self.laboratorio = laboratorio
        self.zona = zona

    def __str__(self):

        # mostrar el mensaje "habilitado" si disponible esta en True y sino "no habilitado" si es False
        if self.disponible is True:
            hab = "Habilitado"
        else:
            hab = "No Habilitado"

        cadena = "Codigo: " + str(self.codigo)
        cadena += " | titulo: " + str(self.titulo)
        cadena += " | importe: " + str(self.importe)
        cadena += " | cant_inv: " + str(self.cant_inv)
        cadena += " | disponible: " + hab
        cadena += " | laboratorio: " + str(self.laboratorio)
        cadena += " | zona: " + str(self.zona)
        return cadena   #
