'''
Ejercicio 2: Conversor de Unidades

Desarrolla un programa en Python que presente al usuario un menú con las siguientes conversiones de
unidades:

Convertir de kilómetros a metros.
Convertir de grados Celsius a grados Kelvin.    (273K = 0°C)
Calcular la edad actual a partir del año de nacimiento.


Salir del programa.
El programa debe permitir al usuario elegir una opción del menú, ingresar el valor a convertir y mostrar
el resultado de la conversión. Debe repetirse hasta que el usuario decida salir.

'''


# =================
# opcion 3
def calcular_edad(edad, year):
    # year - edad
    calc = year - edad
    return calc


# ========================
# Opcion 2
def convertir_c_a_k(grados):
    #   273K            ----->   0 °C
    if grados >= 0:
        c = 273 + grados
    else:
        c = 273 - grados

    c = str(c) + " K"
    return c            # str = "274K" )


# =========================
# Opcion 1
def convertir_km_m(km):
    #   1Km  ---->  1000m
    #   x KM ---->  1000m * x / 1
    c = 1000 * km / 1
    return c


def menu():
    # Alt + 92 = \
    print("=" * 50)
    print(" 1 - Convertir KM a M."
          "\n 2 - Convertir C° a K."               # ctrl + d
          "\n 3 - Calcular Edad."               # ctrl + d
          "\n 0 - Salir.")
    op = int(input("Ingresar una opcion: "))
    return op


def main():

    op = -1
    while op != 0:

        op = menu()
        if op == 1:
            # Convertir de kilómetros a metros.
            km = float(input("Ingrese por teclado los km a convertir en m.: "))
            conv = convertir_km_m(km)
            print("El total de metros es:", conv)

        elif op == 2:
            # Convertir de grados Celsius a grados Kelvin.    (273K = 0°C)
            k = float(input("Ingresa por teclado los grados celsius a convertir: "))
            conv = convertir_c_a_k(k)       # str()
            print("Los grados celsius pasados a kelvins son: ", conv)

        elif op == 3:
            #
            # Calcular la edad actual a partir del año de nacimiento.
            year = 2023
            edad = int(input("Ingresar por teclado año de nacimiento: "))
            calc = calcular_edad(edad, year)
            print("Su edad actual es:", calc)






if __name__ == '__main__':
    main()
