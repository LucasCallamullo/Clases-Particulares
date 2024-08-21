

def collatz_sequence(n):
    """Genera la órbita de Collatz para un número n."""
    # tuplas = ( 1, 10, 20)
    orbit = [n]         # realiza una lista  [13, 40, 20
    # [5, 16, 8, 4, 2, 1]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        orbit.append(n)

    return orbit


def main():
    # Leer el valor de n desde el teclado
    n = int(input("Ingrese un número entero positivo: "))

    # Generar la órbita de n
    orbit = collatz_sequence(n)     # [5, 16, 8, 4, 2, 1]

    # Calcular la longitud de la órbita
    orbit_length = len(orbit)           # 6

    # Calcular el promedio de los valores en la órbita
    acum = 0
    for i in orbit:
        acum += i

    orbit_average = acum / orbit_length
    # orbit_average = sum(orbit) / orbit_length

    # Encontrar el valor máximo en la órbita
    may = None
    for i in orbit:
        if may is None or i > may:
            may = i

    max_value = may
    # max_value = max(orbit)

    # Mostrar los resultados
    print("Órbita de n:", orbit)
    print("Longitud de la órbita:", orbit_length)
    print("Promedio de los valores en la órbita:", orbit_average)
    print("Valor máximo en la órbita:", max_value)


if __name__ == "__main__":
    main()