

class Taxi:
    # num_id INT ; dni INT ; marca(1, 20) INT ; tarifa FLOAT ; nombre STR
    def __init__(self, num_id, dni, marca, tarifa, nombre):
        # ctrl + d
        self.num_id = num_id
        self.dni = dni
        self.marca = marca
        self.tarifa = tarifa
        self.nombre = nombre

    def __str__(self):
        cadena = "Num ID:" + str(self.num_id)
        cadena += " | DNI: " + str(self.dni)
        cadena += " | Marca: " + str(self.marca)
        cadena += " | Tarifa: " + str(self.tarifa)
        cadena += " | Nombre: " + str(self.nombre)
        return cadena
