



def calcular_mayor_lista(lista_generica):
    may = None
    # lista: [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    for i in lista_generica:
        # i = 13, 40, 20, 10, 5, 16
        if may is None or i > may:
            may = i

    return may


def generar_lista(n):
    lista = [n]      # lista vacía

    # 13
    while n > 1:             # mientras

        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1

        lista.append(int(n))
        # lista = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    return lista


def calcular_acumulado_suma_lista(lista_generica):
    acum = 0
    # lista: [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    for i in lista_generica:
        # i = 13, 40, 20, 10, 5, 16
        acum += i
    return acum




def main():

    # n = int(input("Ingresa n:"))
    n = 13251
    # como validar que un numero sea positivo
    while n < 0:
        n = int(input("Ingresa n (debe ser positivo:"))

    # lista
    lista_generica = generar_lista(n)

    tamanio = len(lista_generica)


    acum_suma_lista = calcular_acumulado_suma_lista(lista_generica)

    promedio = acum_suma_lista / tamanio

    mayor = calcular_mayor_lista(lista_generica)    # aca queda almacenado el may


    print("orbita de n:", lista_generica)

    print("Numero elegido:", n)
    print("longitud de n:", tamanio)
    print("promedio de n:", promedio)
    print("mayor de la lista n:", mayor)











if __name__ == '__main__':
    main()