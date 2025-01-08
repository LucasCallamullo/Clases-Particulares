

from funciones_valerio import *



# Opcion 4


# Opcion 5
def opcion5(v_envios, cp):  # cp = s

    pos = -1

    # indices       0      1       2
    # v_envios = [ E1   , E2     , E3]
    # codigo        x      s        t

    for i in range(len(v_envios)):  # range(3)
        # i = 0,    1,      2

        if v_envios[i].codigo == cp:
            pos = i
            break   # romper el ciclo for / while

    return pos      # pos >= 0 significa que encontre un resultado
                    # pos == -1 significa que no encontramos un resultado


# Opcion 6
def opcion6(v_envios, tc):
    # generar el vector
    v_cont = [0] * 7  # tipo_envio(0, 6), o sea 7 valores

    # rellenar el vector
    for i in v_envios:

        if tc == "HC":
            # Si la funcion devuelve True es direccion valida
            if i.check_dir():
                v_cont[i.tipo] += 1

        else:
            v_cont[i.tipo] += 1

    # mostrar el vector
    for i in range(len(v_cont)):
        print("Para el tipo de envio:", i, "Existe la cantidad de envios de:", v_cont[i])


# Opcion 7
def opcion7(v_envios, tc):

    # generar el vector
    v_acum = [0] * 7        # tipo_envio(0, 6), o sea 7 valores

    # rellenar el vector
    for i in v_envios:

        if tc == "HC":
            # Si la funcion devuelve True es direccion valida
            if i.check_dir():

                importe_final = i.calcular_importe_final()  # les devuelve el importe final

                print("importe:", importe_final, "tipo envio:", i.tipo)

                v_acum[i.tipo] += importe_final

        else:
            importe_final = i.calcular_importe_final()  # les devuelve el importe final
            v_acum[i.tipo] += importe_final

    # mostrar el vector
    for i in range(len(v_acum)):
        print("Para el tipo de envio:", i, "Existe la cantidad de envios de:", v_acum[i])

    return v_acum


def principal():
    # variable para almacenar en forma centralizada el nombre fisico del archivo de texto...
    fd = "envios-tp3.txt"
    # fd = "envios-prueba.txt"

    # variable para guardar en forma centralizada el tipo de control de direcciones vigente (por default, "HC")...
    tc = "HC"           # "HC" o "SC"

    # la referencia al arreglo...
    v_envios = []

    v_acum_opcion7 = []

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
            pass


        elif op == 5:
            cp = input("Ingrese codigo postal a buscar: ")

            # busqueda secuencial
            pos = opcion5(v_envios, cp)

            if pos >= 0:
                print("Datos Desactualizados:", v_envios[pos])

                if v_envios[pos].pago == 1:
                    v_envios[pos].pago = 2
                else:       # si es 2
                    v_envios[pos].pago = 1

                print("Datos Actualizados:", v_envios[pos])

            else:
                print("No se encontro un resultado")

        elif op == 6:
            pass

        elif op == 7:

            # generar vector acumulacion opcion 7
            v_acum_opcion7 = opcion7(v_envios, tc)

        elif op == 8:

            if len(v_acum_opcion7) > 0:
                # opcion8(v_acum_opcion7)
                pass

            else:
                print("Todavia no ingreso a la opcion 7")

        elif op == 9:
            acum = 0
            for i in v_envios:
                # i = E1, E2
                # sacar el dato importe final
                importe_final = i.calcular_importe_final()
                acum += importe_final
            # calculan el promedio

            # de vuelta hacer otro ciclo pero ahora para saber cuantos son menores que el proemdio


if __name__ == "__main__":
    principal()
