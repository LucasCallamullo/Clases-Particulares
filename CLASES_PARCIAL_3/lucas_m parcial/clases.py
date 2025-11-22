

# una clase es un boceto o un diseño que agrupa propiedades / atributos y comportamientos a partir
# de los cuales vas a crear muchos objetos
class Teclado:

    # la funcion constructora   / metodo constructor
    def __init__(self, marca, precio, peso):
        # ctrl + d
        self.marca = marca
        self.precio = precio
        self.peso = peso

    def __str__(self):
        cadena = "Marca: " + str(self.marca)
        cadena += " | Precio: " + str(self.precio)
        cadena += " | Peso: " + str(self.peso)
        return cadena


def principal():

    teclado1 = Teclado("Redragon", 5.5, 10)
    teclado2 = Teclado("Logitech", 10.5, 10)

    teclado1.marca = "Genius"

    print(teclado1)
    print(teclado2)


if __name__ == '__main__':
    principal()