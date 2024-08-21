

def calcular_mayor(lista_desafio):
    may = None
    # lista = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    for i in lista_desafio:
        # i = 13, 40, 20
        if may is None or i > may:
            may = i

    return may


def calcular_acumulado(lista_desafio):
    acum = 0
    # lista = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    for i in lista_desafio:
        # i = 13, 40, 20
        acum += i

    return acum


def generar_lista(n):
    lista_generica = [n]             # o list()

    # lista = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1

        lista_generica.append(int(n))

    return lista_generica           # retorno esta lista a la variable que lo iguale


def main():

    # n = int(input("Ingresemos n:"))
    n = 234519

    # para pedir un numero positivo siempre
    while n <= 0:            # mientras
        n = int(input("Ingresar n ( DEBE SER POSITIVO ):"))

    # para generar nuestra lista
    lista_desafio = generar_lista(n)        # me devuelve la lista generada

    # lista = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    tamanio = len(lista_desafio)

    # promedio = una suma de cosas / la cantidad que sumamos
    acumulador_suma_elementos_lista = calcular_acumulado(lista_desafio)
    prom = acumulador_suma_elementos_lista / tamanio

    # calcular mayor
    may = calcular_mayor(lista_desafio)

    print(lista_desafio)
    print("El numero de iteraciones de n:", tamanio)
    print("El promedio es:", prom)
    print("El promedio con un decimal es:", round(prom, 1))
    print("El numero mayor de la lista es:", may)


if __name__ == '__main__':
    main()
