

# clase - registro u objeto
class Alquiler:

    # nombre_juego STR, nombre STR, tipo (10, 14) INT, mes (1, 12), monto FLOAT, stock INT
    def __init__(self, nombre_juego, nombre, tipo, mes, monto, stock):
        self.nombre_juego = nombre_juego
        self.nombre = nombre
        self.tipo = tipo
        self.mes = mes
        self.monto = monto
        self.stock = stock

    def __str__(self):
        # tipo(10, 14)    10-10        11-10       12-10          13          14
        # indices           0           1           2           3           4
        tupla_juegos = ("10: Acción", "11: Aventura", "12: Rol (RPG)", "13: Shooter", "14: Estrategia")

        # ctrl + d
        cadena = "Nombre juego: " + str(self.nombre_juego)
        cadena += " | Nombre: " + str(self.nombre)
        cadena += " | Tipo: " + tupla_juegos[self.tipo - 10]   # tipo 12
        cadena += " | Mes: " + str(self.mes)
        cadena += " | Monto: " + str(self.monto)
        cadena += " | Stock: " + str(self.stock)
        return cadena
