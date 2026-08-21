import random


class Seguro:
    def __init__(self, codigo, nombre, tipo, es_propietario, monto):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.es_propietario = es_propietario
        self.monto = monto

    def __str__(self):
        prop = "No Propietario"
        if self.es_propietario:
            prop = "Propietario"
        cadena = (f"|{self.codigo:>20}|{self.nombre:>30}|"
                  f"{self.tipo:<4}|{prop:<15}|${self.monto:>10.2f}|")
        return cadena


def crear_seguro():
    nombres = ('Juan', 'Pedro', 'Carlos', 'Carla', 'Laura', 'Karina', 'Marcela')
    apellidos = ('Sauron', 'Elfo', 'Gandalf', 'Darth', 'Vader', 'Lobo')
    codigo = random.randint(100000, 999999)
    nombre = f'{random.choice(nombres)} {random.choice(apellidos)}'
    tipo = random.randint(1, 5)
    es_propietario = random.choice([True, False])
    monto = random.uniform(100000, 999999)
    return Seguro(codigo, nombre, tipo, es_propietario, monto)
