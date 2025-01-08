import os.path
import pickle
import random


class Mascota:

    # tipo ( 11, 13 ) 11:Perro, 12:Gato, 13:Conejo                        ; edad (1, 5)
    def __init__(self, nombre, tipo, edad, importe):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.importe = importe

    def __str__(self):

        # tipo(11,13)
        # tipo         11-11   12-11      13-11
        # indices       0       1           2
        desc_tipo = ("Perro", "Gato", "Conejo")

        cad = "Nombre: " + self.nombre
        cad += " | Tipo: " + desc_tipo[self.tipo-11]
        cad += " | Edad: " + str(self.edad)
        cad += " | Importe: " + str(self.importe)

        # desc_curso = ("1K1", 1k2
        # cad += " | Curso: " + "1K" + str(self.curso)

        return cad


# ================= Opcion 1 ==========================
def validar_n():
    n = int(input("Ingresar cantidad de Mascotas a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de Mascotas a cargar(Debe ser positivo): "))
    return n


def cargar_arreglo(v_masc, n):
    nombres = "ABCDEF"
    for i in range(n):      # n = 3             0           1
        nombre = random.choice(nombres)
        tipo = random.randint(11, 13)
        edad = random.randint(1, 5)
        importe = round(random.uniform(0.1, 10), 2)

        mascotita = Mascota(nombre, tipo, edad, importe)
        add_in_order(v_masc, mascotita)


def add_in_order(v_masc, mascotita):      # primera vuelta  len(v_masc) = 0   mascotita.nombre = "C"
    izq, der = 0, len(v_masc) - 1           # segunda vuelta  len(v_masc) = 1  mascotita.nombre = "A"

    while izq <= der:
        c = (izq + der) // 2
        if v_masc[c].nombre == mascotita.nombre:
            pos = c
            break
        elif v_masc[c].nombre > mascotita.nombre:       # si se come al vector esta de menor a mayor
            der = c - 1                                 # si se come al objeto esta de mayor a menor
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    #            0      1
    # v_caso = [ M2,    M1 ]
    v_masc[pos:pos] = [mascotita]


# ================= Opcion 2 ==========================
def mostrar_datos(v_masc):
    # indices    0      1       2       3
    # v_masc = [ M1,    M2,     M3,     M4
    for i in v_masc:
        # i = M1,       M2          ,M3
        print(i)


# ================= Opcion 3 ==========================
def generar_matriz(v_masc):
    # generar la matriz en 0
    filas = 3       # tipo ( 11, 13 )
    columnas = 5    # edad (1, 5)
    matriz = [[0] * columnas for i in range(filas)]

    # [ [1, 0, 0, 0, 0],
    #   [0, 2, 0, 0, 0],
    #   [0, 0, 1, 0, 0] ]

    # rellenamos la matriz
    for i in v_masc:
        # i = M1
        matriz[i.tipo-11][i.edad-1] += 1
        # si te pidieran el total de precios acumulado:
        # matriz[i.tipo][i.edad] += i.importe

    # mostrar la matriz
    desc_tipo = ("Perro", "Gato", "Conejo")
    for f in range(len(matriz)):    # f = 0, 1, 2
        for c in range(len(matriz[0])):     # c = 0, 1, 2, 3, 4
            if matriz[f][c] > 0 and (f+11 == 11 or f+11 == 12):
                print("La cantidad por tipo:", desc_tipo[f], "y por edad:", c+1)
                print("La cantidad total es:", matriz[f][c])


# ================= Opcion 4 ==========================
def cargar_archivo(fd, v_masc, x):
    m = open(fd, "wb")      # write binary      # modo escritura
    cont = 0
    for i in v_masc:
        if i.edad > x and (i.tipo == 11 or i.tipo == 12):
            pickle.dump(i, m)
            m.flush()       # no es necesaria
            cont += 1

    print("LA cantidad de mascotas que se cargaron en el arreglo:", cont)
    m.close()       # SI ES NECESARIO


# ================= Opcion 5 ==========================
def mostrar_archivo(fd):
    if os.path.exists(fd):
        m = open(fd, "rb")      # read binary           modo solo lectura
        tam = os.path.getsize(fd)       # el tamaño del archivo: 186

        # vector = [ M1 , M2 ]
        # fd = [ M1         M2    ]
        #      0      93          186
        cont = 0
        acum = 0

        while m.tell() < tam:
            masc = pickle.load(m)
            print(masc)

            if masc.edad >= 3:
                cont += 1
                acum += masc.importe

        if cont > 0:
            prom = acum / cont
            print("El promedio de las mascotas que superan o igual una edad de 3 es:", prom)
        m.close()

    else:
        print("El archivo:", fd, "No existe. por favor ingrese primero por la opcion 4")


# ================= Opcion 6 ==========================
def busqueda_binaria(v_masc, nom):
    izq, der = 0, len(v_masc) - 1
    # v_masc = [  MA    MB      MC      MD      ME ]
    #                           c
    while izq <= der:
        c = (izq + der) // 2
        if v_masc[c].nombre == nom:
            return c    # c = 0 1 2 ...
        elif v_masc[c].nombre > nom:
            der = c - 1
        else:
            izq = c + 1
    return -1


def busqueda_secuencial(v_masc, tip):
    se_encontro = False
    for i in range(len(v_masc)):
        if v_masc[i].tipo == tip:
            print("Edad:", v_masc[i].edad, "Precio:", v_masc[i].importe)
            se_encontro = True

    if not se_encontro:     # si se encontro esta en falso
        print("No se encontro el tipo buscado.")



def buusqueda_secuencial(vector, num):
    for i in range(len(vector)):
        if vector[i].numero == num:
            return i
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

    # vector principal
    v_masc = []         # list()


    # nombre del archivo binario
    fd = "mascotas.dat"


    # validar la opcion 1
    validar_op1 = False


    op = -1
    while op != 0:

        op = menu()


        if not validar_op1:     # si esta validar_op1 en false
            if op == 1:
                n = validar_n()
                cargar_arreglo(v_masc, n)
                validar_op1 = True
            else:
                print("Primero debe ingresar por la opcion 1.")

        else:                   # si esta validar_op1 en true

            if op == 1:
                n = validar_n()
                cargar_arreglo(v_masc, n)

            elif op == 2:
                mostrar_datos(v_masc)

            elif op == 3:
                generar_matriz(v_masc)

            elif op == 4:
                x = int(input("Edad a superar para guardar en el archivo: "))
                cargar_archivo(fd, v_masc, x)

            elif op == 5:
                mostrar_archivo(fd)

            elif op == 6:
                nom = input("Ingrese nombre a buscar: ")
                pos = busqueda_binaria(v_masc, nom)

                if pos >= 0:
                    # mostrar sus datos
                    print(v_masc[pos])

                    # modifcar su precio con uun aumento del 10%
                    v_masc[pos].importe = v_masc[pos].importe + v_masc[pos].importe * 0.1
                    # x = float(input("ingresar nuevo precio: "))
                    # v_masc[pos].importe = x

                    # datos actualizados
                    print(v_masc[pos])

                else:
                    print("No se encontro el nombre buscado.")


            elif op == 7:
                tip = int(input("Ingrese tipo a buscar(11,13): "))
                busqueda_secuencial(v_masc, tip)



if __name__ == '__main__':
    main()
