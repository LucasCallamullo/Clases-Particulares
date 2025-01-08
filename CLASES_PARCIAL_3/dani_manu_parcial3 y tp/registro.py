

# clase / registro / objeto
class Mascota:
    # tipos = ("Perro", "Gato", "Conejo")
    # id > 0 , nombre, tipo(1, 3), importe > 0, edad(1, 10)

    # funcion constructora o inicializadora
    def __init__(self, id, nombre, tipo, importe, edad):
        # ctrl + d
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.importe = importe
        self.edad = edad

    # funcion que reemplaza al print
    def __str__(self):
        # tipo(1, 3)
        # self.tipo     1        2        3
        # indices        0         1        2
        tupla_tipos = ("Perro", "Gato", "Conejo")

        cadena = "ID: " + str(self.id)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Tipo: " + tupla_tipos[self.tipo-1]
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Edad: " + str(self.edad)
        return cadena


