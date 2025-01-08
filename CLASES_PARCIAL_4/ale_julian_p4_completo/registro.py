

class Consumo:

    # num_tel STR, hora(0, 23) INT, tipo(1, 3), importe FLOAT, titular STR
    def __init__(self, num_tel, hora, tipo, importe, titular):
        self.num_tel = num_tel
        self.hora = hora
        self.tipo = tipo
        self.importe = importe
        self.titular = titular

    def __str__(self):
        # tipo (1, 3)       1-1      2-1           3
        # indices           0           1           2
        tupla_consumos =  ("SMS", "Llamada", "Uso de datos")

        # la tecla que esta al lado del 1 --> |
        cadena = "Num Tel: " + str(self.num_tel)
        cadena += " | Hora: " + str(self.hora)
        cadena += " | tipo: " + tupla_consumos[self.tipo - 1]
        cadena += " | importe: " + str(self.importe)
        cadena += " | titular: " + str(self.titular)
        return cadena
