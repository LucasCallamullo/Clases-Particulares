
# Empleado: Define una clase Empleado con atributos como nombre, salario, cargo, legajo y
# el cargo es un valor entero entre 1 y 3, pero cuando se muestre en pantalla debe salir
# 1 = gerente, 2 = cajero, 3 = repositor segun corresponda
# 1 ) Cargar arreglo por n, donde n es un valor ingresado por el usuario
# 2 ) mostrar_datos ordenardos por legajo y que muestre los empleados con salario t que sean mayores a t, t es
# un valor ingresado por el usuario
# 3 ) buscar por legajo un legajo x que ingrese el usuario. confirmar que previamente haya pasado por la opcion 2
# muestre el primer el valor que coincida y que se no encontro informe por pantalla
# 4 ) calcular el salario anual de todos los empleados
import random


class Empleado:
    # cargo int(1, 3)
    def __init__(self, nombre, salario, cargo, legajo):
        self.nombre = nombre        # Ctrl + d
        self.salario = salario
        self.cargo = cargo
        self.legajo = legajo

    def __str__(self):
        cargo_str = cargo_to_str(self.cargo)
        cadena = "Nombre: " + self.nombre
        cadena += "| Salario: " + str(self.salario)
        cadena += "| Cargo: " + cargo_str
        cadena += "| Legajo: " + str(self.legajo)
        return cadena


def cargo_to_str(cargo):
    #           0           1           2
    cargos = ["Gerente", "Cajero", "Repositor"]
    return cargos[cargo-1]



def menu():
    print("=" * 50)
    print(" 1 - Cargar arreglo."
          "\n 2 - Mostrar datos."
          "\n 3 - Busqueda Binaria legajo."
          "\n 4 - Calculo Salario Anual."
          "\n 0 - Salir.")
    return int(input("Ingresar opcion: "))


# ===================================================================
#                   Opcion 1
# ===================================================================
def cargar_arreglo(v_emp, n):
    nombres = ("Lucas", "Eze", "Matias", "Lautaro")
    for i in range(n):
        nombre = random.choice(nombres)
        salario = round(random.uniform(0.1, 10), 2)
        cargo = random.randint(1, 3)
        legajo = random.randint(1, 15)
        empleadito = Empleado(nombre, salario, cargo, legajo)
        v_emp.append(empleadito)


# ===================================================================
#                   Opcion 2
# ===================================================================
def ordenar(v_emp):
    n = len(v_emp)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_emp[i].legajo > v_emp[j].legajo:
                v_emp[i], v_emp[j] = v_emp[j], v_emp[i]


def mostrar_datos(v_emp, t):
    acum = 0
    for i in range(len(v_emp)):
        # i = 0, 1, 2, 3
        if v_emp[i].salario > t:
            print(v_emp[i])
            acum += v_emp[i].salario


    # v_emp = [ 1, 2, 23, 43]
    #    0    ,  1          , 2
    # v_emp = [ empleadito, empleadito, empleadito, empleadito]
    for i in v_emp:
        # i = empleadito, empleadito, empleadito,
        if i.salario > t:
            print(i)
            acum += i.salario


# ===================================================================
#                   Opcion 3
# ===================================================================
# [1, 8, 9, 15, 18 ,18]
#
def busqueda_binaria(v_emp, x):         # X = 18        # c = 2     # izq = 3   # der = 5
    izq, der = 0, len(v_emp)-1
    while izq <= der:
        c = (izq + der) // 2
        if x == v_emp[c].legajo:
            return c
        if x < v_emp[c].legajo:
            der = c - 1
        else:
            izq = c + 1
    return -1


# ===================================================================
#               Opcion 4
# ===================================================================
def acumuladores_op4(v_emp):
    acum = 0
    for i in v_emp:
        acum += i.salario
    total = acum * 12
    return total


def principal():

    # vector principal
    v_emp = []

    # Banderas
    paso_op1 = False
    paso_op2 = False

    op = -1
    while op != 0:
        op = menu()

        if not paso_op1:
            if op == 1:
                n = int(input("Cuantos empleados quiere cargar: "))
                cargar_arreglo(v_emp, n)
                paso_op1 = True
            else:
                print("Debe ingresar la opcion 1.")

        else:
            if op == 1:
                n = int(input("Cuantos empleados quiere cargar: "))
                cargar_arreglo(v_emp, n)
                paso_op1 = True
                paso_op2 = False

            elif op == 2:
                ordenar(v_emp)
                paso_op2 = True

                t = float(input("Ingresar salario a comparar: "))
                mostrar_datos(v_emp, t)

            elif op == 3:

                if not paso_op2:
                    print("Por favor primero utilize la opcion 2.")

                else:
                    x = int(input("Ingresar legajo a buscar: "))

                    pos = busqueda_binaria(v_emp, x)

                    if pos >= 0:
                        print("La posicion: ", pos)
                        print("Se encontro el empleado con el legajo: ", x)
                        print("Los datos del empleado son: \n", v_emp[pos])
                    else:
                        print("No se encontro el legajo deseado.")


            elif op == 4:
                acum = acumuladores_op4(v_emp)
                print("El total de los salarios anualmente es:", acum)

            # Trampita para ver que tenemos todos el tiempo
            elif op == 6:
                for i in v_emp:
                    print(i)

            elif op == 0:
                print("Gracias por utilizar el programa.")

            else:
                print("Por favor ingrese una opcion correcta.")


if __name__ == '__main__':
    principal()


