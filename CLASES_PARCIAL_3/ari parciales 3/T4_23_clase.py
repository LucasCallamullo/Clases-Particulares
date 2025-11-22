class Juicio:
    def __init__(self, codigo, desc, tipo, nombre, monto):
        self.codigo = codigo
        self.desc = desc
        self.tipo = tipo
        self.nombre = nombre
        self.monto = monto

    def __str__(self):
        cadena = "| Codigo: " + str(self.codigo)
        cadena += "| Descripcion: " + self.desc
        cadena += "| Tipo: " + str(self.tipo)
        cadena += "| nombre: " + self.nombre
        cadena += "| Monto: " + str(self.monto)
        return cadena
