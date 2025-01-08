import os.path
import pickle

from envio import *
#------------------------------------------------------------------------------------------------------------------------
# Opcion 1
def opcion1(fdt, fdb):

    bandera = os.path.exists(fdb)   # retorna TRUE si existe el archivo, y si no FALSE si NO existe
    if bandera is True:     # if bandera:
        print("1 - Sobre escribir el archivo")
        print("2 - cancelar.")
        op = int(input("Ingresar opcion: "))

        if op == 2:
            print("Se cancelo la operación.")
            return      # corta una funcion

    m_csv = open(fdt, "r")  # r = read ) modo de lectura
    m = open(fdb, "wb")  # primer parametro es el nombre del archivo ( fdb )
                # segundo parametro modo de apertura ( "wb" )
    # wb = write binary = crea el archivo si no existe, sobre escribe todo el contenido
    # ab = append binary = crea el archivo si no existe, agrega contenido al final conservando todo lo anterior

    cont = 0
    for linea in m_csv:
        cont += 1
        if cont >= 3:
            datos = linea.strip().split(",")
            codigo = datos[0]
            direccion = datos[1]
            tipo = int(datos[2])
            pago = int(datos[3])

            env = Envio(codigo, direccion, tipo, pago)
            pickle.dump(env, m)  # primer parametro es que quiero guardar ( env )
            # segundo parametro es el archivo ( m )

    print("Se cargaron la cantidad de envios:", cont-2)

    m.close()  # OBLIGATORIO
    m_csv.close() # OBLIGATORIO

#------------------------------------------------------------------------------------------------------------------
# opcion 2

def validar_rango(inf, sup, msj):
    # funcion reutilizada del tp3
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def opcion2(fdb):
    m = open(fdb, "ab")  # append binary, para agregar elementos al final del archivo conservando su contenido anterior

    # codigo STR, direccion STR, tipo INT, pago INT
    codigo = input("Codigo postal: ")
    direccion = input("Direccion postal: ")
    tipo = validar_rango(0, 6, "Tipo de envio (entre 0 y 6): ")
    pago = validar_rango(1, 2, "Forma de pago (entre 1 y 2): ")
    env = Envio(codigo, direccion, tipo, pago)
    pickle.dump(env, m)

    print("Carga terminada..")
    print()
    m.close()

#--------------------------------------------------------------------------------------------------------------------
# opcion 3

def opcion3(fdb):
    if os.path.exists(fdb) is False:  # if not bandera:
        print("El archivo no existe:", fdb)
        return

    m = open(fdb, "rb")     # rb = read binary = modo de lectura
    tam = os.path.getsize(fdb)  # nos dice el tamaño en bytes del archivo = 1500 bytes

    # archivo = [   E1       E2       E3 ]
    # bytes     0       100     200     300
    # m.tell()  0       100

    while m.tell() < tam:

        env = pickle.load(m)    # unico parametro el archivo
        # env = E1,      E2,         E3
        print(env)

    m.close()

#-----------------------------------------------------------------------------------------------------------------
# opcion 4

def opcion4(fdb, cp):

    if not os.path.exists(fdb):
        print("No existe el archivo", fdb)
        return

    m = open(fdb, "rb")
    tam = os.path.getsize(fdb)

    cont = 0

    while m.tell() < tam:
        env = pickle.load(m)

        if env.codigo == cp:
            print(env)
            cont += 1

    print("Se mostraron", cont, "registros")
    m.close()

#--------------------------------------------------------------------------------------------------------------
# opcion 5

def punto5(fdb):
    if not os.path.exists(fdb):
        print("El archivo", fdb, "no existe...")
        print()

    d = input("Ingrese la direccion a buscar: ")
    m = open(fdb, "rb")
    tbm = os.path.getsize(fdb)
    while m.tell() > tbm:
        dp = pickle.load(m)
        t = str(dp.direccion)
        if d == t:
            print("Se encontro la direccion deseada:")
            print(dp)
            print()
            return

    print("No existe la direccion del archivo...")
    print()

#----------------------------------------------------------------------------------------------------------------------
# opcion 6

def generar_matriz(fd):
    if not os.path.exists(fd):
        print(" El archivo ", fd, "no existe")
        return

    mat = [[0] * 2 for i in range(7)]
    t = os.path.getsize(fd)
    m = open(fd, "rb")
    while m.tell() < t:
        env = pickle.load(m)
        f = env.tipo
        c = env.pago -1
        mat[f][c] += 1
    m.close()
    return mat

#----------------------------------------------------------------------------------------------------------------------
# opcion 7

def mostrar_matriz(mat):
    n = len(mat)
    m = len(mat[0])

    print()
    for f in range(n):
        for c in range(m):
            print("Tipo de envio: {:>7} | Forma de pago: {:>7} | Cantidad total de envios: {:>7} | ".format( f, c+1, ma[f][c]))


#----------------------------------------------------------------------------------------------------------------------

def totalizar_por_cada_tipo_de_envio(mat):
    n = len(mat)
    m = len(mat[0])

    print()
    for f in range(n):
        total = 0
        for c in range(m):
            total += mat[f][c]
        print("Tipo de envio: {:>7} | Cantidad total de envios: {:>7} | ".format( f, total))

def totalizar_por_cada_forma_de_pago(mat):
    n = len(mat)
    m = len(mat[0])

    print()
    for c in range(m):
        total = 0
        for f in range(n):
            total += mat[f][c]
        print("Forma de pago: {:>7} | Cantidad total de envios: {:>7} | ".format( c + 1, total))


#----------------------------------------------------------------------------------------------------------------------
# opcion 8
def opcion8_calc_prom(fdb):
    if os.path.exists(fdb) is False:
        print("El archivo no existe:", fdb)
        return

    m = open(fdb, "rb")
    tam = os.path.getsize(fdb)

    # promedio de importes
    # prom = acumulado ( de importes ) / la cantidad de veces que acumule
    acum = 0
    cont = 0

    while m.tell() < tam:

        env = pickle.load(m)
        # env = E1,      E2,         E3
        importe = env.calcular_importe()
        acum += importe
        cont += 1

    # calcular el promedio
    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio es:", prom)
    m.close()
    return prom


def opcion8(fdb, promedio):
    if os.path.exists(fdb) is False:
        print("El archivo no existe:", fdb)
        return

    m = open(fdb, "rb")
    tam = os.path.getsize(fdb)

    # creemos un arreglo que solo contenga los objetos con importes mayores al promedio
    v = []

    while m.tell() < tam:

        env = pickle.load(m)
        # env = E1,      E2,         E3
        importe = env.calcular_importe()
        if importe > promedio:
            add_in_order(v, env)

    m.close()

    # mostrar arreglo
    for i in v:
        print(i)


def add_in_order(v, env):

    izq, der = 0, len(v) - 1

    while izq <= der:
        c = (izq + der) // 2

        # lo que cambia es el atributo que te pidan ordenar
        if v[c].codigo == env.codigo:
            pos = c
            break

        # la boquita ">" determina si esta de menor a mayor o mayor a menor
        elif v[c].codigo > env.codigo:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [env]      # el objeto va ENTRE CORCHETES


def menu():
    print()
    print("1 - Generar Archivo.")
    print("2 - Agregar Archivo.")
    print("3 - Mostrar Archivo.")
    print("4 - Buscar por Código Postal.")
    print("5 - Buscar por Dirección Postal.")
    print("6 - Generar Matriz.")
    print("7 - Mostrar Matriz.")
    print("8 - Generar Arreglo.")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))
    return op


def principal():

    # nombre del archivo csv
    fdt = "envios-tp4.csv"

    # nombre del archivo binario
    # fdb = "envios-tp4.dat"   # file description
    fdb = "envioss.dat"   # file description

    op = -1
    while op != 0:

        op = menu()

        if op == 1:

            opcion1(fdt, fdb)

        elif op == 2:
            opcion2(fdb)

        elif op == 3:
            opcion3(fdb)

        elif op == 4:
            cp = int(input(" Ingrese el codigo postal a buscar: "))
            opcion4(fdb, cp)

        elif op == 5:
            punto5(fdb)

        elif op == 6:
            mat = generar_matriz(fdb)
            print(" Conteo finalizado - Matriz generada")
            mostrar_matriz(mat)
            print()


        elif op == 7:
            print()
            print(" Cantidad total de envios contados por cad tipo de envio posible:")
            totalizar_por_cada_tipo_de_envio(mat)
            print()
            print(" Cantidad total de envios contados por cada forma de pago posible: ")
            totalizar_por_cada_forma_de_pago(mat)
            print()


        elif op == 8:
            promedio = opcion8_calc_prom(fdb)
            opcion8(fdb, promedio)


if __name__ == '__main__':
    principal()
