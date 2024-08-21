import random
random.seed(3374)

# Variables Punto 1
cont_a_p1 = 0
cont_b_p1 = 0
cont_c_p1 = 0

# Variables Punto 2
cont_p2 = 0
acum_p2 = 0

# Variables Punto 3
menor = None

# Variables Punto 4
cont_p4 = 0

n = 19000
for i in range(n):

    num = random.randint(-1000, 15000)

    # =========================================================================
    #                           PUNTO 1
    # =========================================================================
    ''' Determinar cuántos eran negativos '''
    if num < 0:
        cont_a_p1 += 1

    ''' Además, determinar cuántos eran mayores o iguales a 0 y menores
    que 12000 pero además eran divisibles por 5 '''
    # elif num >= 0 and num < 12000: | Expresarlo de esta forma tambien es correcto
    if 0 <= num < 12000 and num % 5 == 0:
        cont_b_p1 += 1

    ''' Y finalmente determinar cuánto es la suma de los que eran
    mayores o iguales a 12000 pero además eran divisibles por 3. '''
    if num >= 12000 and num % 3 == 0:
        cont_c_p1 += 1

    # =========================================================================
    #                           PUNTO 2
    # =========================================================================
    ''' Determinar el promedio entero de todos los números generados que estén entre -200 y 3000 (incluídos
    ambos). '''
    if -200 <= num <= 3000:
        cont_p2 += 1
        acum_p2 += num

    # =========================================================================
    #                           PUNTO 3
    # =========================================================================
    ''' Determinar el menor entre todos los números generados que no sean negativos y además sean divisibles
    por 9. '''
    if num >= 0 and num % 9 == 0:
        if menor is None or num < menor:
            menor = num

    # =========================================================================
    #                           PUNTO 4
    # =========================================================================
    ''' Determinar el porcentaje entero que la cantidad de números generados pares negativos representa sobre
    la cantidad total de números procesados.'''
    if num % 2 == 0 and num < 0:
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
print("El numero menor de la serie es:", menor)

# Punto 4
porc = cont_p4 * 100 // n
print("El porcentaje que representa el punto4:", porc)