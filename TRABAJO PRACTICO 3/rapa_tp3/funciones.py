

from registro import *


# =====================================================================
#                       Opcion 1
# =====================================================================
def cargar_arreglo(v_envios, fd, tc):

    if len(v_envios) == 0:
        v_envios, tc = leer_archivo(v_envios, fd, tc)
        return v_envios, tc

    op = -1
    while op != 2:
        print("1 - Desea borrar el contenido? (Cargar nuevamente)")
        print("2 - Cancelar")
        op = int(input("Ingresar opcion: "))

        if op == 1:
            v_envios = []
            v_envios, tc = leer_archivo(v_envios, fd, tc)
            print("algo")
            return v_envios, tc

        elif op == 2:
            return v_envios, tc


def leer_archivo(v_envios, fd, tc):

    m = open(fd, "rt")
    cont_lineas = 0
    # Bucle para leer cada linea del archivo
    for linea in m:
        cont_lineas += 1

        # Esto es para evitar laprimera linea que es el timestap
        if cont_lineas == 1:
            if "SC" in linea:
                tc = "SC"

        else:
            cod_postal = linea[0:9].strip()

            direccion = linea[9:29].rstrip()
            tipo_envio = int(linea[29])
            forma_pago = int(linea[30])
            envio = Envio(cod_postal, direccion, tipo_envio, forma_pago)
            v_envios.append(envio)

    return v_envios, tc


# =====================================================================
#                       Opcion 2
# =====================================================================
def cargar_envio_manual(v_envios):

    cod_postal = input("Ingrese Código postal: ")
    direccion = input("Ingrese Direccion: ")

    tipo_envio = int(input("Ingrese tipo envio (0, 6): "))
    while tipo_envio > 6 or tipo_envio < 0:
        tipo_envio = int(input("Ingrese tipo envio(0, 6): "))

    forma_pago = int(input("Ingrese 1 para efectivo / 2 para tarjeta de credito: "))
    while forma_pago < 1 or forma_pago > 2:
        forma_pago = int(input("Ingrese 1 para efectivo / 2 para tarjeta de credito: "))

    envio = Envio(cod_postal, direccion, tipo_envio, forma_pago)
    v_envios.append(envio)


# =====================================================================
#                       Opcion 3
# =====================================================================
def mostrar_datos(v_envios):
    n = len(v_envios)
    print("Hay", n, "registros en el arreglo")

    m = int(input("Cantidad a mostrar (al menos 1 y no mas de " + str(n) + ")?: "))
    while m > n or m < 1:
        m = int(input("Cantidad a mostrar (al menos 1 y no mas de " + str(n) + ")?: "))

    print("Listado de envios ordenados por codigo postal...")
    for i in range(m):
        print(v_envios[i])

    print()


def ordenar_arreglo(v_envios):  # shellsort
    n = len(v_envios)
    gap = n // 2  # Inicialmente, la brecha (gap) es la mitad del tamaño de la lista

    while gap > 0:
        for i in range(gap, n):
            temp = v_envios[i]
            j = i
            # Se compara el elemento actual con el elemento 'gap' posiciones atrás
            while j >= gap and v_envios[j - gap].cod_postal > temp.cod_postal:
                v_envios[j] = v_envios[j - gap]
                j -= gap

            v_envios[j] = temp
        gap //= 2  # Reduce la brecha


# ========================================================
#           Opcion 4
# ========================================================
def busqueda_scuencial_op4(v_envios, d, e):
    pos = -1
    for i in range(len(v_envios)):
        if v_envios[i].direccion == d and v_envios[i].tipo_envio == e:
            pos = i
            break

    return pos


# ========================================================
#           Opcion 5
# ========================================================
def busqueda_secuencial_op5(v_envios, cp):
    pos = -1
    for i in range(len(v_envios)):
        if v_envios[i].cod_postal == cp:
            pos = i
            break
    return pos


# ========================================================
#           Opcion 6
# ========================================================
def generar_vector_conteo(v_envios, tc):
    v_cont = [0] * 7

    for i in v_envios:
        if tc == "HC":
            # Solo ingresa si la dirección es válida
            if i.check_dir():
                v_cont[i.tipo_envio] += 1

        else:
            v_cont[i.tipo_envio] += 1

    for i in range(len(v_cont)):
        print("Tipo de envio:", i, "Tiene la cantidad de:", v_cont[i])


# ========================================================
#           Opcion 7
# ========================================================
def generar_vector_acum(v_envios, tc):

    v_acum = [0] * 7

    for i in v_envios:
        if tc == "HC":
            # Solo ingresa si la dirección es válida
            if i.check_dir():
                importe = i.calcular_importe()
                v_acum[i.tipo_envio] += importe

        else:
            importe = i.calcular_importe()
            v_acum[i.tipo_envio] += importe

    for i in range(len(v_acum)):
        print("Tipo de envio:", i, "Tiene la cantidad de:", v_acum[i])

    return v_acum


# ========================================================
#           Opcion 8
# ========================================================
def opcion8(acumulador_op7):

    acum_total = 0
    mayor = None
    tipo = None

    for i in range(len(acumulador_op7)):
        acum_total += acumulador_op7[i]

        if mayor is None or acumulador_op7[i] > mayor:
            mayor = acumulador_op7[i]
            tipo = i

    print("El Tipo de Envio:", tipo, "Tiene el Monto mayor con:", mayor)

    porc = 0
    if acum_total > 0:
        porc = mayor * 100 / acum_total

    print("El porcentaje que representa el monto mayor sobre el total es:", int(porc))


# ========================================================
#           Opcion 9
# ========================================================
def calc_prom_op9(v_envios):
    cont = 0
    acum = 0

    for i in v_envios:
        # i = E1, E2
        cont += 1
        importe = i.calcular_importe()
        acum += importe

    prom = 0
    if cont > 0:
        prom = acum / cont

    print("El promedio de los importes de todos los envios es:", int(prom))
    return prom


def opcion9(v_envios, promedio):
    cont = 0
    for i in v_envios:
        importe = i.calcular_importe()
        if importe < promedio:
            cont += 1

    print("La cantidad de envios con importe menor al promedio es:", cont)