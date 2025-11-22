
# clase es el boceto para crear objetos
# los objetos se crean a partir de la clase
class Taxi:

    # funcion constructora o incializadora

    # id INT, nombre STR, marca (1, 3) INT, importe FLOAT
    def __init__(self, id, nombre, marca, importe):
        # ctrl + d
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.importe = importe

    def __str__(self):
        # las marcas    1- Peugot   2- Citroen    3-Ford

        # en vez de mostrar el valor numerico de la marca debe mostrar la descripcion que corresponda

        # marca(1, 3)      1-1       2 -1      3-1
        # indices           0           1       2
        tupla_marcas = ("Peugot", "Citroen", "Ford")

        cadena = "ID: " + str(self.id)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Marca: " + tupla_marcas[self.marca - 1]
        cadena += " | Importe: " + str(self.importe)
        return cadena       # obligatorio