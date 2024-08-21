


# los siguientes datos: candidato(1, 3) , provincia (codificada de 1 a 23) y votante(codificado de 520 a 530)
# cant_votos > 0.

# 1 - cargar el arreglo ordenado por provincia

# 2 - mostrar datos a razon de un por linea, pero en vez de mostrar los numeros de los candidatos debe
# mostrar los nombres   (1: Massa, 2: Bullrich, 3:Milei)

# 4 -A partir del arreglo generar un archivo binario donde se incluyan los datos de todos los elecciones
# de las provincias menores o iguales a 14

# 5 - Mostrar el archivo generado en el punto anterior y ademas al final debe mostrar los votos totales
# de las provincias mayores a 7

import os.path
import pickle
import random
from registro import *


#       ========================        Opcion 1    ============================
def validar_n():
    n = int(input("Ingresar cantidad de elcciones a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de elcciones a cargar(debe ser positivo): "))
    return n


def cargar_arreglo(v_elec, n):

    for i in range(n):  # 3
        candidato = random.randint(1, 3)
        provincia = random.randint(1, 23)
        votante = random.randint(520, 530)
        votos = random.randint(1, 9)
        elec = Eleccion(candidato, provincia, votante, votos)
        add_in_order(v_elec, elec)


def add_in_order(v_elec, elec):

    izq, der = 0, len(v_elec) - 1           # E1.provincia: 6       # elec.provincia = 5

    while izq <= der:
        c = (izq + der) // 2
        if v_elec[c].provincia == elec.provincia:
            pos = c
            break
        elif v_elec[c].provincia > elec.provincia:          # si se come al vector es de menor a mayor
            der = c - 1                                     # si se come al objeto es de mayor a menor
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    # v_elec = [ E2,    E1 ]
    v_elec[pos:pos] = [elec]


#       ========================        Opcion 2    ============================
def mostrar_datos(v_elec):
    for i in v_elec:
        # i = E , E, E, E
        print(i)


#       ========================        Opcion 3    ============================
def generar_matriz(v_elec):
    # crear la matriz con 0
    # candidato(1, 3) , provincia (codificada de 1 a 23)
    filas = 3       # candidatos
    columnas = 23   # provincias
    matriz = [[0] * columnas for i in range(filas)]

    # print(matriz)
    # [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]

    # rellenar la matriz
    for i in v_elec:
        # i = E1, E2, E3
        matriz[i.candidato-1][i.provincia-1] += i.votos

    # mostrar la matriz
    candidatos = ["Massa", "Bullrich", "Milei"]
    for f in range(len(matriz)):        # f = 0, 1, 2
        for c in range(len(matriz[0])):     # c = 0, 1, 2, ..., 22
            if c+1 > 12 and matriz[f][c] > 0:
                print("La cantidad de votos por candidato:", candidatos[f], "y por provincia:", c+1)
                print("La cantidad acumulada de votos es:", matriz[f][c])


#       ========================        Opcion 4    ============================
def generar_archivo(v_elec, fd):
    m = open(fd, "wb")

    cont = 0
    #           0   1   2   3
    # v_elec = [ E, E, E, E ]
    for i in v_elec:
        # i = E, E, E
        if i.provincia <= 14:
            pickle.dump(i, m)
            m.flush()          # no es necesaria
            cont += 1

    if cont > 0:
        print("Que se grabo en el archivo", fd, "untotal de", cont, "elecciones.")
    else:
        print("Se grabaron 0 eleciones en el archivo.")

    m.close()           # SI ES NECESARIO


    # for i in range(len(v_elec)):
    # 0 1 2 3
    #    if v_elec[i].provincia >= 14:
    #        pickle.dump(v_elec[i], m)


#       ========================        Opcion 5    ============================
def mostrar_archivo(fd):

    if os.path.exists(fd):
        m = open(fd, "rb")
        tam = os.path.getsize(fd)   # 70

        # listas = 0 1 2
        # archivos = [ E    E       E]
        #             0   20    45    70

        # Prom = sumatoria / cantidad
        acum, cont = 0, 0
        while m.tell() < tam:
            elec = pickle.load(m)
            print(elec)
            if elec.provincia > 7:
                acum += elec.votos
                cont += 1

        if cont > 0:
            prom = acum / cont
            print("Los votos promedio de las provincias mayores a 7 fueron tal:", prom)

        m.close()

    else:
        print("El archivo no existe ingrese por laopcion 4 primero.")


#       ========================        Opcion 6    ============================
def busqueda_binaria(v_elec, c_busca):
    izq, der = 0, len(v_elec) - 1           # E1.provincia: 6       # elec.provincia = 5

    while izq <= der:
        c = (izq + der) // 2
        if v_elec[c].provincia == c_busca:
            return c        #   0   1       2       3       ...
        elif v_elec[c].provincia > c_busca:          # si se come al vector es de menor a mayor
            der = c - 1                                     # si se come al objeto es de mayor a menor
        else:
            izq = c + 1
    return -1


def busqueda_secuencial(v_elec, cand):
    se_encontro = False
    cont = 0
    for i in range(len(v_elec)):
        if v_elec[i].candidato == cand:
            print(v_elec[i])
            se_encontro = True
            cont += 1

    if cont > 0:
        print("Se mostrar la cantidad de:", cont)

    if not se_encontro:
        print("No se encontro ningun candidato con ese numero.")




def menu():
    print("=" * 50)
    print(" 1 - Cargar Arreglo."
          "\n 2 - Mostrar datos"
          "\n 3 - Matriz."
          "\n 4 - Generar archivo."
          "\n 5 - Mostrar archivo."
          "\n - ")
    return int(input("INgresar opcion: "))


def main():

    # vector principal
    v_elec = []

    # file/archivo
    fd = "eleciones.dat"

    # validar si pasamos por la opcion 1
    validar_op1 = False

    op = -1
    while op != 0:

        op = menu()

        if not validar_op1:     # si validar_op es igual False
            if op == 1:
                n = validar_n()
                cargar_arreglo(v_elec, n)
                validar_op1 = True
            else:
                print("Primero debe ingresar por la opcion 1.")

        else:               # cuando sea True
            if op == 1:
                n = validar_n()
                cargar_arreglo(v_elec, n)

            elif op == 2:
                mostrar_datos(v_elec)

            elif op == 3:
                generar_matriz(v_elec)

            elif op == 4:

                generar_archivo(v_elec, fd)

            elif op == 5:
                mostrar_archivo(fd)

            elif op == 6:
                c = int(input("Ingresar provincia a buscar : "))
                pos = busqueda_binaria(v_elec, c)

                if pos >= 0:
                    print(v_elec[pos])

                    # modificar los votos obtenidos por un valor x ingresado por teclado:
                    x = int(input("Ingrese nueva cantidad de votos: "))
                    v_elec[pos].votos = x

                    # aumentarle un 10% de votos
                    # v_elec[pos].votos = v_elec[pos].votos + v_elec[pos].votos * 0.1

                    # print(v_elec[pos].votos, v_elec[pos].provincia
                    print(v_elec[pos])

                else:
                    print("No se encontro la provincia buscada")

            elif op == 7:
                cand = int(input("Ingrese candidato a buscar: "))
                busqueda_secuencial(v_elec, cand)




if __name__ == '__main__':
    main()
