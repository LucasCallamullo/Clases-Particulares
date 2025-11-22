# Desarrolle un programa completo en Python que permita generar una sucesión de 14000
# númerosenteros aleatorios, usando como semilla del generador al valor 973 (es decir,
# random.seed(973)). Los valores decada uno de esos 14000 números deben estar entre
# 100 y 21100 (incluidos ambos -DEBE usar random.randint(100, 21100) para generar cada
# uno de estos números).

import random
random.seed(973)

cont_11= 0
cont_12 = 0
cont_13 = 0

cont_22 = 0
acum_22 = 0


cont_33 = 0

may = None
for i in range(14000):
    num = random.randint(100, 21100)


    #1. Determinar cuántos eran menores o iguales que 11000,
    # cuántos eran mayores que 11000 pero menores que 17000 y además eran divisibles por 3 y por 8
    # y cuántos eran mayores o iguales que 17000.
    if num <= 11000:
        cont_11 += 1
    if num >= 11000 and num < 17000 and num % 3 == 0 and num % 8 == 0:
        cont_12 += 1
    if num >= 17000:
        cont_13 += 1


    #2. Determinar el promedio entero de todos los números generados que sean divisibles por 9
    # pero que seantambién menores o iguales a 15000.
    # Aclaración: NO se pide el promedio redondeado, sino el promedio truncado, sin decimales.

    if num % 9 == 0 and num <= 15000:
        cont_22 +=1
        acum_22 = num

    #3. Determinar el mayor entre todos los números generados cuyo valor esté entre 1000 y 14000
    # (includos ambos).
    if num <= 1000 and num <= 14000:

        if may is None or num > may:
            may = num


    #4. Determinar el porcentaje entero que la cantidad de números divisibles por 6
    # representa sobre la cantidad total de números. Aclaración: NO se pide el porcentaje redondeado,
    # sino truncado, sin decimales.
    # Observación: en el cálculo de este porcentaje, haga primero la multiplicación que corresponda,
    # y luego la división.
    if num % 6 == 0:
        cont_33 += 1

# PUNTO 1
print("Numeros menores o iguales que 11000: ", cont_11)
print("Numeros mayores, menores y divisibles: ", cont_12)
print("Numeros mayores o iguales que 17000: ", cont_13)

# PUNTO 2
prom = acum_22 // cont_22
print("El promedio entre los numeros pedidos; ", prom)


# PUNTO 3
print("El numero mayor es: ", may)

# PUNTO 4
porc = (cont_33 * 100) // 14000
print("El procentaje es: ", porc)