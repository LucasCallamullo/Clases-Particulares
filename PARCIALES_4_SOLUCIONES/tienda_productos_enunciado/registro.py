

class Producto:
    # constructor
    # tipo (1, 4)   1:Motherboard, 2: Procesador, 3:Ram, 4:Gabinete
    # marca (555, 559)  555:Asus, 556: Gygabite, 557: AMD, 558:Logitech, 559:Redragon
    def __init__(self, id, nombre, marca, tipo, importe):
        self.id = id                    # ctrl + d
        self.nombre = nombre
        self.marca = marca
        self.tipo = tipo
        self.importe = importe          # ctrl + z

    #
    def __str__(self):
        # marcas      555-555,    556,      557   ,    558,         559-555
        # indices      0        1           2       3           4
        marcas_str = ("Asus", "Gygabite", "AMD", "Logitech", "Redragon")

        # self.tipo    1-1             2-1         3-1         4-1
        # indices       0               1           2           3
        tipos_str = ("Motherboard", "Procesador", "Cooler", "Gabinete")

        cadena = "Id: " + str(self.id)     #
        cadena += " | Nombre: " + self.nombre
        cadena += " | Marca: " + marcas_str[self.marca-555]
        cadena += " | Tipo: " + tipos_str[self.tipo-1]
        cadena += " | Importe: " + str(self.importe)
        return cadena
