import envio
import os.path
import pickle

def validar_mayor(inf, msj):
    valor = int(input(msj))
    while valor <= inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor

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

    # apertura del archivo de entrada...
    datos = open(fdt, "rt")

    # leo la linea de timestamp...
    ts = datos.readline()

    # leo la linea de encabezados...
    hd = datos.readline()

    # apertura del archivo de salida...
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


def opcion1(fdb, fdt):
    if not os.path.exists(fdt):
        print("El archivo", fdt, "no existe...")
        print("Controle y vuelva por aquí...")
        return

    if os.path.exists(fdb):
        print("El archivo", fdb, "existe...")
        r = int(input("¿Desea borrar los datos previos? (1: Sí - 2: No (volver al menú): "))
        if r == 1:
            datos = open(fdt, "rt")

            # leo la linea de timestamp...
            ts = datos.readline()

            # leo la linea de encabezados...
            hd = datos.readline()
            print('El archivo binario previo fue eliminado...')
            generar_archivo_binario(fdt,fdb)
            print('Se creo el archivo binario nuevo... ')
        else:
            print('La carga se cancela, el archivo binario se mantiene...')
    else:
        generar_archivo_binario(fdt,fdb)
        print("Carga de archivo binario terminada...")
    return


def carga_por_teclado(fdb):
    m = open(fdb, "ab")
    n = validar_mayor(0, "¿Cuántos registros quiere agregar al arreglo (al menos 1)?: ")
    for i in range(n):
        cod = input("Código postal: ")
        dp = input("Dirección postal: ")
        tip = validar_rango(0, 6, "Tipo de envío (entre 0 y 6): ")
        fp = validar_rango(1, 2, "Forma de pago (entre 1 y 2): ")
        env = envio.Envio(cod, dp, tip, fp)
        pickle.dump(env, m)
    m.close()

def mostrar_archivo_binario(fdb):
    if not os.path.exists(fdb):
        print("El archivo", fdb, "no existe...")
        print("Controle y vuelva por aquí...")
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


def mostrar_cp(fdb,cp):
    if not os.path.exists(fdb):
        print("El archivo", fdb, "no existe...")
        print("Controle y vuelva por aquí...")
        return

    print("Listado general de envios...")
    c = 0
    m = open(fdb, "rb")
    t = os.path.getsize(fdb)
    while m.tell() < t:
        env = pickle.load(m)
        if cp == env.codigo:
            print(env)
            c += 1
    m.close()
    print("Se listaron", c, "registros...")


def mostrar_direc(fdb,direc):
    if not os.path.exists(fdb):
        print("El archivo", fdb, "no existe...")
        print("Controle y vuelva por aquí...")
        return
    print("Listado general de envios...")
    m = open(fdb, "rb")
    t = os.path.getsize(fdb)
    while m.tell() < t:
        env = pickle.load(m)
        if direc == env.direccion:
            print(env)
            return
            break
    print('No se encontró la dirección solicitada...')
    m.close()


def contadores_tipo_forma(fdb,mat):
    if not os.path.exists(fdb):
        print("El archivo", fdb, "no existe...")
        print("Controle y vuelva por aquí...")
        return
    print("Listado general de envios...")
    m = open(fdb, "rb")
    t = os.path.getsize(fdb)
    while m.tell() < t:
        env = pickle.load(m)
        fila = env.pago - 1
        col = env.tipo
        mat[fila][col] += 1
    m.close()
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > 0:
                print('Forma de pago: ', i + 1, ' - Tipo de envio: ', j, ' - Cantidad de envios: ', mat[i][j])
    return mat

def matriz_final_pago(fdb,mat):
    if not os.path.exists(fdb):
        print("El archivo", fdb, "no existe...")
        print("Controle y vuelva por aquí...")
        return
    print("Listado general de envios...")
    pago = len(mat)
    envio = len(mat[0])
    print('Se mostrara a razón de la foma de pago...')
    for f in range(pago):
        ac = 0
        for c in range(envio):
            ac += mat[f][c]
        print('La cantidad de envios por la forma de pago: ', ac)
    print()

def matriz_final_envio(fdb,mat):
    if not os.path.exists(fdb):
        print("El archivo", fdb, "no existe...")
        print("Controle y vuelva por aquí...")
        return
    print("Listado general de envios...")
    pago = len(mat)
    envio = len(mat[0])
    print('Se mostrara a razón de la foma de pago...')
    for c in range(envio):
        ac = 0
        for f in range(pago):
            ac += mat[f][c]
        print('La cantidad de envios por tipo de envio: ', ac)
    print()


def binario_promedio(fdb):
    if not os.path.exists(fdb):
        print("El archivo", fdb, "no existe...")
        print("Controle y vuelva por aquí...")
        return
    c = 0
    ac = 0
    m = open(fdb, "rb")
    t = os.path.getsize(fdb)
    while m.tell() < t:
        env = pickle.load(m)
        c += 1
        ac += env.final_amount()
    # promedio = int(ac) / int(c)
    promedio = ac / c
    return promedio


def shell_sort(v):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1
    while h > 0:
        for j in range(h, n):
            y = v[j].codigo
            k = j - h
            while k >= 0 and y < v[k].codigo:
                v[k + h].codigo = v[k].codigo
                k -= h
            v[k + h].codigo = y
        h //= 3
    return v

def procesar_archivo(fdb, prom):
    if not os.path.exists(fdb):
        print("El archivo", fdb, "no existe...")
        print("Controle y vuelva por aquí...")
        return

    m = open(fdb, "rb")
    t = os.path.getsize(fdb)

    v = []
    while m.tell() < t:
        env = pickle.load(m)
        if env.final_amount() > prom:
            v.append(env)
    return v

def procesar_archivo2():
    v = []
    fdt = "envios-tp4.csv"
    if not os.path.exists(fdt):
        print("El archivo", fdt, "no existe...")
        print("Controle y vuelva por aquí...")
        return
    m = open(fdt, 'rt')
    # leo la linea de timestamp...
    ts = m.readline()

    # leo la linea de encabezados...
    hd = m.readline()

    for linea in m:
        if linea[-1] == '\n':
            linea = linea[:-1]
        obj = envio.generar_objeto(linea)
        v.append(obj)
    m.close()
    return v


def mostrar_vector(v,promedio):
    n = len(v)
    for i in range(n):
        if v[i].final_amount() > promedio:
            print(v[i])

    print("cantidad de envios:", len(v))


def principal():
    v = []
    op = 0
    fdt = "envios-tp4.csv"
    fdb = "envios-tp4.dat"
    while op != 9:
        print("Trabajo Práctico 4")
        print("1. Crear archivo binario")
        print("2. Cargar datos por teclado")
        print("3. Mostrar registro")
        print("4. Busqueda por código postal")
        print("5. Busqueda por dirección")
        print("6. Combinación de tipos de envio y forma de pago")
        print("7. Cantidad de tipos de envio y forma de pago")
        print("8. Promedio de importes pagados")
        print("9. Salir")
        op = int(input("Ingrese número de opción: "))
        if op == 1:

            opcion1(fdb,fdt)
            print("Terminado...")
        elif op == 2:
            carga_por_teclado(fdb)
        elif op == 3:
            mostrar_archivo_binario(fdb)
        elif op == 4:
            cp = input('Ingrese el código postal a buscar (se mostraran todos los cp encontrados) : ')
            mostrar_cp(fdb, cp)
        elif op == 5:
            direc = input('Ingrese direccion a buscar: ')
            mostrar_direc(fdb, direc)
        elif op == 6:
            mat = [[0] * 7 for i in range(2)]
            contadores_tipo_forma(fdb,mat)
        elif op == 7:
            matriz_final_pago(fdb,mat)
            matriz_final_envio(fdb,mat)
        elif op == 8:
            promedio = binario_promedio(fdb)

            # v = procesar_archivo()
            v = procesar_archivo(fdb, promedio)
            shell_sort(v)

            mostrar_vector(v,promedio)
            print(promedio) # 9752.71025
        elif op == 9:
            print('Gracias por salir =D ...')


if __name__ == "__main__":
    principal()