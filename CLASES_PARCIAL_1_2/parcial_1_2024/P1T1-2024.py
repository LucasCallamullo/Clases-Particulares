import random

# Parcial 1 - Tema 1 - 2024
# iniciar el generador de valores aleatorios con un valor fijo...
random.seed(2759)

# cantidad fija de números a procesar...
n = 15000

# variable para contener al menor pedido...
may = None

# inicialización de contadores, acumuladores y otras variables necesarias...
r1, r2, r3, cm4, sm4, cm5 = 0, 0, 0, 0, 0, 0

# acumulador de TODOS los números generados, como elemento de control...
st = 0

# ciclo de procesamiento para los n números...
print('Procesamiento de una sucesión de', n, 'números enteros aleatorios...')
for i in range(1, n+1):
    # generar un número aleatorio en el rango pedido...
    num = random.randint(1, 53000)
    st += num

    # 1. contar cada número en los intervalos pedidos...
    if 1 <= num < 17000:
        r1 += 1
    elif 17000 <= num < 37000:
        r2 += 1
    else:
        r3 += 1

    # 2. conteo y suma de los números mayores o iguales que 25000 y divisibles por 4...
    if num >= 25000 and num % 4 == 0:
        cm4 += 1
        sm4 += num

    # 3. determinar el mayor de todos los divisibles por 3...
    if num % 3 == 0:
        if may is None:
            may = num
        elif num > may:
            may = num

    # 4. contar los múltiplos de 5 para el cálculo del porcentaje...
    if num % 5 == 0:
        cm5 += 1

# Mostrar la suma de todos los números, para controlar validez del conjunto generado...
print('Control de validez de los números generados - La suma de todos ellos es:', st)
print()

print('Punto 1...')
print('\tCantidad de números en [1, 17000):', r1)
print('\tCantidad de números en [17000, 37000):', r2)
print('\tCantidad de números mayores o iguales a 37000:', r3)
print()

print('Punto 2...')
prm4 = 0
if cm4 != 0:
    prm4 = sm4 // cm4
print('\tPromedio de números >= 25000 y divisibles por 4:', prm4)
print()

print('Punto 3...')
print('\tEl mayor de todos los numeros generados divisibles por 3 es:', may)
print()

print('Punto 4...')
porc = cm5 * 100 // n
print('\tPorcentaje (entero) de la cantidad de múltiplos de 5 entre todos los números:', porc, '\b%')
print()
