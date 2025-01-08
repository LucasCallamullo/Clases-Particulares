

# clases , registros,               objetos
class Tablet:
    # marcas = 1=Apple. 2=Google. 3=OnePlus. 4=Samsung.
    # id > 0, pulgadas(8, 20), marca(1, 4), importe > 0, peso
    def __init__(self, id, pulgadas, marca, importe, peso):
        # ctrl + d  ; ctrl + c ; ctrl + v
        self.id = id
        self.pulgadas = pulgadas
        self.marca = marca
        self.importe = importe
        self.peso = peso

    # Nuestra funcion para ver los datos del objeto / clase / registro
    def __str__(self):

        cadena = "ID: " + str(self.id)                # ID: Cadena
        cadena += " | Pulgadas: " + str(self.pulgadas)
        cadena += " | Marca: " + str(self.marca)
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Peso: " + str(self.peso)
        return cadena
