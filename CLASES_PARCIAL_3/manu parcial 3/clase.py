

class Producto:
    # codigo INT ; descripcion STR ; calorias INT ; tipo (1, 30) INT ; precio FLOAT
    def __init__(self, codigo, descripcion, calorias, tipo, precio):
        # ctrl + d
        self.codigo = codigo
        self.descripcion = descripcion
        self.calorias = calorias
        self.tipo = tipo
        self.precio = precio

    def __str__(self):
        """
            cadena = "Codigo: " + str(self.codigo)
            cadena += " | Descripcion: " + str(self.descripcion)
            cadena += " | calorias: " + str(self.calorias)
            cadena += " | tipo: " + str(self.tipo)
            cadena += " | precio: " + str(self.precio)
        """
        # alt + 123 ; alt + 125   --> codigos asci
        cadena = (f"Codigo: {self.codigo}"
                  f" | Descripcion: {self.descripcion}"
                  f" | calorias: {self.calorias}"
                  f" | tipo: {self.tipo}"
                  f" | precio: {self.precio}")
        return cadena

