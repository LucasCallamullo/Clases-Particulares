import os
import pickle
import struct
from envio2 import Envio

# Funciones auxiliares de validación


def rango(men, may, msj):
    valor = int(input(msj))
    while men > valor or may < valor:
        print(f"El valor cargado no pertenece al rango [{men}, {may}]")
        valor = int(input(msj))
    return valor


def generar_archivo_binario(fdt, fdb):
    if os.path.exists(fdb):
        respuesta = input(f"El archivo {fdb} ya existe. ¿Desea sobrescribirlo? (s/n): ")
        if respuesta.lower() != 's':
            print("Operación cancelada.")
            return

    if not os.path.exists(fdt):
        print(f"El archivo {fdt} no existe.")
        return

    with open(fdt, "rt") as datos, open(fdb, "wb") as bin_file:
        datos.readline()  # Omitimos el encabezado
        for linea in datos:
            d = linea.strip().split(",")
            cp = d[0]
            de = d[1]
            te = int(d[2])
            fp = int(d[3])
            envio_obj = Envio(cp, de, te, fp)
            pickle.dump(envio_obj, bin_file)

    print(f"Archivo binario {fdb} creado exitosamente.")


def cargar_envio(fd_binario):
    cod = input("Ingrese Código postal (10 caracteres): ").strip()[:10]
    dp = input("Ingrese Dirección postal (50 caracteres): ").strip()[:50]
    tip = rango(0, 6, "Tipo de envío (entre 0 y 6): ")
    fp = rango(1, 2, "Forma de pago (1 o 2): ")

    with open(fd_binario, "ab") as bin_file:
        bin_file.write(struct.pack('10s50sii', cod.encode(), dp.encode(), tip, fp))

    print("Registro agregado exitosamente al archivo binario.")


def mostrar_archivo_binario(fdb):
    if not os.path.exists(fdb):
        print(f"El archivo {fdb} no existe.")
        return

    print("Listado general de envíos...")
    with open(fdb, "rb") as bin_file:
        while True:
            try:
                envio_obj = pickle.load(bin_file)
                print(envio_obj)
            except EOFError:
                break


def buscar_por_codigo(fd_binario, cod_buscado):
    if not os.path.exists(fd_binario):
        print(f"El archivo {fd_binario} no existe.")
        return

    encontrado = 0
    with open(fd_binario, "rb") as bin_file:
        while True:
            try:
                envio_obj = pickle.load(bin_file)
                if envio_obj.codigo == cod_buscado:
                    print(envio_obj)
                    encontrado += 1
            except EOFError:
                break

    if encontrado == 0:
        print("No se encontraron registros con ese código postal.")
    else:
        print(f"Total de registros encontrados: {encontrado}")


def buscar_por_direccion(fd_binario, direccion_buscada):
    if not os.path.exists(fd_binario):
        print(f"El archivo {fd_binario} no existe.")
        return

    with open(fd_binario, "rb") as bin_file:
        while True:
            try:
                envio_obj = pickle.load(bin_file)
                if envio_obj.direccion == direccion_buscada:
                    print(f"Registro encontrado: {envio_obj}")
                    return
            except EOFError:
                break
    print("No se encontró ningún registro con esa dirección.")


def contar_envios_por_combinaciones(fd_binario):
    if not os.path.exists(fd_binario):
        print(f"El archivo {fd_binario} no existe.")
        return

    # Matriz de 7 tipos de envíos y 2 formas de pago
    conteo = [[0 for _ in range(2)] for _ in range(7)]

    with open(fd_binario, "rb") as bin_file:
        while True:
            try:
                envio_obj = pickle.load(bin_file)
                tipo_envio = envio_obj.tipo
                forma_pago = envio_obj.pago - 1  # Para ajustar a 0 y 1
                conteo[tipo_envio][forma_pago] += 1
            except EOFError:
                break

    # Mostrar solo las combinaciones con valores mayores a cero
    for tipo in range(7):
        for pago in range(2):
            if conteo[tipo][pago] > 0:
                print(f"Tipo de envío {tipo}, Forma de pago {pago+1}: {conteo[tipo][pago]} envíos")


def totalizar_envios_por_tipo_y_pago(fd_binario):
    if not os.path.exists(fd_binario):
        print(f"El archivo {fd_binario} no existe.")
        return

    conteo = [[0 for _ in range(2)] for _ in range(7)]

    with open(fd_binario, "rb") as bin_file:
        while True:
            try:
                envio_obj = pickle.load(bin_file)
                tipo_envio = envio_obj.tipo
                forma_pago = envio_obj.pago - 1
                conteo[tipo_envio][forma_pago] += 1
            except EOFError:
                break

    # Total por tipo de envío
    print("Total por tipo de envío:")
    for tipo in range(7):
        total_tipo = sum(conteo[tipo])
        print(f"Tipo de envío {tipo}: {total_tipo} envíos")

    # Total por forma de pago
    print("\nTotal por forma de pago:")
    for pago in range(2):
        total_pago = sum(conteo[tipo][pago] for tipo in range(7))
        print(f"Forma de pago {pago + 1}: {total_pago} envíos")


def calcular_importe_promedio(fd_binario):
    if not os.path.exists(fd_binario):
        print(f"El archivo {fd_binario} no existe.")
        return

    total_importe = 0
    total_envios = 0
    envios_mayores = []

    with open(fd_binario, "rb") as bin_file:
        while True:
            try:
                envio_obj = pickle.load(bin_file)
                importe = envio_obj.tipo * 100  # Suponiendo que el tipo de envío determina el importe
                total_importe += importe
                total_envios += 1
            except EOFError:
                break

    if total_envios == 0:
        print("No hay envíos para calcular el promedio.")
        return

    importe_promedio = total_importe / total_envios
    print(f"Importe promedio: {importe_promedio}")

    # Segunda pasada: encontrar envíos con importe mayor al promedio
    with open(fd_binario, "rb") as bin_file:
        while True:
            try:
                envio_obj = pickle.load(bin_file)
                importe = envio_obj.tipo * 100  # Suponiendo que el tipo de envío determina el importe
                if importe > importe_promedio:
                    envios_mayores.append(envio_obj)
            except EOFError:
                break

    # Ordenar por código postal
    envios_mayores.sort(key=lambda envio2: envio.codigo)

    # Mostrar los envíos con importe mayor al promedio
    print("\nEnvíos con importe mayor al promedio:")
    for envio in envios_mayores:
        print(envio)
