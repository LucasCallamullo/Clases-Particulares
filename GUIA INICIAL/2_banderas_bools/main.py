
'''
    numeros = "1234567890"
    es_numero = False
    for i in num:
        if i in numeros:
            es_numero = True
        else:
            es_numero = False
'''


def main():
    # Bools iniciadores
    es_par = False
    es_impar = False

    num = int(input("Ingresar numero: "))

    if num % 2 == 0:
        es_par = True
    else:
        es_impar = True

    # if
    if es_par:
        print(num, "El numero es par.")

    elif es_impar:
        print(num, "El numero es impar.")

    # if not
    if not es_impar:
        print(num, "El numero es par.")
    elif not es_par:
        print(num, "El numero es impar.")



    if num == 5 and es_impar:
        print("El numero es el 5 y es impar.")


    if num <= 10:
        print("Menor a 10")
    elif num < 20:
        print("el numero esta entre 10 y 20.")
    else:
        print(" El numero es mayor a 20")


if __name__ == '__main__':
    main()
