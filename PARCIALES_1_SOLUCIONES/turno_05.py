import random
random.seed(2753)

# Variables Punto 1
cont_a_p1 = 0
acum_b_p1 = 0
cont_c_p1 = 0

# Variables Punto 2
cont_p2 = 0
acum_p2 = 0

# Variables Punto 3
menor = None

# Variables Punto 4
cont_p4 = 0

n = 30000
for i in range(n):

    num = random.randint(-15000, 15000)

    # =========================================================================
    #                           PUNTO 1
    # =========================================================================
    ''' Determinar la cantidad de números que eran negativos; '''
    if num < 0:
        cont_a_p1 += 1

    ''' también determinar la suma de todos los
    números que eran mayores o iguales a cero pero menores que 5000 '''
    # elif num >= 0 and num < 5000: | Expresarlo de esta forma tambien es correcto
    if 0 <= num < 5000:
        acum_b_p1 += num

    '''  y la cantidad de números eran
    mayores o iguales que 5000 pero además eran impares. '''
    if num >= 5000 and num % 2 != 0:
        cont_c_p1 += 1

    # =========================================================================
    #                           PUNTO 2
    # =========================================================================
    ''' Determinar el promedio entero de todos los números generados que sean negativos pero que además sean
    divisibles por 3 y por 5 '''
    if num < 0 and num % 3 == 0 and num % 5 == 0:
        cont_p2 += 1
        acum_p2 += num

    # =========================================================================
    #                           PUNTO 3
    # =========================================================================
    ''' Determinar el menor entre todos los números generados que sean mayores a cero y divisibles por 3 pero
    no divisibles por 4.'''
    if num > 0 and num % 3 == 0 and num % 4 != 0:
        if menor is None or num < menor:
            menor = num

    # =========================================================================
    #                           PUNTO 4
    # =========================================================================
    ''' Determinar el porcentaje entero que la cantidad de números negativos impares representa sobre la
    cantidad total de números. '''
    if num % 2 != 0 and num < 0:
        cont_p4 += 1


# =========================================================================
#                           RESULTADOS
# =========================================================================

# Punto 1
print("La cantidad del contador del punto 1a:", cont_a_p1)
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