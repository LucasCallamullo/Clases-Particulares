import envio
import os.path
import pickle


def existe_archivo(fdb):
    if not os.path.exists(fdb):
        print("El archivo", fdb, "no existe...")
        return False
    return True


def validar_rango(inf, sup, msj):
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def generar_archivo_binario(fdt, fdb):
    if not os.path.exists(fdt):
        print("El archivo", fdt, "no existe...")
        print("Controle y vuelva por aquí...")
        return

    if os.path.exists(fdb):
        opcion = input("El archivo " + fdb + " ya existe. Está seguro de que desea eliminarlo y crear uno nuevo? (s/n): ")
        if opcion.lower() != 's':
            print("Operación cancelada. No se ha creado el archivo binario.")
            return
        else:
            os.remove(fdb)

    datos = open(fdt, "rt")
    ts = datos.readline()
    hd = datos.readline()

    m = open(fdb, "wb")
    for linea in datos:
        d = linea.split(",")
        cp = d[0]
        de = d[1]
        te = int(d[2])
        fp = int(d[3])
        env = envio.Envio(cp, de, te, fp)
        pickle.dump(env, m)

    datos.close()
    m.close()


def opcion2(fdb):
    cod = input("Ingrese el código postal: ")
    dp = input("Ingrese la dirección: ")
    tip = validar_rango(0, 6, "Ingrese el tipo de envío (0-6): ")
    fp = validar_rango(1, 2, "Ingrese el tipo de pago (1: Efectivo, 2: Tarjeta): ")

    nuevo_env = envio.Envio(cod, dp, tip, fp)

    m = open(fdb, 'ab')
    pickle.dump(nuevo_env, m)
    print("Envío agregado con éxito.")
    m.close()


def opcion3(fdb):
    if not existe_archivo(fdb):
        return

    print("Listado general de envios...")
    c = 0
    m = open(fdb, "rb")
    t = os.path.getsize(fdb)
    while m.tell() < t:
        env = pickle.load(m)
        print(env)
        c += 1
    m.close()
    print("Se listaron", c, "registros...")


def opcion4(fdb):
    if not existe_archivo(fdb):
        return

    cp = input("Ingrese el código postal a buscar: ")
    print("Listado de envíos con código postal", cp, "\b:")

    c = 0
    m = open(fdb, "rb")
    t = os.path.getsize(fdb)

    while m.tell() < t:
        env = pickle.load(m)
        if cp == env.codigo:
            print(env)
            c += 1

    m.close()
    print("Se mostraron", c, "registros.")


def opcion5(fdb):
    if existe_archivo(fdb):
        m = open(fdb, "rb")
        t = os.path.getsize(fdb)
        d = input("Ingrese la dirección a buscar: ")
        while m.tell() < t:
            r = pickle.load(m)
            if r.direccion == d:
                print("Dirección encontrada...")
                print("\t", r)
                return
        print("La dirección", d, "no ha sido encontrada...")
        m.close()


def opcion6(fdb):
    bandera = os.path.exists(fdb)
    if bandera is False:
        print("El archivo", fdb, "no existe...")
        print("Controle y vuelva por aquí...")
        return

    # crear la matriz
    f = 2
    c = 7
    matriz = [ [0] * c for i in range(f) ]

    m = open(fdb, "rb")
    tam = os.path.getsize(fdb)

    while m.tell() < tam:

        env = pickle.load(m)
        matriz[env.pago - 1][env.tipo] += 1

    m.close()

    # mostrar la matriz
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            #  Muestre solo los contadores cuyo valor final sea diferente de cero
            if matriz[f][c] > 0:
                print("Tipo de Envio:", c, "| Forma de Pago:", f+1, "| Cantidad:", matriz[f][c])
    return matriz


def opcion7(matriz):
    # totalizar las filas
    for f in range(len(matriz)):
        acum = 0

        for c in range(len(matriz[0])):
            acum += matriz[f][c]
        print("Para la forma de pago:", f+1, "tiene total de:", acum)

    # totalizar las columnas
    for c in range(len(matriz[0])):
        acum = 0

        for f in range(len(matriz)):
            acum += matriz[f][c]
        print("Para el tipo de envio:", c, "tiene total de:", acum)


def calcular_importe(envio):
    montos = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    precio = montos[envio.tipo]
    pais = envio.country()

    if pais in ["Bolivia", "Paraguay"]:
        porc = 1.2
    elif pais == "Uruguay":
        if envio.codigo[0] == "1":
            porc = 1.2
        else:
            porc = 1.25
    elif pais == "Chile":
        porc = 1.25
    elif pais == "Brasil":
        if envio.codigo[0] in "89":
            porc = 1.2
        elif envio.codigo[0] in "0123":
            porc = 1.25
        elif envio.codigo[0] in "4567":
            porc = 1.3
        else:
            porc = 1.5
    elif pais == "Argentina":
        porc = 1
    else:
        porc = 1.5

    importe_final = precio * porc
    if envio.pago == 1:
        importe_final *= 0.90

    return importe_final


def promedio_envios(fdb):
    total_importe = 0
    total_envios = 0

    m = open(fdb, "rb")
    t = os.path.getsize(fdb)

    while m.tell() < t:
        env = pickle.load(m)
        total_importe += calcular_importe(env)
        total_envios += 1

    m.close()

    if total_envios == 0:
        return 0

    return total_importe / total_envios


def mayores_al_promedio(fdb, prom):
    envios_mayores = []

    m = open(fdb, "rb")
    t = os.path.getsize(fdb)

    while m.tell() < t:
        env = pickle.load(m)
        imp = calcular_importe(env)
        if imp > prom:
            envios_mayores.append(env)

    m.close()
    return envios_mayores


def ordenar_cp(env):
    n = len(env)
    h = 1

    while h <= n // 9:
        h = 3*h + 1

    while h > 0:
        for j in range(h, n):
            y = env[j]
            k = j - h
            while k >= 0 and y.codigo < env[k].codigo:
                env[k+h] = env[k]
                k -= h
            env[k+h] = y
        h //= 3


def opcion8(fdb):
    prom = promedio_envios(fdb)
    print("El importe promedio es:", prom)

    envios_mayores = mayores_al_promedio(fdb, prom)

    if not envios_mayores:
        print("No hay envíos mayores al promedio.")
        return

    ordenar_cp(envios_mayores)

    print("Envios mayores al promedio (ordenados por código postal):")
    print("total envios:", len(envios_mayores)) # pq queria ver cuantos eran A
    for env in envios_mayores:
        print(env)


def principal():
    fdt = "envios-tp4.csv"
    fdb = "envios-tp4.dat"
    op = 0

    while op != 9:
        print("Menú de opciones:")
        print("1. Crear archivo binario")
        print("2. Agregar un envío")
        print("3. Mostrar todos los envíos")
        print("4. Mostrar envíos por código postal")
        print("5. Buscar envío por dirección")
        print("6. Cantidad de envíos por tipo y forma de pago")
        print("7. Totales por tipo de envío y forma de pago")
        print("8. Promedio y envíos mayores al promedio")
        print("9. Salir")
        op = int(input("Seleccione una opción: "))

        if op == 1:
            generar_archivo_binario(fdt, fdb)
            print("Terminado...")

        elif op == 2:
            opcion2(fdb)

        elif op == 3:
            opcion3(fdb)

        elif op == 4:
            opcion4(fdb)

        elif op == 5:
            opcion5(fdb)

        elif op == 6:
            matriz = opcion6(fdb)

        elif op == 7:
            if matriz is None:
                print("Error! Pasar por la opcion 6 primero.")
            else:
                opcion7(matriz)

        elif op == 8:
            opcion8(fdb)

        elif op == 9:
            print("Programa terminado.")


if __name__ == "__main__":
    principal()
