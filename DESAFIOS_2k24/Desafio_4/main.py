

import math


class Point:
    def __init__(self, eje_x, eje_y):
        self.eje_x = eje_x
        self.eje_y = eje_y


def calcular_distancia(p1, p2):
    # Calcula la distancia en cada eje
    delta_x = p2.eje_x - p1.eje_x
    delta_y = p2.eje_y - p1.eje_y

    # Aplica el Teorema de Pitágoras
    distancia = math.sqrt(delta_x ** 2 + delta_y ** 2)
    return distancia


def main():

    fd = "puntos.csv"
    # fd = "prueba.csv"
    m = open(fd, "r")
    v_puntos = []

    for linea in m:

        data = linea.strip().split(",")
        # data = ["9034", "16923"]
        eje_x = int(data[0])
        eje_y = int(data[1])
        punto = Point(eje_x, eje_y)

        v_puntos.append(punto)
        # v_puntos = [ P1, P2, P3 ]

    m.close()

    #
    # Calculemos distancia minima y maxima
    dmax = 0

    dmin = calcular_distancia(v_puntos[0], v_puntos[1])

    n = len(v_puntos)
    for i in range(0, n-1):
        for j in range(i+1, n):

            distancia = calcular_distancia(v_puntos[i], v_puntos[j])

            if distancia < dmin:
                dmin = distancia

            elif distancia > dmax:
                dmax = distancia


    # Mostrar resultados
    print("La distancia minima es:", round(dmin))
    print("La distancia maxima es:", round(dmax))

    # Para i en el rango(0, n-1):
    # Para j en el rango(i+1, n):
    # 1.1) Sea d = distancia entre puntos[i] y puntos[j]
    # 1.2) Si d < dmin:
    # 1.2.1) dmin = d
    # 1.3) Si d > dmax:
    # 1.3.1) dmax = d


if __name__ == '__main__':
    main()






