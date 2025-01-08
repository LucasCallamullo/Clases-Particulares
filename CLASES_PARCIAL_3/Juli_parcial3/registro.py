

# clase, registro, objeto
class Tele:
    # ID: valor positivo, Marca = ("Hitachi", "LG", "Samsung"), Precio: flotante, pulgadas: (32-50)
    # Funcion constructor, inicializador
    def __init__(self, id, marca, precio, pulgadas):
        # ctrl + d
        self.id = id
        self.marca = marca
        self.precio = precio
        self.pulgadas = pulgadas

    def __str__(self):
        cadena = "ID: " + str(self.id)   # str + str , el más concatena
        cadena += " | Marca: " + self.marca
        cadena += " | Precio: " + str(self.precio)
        cadena += " | Pulgadas: " + str(self.pulgadas)
        return cadena
