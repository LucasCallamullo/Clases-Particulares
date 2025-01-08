

class Juicio:

    # tupla_clientes = ( "CLIENTE 1" , "CLIENTE 2", "CLIENTE 3
    # codigo INT , descripcion STR, tipo (1, 15), cliente(1, 3), importe FLOAT

    # funcion constructora o incializadora
    def __init__(self, codigo, descripcion, tipo, cliente, importe):
        self.codigo = codigo
        self.descripcion = descripcion
        self.tipo = tipo
        self.cliente = cliente
        self.importe = importe

    def __str__(self):
        # clientes(1, 3)       1-1         2-1         3-1
        # indices               0           1           2
        tupla_clientes = ("CLIENTE 1", "CLIENTE 2", "CLIENTE 3")

        cadena = "Codigo: " + str(self.codigo)
        cadena += " | Descripcion: " + self.descripcion
        cadena += " | Tipo: " + str(self.tipo)
        cadena += " | Cliente: " + tupla_clientes[self.cliente-1]
        cadena += " | Importe: " + str(self.importe)
        return cadena
