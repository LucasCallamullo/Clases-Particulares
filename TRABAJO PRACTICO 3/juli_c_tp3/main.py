
from funciones_valerio import *


# ======================================================================
#                       Opcion 4
# ======================================================================
def busqueda_direc_tipo(envios):
    d = input("ingrese la direccion: ")
    e = int(input("ingrese el tipo de envio: "))
    existe = False
    for i in range(len(envios)):
        if d == envios[i].direccion and e == envios[i].tipo:
            existe = True
            break
    if existe:
        print(envios[i])

    else:
        print("no se encontro la direccion", d + str(e))


# ======================================================================
#                       Opcion 5
# ======================================================================
def busqueda_secuencial_cp(envios, cp):
    pos = -1
    for i in range(len(envios)):
        if envios[i].codigo == cp:
            pos = i
            break

    return pos


# ======================================================================
#                       Opcion 6
# ======================================================================
def opcion6(v_envios, tc):

    v_cont = [0] * 7

    for i in v_envios:

        if tc == "HC":
            # Si la funcion devuelve True
            if i.check_dir():   # retorna True si es direccion Valida
                v_cont[i.tipo] += 1

        else:       # tc == "SC"
            v_cont[i.tipo] += 1

    for i in range(len(v_cont)):
        print("Para el tipo de envio:", i, "tengo la cantidad de envios de:", v_cont[i])


# ======================================================================
#                       Opcion 7
# ======================================================================
def opcion7(v_envios, tc):

    v_acum = [0] * 7

    for i in v_envios:

        if tc == "HC":
            # Si la funcion devuelve True
            if i.check_dir():   # retorna True si es direccion Valida
                importe = i.calcular_importe_final()        # nos devuelve el importe final de ese envio
                v_acum[i.tipo] += importe

        else:       # tc == "SC"
            importe = i.calcular_importe_final()  # nos devuelve el importe final de ese envio
            v_acum[i.tipo] += importe

    for i in range(len(v_acum)):
        print("Para el tipo de envio:", i, "tengo la cantidad de envios de:", v_acum[i])

    return v_acum


def principal():
    # variable para almacenar en forma centralizada el nombre fisico del archivo de texto...
    fd = "envios-tp3.txt"
    # fd = "envios-prueba.txt"

    # variable para guardar en forma centralizada el tipo de control de direcciones vigente (por default, "HC")...
    tc = "HC"           # "HC" o "SC"

    # la referencia al arreglo...
    v_envios = []

    v_acum_op7 = []

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
            v_envios, tc = opcion1(v_envios, tc, fd)

        elif op == 2:
            opcion2(v_envios)

        elif op == 3:
            if len(v_envios) != 0:
                opcion3(v_envios)
            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()

        elif op == 4:
            if len(v_envios) > 0:
                busqueda_direc_tipo(v_envios)
            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()

            # VER SI FALTA ALGO CUANDO HAGAMOS LA PRUEBA FINAL

        elif op == 5:
            if len(v_envios) > 0:
                cp = input("Ingrese un código postal: ")
                pos = busqueda_secuencial_cp(v_envios, cp)
                if pos >= 0:
                    print("Datos viejos: ", v_envios[pos])
                    if v_envios[pos].pago == 1:
                        v_envios[pos].pago += 1
                    else:
                        v_envios[pos].pago -= 1

                    print("Datos actualizados: ", v_envios[pos])
                else:
                    print("No se encontraron resultados.")

            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()

        elif op == 6:
            # generar y mostrar vector de conteo
            opcion6(v_envios, tc)

        elif op == 7:
            if len(v_envios) > 0:

                v_acum_op7 = opcion7(v_envios, tc)

            else:
                print("Todavia no hay datos cargados en el arreglo...")
                print()

        elif op == 8:

            if len(v_acum_op7) > 0:

                # indices        0    1
                # v_acum_op7 = [ 5.5, 3.5,
                may = None
                for i in v_acum_op7:
                    # i = 5.5, 3.5
                    if may is None or i > may:
                        may = i

            else:
                print("No se ingreso a la opcion 7")

        elif op == 9:
            acum = 0
            for i in v_envios:
                # i = E1, E2
                # sacar el dato importe
                importe = i.calcular_importe_final()
                acum += importe


if __name__ == "__main__":
    principal()
