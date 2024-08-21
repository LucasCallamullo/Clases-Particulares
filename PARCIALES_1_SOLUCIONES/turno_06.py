import random
random.seed(1779)

# Variables Punto 1
acum_a_p1 = 0
acum_b_p1 = 0
cont_c_p1 = 0

# Variables Punto 2
cont_p2 = 0
acum_p2 = 0

# Variables Punto 3
menor = None

# Variables Punto 4
cont_p4 = 0

n = 13000
for i in range(n):

    num = random.randint(-25000, -1000)

    # =========================================================================
    #                           PUNTO 1
    # =========================================================================
    ''' Determinar la suma de todos los números que eran pares; '''
    if num % 2 == 0:
        acum_a_p1 += num

    ''' ; la suma de todos los que eran divisibles por 5'''
    if num % 5 == 0:
        acum_b_p1 += num

    ''' ,y la cantidad de números que eran mayores o iguales que -2000 pero además no eran divisibles por 4.'''
    if num >= -2000 and num % 4 != 0:
        cont_c_p1 += 1

    # =========================================================================
    #                           PUNTO 2
    # =========================================================================
    ''' Determinar el promedio entero de todos los números generados que eran mayores que -6000 pero
    menores que -2000 y que además no sean divisibles por 6.'''
    if -6000 < num < -2000 and num % 6 != 0:
        cont_p2 += 1
        acum_p2 += num

    # =========================================================================
    #                           PUNTO 3
    # =========================================================================
    ''' Determinar el menor entre todos los números generados que estén comprendidos entre -20000 y -5000
    (incluidos ambos) y que sean también divisibles por 8.'''
    if -20000 < num < -5000 and num % 8 == 0:
        if menor is None or num < menor:
            menor = num

    # =========================================================================
    #                           PUNTO 4
    # =========================================================================
    ''' Determinar el porcentaje entero que la cantidad de números mayores que -3000 pero que sean divisibles
    por 3 representa sobre la cantidad total de números procesados '''
    if num > -3000 and num % 3 == 0:
        cont_p4 += 1


# =========================================================================
#                           RESULTADOS
# =========================================================================

# Punto 1
print("La cantidad del contador del punto 1a:", acum_a_p1)
print("La suma del acumulador del punto 1b:", acum_b_p1)
print("La cantidad del contador del punto 1c:", cont_c_p1)

# Punto 2
prom = acum_p2 // cont_p2
print("El promedio es: ", prom)

# Punto 3
print("El numero menor de la serie es:", menor)

# Punto 4
porc = cont_p4 * 100 // n
print("El porcentaje que representa el punto4:", porc)