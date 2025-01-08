# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


class Cuenta:
    # id > 0        ; gastos >= 0       ; saldo(-1, 1)
    def __init__(self, id, nombre, saldo, gastos, num_cuenta):
        self.id = id
        self.nombre = nombre
        self.saldo = saldo
        self.gastos = gastos
        self.num_cuenta = num_cuenta

    def __str__(self):
        r = "ID: " + str(self.id)
        r += " | Nombre: " + self.nombre
        r += " | Saldo: " + str(self.saldo)
        r += " | Gastos: " + str(self.gastos)
        r += " | Num Cuenta: " + str(self.num_cuenta)
        return r


# ================================================
#                    Opcion 1
# ================================================
def validar_n():
    n = int(input("Ingrese cantidad de Cuentas a cargar: "))
    while n <= 0:
        n = int(input("Ingrese cantidad de Cuentas a cargar(Ingrese un valor positivo): "))
    return n


def cargar_arreglo(v_cuenta, n):
    # id > 0        ; gastos >= 0       ; saldo(-1, 1)
    # def __init__(self, id, nombre, saldo, gastos):
    nombres = "ABCD"
    for i in range(n):
        id = random.randint(1, 10)
        nombre = random.choice(nombres)
        saldo = round(random.uniform(-5, 5), 2)
        gastos = round(random.uniform(0, 10), 2)
        num_cuenta = random.randint(100, 109)
        cuentita = Cuenta(id, nombre, saldo, gastos, num_cuenta)
        v_cuenta.append(cuentita)


# ================================================
#                    Opcion 2
# ================================================
def ordenar(v_cuenta):
    n = len(v_cuenta)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_cuenta[i].nombre > v_cuenta[j].nombre:
                v_cuenta[i], v_cuenta[j] = v_cuenta[j], v_cuenta[i]


def mostrar_datos(v_cuenta):
    for i in v_cuenta:
        # i = C, C, C, C
        print(i)

    # for i in range(len(v_cuenta)):
        # i = 0 1 2 3
        # print(v_cuenta[i])


# ================================================
#                    Opcion 3
# ================================================
def mostrar_datos_op3(v_cuenta):
    bandera_op3 = False
    for i in range(len(v_cuenta)):
        if v_cuenta[i].saldo < 0:
            print(v_cuenta[i])
            bandera_op3 = True

    if not bandera_op3:
        print("Ninguna cuenta tiene saldo negativo")


# ================================================
#                    Opcion 4
# ================================================
def busqueda_lineal(v_cuenta, x, nom):
    for i in range(len(v_cuenta)):
        # i = 0 1 2 3 ....
        if v_cuenta[i].id == x and v_cuenta[i].nombre == nom:
            return i

    return -1


# ================================================
#                    Opcion 5
# ================================================
# 3- Determinar el saldo acumulado por num_cuenta(100, 110) que se hicieron de cada tipo posible de cuenta
# en total 10 acumuladores, solo mostrar los saldos de los acumuladores que superen el promedio de los importes saldos
# positivos
def acumuladores_op5(v_cuenta):
    # num_cuenta(100, 109)
    #
    #           100 101 102
    # ind       0   1   2                    9                                                  100
    # v_acum = [0,  5,  10, 0, 0, 0, 0, 0, 0, 0]
    v_acum = [0] * 10
    for i in range(len(v_cuenta)):
        v_acum[v_cuenta[i].num_cuenta-100] += v_cuenta[i].saldo

    return v_acum


def calcular_promedio_op5(v_cuenta):
    acum, cont = 0, 0
    for i in v_cuenta:
        if i.saldo > 0:
            acum += i.saldo
            cont += 1

    prom = 0
    if cont >= 0:
        prom = acum / cont
    print("Promedio:", prom)
    return prom


def mostrar_datos_op5(v_acum, prom):
    for i in range(len(v_acum)):
        if v_acum[i] > prom:
            print("El num de cuenta:", i+100, "Tiene un saldo acumulado de:", v_acum[i])


def menu():
    print("=" * 50)
    print(" 1 - Cargar arreglo."
          "\n 2 - Mostrar datos."
          "\n 3 - Opcion 3"
          "\n 4 - "
          "\n 0 - Salir.")
    return int(input("Ingresar una opcion: "))



def main():

    # vector
    v_cuenta = []           # list()

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_cuenta, n)

        elif op == 2:
            ordenar(v_cuenta)
            # s = saldo
            #
            mostrar_datos(v_cuenta)

        elif op == 3:
            mostrar_datos_op3(v_cuenta)

        elif op == 4:
            x = int(input("Buscar Num ID: "))

            # y que el nombre sea un valor nom ingresado por teclado
            nom = input("Ingresar nombre a buscar: ")

            pos = busqueda_lineal(v_cuenta, x, nom)

            if pos >= 0:
                # original
                # print

                # 4) Se pide modificar el saldo de la cuenta a un valor = 1000, y debe mostrar el valor actualizado,
                # junto con el nombre y su id
                #
                v_cuenta[pos].saldo = 1000
                print("Id:", v_cuenta[pos].id, "Nombre:", v_cuenta[pos].nombre, "Saldo:", v_cuenta[pos].saldo)

            else:
                print("No se encontraron datos.")


        elif op == 5:
            v_acum = acumuladores_op5(v_cuenta)
            prom = calcular_promedio_op5(v_cuenta)
            mostrar_datos_op5(v_acum, prom)



        elif op == 6:
            for i in v_cuenta:
                print(i)



if __name__ == '__main__':
    main()
