import os.path
from Tp3 import *


# Opción 1
def cargar_desde_archivo(v, tc, fd):
    if not os.path.exists(fd):
        print('El archivo no existe')
        return
    primera = True
    archivo = open(fd, "rt")
    for line in archivo:
        if primera is True:
            if "SC" in line:
                tc = "SC"
            primera = False
        else:
            cp = line[0:9].strip().upper()
            direccion = line[9:29].strip()
            tipo = int(line[29])
            pago = int(line[30])

            envios = Envio(cp, direccion, tipo, pago)
            v.append(envios)
    archivo.close()
    return tc


# Opcion 2
def cargar_ticket(v):
    m = validar_mayor(0, "Cuantos registros quiere agregar al arreglo?: ")
    for i in range(m):
        cod = input("Codigo postal: ")
        dp = input("Direccion postal: ")
        tip = validar_rango(0, 6, "Tipo de envio (entre 0 y 6): ")
        fp = validar_rango(1, 2, "Forma de pago (entre 1 y 2): ")
        envios = Envio(cod, dp, tip, fp)
        v.append(envios)


# Opcion 3
def ordenar(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]


def mostrar(v):
    n = len(v)
    ordenar(v)
    print("Hay", n, "registros en el arreglo")
    m = validar_rango(1, n, "Cantidad a mostrar (al menos 1 y no mas de " + str(n) + ")?: ")
    print("Listado de envios ordenados por codigo postal:")
    for i in range(m):
        print(v[i])


# Opción 4
def buscar_direccion_y_tipo(v):
    d = input("Ingrese la dirección de envío a buscar: ")
    e = int(input("Ingrese el tipo de envío a buscar (0 a 6): "))
    for envio in v:
        if envio.direccion == d and envio.tipo == e:
            print("Envío Encontrado")
            print(envio)
            return
    print("No se encontró un envió con esos datos")


# Opción 5
def buscar_codigo(v):
    cp = input("Ingrese el código postal del envío que desea modificar: ")
    for envio in v:
        if envio.codigo == cp:
            if envio.pago == 1:
                envio.pago = 2
            else:
                envio.pago = 1
            print("Envío Modificado")
            print(envio)
            return
    print("No se encontró un envió con ese código postal")


# Opción 6
def contar(v, tc):
    v_cont = [0] * 7
    for i in v:
        if tc == "HC":
            if i.check_dir():
                v_cont[i.tipo] += 1

        else:
            v_cont[i.tipo] += 1

    for i in range(len(v_cont)):
        print("Tipo de envio: ", i, "| Cantidad de envios:", v_cont[i])


# Opción 7
def acumular(v, tc):
    v_acum = [0] * 7
    for i in v:
        if tc == "HC":
            if i.check_dir():
                importe = i.calcular_importe()
                v_acum[i.tipo] += importe

        else:
            importe = i.calcular_importe()
            v_acum[i.tipo] += importe

    for i in range(len(v_acum)):
        print("Tipo de envio: ", i, "| acumulado de importes:", v_acum[i])

    return v_acum


# Opcion 8
def mayor(v_acum):
    acum = 0
    may = None
    tipo = None
    for i in range(len(v_acum)):
        acum += v_acum[i]

        if may is None or v_acum[i] > may:
            may = v_acum[i]
            tipo = i

    print("El mayor Importe del tipo de Envio:", tipo, "con un acumulado de:", may)

    porc = 100 * may / acum
    print("El Porcentaje sobre el total es:", int(porc))


# Opcion 9
def promedio(v):
    acum = 0
    cont = 0
    for i in v:
        importe = i.calcular_importe()
        acum += importe
        cont += 1

    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El importe promedio de los envios es:", int(prom))
    return prom


def menor(v, prom):
    cont = 0
    for i in v:
        importe = i.calcular_importe()
        if importe < prom:
            cont += 1

    print("Los envios con un importe menor al promedio:", cont)


def principal():
    fd = "envios-tp3.txt"
    tc = "HC"
    v = []
    band_7 = False

    opcion = -1
    while opcion != 10:
        opcion = menu()
        if opcion == 1:
            if len(v) != 0:
                r = int(input("¿Desea borrar los datos previos? (1: Si - 2: No: "))
                if r == 1:
                    v = []
                    tc = cargar_desde_archivo(v, tc, fd)
                    print("Carga terminada...")
                else:
                    print("Carga cancelada... El arreglo mantiene los datos que contenia...")
            else:
                tc = cargar_desde_archivo(v, tc, fd)
                print("Carga terminada...")

        elif opcion == 2:
            cargar_ticket(v)
            print("Carga terminada")
        elif opcion == 3:
            if len(v) != 0:
                mostrar(v)
            else:
                print("Todavia no hay datos cargados en el arreglo")
        elif opcion == 4:
            if len(v) != 0:
                buscar_direccion_y_tipo(v)
            else:
                print("Debe cargar el arreglo primero")

        elif opcion == 5:
            if len(v) != 0:
                buscar_codigo(v)
            else:
                print("No hay envíos cargados.")

        elif opcion == 6:
            if len(v) != 0:
                contar(v, tc)
            else:
                print("Cargar el arreglo primero")

        elif opcion == 7:
            if len(v) != 0:
                v_acum = acumular(v, tc)
                band_7 = True
            else:
                print("Cargar el arreglo primero")

        elif opcion == 8:
            if band_7:
                mayor(v_acum)

            else:
                print("Primero debe ingresar a la Opcion 7")
                print()

        elif opcion == 9:
            if len(v) != 0:
                prom = promedio(v)
                menor(v, prom)

            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()

        elif opcion == 10:
            print("-=" * 50)
            print("Hasta Luego")
            print("-=" * 50)

        else:
            print("Elija una opción correcta.")


if __name__ == "__main__":
    principal()
