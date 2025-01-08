import os.path
import pickle
import random


class Empleado:

    # cargo (1, 4)      ; edad ( 18, 30 )
    def __init__(self, nombre, importe, cargo, edad):
        self.nombre = nombre        # ctrl + d
        self.importe = importe
        self.cargo = cargo
        self.edad = edad

    def __str__(self):

        # self.cargo(1,4)   1-1        2-1         3-1         4-1
        # indices           0           1           2           3
        cargos_desc = ("Gerente", "Cajero", "Repositor", "Jefe de caja")

        r = "Nombre: " + self.nombre
        r += " | Importe: " + str(self.importe)
        r += " | Cargo: " + cargos_desc[self.cargo-1]
        r += " | Edad: " + str(self.edad)

        # r+= " | Curso: " + "1K" + str(self.curso)
        return r


# ====================================================================
#                        Opcion 1
# ====================================================================
def validar_n():
    n = int(input("Ingresar cantidad de empleados a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de empleados a cargar(debe ser positivo): "))
    return n


def cargar_arreglo(v_emp, n):
    # cargo (1, 4)      ; edad ( 18, 30 )
    # def __init__(self, nombre, importe, cargo, edad):

    nombres = "ABCDEF"
    for i in range(n):          # n = 3
        # i = 0         1       2
        nombre = random.choice(nombres)
        importe = round(random.uniform(0.1, 10), 2)      # para crear flotantes
        cargo = random.randint(1, 4)
        edad = random.randint(18, 30)
        empleadito = Empleado(nombre, importe, cargo, edad)
        add_in_order(v_emp, empleadito)

    print("Se cargaron exitosamente", n, "empleados.")


def add_in_order(v_emp, empleadito):    # vuelta 0:        len = 0  ; empleadito.nombre = C
    izq, der = 0, len(v_emp) - 1        # vuelta 1:         len = 1 ; empleadito.nombre = A

    while izq <= der:
        c = (izq + der) // 2
        if v_emp[c].nombre == empleadito.nombre:
            pos = c
            break
        elif v_emp[c].nombre > empleadito.nombre:       # si se come al vector es de menor a mayor.
            der = c - 1                                 # si se come al objeto es de mayor a menor.
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    #           0       1
    # v_emp = [ E2,     E1 ]
    v_emp[pos:pos] = [empleadito]


# ====================================================================
#                        Opcion 2
# ====================================================================
def mostrar_datos(v_emp, t):
    # indices    0   1   2
    # v_emp = [ E1, E2, E3 ]
    for i in v_emp:
        # i = E1, E2,
        if i.importe > t:
            print(i)


# ====================================================================
#                        Opcion 4
# ====================================================================
def generar_archivo(fd, v_emp, x):
    m = open(fd, "wb")      # "ab"
    #
    se_cargo_archivo = False

    for i in v_emp:
        # i = E , E , E
        if i.edad > x and i.cargo != 1:
            pickle.dump(i, m)
            m.flush()           # No es necesaria
            se_cargo_archivo = True


    if se_cargo_archivo:
        print("Se cargaron datos de empleados en el archivo:", fd)
    else:
        print("No se cargo ningun dato de empleado en esta vuelta de ciclo.")


    tam = os.path.getsize(fd)
    if tam == 0:
        print("No se cargo ningun dato de empleado en esta vuelta de ciclo.")
    else:
        print("Se cargaron datos de empleados en el archivo:", fd)

    m.close()       # SI ES NECESARIO


# ====================================================================
#                        Opcion 5
# ====================================================================
def mostrar_archivo(fd):
    if os.path.exists(fd):
        m = open(fd, "rb")
        tam = os.path.getsize(fd)

        cont, acum = 0, 0

        # indices   0   1   2
        # v_emp = [ E1, E2, E3 ]

        # fd        = [ E1         E2          E3 ]
        # m.tell()  = 0     25          50         70

        while m.tell() < tam:
            emp = pickle.load(m)
            print(emp)
            if emp.cargo == 2 or emp.cargo == 3:
                cont += 1
                acum += emp.importe

        if cont > 0:
            prom = acum / cont
            print("El promedio total de los empleados Cajero y Repositor es:", prom)
        else:
            print("No se encontro ningun empleado cajero o repositor e nel archivo.")

        m.close()

    else:
        print("El archivo no existe por favor ingrese primero por la opcion 4.")



def menu():

    print("=" * 50)
    print(" 1 - Cargar arreglo."
          "\n 2 - Mostrar datos."
          "\n 3 -  ."
          "\n 4 -  .")

    return int(input("Elegir opcion: "))


def main():

    # vector arreglo lista principal
    v_emp = []          # list()


    # archivo principal
    fd = "empleados.dat"


    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_emp, n)

        elif op == 2:
            t = float(input("Ingresar importe a superar: "))
            mostrar_datos(v_emp, t)

        elif op == 3:
            pass

        elif op == 4:
            x = int(input("Guardar solo los que superen la edad: "))
            generar_archivo(fd, v_emp, x)

        elif op == 5:
            mostrar_archivo(fd)





if __name__ == '__main__':
    main()
