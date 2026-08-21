class Proyecto:
    def __init__(self, numero, nombre, cliente, lenguaje,horas):
        self.numero = numero
        self.nombre = nombre
        self.cliente = cliente
        self.lenguaje = lenguaje
        self.horas = horas

    def __str__(self):
        lenguajes = ('Python','Java','TypeScript','JavaScript','Go')
        cad = 'Numero {} | Nombre {} | Cliente {} | Lenguaje {} | Horas {}'
        return cad.format(self.numero, self.nombre, self.cliente, lenguajes[self.lenguaje-1], self.horas)