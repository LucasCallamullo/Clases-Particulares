import clase

def procesar_linea(linea):
    cp = linea[0:9].strip()
    direccion = linea[9:29].strip()
    tipo = linea[29]
    fp = linea[30]
    envio = clase.Envio(cp, direccion, tipo, fp)
    return envio


def tipo_control(ts):
    bandera_tiene_s = False
    bandera_tiene_h = False
    anterior = " "
    control = " "
    for car in ts:

        if car == "H":
            bandera_tiene_h = True
            anterior = car

        if bandera_tiene_h and anterior == "C":
            return "Hard Control"

        if car == "S":
            bandera_tiene_s = True
            anterior = car

        if bandera_tiene_s and anterior == "C":
            return "Soft Control"

    return "Hard Control"   # sea por defecto HC
        #if control == "Hard Control":



def mostrar_vector(v):
    for i in range(len(v)):
        print(v[i])

def cargar_manual(v):
    tipo_valido = "0123456"
    forma_valida = "12"
    cp = input("ingrese codigo postal:")
    dir = input("ingrese direccion:")
    tipo =input("ingrese tipo de envio:")  #validar
    while tipo not in tipo_valido:
        tipo = input("tipo incorrecto, ingrese un valor entre 0 y 6:")
    forma_pago = input("ingrese forma de pago:")  #validar
    while forma_pago not in forma_valida:
        forma_pago =input("forma de pago  incorrecta, ingrese 1 o 2:")
    envio = clase.Envio(cp,dir,tipo,forma_pago)
    v.append(envio)



def ordenar(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[j].codigo_postal < v[i].codigo_postal:
                v[i], v[j] = v[j], v[i]


def proceso_archivo():
    v = []
    control = ""
    m = open("envios-tp3.txt")

    ts = m.readline()  # validar timestamp
    tc = tipo_control(ts)

    for linea in m:
        envio = procesar_linea(linea)
        v.append(envio)
    m.close()

    return v, tc



def busqueda_secuencial(v, d , e):
    for i in range(len(v)):
        #print(v[i])
        if v[i].direccion == d and v[i].tipo == e :
            return i
    return -1


def busqueda_cp(cp_ingresado, v):
    for i in range(len(v)):
        if v[i].codigo_postal == cp_ingresado:
            return i
    return -1


def mostrar_m_primeros(v,m):
    ordenar(v)
    for i in range(m):
        print(v[i])


def principal():
    op = 0
    v = []

    tc = "Hard Control"

    #control = tipo_control(ts)
    while op != -1:
        print("menu de opciones")
        print("1-cargar de archivo")
        print("2- carga por teclado")
        print("3-mostrar todos los registros")
        print("4-ingresar dirección y tipo de envio")
        print("5- buscar envio por código postal(se intercambia la forma de pago, es decir, si es 1 pasa a ser 2 y viceversa")
        print("-1- salir")
        op = int(input("ingrese opcion:"))

        #b_borrar_vector = False
        #cargar por texto
        if op == 1  :
            # v, tc = opcion_1(fd)

            if len(v) != 0:
                print("¡vector ya tiene datos!")
                borrar = int(input("Desea continuar de todos modos? (0: no - 1: si"))
                if borrar == 1:

                    v, tc = proceso_archivo()
                    mostrar_vector(v)
                    print("Carga terminada")
                else:
                    print("Carga cancelada")
            else:
                v, tc = proceso_archivo()
                mostrar_vector(v)

        elif op == 2 :
            cargar_manual(v)
            mostrar_vector(v)
        elif op == 3:
            buscar_registro = int(input("Desea solicitar una cantidad especifica de registros?(1-si 0-no:"))
            if buscar_registro == 1:
                m = int(input("Ingrese la cantidad de registros a mostar:"))
                mostrar_m_primeros(v,m)
            if buscar_registro == 0:
                ordenar(v)
                mostrar_vector(v)
        elif op == 4:
            d=input("Ingrese la direccion a buscar:")
            e = input ("Ingrese el tipo de envio a buscar:")
            envio_solicitado = busqueda_secuencial(v,d,e)
            if envio_solicitado == -1:
                print("No se encontró")
            else:
                print("Envio encontrado!!")
                print(v[envio_solicitado])
        elif op == 5:
            cp_ingresado = input("Ingrese el código postAL a buscar:")
            cp_busqueda = busqueda_cp(cp_ingresado , v)
            if cp_busqueda == -1:
                print("No se encontró el código postal :(")
            else:
                print("CP encontrado")
                if v[cp_busqueda].forma_pago == "1":
                    v[cp_busqueda].forma_pago = "2"
                    print(v[cp_busqueda])
                else:
                    v[cp_busqueda].forma_pago = "1"
                    print(v[cp_busqueda])
        elif op == 6:
            print(tc)
        else:
            print("opcion incorrecta")


if __name__ == "__main__":
    principal()
