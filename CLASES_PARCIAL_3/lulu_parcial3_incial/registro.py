

# clases - registros - objetos
class Celular:

    # num id de fabricacion > 0, Marca, pulgadas(5, 13), precio


    # marca = (1: Samsung, 2: Xiaomi, 3: Hauwei)
    # id > 0, descripcion, marca(1, 3), pulgadas(5, 13), importe > 0

    # funcion constructora o inicializadora
    def __init__(self, id, descripcion, marca, pulgadas, importe):
        self.id = id
        self.descripcion = descripcion
        self.marca = marca
        self.pulgadas = pulgadas
        self.importe = importe

    # reemplazar el print de nuestro objeto
    def __str__(self):

        # marca(1, 3)       1-1         2-1     3-2
        # indices           0           1         2
        tupla_marcas = ("Samsung", "Xiaomi", "Hauwei")

        cadena = "ID: " + str(self.id)
        cadena += " | Descripcion: " + self.descripcion
        cadena += " | Marca: " + tupla_marcas[self.marca-1]
        cadena += " | Pulgadas: " + str(self.pulgadas)
        cadena += " | Importe: " + str(self.importe)
        return cadena