import random
random.seed(7658)

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

n = 25000
for i in range(n):

    num = random.randint(-2500, 45000)

    # =========================================================================
    #                           PUNTO 1
    # =========================================================================
    ''' Determinar cuántos eran menores o iguales que -500'''
    if num <= -500:
        cont_a_p1 += 1

    ''' cuántos eran mayores que -500 y menores que 27000 '''
    # elif num >= -500 and num < 27000: | Expresarlo de esta forma tambien es correcto
    if -500 < num < 27000:
        cont_b_p1 += 1

    ''' , y cuántos eran mayores o iguales que 27000 pero además eran divisibles por 10. '''
    if num >= 27000 and num % 10 == 0:
        cont_c_p1 += 1

    # =========================================================================
    #                           PUNTO 2
    # =========================================================================
    ''' Determinar el promedio entero entre los números mayores a 0 y divisibles por 7 o por 8 '''
    # ojo en este los parentesis van si o si sino toma mal las condiciones
    if num > 0 and (num % 7 == 0 or num % 8 == 0):
        cont_p2 += 1
        acum_p2 += num

    # =========================================================================
    #                           PUNTO 3
    # =========================================================================
    ''' Determinar el mayor entre todos los números generados que sean negativos divisibles por 4 '''
    if num < 0 and num % 4 == 0:
        if mayor is None or num < mayor:
            mayor = num

    # =========================================================================
    #                           PUNTO 4
    # =========================================================================
    ''' Determinar el porcentaje entero que la cantidad de números menores que 5000 representa sobre la
    cantidad total de números.'''
    if num < 5000:
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