import random
from registro import *








# opcion 1
def validar_n():
    n = int(input("Cantidad de Pasajes a cargar: "))
    while n <= 0:
        n = int(input("Cantidad de Pasajes a cargar(Por favor ingrese un valor positivo): "))
    return n


def cargar_arreglo(v_pasaje, n):
    # destino(100, 103)  (100: Bahamas, 101: Bermudas: 102: Puerto Rico, 103: República Dominicana)
    # pasaporte = str   ; clase (1, 10)         ; importe > 0
    # def __init__(self, pasaporte, nombre, destino, clase, importe):
    pasaportes = "ABCDE"
    nombres = ("Lucas", "Matias", "Santi")

    for i in range(n):
        # i = 0, 1, 2, 3, 4
        pasaporte = random.choice(pasaportes)
        nombre = random.choice(nombres)
        destino = random.randint(100, 103)
        clase = random.randint(3, 3)
        # flotante con dos decimales
        importe = round(random.uniform(0.1, 10), 2)

        pas = Pasaje(pasaporte, nombre, destino, clase, importe)
        v_pasaje.append(pas)


# opcion 2
def ordenar(v_pasaje):
    n = len(v_pasaje)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_pasaje[i].importe < v_pasaje[j].importe:
                v_pasaje[i], v_pasaje[j] = v_pasaje[j], v_pasaje[i]


def mostrar_datos(v_pasaje):
    for i in v_pasaje:
        # if i.importe > 2.0:
        print(i)


# oipcion 3
def acumuladores_op3(v_pasaje):
    # clase(1, 10)
    # resto -1  1  2  3  4  5  6  7  8  9  10
    # indices=  0  1  2  3  4  5  6  7  8  9
    # v_acum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    v_acum = [0] * 10
    for i in v_pasaje:
        v_acum[i.clase-1] += i.importe

    return v_acum


def mostrar_v_acum(v_acum):
    may = 0
    ind = -1
    for i in range(len(v_acum)):
        # i = 0, 9
        if v_acum[i] > 0:
            print("El importe acumulado es:", round(v_acum[i], 2), "en la clase:", i+1)

        if v_acum[i] > may:
            may = v_acum[i]
            ind = i

    print("=" * 50)
    print("El mayor importe acumulado es:", round(v_acum[ind], 2), "en la clase:", ind+1)


# opcionj 4
def promedio_clase_op4(v_pasaje):
    acum = 0
    total = 0
    for i in v_pasaje:
        if i.clase == 3:
            acum += i.importe
            total += 1

    prom = acum / total
    return prom


def mostrar_op4(v_pasaje, prom):
    for i in v_pasaje:
        if i.clase == 3 and i.importe > prom:
            print(i)


# opcion 5
def busqueda_lineal(v_pasaje, pasaporte):
    for i in range(len(v_pasaje)):
        # i = 0 1 2 3 ...
        if v_pasaje[i].pasaporte == pasaporte:
            return i
    return -1





def menu():
    print("=" * 50)
    print(" 1 - Cargar arreglo."
          "\n 2 - Mostrar datos"
          "\n 3 - "
          "\n 4 - "
          "\n 5 - ")
    return int(input("Ingresar opcion: "))


def main():

    # Vector / arreglo / lista
    v_pasaje = []           # list()

    # bandera opcion 1
    validar_op1 = False

    op = -1
    while op != 0:

        op = menu()

        if op == 0:
            print("Gracias por usar el menu.")

        elif not validar_op1:
            if op == 1:
                n = validar_n()
                cargar_arreglo(v_pasaje, n)
                validar_op1 = True
            else:
                print("Primero debe ingresar por la opcion 1: ")

        else:
            if op == 1:
                n = validar_n()
                cargar_arreglo(v_pasaje, n)

            elif op == 2:
                ordenar(v_pasaje)
                mostrar_datos(v_pasaje)

            elif op == 3:
                v_acum = acumuladores_op3(v_pasaje)
                mostrar_v_acum(v_acum)

            elif op == 4:
                prom = promedio_clase_op4(v_pasaje)
                mostrar_op4(v_pasaje, prom)

            elif op == 5:
                pasaporte = input("Ingresar pasaporte a buscar: ")

                pos = busqueda_lineal(v_pasaje, pasaporte)

                if pos >= 0:
                    print("Pasajero", v_pasaje[pos].nombre, ", por favor concurrir a atención al cliente")
                else:
                    print("No se encontro el pasaporte indicado.")



            elif op == 6:
                #             0  1  2  3  4
                # v_pasaje = [P, P, P, P, P]
                # for i in range(len(v_pasaje)):
                    # i = 0, 1, 2, 3, 4
                #     print(v_pasaje[i])


                # v_pasaje = [P, P, P, P, P]
                for i in v_pasaje:
                    # i = P, P, P
                    print(i)

            else:
                print("Ingrese una opcion correcta.")


if __name__ == '__main__':
    main()
