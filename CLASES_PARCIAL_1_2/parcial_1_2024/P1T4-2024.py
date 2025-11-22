import random

# Parcial 1 - Tema 4 - 2024
# iniciar el generador de valores aleatorios con un valor fijo...
random.seed(1475)

# cantidad fija de números a procesar...
# n = 50
n = 17000

# variable para contener al mayor pedido...
may = None

# inicialización de contadores, acumuladores y otras variables necesarias...
c1, c2, c3, a, c, ci = 0, 0, 0, 0, 0, 0

# acumulador de TODOS los números generados, como elemento de control...
st = 0

# ciclo de procesamiento para los n números...
print('Procesamiento de una sucesión de', n, 'números enteros aleatorios...')
for i in range(1, n + 1):
    # generar un número aleatorio en el rango pedido...
    num = random.randint(-100, 15000)
    st += num

    # 1. contar/sumar cada número en los intervalos pedidos...
    if num < 0:
        c1 += num
    elif 0 <= num < 10000 and num % 4 == 0:
        c2 += 1
    elif num >= 10000:
        c3 += 1

    # 2. sumar y contar los números para el promedio pedido...
    if 0 < num <= 8000 and num % 6 == 0:
        a += num
        c += 1

    # 3. determinar el mayor entre los números pedidos...
    if num > 5000 and num % 5 == 0:
        if may is None:
            may = num
        elif num > may:
            may = num

    # 4. contar los pares para el porcentaje pedido...
    if num % 2 == 0:
        ci += 1

# Mostrar la suma de todos los números, para controlar validez del conjunto generado...
print('Control de validez de los números generados - La suma de todos ellos es:', st)
print()

print('Punto 1...')
print('\tSuma de los números negativos:', c1)
print('\tCantidad de números en [0, 10000) divisibles por 4:', c2)
print('\tCantidad de números mayores o iguales que 10000:', c3)
print()

print('Punto 2...')
prom = 0
if c != 0:
    prom = a // c
print('\tPromedio entero de los números en (0, 8000] y divisibles por 6:', prom)
print()

print('Punto 3...')
print('\tEl mayor de todos los números generados que sean mayores que 5000 y divisibles por 5:', may)
print()

print('Punto 4...')
porc = ci * 100 // n
print('\tPorcentaje (entero) que los números pares generados representan en el total:', porc, '\b%')
print()
