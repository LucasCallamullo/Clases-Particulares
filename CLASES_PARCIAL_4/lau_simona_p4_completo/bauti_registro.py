'''Una librería necesita gestionar los datos de los libros que vende. De cada libro se conoce: El número ISBN (considere,
simplemente, un entero de 13 dígitos), el título (una cadena), el autor (una cadena), un código de idioma (1:
Español, 2: Inglés, 3: Portugués, 4: Francés, 5: Italiano), y el precio de venta. Se pide definir la clase Libro y
desarrollar un programa en Python controlado por un menú de opciones'''
class Libro:
    def __init__(self,num,tit,aut,idi,pre):
        self.numero = num
        self.titulo = tit
        self.autor = aut
        self.idioma = idi
        self.precio = pre
    def __str__(self):
        punto = ("espanol","ingles","portugues","frances","italiano")
        cadena = "numero ISBN: " + str(self.numero)
        cadena += " | titulo: " + self.titulo
        cadena += " | autor: " + self.autor
        cadena += " | codigo de idioma: " + punto[self.idioma - 1]
        cadena += " | precio del libro: " + str(self.precio)
        return cadena