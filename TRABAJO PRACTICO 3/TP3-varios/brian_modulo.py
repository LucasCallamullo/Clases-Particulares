import os.path


class Envio:
    def __init__(self, codigo_postal, direccion, tipo_envio, forma_pago):
        self.codigo_postal = codigo_postal
        self.direccion = direccion
        self.tipo_envio = tipo_envio
        self.forma_pago = forma_pago

    def __str__(self):
        cadena = "Pais: " + self.pais() + " | Código Postal: " + self.codigo_postal
        cadena += " | Dirección: " + self.direccion
        cadena += " | Tipo Envío: " + str(self.tipo_envio)
        cadena += " | Forma Pago: " + str(self.forma_pago)
        return cadena

    def pais(self):
        cp = self.codigo_postal
        n = len(cp)
        if n < 4 or n > 9:
            return 'Otro'

        # ¿es Argentina?
        if n == 8:
            if cp[0].isalpha() and cp[0] not in 'IO' and cp[1:5].isdigit() and cp[5:8].isalpha():
                return 'Argentina'
            else:
                return 'Otro'

        # ¿es Brasil?
        if n == 9:
            if cp[0:5].isdigit() and cp[5] == '-' and cp[6:9].isdigit():
                return 'Brasil'
            else:
                return 'Otro'

        if cp.isdigit():
            # ¿es Bolivia?
            if n == 4:
                return 'Bolivia'

            # ¿es Chile?
            if n == 7:
                return 'Chile'

            # ¿es Paraguay?
            if n == 6:
                return 'Paraguay'

            # ¿es Uruguay?
            if n == 5:
                return 'Uruguay'

        # ...si nada fue cierto, entonces sea lo que sea, es otro...
        return 'Otro'



    def check_dir(self):
        cl = cd = 0
        td = False
        ant = " "
        for car in self.direccion:
            if car in " .":
                if cl == cd:
                    td = True

                cl = cd = 0
                ant = " "

            else:
                cl += 1

                if not car.isdigit() and not car.isalpha():
                    return False


                if ant.isupper() and car.isupper():
                    return False

                if car.isdigit():
                    cd += 1

                ant = car

        return td


    def calcular_importe_final(self):
        importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
        monto = importes[self.tipo_envio]

        destino = self.pais()
        cp = self.codigo_postal
        pago = self.forma_pago

        if destino == 'Argentina':
            inicial = monto
        else:
            if destino in ['Bolivia', 'Paraguay'] or (destino == 'Uruguay' and cp[0] == '1'):
                inicial = int(monto * 1.20)
            elif destino == 'Chile' or (destino == 'Uruguay' and cp[0] != '1'):
                inicial = int(monto * 1.25)
            elif destino == 'Brasil':
                if cp[0] in '89':
                    inicial = int(monto * 1.20)
                elif cp[0] in '0123':
                    inicial = int(monto * 1.25)
                else:
                    inicial = int(monto * 1.30)
            else:
                inicial = int(monto * 1.50)

        final = inicial

        if pago == 1:
            final = int(0.9 * inicial)

        return final

#################################################
#                opción 1
#################################################
def cargar_desde_archivo(envios, tc, fd):
    if not os.path.exists(fd):
        print("El archivo', fd, 'no existe...")
        print("Revise, y reinicie el programa...")
        return

    pr = True
    m = open(fd, "rt")
    for linea in m:
        if pr is True:
            if "SC" in linea:
                tc = "SC"
            pr = False

        else:
            codigo_postal = linea[:9].strip().upper()
            direccion = linea[9:29].strip()
            tipo_envio = int(linea[29:30])
            forma_pago = int(linea[30:31])
            envio = Envio(codigo_postal, direccion, tipo_envio, forma_pago)
            envios.append(envio)

    m.close()
    return tc


def opcion1(envios, tc, fd):
    if len(envios) != 0:
        r = int(input("¿Desea borrar los datos previos? (1: Si - 2: No (volver al menu): "))
        if r == 1:
            v = []
            tc = cargar_desde_archivo(envios, tc, fd)
            print("Carga terminada...")
        else:
            print("Carga cancelada... El arreglo mantiene los datos que contenia...")
    else:
        tc = cargar_desde_archivo(envios, tc, fd)
        print("Carga terminada...")

    print()
    return envios, tc


#################################################
#                opción 2
#################################################

def validar_opciones(lim_inf, lim_sup, mensaje="ingrese la opcion deseada"):
    n = int(input(mensaje))
    while n < lim_inf or n > lim_sup:
        print("El valor dabe estar entre", lim_inf, "y", lim_sup)
        n = int(input(mensaje))

    return n

def cargar_envio_manual(envios):
    codigo_postal = input("Ingrese el código postal: ")
    direccion = input("Ingrese la dirección: ")
    tipo_envio = validar_opciones(0, 6, "Ingrese el tipo de envio entre (0 y 6): ")
    forma_pago = validar_opciones(0, 1, "Ingrese el forma de pago entre (0 y 1): ")
    envio = Envio(codigo_postal, direccion, tipo_envio, forma_pago)
    envios.append(envio)

#################################################
#                opción 3
#################################################

def validar_rango(inf, sup, msj):
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def ordenar_arreglo(envios):
    n = len(envios)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if envios[i].codigo_postal > envios[j].codigo_postal:
                envios[i], envios[j] = envios[j], envios[i]


def mostrar_arreglo(envios):
    n = len(envios)
    print("hay '" + str(n) + "' registro en el arreglo")
    validar_op = validar_opciones(0, 1,"¿Desea mostrar todos los registros o solo los primeros m? (0: Todos, 1: Solo m): ")
    if validar_op == 1:
        m = int(validar_rango(1, n, "Ingrese la cantidad de registros a mostrar: "))
        for i in range(m):
            envio = envios[i]
            print(envio)
    else:
        for envio in envios:
            print(envio)

#################################################
#                opción 4
#################################################
def busqueda_secuencial_p4(envios, d, e):
    pos = -1
    for i in range(len(envios)):
        if envios[i].direccion == d and envios[i].tipo_envio == e:
            pos = i
            break
    return pos


#################################################
#                opción 5
#################################################
def busqueda_secuencial_p5(envios, cp):
    pos = -1
    for i in range(len(envios)):
        if envios[i].codigo_postal == cp:
            pos = i
            break
    return pos


#################################################
#                opción 6
#################################################
def vector_acum_hc(envios):
    hc = [0] * 7
    for i in envios:
        if i.check_dir():
            hc[i.tipo_envio] += 1

    return hc


def vector_acum_sc(envios):
    sc = [0] * 7
    for i in envios:
        if not i.check_dir():
            sc[i.tipo_envio] += 1

    return sc


def mostrar_conteo_hc(vec_cont_hc):
    print("Conteo de envíos HC:")
    for i in range(len(vec_cont_hc)):
        print("Tipo de envio: ", i, "envíos válidos (HC): ", vec_cont_hc[i])


def mostrar_conteo_sc(vec_cont_sc):
    print("Conteo de envíos SC:")
    for i in range(len(vec_cont_sc)):
        print("Tipo de envio: ", i, "envíos válidos (SC): ", vec_cont_sc[i])

#################################################
#                opción 7
#################################################
def vector_acum_op7(envios):
    v_acum = [0] * 7
    for i in envios:
        if i.check_dir():
            importe = i.calcular_importe_final()
            v_acum[i.tipo_envio] += importe

    return v_acum


def vector_acum_hc_p_7(envios):
    hc = [0] * 7
    for i in envios:
        if i.check_dir():
            importe = i.calcular_importe_final()
            hc[i.tipo_envio] += importe

    return hc


def vector_acum_sc_p_7(envios):
    sc = [0] * 7
    for i in envios:
        if not i.check_dir():
            importe = i.calcular_importe_final()
            sc[i.tipo_envio] += importe

    return sc


def mostrar_conteo_hc_p7(vec_acum_hc):
    print("Conteo de envíos HC:")
    for i in range(len(vec_acum_hc)):
        print("Tipo de envio: ", i, "Importe final acumulado es (HC): $", vec_acum_hc[i],)


def mostrar_conteo_sc_p7(vec_acum_sc):
    print("Conteo de envíos SC:")
    for i in range(len(vec_acum_sc)):
        print("Tipo de envio: ", i, "Importe final acumulado es (SC): $", vec_acum_sc[i])


#################################################
#                opción 8
#################################################
def encontrar_mayor_monto(vec_acum_hc, vec_acum_sc):
    max_hc = vec_acum_hc[0]
    max_sc = vec_acum_sc[0]

    # Encuentra el máximo en vec_acum_hc
    for i in vec_acum_hc:
        if i > max_hc:
            max_hc = i

    # Encuentra el máximo en vec_acum_sc
    for i in vec_acum_sc:
        if i > max_sc:
            max_sc = i

    # Compara los máximos
    if max_hc > max_sc:
        return max_hc
    else:
        return max_sc

def calcular_porcentaje_mayor(vec_acum_hc, vec_acum_sc, may):
    total = 0
    total_2 = 0
    for monto in vec_acum_hc:
        total += monto

    for monto_2 in vec_acum_sc:
        total_2 += monto_2

    monto_total = total + total_2

    por = round(((may / monto_total) * 100), 3)

    return por
#################################################
#                opción 9
#################################################
