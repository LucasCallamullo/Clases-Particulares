import pickle
import os.path


# ====================================================================
#                       Punto 6
# ====================================================================
def mostrar_archivo_binario(fd):
    if os.path.exists(fd):  # no dice si existe o no el archivo, True existe, False no existe
        file = open(fd, "rb")  # read binary
        size = os.path.getsize(fd)  # nos devuelve el valor en bytes del archivo

        """ 
        Muestre al final una línea extra con el monto total promedio entre todos los registros mostrados"""
        cont = 0
        acum = 0

        # lista = [ 15, 25, 45]
        # file [             ] 236
        #      0    115      236
        while file.tell() < size:
            beca = pickle.load(file)  # nos recupera al objeto almacenado

            if beca.carrera != 1:
                print(beca)
                cont += 1
                acum += beca.monto

        promedio = acum / cont
        print("El promedio de los montos de los valores mostrados:", round(promedio, 2))

    else:
        print("El archivo binario todavía no fue creado: ", fd)



# ====================================================================
#                       Punto 5
# ====================================================================
def generar_archivo_binario(vec, fd, m):

    # mostrar al final la cantidad de becas guardas
    cont = 0

    file = open(fd, "wb")   # write binary:   escribir en un archivo binario, recorda que sobreescribe
    # append binary:  agregar al final del archivo, mantiene el contenido

    for i in vec:
        # vec = [BECA1, BECA2, BECA3 ...
        # i = BECA1, Beca2,

        if i.monto > m:
            pickle.dump(i, file)
            file.flush()        # guardar de mejor forma el objeto de forma binaria
            cont += 1

    print("La cantidad de becas cargadas es:", cont)

    file.close()           # SI O SI


# ====================================================================
#                       Punto 3
# ====================================================================
def busqueda_secuencial(vec, d):
    #           0   1   2
    # lista = [15, 25, 35
    pos = -1

    for i in range(len(vec)):   #
        # i = 0, 1, 2

        if vec[i].dni == d:
            pos = i
            break

    return pos


# ====================================================================
#                       Punto 4
# ====================================================================
def generar_matriz(vec, t):
    # generar la matriz en 0
    filas = 5  # carrera(1, 5)
    columnas = 10  # tipo(1, 10)
    matriz = [[0] * columnas for i in range(filas)]

    # matriz =  [[0, 0, 0, 0, 0, 0, 0, 0, 0],           # matriz[][]
    #            [0, 0, 0, 0, 1, 0, 1, 0, 0],
    #            [0, 0, 0, 0, 0, 1, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0] ]

    # completar la matriz
    for i in vec:
        # vec = [BECA1, BECA2, BECA3, ... ]
        # i = BECA1, BECA2, BECA3
        matriz[i.carrera - 1][i.tipo - 1] += 1
        # matriz[i.carrera][i.tipo] += i.monto

    # mostrar la matriz
    for f in range(len(matriz)):  # f = carreras
        # f = 0, 1, 2, 3, 4

        for c in range(len(matriz[0])):  # c = tipo
            # c = 0, 1, 2, ..., 9

            # if matriz[f][c] > t:
            # que sean del tipo mayor a 5
            if matriz[f][c] > t and c+1 > 5:
                print("En la carrera:", f + 1, "y del tipo:", c + 1)
                print("El contador es:", matriz[f][c])