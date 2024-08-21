import os.path
import pickle
import random


class Caso:
    # tipo ( 30, 33), tribunal (1, 3)
    def __init__(self, id, desc, importe, tipo, tribunal):
        self.id = id
        self.desc = desc
        self.importe = importe
        self.tipo = tipo
        self.tribunal = tribunal

    def __str__(self):
        #               540-540      541    542     543
        # tribunales    1-1           2           3       4
        # indices       0           1           2       3
        tribunales = ("Sala 1", "Sala 2", "Sala 3")


        #               0           1           2
        # tipo_cels = ("SMS", "Llamada", "Uso de datos")
        # tipo_cels[self.tipo-1]

        cad = "Id: " + str(self.id)
        cad += " | Desc: " + self.desc
        cad += " | importe: " + str(self.importe)
        cad += " | tipo: " + str(self.tipo)
        # cad += " | tribunal: " + "Sala " + str(self.tribunal)
        cad += " | tribunal: " + tribunales[self.tribunal-1]
        # curso: "curso 1K + str(self.curso)
        return cad


# ================= Opcion 1 ==========================
def validar_n():
    n = int(input("Ingresar cantidad de Casos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de Casos a cargar(Debe ser positivo): "))
    return n


def cargar_arreglo(v_caso, n):
    descripciones = "ABCDEF"
    # tipo ( 0, 5), tribunal (1, 4)
    # def __init__(self, id, desc, importe, tipo, tribunal):
    for i in range(n):          # 3         0       1       2
        id = random.randint(1, 15)
        desc = random.choice(descripciones)
        importe = round(random.uniform(0.1, 10), 2)
        tipo = random.randint(30, 33)
        tribunal = random.randint(1, 3)

        caso_temporal = Caso(id, desc, importe, tipo, tribunal)
        add_in_order(v_caso, caso_temporal)


def add_in_order(v_caso, caso_temporal):    # primera vuelta  len = 0   caso_temporal.id = 5
    izq, der = 0, len(v_caso) - 1           # segunda vuelta  len = 1  caso_temporal.id = 3

    while izq <= der:
        c = (izq + der) // 2
        if v_caso[c].id == caso_temporal.id:
            pos = c
            break
        elif v_caso[c].id > caso_temporal.id:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    #            0      1
    # v_caso = [ C2,    C1 ]
    v_caso[pos:pos] = [caso_temporal]


# ================= Opcion 2 ==========================
def mostrar_datos(v_caso, t):
    for i in v_caso:
        # v_caso = [ C1,    C2,   C3 ]
        # i = C1    , C2    , C3
        if i.tribunal != t:
            print(i)

    # for i in range(len(v_caso)):        # tamaño = 3
        #           0,      1,  2
        # v_caso = [ C1,    C2,   C3 ]
        # if v_caso[i].tribunal != t:
            # print(v_caso[i])


# ================= Opcion 3 ==========================
def generar_matriz(v_caso):

    # crear la matriz todo en 0
    filas = 4       # tipo ( 30, 33)
    columnas = 3    # tribunal (1, 3)
    matriz_conteo = [[0] * columnas for i in range(filas)]

    print(matriz_conteo)
    #       0           1           2           3
    #   [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # [ [0, 0, 0],
    #   [0, 0, 0],
    #   [0, 0, 0],
    #   [0, 0, 0] ]

    # rellenar la matriz con los datos
    for i in v_caso:
        # i = C1, C2, C3
        matriz_conteo[i.tipo-30][i.tribunal-1] += 1
        # matriz_acum[i.tipo-30][i.tribunal-1] += i.importe


    # mostrar la matriz
    # indices       0           1       2
    tribunales = ("Sala 1", "Sala 2", "Sala 3")
    for f in range(len(matriz_conteo)):    # = 4
        # f = 0, 1,  2 , 3
        for c in range(len(matriz_conteo[0])):     # = 3
            if matriz_conteo[f][c] > 0 and (f+30 == 30 or f+30 == 31):
                print("La cantidad por tipo:", f+30, "Y tribunal:", tribunales[c])
                print("La cantidad total es:", matriz_conteo[f][c])


# ================= Opcion 4 ==========================
def generar_archivo(fd, v_caso, x):
    m = open(fd, "wb")
    se_genero = False
    for i in v_caso:
        # i = C1, C2, C3
        if i.importe < x and (i.tipo == 3 or i.tipo == 4):
            pickle.dump(i, m)
            m.flush()       # No es necesaria
            se_genero = True

    # for i in range(len(v_caso)):
    #    if v_caso[i].importe < x and (v_caso[i].tipo == 3 or v_caso[i].tipo == 4):
    #        pickle.dump(v_caso[i], m)
    #        m.flush()       # No es necesaria

    if se_genero:
        print("Se genero el archivo:", fd)
    m.close()       # SI ES NECESARIO


# ================= Opcion 5 ==========================
def mostrar_archivo(fd):
    if os.path.exists(fd):
        m = open(fd, "rb")
        tam = os.path.getsize(fd)
        cont = 0
        acum = 0

        #           0       1   2
        # v_caso = [ C,    C,   C ]

        # fd = [ C      C       C ]
        #       0   25      50      70
        while m.tell() < tam:
            caso = pickle.load(m)
            cont += 1
            acum += caso.importe
            print(caso)

        print("Se mostraron un total de:", cont)
        print("El acumulado de sus montos total es:", acum)
        m.close()

    else:
        print("No existe el archivo debe pasar primero por la opcion 4.")


# ================= Opcion 6 ==========================
def busqueda_secuencial(v_caso, des):
    for i in range(len(v_caso)):
        # i = 0 1 2 3 4 5
        if v_caso[i].desc == des:
            return i
    return -1


# ================= Opcion 7 ==========================
def busqueda_binaria(v_caso, x):
    izq, der = 0, len(v_caso) - 1

    while izq <= der:
        c = (izq + der) // 2
        if v_caso[c].id == x:
            return c
        elif v_caso[c].id > x:
            der = c - 1
        else:
            izq = c + 1
    return -1


def menu():
    print("=" * 50)
    print(" 1 - Cargar arreglo"
          "\n 2 - Mostrar dats"
          "\n 3 - Matriz"
          "\n 4 - Generar Archivo"
          "\n 5 - Mostrar Archivo"
          "\n 6 - Busqueda secuencial."
          "\n 7 - Busqueda binaria.")

    return int(input("Ingresar opcion: "))


def main():

    # vector/arreglo principal
    v_caso = []

    # archivo datos
    fd = "casos.dat"

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_caso, n)

        elif op == 2:
            t = int(input("Valores de la sala que no debe mostrar(1, 4): "))
            mostrar_datos(v_caso, t)

        elif op == 3:
            generar_matriz(v_caso)

        elif op == 4:
            x = float(input("Ingrese valor de monto al que debe ser menor: "))
            generar_archivo(fd, v_caso, x)

        elif op == 5:
            mostrar_archivo(fd)

        elif op == 6:
            des = input("descripcion a buscar: ")
            pos = busqueda_secuencial(v_caso, des)
            if pos >= 0:
                print(v_caso[pos])
            else:
                print("No existe un caso con ese nombre.")

        elif op == 7:
            x = int(input("INgresar caso id a buscar: "))
            pos = busqueda_binaria(v_caso, x)
            if pos >= 0:
                # datos viejos
                print(v_caso[pos])
                if v_caso[pos].tipo == 30 or v_caso[pos].tipo == 31:
                    print("Caso gabable.")
                    # modificar importe y hacer recargo del 25 %
                    v_caso[pos].importe = v_caso[pos].importe + v_caso[pos].importe * 0.25

                    # valor = intinput
                    # v_caso[pos].importe = valor
                    # datos nuevos
                    print(v_caso[pos])

            else:
                print("No se encontro un caso con ese id.")


        elif op == 9:
            for i in v_caso:
                print(i)





if __name__ == '__main__':
    main()
