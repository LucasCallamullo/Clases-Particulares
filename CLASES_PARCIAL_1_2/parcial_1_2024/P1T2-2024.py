import random

# Parcial 1 - Tema 2 - 2024
# iniciar el generador de valores aleatorios con un valor fijo...
random.seed(7633)

# cantidad fija de números a procesar...
n = 18000

# variable para contener al mayor pedido...
men = None

# inicialización de contadores, acumuladores y otras variables necesarias...
tn, c1, c2, c3, cpr, apr, cd8 = 0, 0, 0, 0, 0, 0, 0

# acumulador de TODOS los números generados, como elemento de control...
st = 0

# ciclo de procesamiento para los n números...
print('Procesamiento de una sucesión de', n, 'números enteros aleatorios...')
for i in range(1, n + 1):
    # generar un número aleatorio en el rango pedido...
    num = random.randint(500, 13500)
    st += num

    # 4. cantidad total de números para el porcentaje pedido...
    # uso un contador solo para controlar si realmente se hicieron n vueltas...
    tn += 1

    # 1. contar cada número en los intervalos pedidos...
    if num <= 4000:
        c1 += 1
    elif 4000 < num < 10000:
        if num % 4 == 0:
            c2 += 1
    else:
        c3 += 1

    # 2. contar y acumular los pares divisibles por 6 para el promedio pedido...
    if num % 2 == 0 and num % 6 == 0:
        cpr += 1
        apr += num

    # 3. determinar el menor entre los menores o iguales a 12000...
    if num <= 12000:
        if men is None:
            men = num
        elif num < men:
            men = num

    # 4. cantidad de números divisibles por 8, para el porcentaje pedido...
    if num % 8 == 0:
        cd8 += 1

# Mostrar la suma de todos los números, para controlar validez del conjunto generado...
print('Control de validez de los números generados - La suma de todos ellos es:', st)
print()

# calcular y mostrar resultados finales y terminar...
print('Cantidad de números procesados (para verificar...):', tn)
print()

print('Punto 1...')
print('\tCantidad de números menores o iguales a 4000:', c1)
print('\tCantidad de números en (4000, 10000) y divisibles por 4:', c2)
print('\tCantidad de números mayores o iguales a 10000:', c3)
print()

print('Punto 2...')
prom = 0
if cpr != 0:
    prom = apr // cpr
print('\tPromedio (entero) de los números pares divisibles por 6:', prom)
print()

print('Punto 3...')
print('\tEl menor de todos los números menores o iguales que 12000 es:', men)
print()

print('Punto 4...')
porc = cd8 * 100 // n
print('\tPorcentaje (entero) que los divisibles por 8 representan en el total:', porc, '\b%')
print()
