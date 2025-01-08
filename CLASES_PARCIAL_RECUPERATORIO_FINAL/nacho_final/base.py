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
    n = len(vec)
    izq = 0
    der = n - 1
    while izq <= der:
        c = (izq + der) // 2
        if t.nombre == vec[c].nombre:
            pos = c
            break
        elif t.nombre < vec[c].nombre:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

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


def menu():
    print('----------------------- Menú de opciones - Becas de Estudio -------------------------')
    print('1. Cargar arreglo (ordenado por nombre)')
    print('2. Mostrar arreglo completo')
    print('3. Buscar por dni (Busqueda Secuencial')
    print('4. Conteo por tipo de beca y carrera ( MAtriz)')
    print('5. Generar archivo con condición de filtro( Archivo Binario )')
    print('6. Mostrar archivo (incluir promedio al final)')
    print('7. Busqueda Binaria')
    print('0. Salir')
    print('--------------------------------------------------------------------------------------------')
    return int(input('Ingrese número de opción: '))


def principal():
    vec = []    # list()            # vector, lista, arreglo

    # Punto archivos
    fd = "becas.dat"        # file description ; nombre del archivo

    opcion = -1
    while opcion != 0:

        opcion = menu()

        if opcion == 1:
            vec = cargar_arreglo()      # 5
            print("Carga finalizada - Arreglo generado")
            print()

        elif opcion == 2:
            if not vec:     # pregunta si vec = []
                print('El arreglo no ha sido cargado todavía..')
            else:
                mostrar_arreglo(vec)
                print()

        elif opcion == 3:
            if not vec:     # pregunta si vec = []
                print('El arreglo no ha sido cargado todavía..')
            else:
                pass

        elif opcion == 4:
            if not vec:     # pregunta si vec = []
                print('El arreglo no ha sido cargado todavía..')
            else:
                pass

        elif opcion == 5:
            if not vec:     # pregunta si vec = []
                print('El arreglo no ha sido cargado todavía..')
            else:
                pass
