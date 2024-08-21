import random
random.seed(973)

# Variables Punto 1
cont_a_p1 = 0
cont_b_p1 = 0
cont_c_p1 = 0

# Variables Punto 2
cont_p2 = 0
acum_p2 = 0

# Variables Punto 3
mayor = None

# Variables Punto 4
cont_p4 = 0

n = 14000
for i in range(n):

    num = random.randint(100, 21100)

    # =========================================================================
    #                           PUNTO 1
    # =========================================================================
    ''' Determinar cuántos eran menores o iguales que 11000 '''
    if num <= 11000:
        cont_a_p1 += 1

    ''' cuántos eran mayores que 11000 pero menores que 17000 y además eran divisibles por 3 y por 8 al mismo tiempo '''
    # elif num >= 11000 and num < 17000: | Expresarlo de esta forma tambien es correcto
    if 11000 <= num < 17000 and num % 3 == 0 and num % 8 == 3:
        cont_b_p1 += 1

    ''' y cuántos eran mayores o iguales que 17000. '''
    if num >= 17000:
        cont_c_p1 += 1

    # =========================================================================
    #                           PUNTO 2
    # =========================================================================
    ''' Determinar el promedio entero de todos los números generados que sean divisibles por 9 pero que sean
    también menores o iguales a 15000. '''
    if num % 9 == 0 and num <= 15000:
        cont_p2 += 1
        acum_p2 += num

    # =========================================================================
    #                           PUNTO 3
    # =========================================================================
    ''' Determinar el mayor entre todos los números generados cuyo valor esté entre 1000 y 14000 
    (includos ambos). '''
    if 1000 <= num <= 14000:
        if mayor is None or num < mayor:
            mayor = num

    # =========================================================================
    #                           PUNTO 4
    # =========================================================================
    ''' Determinar el porcentaje entero que la cantidad de números divisibles por 6 representa sobre la cantidad
    total de números.'''
    if num % 6 == 0:
        cont_p4 += 1


# =========================================================================
#                           RESULTADOS
# =========================================================================

# Punto 1
print("La cantidad del contador del punto 1a:", cont_a_p1)
print("La cantidad del contador del punto 1b:", cont_b_p1)
print("La cantidad del contador del punto 1c:", cont_c_p1)

# Punto 2
prom = acum_p2 // cont_p2
print("El promedio es: ", prom)

# Punto 3
print("El numero mayor de la serie es:", mayor)

# Punto 4
porc = cont_p4 * 100 // n
print("El porcentaje que representa el punto4:", porc)