import random
random.seed(1157)

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

n = 17000
for i in range(n):

    num = random.randint(1000, 37000)

    # =========================================================================
    #                           PUNTO 1
    # =========================================================================
    ''' Determinar cuántos de esos números eran mayores o iguales a 1000 pero menores que 15000 '''
    # if num >= 1000 and num < 15000:   | Expresarlo de esta forma tambien es correcto
    if 1000 <= num < 15000:
        cont_a_p1 += 1

    ''' cuál es la suma de los que eran mayores o iguales que 15000 y menores que 30000 '''
    # elif num >= 15000 and num < 30000: | Expresarlo de esta forma tambien es correcto
    if 15000 <= num < 30000:
        acum_b_p1 += num

    ''' y cuántos eran mayores o iguales que 30000. '''
    if num >= 30000:
        cont_c_p1 += 1

    # =========================================================================
    #                           PUNTO 2
    # =========================================================================
    ''' Determinar el promedio entero de los números generados que eran divisibles por 7 pero no por 3. '''
    if num % 7 == 0 and num % 3 != 0:
        cont_p2 += 1
        acum_p2 += num

    # =========================================================================
    #                           PUNTO 3
    # =========================================================================
    ''' Determinar el menor entre todos los números generados que sean impares. '''
    if num % 2 != 0:
        if menor is None or num < menor:
            menor = num

    # =========================================================================
    #                           PUNTO 4
    # =========================================================================
    ''' Determinar el porcentaje entero que representa la cantidad de números pares generados sobre la cantidad
    total de números procesados. '''
    if num % 2 == 0:
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
