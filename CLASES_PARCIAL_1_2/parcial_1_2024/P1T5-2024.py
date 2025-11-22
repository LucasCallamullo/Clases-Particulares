import random

# Parcial 1 - Tema 5 - 2024
# iniciar el generador de valores aleatorios con un valor fijo...
random.seed(8665)

# cantidad fija de números a procesar...
n = 16000

# variable para contener al menor pedido...
men = None

# inicialización de contadores, acumuladores y otras variables necesarias...
c1, c2, c3, a, c, ci = 0, 0, 0, 0, 0, 0

# acumulador de TODOS los números generados, como elemento de control...
st = 0

# ciclo de procesamiento para los n números...
print('Procesamiento de una sucesión de', n, 'números enteros aleatorios...')
for i in range(1, n + 1):
    # generar un número aleatorio en el rango pedido...
    num = random.randint(-1000, 18000)
    st += num

    # 1. contar/sumar cada número en los intervalos pedidos...
    if num <= 3000:
        c1 += 1
    elif 3000 < num < 12000:
        c2 += num
    elif num >= 12000 and num % 3 != 0 and num % 4 != 0:
        c3 += 1

    # 2. sumar y contar los números para el promedio pedido...
    if num >= 0 and num % 8 == 0:
        a += num
        c += 1

    # 3. determinar el menor entre los números pedidos...
    if 5000 <= num <= 13000 and num % 2 == 0:
        if men is None:
            men = num
        elif num < men:
            men = num

    # 4. contar los números para el porcentaje pedido...
    if num >= 0 and num % 2 == 1:
        ci += 1

# Mostrar la suma de todos los números, para controlar validez del conjunto generado...
print('Control de validez de los números generados - La suma de todos ellos es:', st)
print()

print('Punto 1...')
print('\tCantidad de números que eran menores o iguales a 3000:', c1)
print('\tSuma de los números en (3000, 12000):', c2)
print('\tCantidad de números mayores o iguales que 12000 pero no divisibles ni por 3 ni por 4:', c3)
print()

print('Punto 2...')
prom = 0
if c != 0:
    prom = a // c
print('\tPromedio entero de los números generados no negativos y divisibles por 8:', prom)
print()

print('Punto 3...')
print('\tEl menor de todos los números pares en [5000, 13000]:', men)
print()

print('Punto 4...')
porc = ci * 100 // n
print('\tPorcentaje (entero) que la cantidad de no negativos impares representan en el total:', porc, '\b%')
print()
