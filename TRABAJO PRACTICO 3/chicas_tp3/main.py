

import os.path
from envio import *


def validar_rango(inf, sup, msj):
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def validar_mayor(inf, msj):
    valor = int(input(msj))
    while valor <= inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def cargar_desde_archivo(v, tc, fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        print('Revise..')
        return

    pr = True
    m = open(fd, "rt")
    for line in m:
        if pr is True:
            if "SC" in line:
                tc = "SC"
            pr = False

        else:
            cp = line[0:9].strip().upper()      # str
            direccion = line[9:29].strip()      # str
            tipo = int(line[29])                # int
            pago = int(line[30])                # int

            env = Envio(cp, direccion, tipo, pago)
            v.append(env)

    m.close()
    return tc


def opcion1(v, tc, fd):
    if len(v) != 0:
        r = int(input("¿Desea borrar los datos previos? (1: Si - 2: No (volver al menu): "))
        if r == 1:
            v = []
            tc = cargar_desde_archivo(v, tc, fd)
            print("Carga terminada...")
        else:
            print("Carga cancelada... El arreglo mantiene los datos que contenia...")
    else:
        tc = cargar_desde_archivo(v, tc, fd)
        print("Carga terminada...")

    print()
    return v, tc


def opcion2(v):
    m = validar_mayor(0, "Cuantos registros quiere agregar al arreglo (al menos 1)?: ")

    for i in range(m):
        cod = input("Codigo postal: ")
        dp = input("Direccion postal: ")
        tip = validar_rango(0, 6, "Tipo de envio (entre 0 y 6): ")
        fp = validar_rango(1, 2, "Forma de pago (entre 1 y 2): ")

        env = Envio(cod, dp, tip, fp)
        v.append(env)

    print("Carga terminada")
    print()


def ordenar(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]


def opcion3(v):
    n = len(v)
    ordenar(v)
    print("Hay", n, "registros en el arreglo")
    m = validar_rango(1, n, "Cantidad a mostrar (al menos 1 y no mas de " + str(n) + ")?: ")
    print("Listado de envios ordenados por codigo postal...")
    for i in range(m):
        print(v[i])

    print()


# ======================================================================
#                       Opcion 5
# ======================================================================
def busqueda_secuencial_op5(v, cp):

    pos = -1
    for i in range(len(v)):
        if v[i].codigo == cp:
            pos = i
            break

    return pos


# ======================================================================
#                       Opcion 7
# ======================================================================
def generar_vectores_acum_op7(v, tc):

    # generar o crear el vector
    v_acum = [0] * 7

    # rellenar datos
    for i in v:
        # i = E1, E2, E3
        #
        importe = i.calcular_importe()

        print("importe", importe, "para el tipo de envio:", i.tipo)

        if tc == "HC":

            # si la direccin es valida
            if i.check_dir():
                v_acum[i.tipo] += importe

        # cuando tc es == "SC"
        else:
            v_acum[i.tipo] += importe

    # mostrar los datos
    for i in range(len(v_acum)):

        print("La cantidad de envios para el tipo", i, "es:", v_acum[i])

    return v_acum




def principal():
    # variable para almacenar en forma centralizada el nombre fisico del archivo de texto...
    fd = "envios-tp3.txt"
    # fd = "envios-prueba.txt"

    # variable para guardar en forma centralizada el tipo de control de direcciones vigente (por default, "HC")...
    tc = "HC"

    # la referencia al arreglo...
    v = []

    v_acum = []

    op = 0
    while op != 10:
        print("Trabajo Practico 3")
        print("1. Cargar arreglo desde archivo de texto")
        print("2. Cargar arreglo desde teclado")
        print("3. Listado ordenado")
        print("4. Busqueda por direccion")
        print("5. Busqueda por codigo postal")
        print("6. Cantidad de envios con direccion válida")
        print("7. Importe final acumulado")
        print("8. Envio con mayor importe")
        print("9. Importe final promedio")
        print("10. Salir")
        op = int(input("Ingrese numero de opcion: "))

        if op == 1:
            # v = vector de trabajo
            # tc = tipo de control que es HC O SC
            v, tc = opcion1(v, tc, fd)

        elif op == 2:
            opcion2(v)

        elif op == 3:
            if len(v) != 0:
                opcion3(v)
            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()

        elif op == 4:
            pass

        elif op == 5:
            # que preguntes si tenes que hacer alguna condicion que verifique si ingreso a la op 3 o no y hacer
            # busqueda binaria o secuencial segun corresponda

            cp = input("Ingresar codidgo postal a buscar: ")

            pos = busqueda_secuencial_op5(v, cp)

            if pos >= 0:
                print("Datos Viejos:", v[pos])

                if v[pos].pago == 1:
                    v[pos].pago = 2
                else:
                    v[pos].pago = 1

                print("Datos Actualizados:", v[pos])

                # modifiques su importe por un valor "x" que ingresa por teclado
                # x = float(input("Ingresar nuevo precio: "))
                # v[pos].importe = x

                # aumentes su precio un 10%
                # v[pos].importe += 0.1 * v[pos].importe

            else:
                print("No se encontro un codigo postal con ese codigo", cp)


        elif op == 6:
            # generar_vectores_acum_op7(v, tc)
            pass

        elif op == 7:

            v_acum = generar_vectores_acum_op7(v, tc)


        elif op == 8:

            if len(v_acum) > 0:
                opcion3(v_acum)
            else:
                print("No se ingreso a la opcion 7")


        elif op == 9:
            pass


if __name__ == "__main__":
    principal()
