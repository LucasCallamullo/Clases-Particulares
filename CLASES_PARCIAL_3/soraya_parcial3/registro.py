

# Clase / Registro / Objetos
class Paquete:
    # Funcion constructora o inicializadora
    # id INT > 0, descripcion STR , tipo INT (0, 19) , cantidad INT , importe FLOAT
    def __init__(self, id, descripcion, tipo, cantidad, importe):
        # ctrl + d
        self.id = id
        self.descripcion = descripcion
        self.tipo = tipo
        self.cantidad = cantidad
        self.importe = importe

    def __str__(self):
        # esta al lado del 1 y arriba del tab |
        cadena = "ID: " + str(self.id)
        cadena += " | Descripcion: " + str(self.descripcion)
        cadena += " | Tipo: " + str(self.tipo)
        cadena += " | Cantidad: " + str(self.cantidad)
        cadena += " | Importe: " + str(self.importe)
        return cadena
