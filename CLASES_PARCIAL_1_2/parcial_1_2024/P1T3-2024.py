import random

# Parcial 1 - Tema 3 - 2024
# iniciar el generador de valores aleatorios con un valor fijo...
random.seed(9655)

# cantidad fija de números a procesar...
n = 21000

# variable para contener al menor pedido...
men = None

# inicialización de contadores, acumuladores y otras variables necesarias...
r1, r2, r3, ai, ci, cpn = 0, 0, 0, 0, 0, 0

# acumulador de TODOS los números generados, como elemento de control...
st = 0

# ciclo de procesamiento para los n números...
print('Procesamiento de una sucesión de', n, 'números enteros aleatorios...')
for i in range(1, n + 1):
    # generar un número aleatorio en el rango pedido...
    num = random.randint(1000, 29000)
    st += num

    # 1. contar cada número en los intervalos pedidos...
    if 1000 <= num < 9000:
        r1 += 1
    elif 9000 <= num < 19000 and num % 2 == 1 and num % 7 == 0:
        r2 += 1
    elif num >= 19000 and num % 3 == 0:
        r3 += 1

    # 2. contar y sumar los números del intervalo [4000, 10000] para el promedio pedido...
    if 4000 <= num <= 10000:
        ai += num
        ci += 1

    # 3. determinar el menor entre los no divisibles por 5...
    if num % 5 != 0:
        if men is None:
            men = num
        elif num < men:
            men = num

    # 4. contar los mayores o iguales a 15000 para el porcentaje pedido...
    if num >= 15000:
        cpn += 1

# Mostrar la suma de todos los números, para controlar validez del conjunto generado...
print('Control de validez de los números generados - La suma de todos ellos es:', st)
print()

print('Punto 1...')
print('\tCantidad de números en [1000, 9000):', r1)
print('\tCantidad de números en [9000, 19000) impares divisibles por 7:', r2)
print('\tCantidad de números mayores o iguales a 19000 divisibles por 3:', r3)
print()

print('Punto 2...')
prom = 0
if ci != 0:
    prom = ai // ci
print('\tPromedio de los números generados que están en [4000, 10000]:', prom)
print()

print('Punto 3...')
print('\tEl menor de los números no divisibles por 5:', men)
print()

print('Punto 4...')
porc = cpn * 100 // n
print('\tPorcentaje (entero) que los números mayores o iguales que 15000 representan en el total:', porc, '\b%')
print()
