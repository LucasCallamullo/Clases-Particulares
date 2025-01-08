
class Interno:

    # funcion constructora

    # dni INT, nombre STR, tipo (0, 14), pago (0, 4), edad INT, importe FLOAT
    def __init__(self, dni, nombre, tipo, pago, edad, importe):
        self.dni = dni
        self.nombre = nombre
        self.tipo = tipo
        self.pago = pago
        self.edad = edad
        self.importe = importe

    def __str__(self):
        cadena = "DNI: " + str(self.dni)
        cadena += " | Nombre: " + str(self.nombre)
        cadena += " | tipo: " + str(self.tipo)
        cadena += " | pago: " + str(self.pago)
        cadena += " | edad: " + str(self.edad)
        cadena += " | importe: " + str(self.importe)
        return cadena           # NO TE OLVIDES DE RETORNAR LA CADENA

