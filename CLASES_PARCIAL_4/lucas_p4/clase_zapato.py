

class Zapato:
    # codigo INT > 0, nombre STR, talle INT (35, 45), ancho (0, 2), disponible bool, precio FLOAT
    def __init__(self, codigo, nombre, talle, ancho, disponible, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.talle = talle
        self.ancho = ancho
        self.disponible = disponible
        self.precio = precio

    def __str__(self):
        # ancho(0,2 )       0         1               2
        # indices           0           1           2
        tupla_anchos = ("Delgado", "Normal", "Extra ancho")

        cadena = "Codigo: " + str(self.codigo)
        cadena += "| Nombre: " + self.nombre
        cadena += "| Talle: " + str(self.talle)
        cadena += "| Ancho: " + tupla_anchos[self.ancho]
        cadena += "| Disponible: " + str(self.disponible)
        cadena += "| Precio: " + str(self.precio)
        return cadena



