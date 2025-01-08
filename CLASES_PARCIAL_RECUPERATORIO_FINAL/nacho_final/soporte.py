

import random


class Beca:
    def __init__(self, d, nom, tip, car, mon):
        self.dni = d
        self.nombre = nom
        self.tipo = tip
        self.carrera = car
        self.monto = mon

    def __str__(self):
        cad = 'Dni: {:<10} | Nombre: {:<30} |  Tipo beca: {:<12} |  Carrera: {:<12} |  Monto: {:<10}'
        return cad.format(self.dni, self.nombre, self.tipo, self.carrera, self.monto)


def validar():
    n = int(input('Ingrese la cantidad de becas a cargar (mayor a cero): '))
    while n <= 0:
        n = int(input('Error... Se pidió mayor a cero... Ingrese nuevamente la cantidad (mayor a cero): '))
    return n


def add_in_order(vec, t):
    # vec []     t1.nombre = B       # 1
    # vec [t1]      t2.nombre = A
    # vec [t2, t1, t3]   t3.nombre = C
    n = len(vec)        # 2
    izq = 0
    der = n - 1     # 1
    while izq <= der:
        c = (izq + der) // 2            # 1
        if t.nombre == vec[c].nombre:
            pos = c
            break
        elif t.nombre < vec[c].nombre:
            der = c - 1         # 1
        else:
            izq = c + 1         # 2

    if izq > der:
        pos = izq

    # vec[t2, t1]
    vec[pos:pos] = [t]


def cargar_arreglo():
    nombres = ("Juan", "Ana", "Luis", "Carla", "Pedro", "Diana", "Matias", "Sandra", "Jose", "Maria", "Lucas")
    apellidos = ("Perez", "Gomez", "Suarez", "Dimarco", "Franceschi", "Tomasini", "Quispe", "Mamani", "Smith", "Evans")
    vec = []
    n = validar()       # 5
    for i in range(n):
        dni = random.randint(1, 99999999)           # int
        nom = random.choice(nombres) + " " + random.choice(apellidos) + " " + random.choice(apellidos)  # str
        tip = random.randint(1, 10)
        car = random.randint(1, 5)
        mon = round(random.uniform(0, 9000000), 2)  # float

        t = Beca(dni, nom, tip, car, mon)
        add_in_order(vec, t)
    return vec


def mostrar_arreglo(vec):
    print('Listado completo de beca')
    for beca in vec:
        print(beca)
