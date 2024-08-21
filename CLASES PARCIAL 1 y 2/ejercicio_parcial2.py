import random
random.seed(7658)

# random.seed(23)


n = 25000

# acumuladores
acum_total = 0

# contadores puntos 1
cont_menor_500 = 0
cont_mayor_500 = 0
cont_mayor_27k = 0

# cosas puntos 2
acum_punto2 = 0
cont_punto2 = 0


# cosas punto 3
mayor = None

# cosas punto 4
cont_punto4 = 0


menor = None


for i in range(n):
    num = random.randint(-2500, 45000)
    # num = random.randint(1, 10)
    # print("El valor de num:", num)

    # ====================================================================
    #                       Ejercicio Punto 1
    # ====================================================================
    if num <= -500:
        cont_menor_500 += 1

    elif -500 < num < 27000:
        cont_mayor_500 += 1

    # 10 / 5 = 2 + 0 , el 0 = resto
    # 9 / 2 = 4 + 1 , el 1 = resto
    # 8 / 2 = 4 + 0 , el 0 = resto
    # 100 / 10 = 10 + 0
    # 101 / 10 = 10 + 1
    elif num >= 27000 and num % 10 == 0:
        cont_mayor_27k += 1

    # ====================================================================
    #                       Ejercicio Punto 2
    # ====================================================================
    # que es un promedio
    # prom = la sumatoria de cosas / cantidad de cosas que sumamos
    # prom = (nota1 + nota2 + nota3) / cant_notas_sumadas
    '''
    Determinar el promedio entero entre los números mayores a 0 y divisibles por 7 o por 8.
    '''
    if num > 0 and (num % 7 == 0 or num % 8 == 0):
        acum_punto2 += num
        cont_punto2 += 1

    # ====================================================================
    #                       Ejercicio Punto 3
    # ====================================================================
    '''
    Determinar el mayor entre todos los números generados que sean negativos divisibles por 4.
    '''
    # num = -16 ; mayor = -16
    # num = -8 ; mayor -8
    # -16  -8  -4  0
    # if num < 0 and num % 4 == 0 and (mayor is None or num > mayor):
    if num < 0 and num % 4 == 0:
        if mayor is None or num > mayor:
            mayor = num

    # ====================================================================
    #                       Ejercicio Punto 4
    # ====================================================================
    '''
    Determinar el porcentaje entero que la cantidad de números menores que 5000 representa sobre la
    cantidad total de números
    '''
    if num < 5000:
        cont_punto4 += 1

    # ====================================================================
    #                     Ejercicio Punto 3 / Parcial 03
    # ====================================================================
    '''
    menor = None 
    
    Determinar el menor entre todos los números generados que no sean negativos y además sean divisibles
    por 9
    '''
    if num >= 0 and num % 9 == 0:
        if menor is None or num < menor:
            menor = num


    '''
    acum_prom = 0
    cont_prom = 0
    Determinar el promedio entero de todos los números generados que estén entre -200 y 3000 (incluídos
    ambos).
    '''
    # if num >= -200 and num <= 3000:
    if -200 <= num <= 3000:
        # acum_prom = 0
        # cont_prom = 0
        pass


    '''
    acum_prom = 0
    cont_prom = 0
    Determinar el promedio entero de todos los números generados que sean negativos pero que además sean
    divisibles por 3 y por 5.
    '''
    if num < 0 and num % 3 == 0 and num % 5 == 0:
        # acum_prom = 0
        # cont_prom = 0
        pass

    '''
    menor = None
    Determinar el menor entre todos los números generados que sean mayores a cero y divisibles por 3 pero
    no divisibles por 4.
    '''
    # 8 / 4 = 2 + 0             10 / 4 = 2 * 4 + 2
    if num > 0 and num % 3 == 0 and num % 4 != 0:
        if menor is None or num < menor:
            # menor = num
            pass

    '''
    # acum_pares = 0    
    # acum divisibles por 5 = 0
    # cont_mayores -2000 = 0
    
    Determinar la suma de todos los números que eran pares; la suma de todos los que eran divisibles por 5, y
    la cantidad de números que eran mayores o iguales que -2000 pero además no eran divisibles por 4.
    '''
    # num = 10
    if num % 2 == 0:
        # acum_pares += num
        pass

    if num % 5 == 0:
        # acum divisibles por 5 += num
        pass


    acum_total += num



# Resultados
# Punto 1               # ctrl + d
print()
print("Cantidad Numeros menores a -500:", cont_menor_500)
print("Cantidad Numeros mayores a -500 y menor 27k:", cont_mayor_500)
print("Cantidad Numeros mayores a 27k:", cont_mayor_27k)
print()
print()

# punto 2
# el promedio entero o truncado
if cont_punto2 > 0:
    prom = acum_punto2 // cont_punto2
    print("El promedio del punto2:", prom)
print()
print()

# Punto 3
print("El numero mayor es igual:", mayor)
print()
print()

# Punto 4
# Como calcular un porcentaje con regla de 3
# n = cantidad total de numeros
# cont_punto 4 = cantidad que cumple la condicion menor qe 5k

# n          ---> 100%
# cont_punto ---> x = cont_punto4 * 100 / n
porc = (cont_punto4 * 100) // n
print("El porcentaje es:", porc)
print()
print()

# print("El acumulado total es:", acum_total)
