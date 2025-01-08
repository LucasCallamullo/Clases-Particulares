import envio
import os.path
import pickle


# -----------------------------------------------
#               PUNTO 1
# -----------------------------------------------

def generar_archivo_binario(fdt, fdb):
    if not os.path.exists(fdt):
        print("El archivo", fdt, "no existe...")
        print("Controle y vuelva por aquí...")
        return

    with open(fdt, "rt") as datos, open(fdb, "wb") as m:
        # Leo la línea de timestamp...
        ts = datos.readline()
        # Leo la línea de encabezados...
        hd = datos.readline()
        for linea in datos:
            d = linea.split(",")
            cp = d[0]
            de = d[1]
            te = int(d[2])
            fp = int(d[3])
            env = envio.Envio(cp, de, te, fp)
            pickle.dump(env, m)


# -----------------------------------------------
#               PUNTO 2
# -----------------------------------------------

def agregar_envio(fdb):
    # falta proceso de validacion si el tipo envio ingresado esta entre 0-6
    # falta proceso de validacion si la forma pago ingresado esta entre 1-2
    cp = input("Ingrese el código postal: ")
    direccion = input("Ingrese la dirección: ")
    tipo_envio = int(input("Ingrese el tipo de envío (0-6): "))
    forma_pago = int(input("Ingrese la forma de pago (1: efectivo, 2: tarjeta de crédito): "))

    env = envio.Envio(cp, direccion, tipo_envio, forma_pago)

    with open(fdb, "ab") as m:
        pickle.dump(env, m)


# -----------------------------------------------
#               PUNTO 3
# -----------------------------------------------

def mostrar_archivo_binario(fdb):
    print("Mostrando todos los registros del archivo binario:")
    with open(fdb, "rb") as m:
        while True:
            try:
                env = pickle.load(m)
                # Asumimos que env tiene un método __str__ que formatea la salida
                print(env)
            except EOFError:
                break

    # --->
    # Esto lo hicieron ustedes o el profe subio esta forma o chat gpt?
    # no vieron ni try ni except tienen que hacer la forma que vieron para abrir y leer archivos binarios
    # deberian de usar esta forma que es la que les enseñaron
    if not os.path.exists(fdb):
        print("No existe el archivo:", fdb)
        print("Ingrese primero algún registro con la opción 1 o 2.")
        return

    m = open(fdb, "rb")  # read binary, porque solo nos interesa leer el contenido del archivo
    tam = os.path.getsize(fdb)

    while m.tell() < tam:
        env = pickle.load(m)        # env = E1, E2, E3
        print(env)

    m.close()

# -----------------------------------------------
#               PUNTO 4
# -----------------------------------------------
def mostrar_por_codigo_postal(fdb):
    cp = input("Ingrese el código postal a buscar: ")
    c = 0
    registros = []

    with open(fdb, "rb") as m:
        # Cargar todos los registros en memoria
        while True:
            try:
                env = pickle.load(m)
                registros.append(env)
            except EOFError:
                break

    # Filtrar y mostrar los registros por código postal
    for env in registros:
        if env.codigo == cp:
            print(env)
            c += 1

    print("Se mostraron", c, "registros.")


# -----------------------------------------------
#               PUNTO 5
# -----------------------------------------------

def buscar_por_direccion(fdb):
    direccion = input("Ingrese la dirección a buscar: ")
    encontrado = False
    registros = []

    with open(fdb, "rb") as m:
        # Cargar todos los registros en memoria
        while True:
            try:
                env = pickle.load(m)
                registros.append(env)
            except EOFError:
                break

    # Filtrar y mostrar los registros por dirección
    for env in registros:
        if env.direccion == direccion:
            print(env)
            encontrado = True
            break

    if not encontrado:
        print("No se encontró el registro.")


# -----------------------------------------------
#               PUNTO 6
# -----------------------------------------------

def contar_envios(fdb):
    matriz = [[0 for _ in range(2)] for _ in range(7)]  # 7 tipos de envío, 2 formas de pago
    with open(fdb, "rb") as m:
        while True:
            try:
                env = pickle.load(m)
                matriz[env.tipo][env.pago - 1] += 1
            except EOFError:
                break

    print("Cantidad de envíos por tipo y forma de pago:")
    for i in range(7):
        for j in range(2):
            if matriz[i][j] != 0:
                print(f"Tipo {i}, Forma de pago {j + 1}: {matriz[i][j]}")

    return matriz  # Devuelve la matriz para uso posterior


# -----------------------------------------------
#               PUNTO 7
# -----------------------------------------------

def totalizar_envios(matriz):
    totales_tipo = [0] * 7
    totales_pago = [0] * 2
    for i in range(7):
        for j in range(2):
            totales_tipo[i] += matriz[i][j]
            totales_pago[j] += matriz[i][j]

    print("Total de envíos por tipo:")
    for i in range(7):
        print(f"Tipo {i}: {totales_tipo[i]}")

    print("Total de envíos por forma de pago:")
    for j in range(2):
        print(f"Forma de pago {j + 1}: {totales_pago[j]}")


# -----------------------------------------------
#               PUNTO 8
# -----------------------------------------------

def calcular_importe_promedio(fdb):
    total_importe = 0
    contador = 0
    registros = []

    with open(fdb, "rb") as m:
        while True:
            try:
                env = pickle.load(m)
                total_importe += env.pago  # Suponiendo que el atributo 'pago' es el importe
                registros.append(env)
                contador += 1
            except EOFError:
                break

    if contador > 0:
        promedio = total_importe / contador
        print(f"Importe promedio: {promedio}")

        # Mostrar envíos que superan el promedio
        print("Envíos con importe mayor al promedio:")
        envios_mayores = [env for env in registros if env.pago > promedio]

        # Ordenar y mostrar
        envios_mayores.sort(key=lambda x: x.codigo)  # Ordenar por código postal
        for envio in envios_mayores:
            print(envio)


# -----------------------------------------------
#              MENU
# -----------------------------------------------

def menu():
    print(". Menú de opciones:")
    print("1. Crear archivo binario")
    print("2. Agregar un envío")
    print("3. Mostrar todos los envíos")
    print("4. Mostrar envíos por código postal")
    print("5. Buscar envío por dirección")
    print("6. Contar envíos por tipo y forma de pago")
    print("7. Totalizar envíos")
    print("8. Calcular importe promedio y mostrar envíos mayores")
    print("0. Salir")


# -----------------------------------------------
#               PRINCIPAL
# -----------------------------------------------

def principal():
    fdt = "envios-tp4.csv"
    fdb = "envios-tp4.dat"
    generar_archivo_binario(fdt, fdb)
    print("Terminado...")
    mostrar_archivo_binario(fdb)  # Mostrar todos los registros después de crear el archivo
    agregar_envio(fdb)
    mostrar_por_codigo_postal(fdb)
    buscar_por_direccion(fdb)

    # Contar envíos y guardar matriz
    matriz = contar_envios(fdb)

    # Totalizar envíos
    totalizar_envios(matriz)

    # Calcular importe promedio
    calcular_importe_promedio(fdb)

    # Menú en la función principal para manejar opciones
    opcion = None
    while opcion != "0":
        menu()  # Llamar a la función de menú
        opcion = input("Elija una opción: ")
        if opcion == "1":
            generar_archivo_binario(fdt, fdb)
        elif opcion == "2":
            agregar_envio(fdb)
        elif opcion == "3":
            mostrar_archivo_binario(fdb)  # Llamada para mostrar todos los envíos
        elif opcion == "4":
            mostrar_por_codigo_postal(fdb)
        elif opcion == "5":
            buscar_por_direccion(fdb)
        elif opcion == "6":
            matriz = contar_envios(fdb)
        elif opcion == "7":
            totalizar_envios(matriz)
        elif opcion == "8":
            calcular_importe_promedio(fdb)
        elif opcion == "0":
            print("Saliendo...")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    principal()
