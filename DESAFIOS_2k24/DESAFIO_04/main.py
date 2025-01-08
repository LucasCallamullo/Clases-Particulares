import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        cad = "Punto X: " + str(self.x)
        cad += " | Punto Y: " + str(self.y)
        return cad

    def distance_to(self, other):
        # 4xy
        # 4x + 4y
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    # def distance_to(self, other):
    #    return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5



def cargar_archivo(v_point, fd):
    m = open(fd, "rt")
    lineas = m.readlines()
    for i in lineas:
        token = i.split(",")
        punto = Point(int(token[0]), int(token[1]))
        v_point.append(punto)


def mostrar_datos(v_point):
    for i in v_point:
        print(i)


'''
def busqueda_secuncial(v):
    # lista = [1, 2, 3, 4, 5 ]
    #                0
    

    # lista = [6, 4, 3, 2, 1 ]
    #                0

    #
    izq, der = 0, len(v_caso) - 1           # segunda vuelta  len = 1  caso_temporal.id = 3

    while izq <= der:
        c = (izq + der) // 2
        if v_caso[c].id == caso_temporal.id:
            return c
        elif v_caso[c].id > caso_temporal.id:
            der = c - 1
        else:
            izq = c + 1

    return -1
'''


def main():
    v_point = []

    fd = "cortos-points.csv"
    # fd = "puntos.csv"

    cargar_archivo(v_point, fd)
    mostrar_datos(v_point)

    # Inicializar las distancias mínima y máxima
    d_min = v_point[0].distance_to(v_point[1])
    print("Distancia minima entre 0 y 1:", d_min)

    d_max = 0

    # Encontrar la distancia mínima y máxima
    n = len(v_point)
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = v_point[i].distance_to(v_point[j])
            d_min = min(d_min, d)
            d_max = max(d_max, d)

            print("Distancia mínima entre {} y {}: {}".format(i, j, d_min))
            print("Distancia Maxima entre {} y {}: {}".format(i, j, d_max))
            # print(f"Distancia mínima entre {i} y {j}: {d_min}")


    # Redondear los resultados al entero más cercano
    d_min = round(d_min)
    d_max = round(d_max)

    # Imprimir las distancias mínima y máxima como números enteros
    print("Distancia Mínima:", d_min)
    print("Distancia Máxima:", d_max)


if __name__ == '__main__':
    main()
