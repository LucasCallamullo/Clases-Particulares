import os.path
import pickle
import random
from soporte import *
import soporte


# opcion 1
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


# opcion 2
def mostrar_arreglo(vec):
    print('Listado completo de beca')
    for beca in vec:
        print(beca)


# =============================================================================
#   Opcion 3    -   BUSQUEDA BINARIA
# =============================================================================
# BUSQUEDA BINARIA
# CONDICION NECESARIA QUE EL ARREGLO ESTE ORDENADO POR EL MISMO ATRIBUTO QUE TE PIDEN BUSCAR

def busqueda_binaria(vec, nom):     # nom = matias
    # buscar una beca cuyo nombre sea "nom", si se encuentra aplicarle un 10% de descuento a su monto
    # mostrar sus datos antes y despues del cambio,
    # detenerse al primer resultado, informar si no se encontro
    n = len(vec)    # 5
    izq = 0         # 3
    der = n - 1     # 4
    while izq <= der:       # mientras izq sea menor o igual a derecha ingreso al ciclo while
        c = (izq + der) // 2        # 3
        # if t.nombre == vec[c].nombre:
        if nom == vec[c].nombre:
            # pos = c
            # break

            # aca es donde encontramos un resultado

            # previo al descuento
            print(vec[c])

            # aplicarle un 10% de descuento a su monto
            vec[c].monto -= vec[c].monto * 0.1

            # aplicarle un 25% de aumento a su monto
            # vec[c].monto += vec[c].monto * 0.25

            # modifcarle su importe/monto por un valor "mon" que se carga por teclado
            # mon = int(input("Ingresar valor del nuevo monto: "))
            # vec[c].monto = mon

            # despues del descuento
            print(vec[c])

            return      # no te olvides el return

        # elif t.nombre < vec[c].nombre:
        elif nom < vec[c].nombre:
            der = c - 1
        else:
            izq = c + 1

    # si salgo del while es porque no encontre resultados
    print("No existe una beca con el nombre tal:", nom)


# =============================================================================
#   Opcion 4    -   BUSQUEDA SECUENCIAL
# =============================================================================
def busqueda_secuencial(vec, d):        # d = 4
    # buscar una beca cuyo dni sea "d", si existe mostrar sus datos y detenerse al primer resultado
    # , y si no existe informar

    n = len(vec)    #   5
    for i in range(n):
        # i = 0, 1,         2, 3, 4
        if vec[i].dni == d:
            # existe un objeto que cumple

            # mostrar sus datos
            print(vec[i])

            # mostrar su nombre y su carrera
            print("Nombre:", vec[i].nombre, " - Carrera:", vec[i].carrera)

            return      # esto es para que se detenga al primer resultado

    # el caso de que no exista
    print("No se encontra una beca que cumpla con ese dni:", d)


# =============================================================================
#   Opcion 5    -   Generar archivo binario
# =============================================================================
# generar un archivo binario que contenga solo las becas que superan un importe/monto "x"
def generar_archivo_binario(vec, x, fd):

    m = open(fd, "wb")  # primer parametro: nombre del archivo
                        # segundo parametro: el modo de apertura --> "wb"
    # "wb" = write binary, sobreescribe el archivo cada vez que se ingresa a esta funcion
    # "ab" = append binary, agrega contenido al final conservando todo lo anterior

    # al final mostrar cuantos registros/objetos/becas se guardaron
    cont = 0

    n = len(vec)    # 5
    for i in range(n):
        # i = 0, 1, 2, 3, 4

        # solo las becas que superan un importe/monto "x" pero que sea de la carrera 1, 2 o 3
        if vec[i].monto > x and 1 <= vec[i].carrera <= 3:
            pickle.dump(m, vec[i])      # primer parametro es el archivo: --> m
                                        # segundo parametro es lo que quiero guardar --> objeto --> vec[i]
            cont += 1

    print("Se genero un archivo con", cont, "cantidad de becas.")
    m.close()   # ESTO ES OBLIGATORIO


# =============================================================================
#   Opcion 6    -   Mostrar archivo binario
# =============================================================================
def mostrar_archivo_binario(fd):
    # mostrar el archivo binario generado en el punto anterior, mostrarlo a razon de uno
    # por linea, mostrar al final el monto promedio de los registros(objetos - becas)
    # que se mostraron

    # os.path se utiliza con --> fd
    # pickle. se usa a la --> "m"
    bandera = os.path.exists(fd)    # return True or False
    if bandera is False:
        # si la bandera esta en falso significa que el archivo no existe, o sea que no podes trabajar
        print("no existe el archivo:", fd)
        return      # obligatorio para cortar una funcion

    # mostrar al final el monto promedio de los registros(objetos - becas) que se mostraron
    # prom = sumatoria de los montos / cantidad de veces que sume
    acum = 0
    cont = 0

    #
    m = open(fd, "rb")      # rb = read binary
    tam = os.path.getsize(fd)   # devolver el tamaño en bytes del archivo

    while m.tell() < tam:

        # que cada vuelta de ciclo voy a recuperar un objeto y se va a guardar en "beca"
        beca = pickle.load(m)   # recibie unico parametro al archivo

        # solo mostrar los que sean de la carrera 1
        if beca.carrera == 1:
            print(beca)
            acum += beca.monto
            cont += 1

    # calcular promedio
    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de los montos de las becas mostrdas es: ", prom)

    m.close()   # OBLIGATORIO NO TE LO OLVIDES





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
    # lista , vector, arreglo , array
    vec = []    # list()

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
                # BUSQUEDA BINARIA
                # buscar una beca cuyo nombre sea "nom", si se encuentra aplicarle un 10% de descuento,
                # detenerse al primer resultado informar si no se encontro
                nom = input("Ingresar nombre a buscar: ")   # el input solito pide un str
                busqueda_binaria(vec, nom)          # ctrl + c -> copiar

        elif opcion == 4:
            if not vec:     # pregunta si vec = []
                print('El arreglo no ha sido cargado todavía..')
            else:
                # BUSQUEDA SECUENCIAL
                # buscar una beca cuyo dni sea "d", si se encuentra aplicarle un 10% de descuento,
                # detenerse al primer resultado informar si no se encontro
                d = int(input("Ingresar a dni a buscar: "))
                busqueda_secuencial(vec, d)

        elif opcion == 5:
            if not vec:     # pregunta si vec = []
                print('El arreglo no ha sido cargado todavía..')
            else:
                # generar un archivo binario que contenga solo las becas que superan un importe/monto
                # "x"
                x = int(input("Ingresar monto a superar: "))
                generar_archivo_binario(vec, x, fd)

        elif opcion == 6:
            if not vec:     # pregunta si vec = []
                print('El arreglo no ha sido cargado todavía..')
            else:
                # mostrar el archivo binario generado en el punto anterior, mostrarlo a razon de uno
                # por linea, mostrar al final el monto promedio de los registros(objetos - becas)
                # que se mostraron
                mostrar_archivo_binario(fd)

