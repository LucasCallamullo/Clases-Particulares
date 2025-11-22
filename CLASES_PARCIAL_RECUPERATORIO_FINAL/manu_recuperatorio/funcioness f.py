
import os.path
import pickle


def generar_matriz(matriz, fd):
    bandera = os.path.exists(fd)
    if bandera is False:
        print("El archivo no existe:", fd)
        return  # cortar la funcion

    # generar matriz
    f = 5   # f = filas = delegacion(0, 4) = 4 - 0 + 1 = 5
    c = 25   # c = columnas = especialidad(0, 24) = 24 - 0 + 1 = 25
    matriz = [ [0] * c for i in range(f) ]

    # Rellenar la matriz
    m = open(fd, "rb")
    tamanio = os.path.getsize(fd)
    while m.tell() < tamanio:
        obj = pickle.load(m)        # obj = O1, O2, O3
        matriz[obj.delegacion][obj.especialidad] += 1
    m.close()

    # mostrar la matriz
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):

            # te pide solo mostrar los contadores mayores a cero
            if matriz[f][c] > 0:
                print("Delegacion:", f, "- especialidad:", c, "- cantidad:", matriz[f][c])
