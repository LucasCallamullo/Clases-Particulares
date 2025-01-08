

# Clase / objeto / registro
class Paseo:
    """
        La funcion constructora o inicializadora
    """
    #                 1          2       3
    # destinos = ("Montañas", "Lago", "Sierra")
    # id > 0 INT, nombre STR, tipo (0, 19) INT, importe > 0 FLOAT, destino int(1, 3)

    def __init__(self, id, nombre, tipo, importe, destino):
        # ctrl + d
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.importe = importe
        self.destino = destino

    def __str__(self):          # paseito2
        # esta al lado del 1 y arriba del tab: |

        # destino int(1, 3)

        # self.destino         1-1           2      3
        # indices              0        1         2
        tupla_destinos = ("Montañas", "Lago", "Sierra")

        cadena = "ID: " + str(self.id)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Tipo: " + str(self.tipo)
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Destino: " + tupla_destinos[self.destino-1]
        return cadena
