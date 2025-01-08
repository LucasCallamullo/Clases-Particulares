import math


def calcular_distancia(p1, p2):
    # Calcula la distancia en cada eje
    delta_x = p2.eje_x - p1.eje_x
    delta_y = p2.eje_y - p1.eje_y

    # Aplica el Teorema de Pitágoras
    distancia = math.sqrt(delta_x ** 2 + delta_y ** 2)
    return distancia
