import random


class Zapato:
    def __init__(self, codigo, nombre, talle, ancho, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.talle = talle
        self.ancho = ancho
        self.stock = stock

    def __str__(self):
        return f'Codigo: {self.codigo} | Nombre: {self.nombre} | Talle: {self.talle} | Ancho: {self.ancho} | Stock: {self.stock}'


def generar_zapato():
    modelos = ("Samba", "Zpecial", "Superstar", "Campus", "Gazelle", "Rivalry")
    codigo = random.randint(1000, 9999)
    nombre = random.choice(modelos) + " " + str(random.randint(1990, 2010))
    talle = random.randint(35, 45)
    ancho = random.randint(0, 2)
    stock = random.randint(0, 1000)
    return Zapato(codigo, nombre, talle, ancho, stock)