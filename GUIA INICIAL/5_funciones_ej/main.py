
from funciones import *


#                     n1  n2
def calcular_promedio(x, y):
    p = (x + y) / 2
    return p


def mult_num(n1, n2):
    return n1 * n2


def div_num(n1, n2):
    # div = n1 / n2   != n2 / n1
    pass



def menu():
    print("=" * 50)     # ============================================
    # alt + 92 = \
    print(" 1 - Calcular promedio." 
          "\n 2 - Producto entre dos numeros."  
          "\n 3 - Cambiar numeros."
          "\n 4 - Hola Mundo."
          "\n 0 - Salir.")

    x = int(input("Ingresar una opcion: "))     # x = 2

    return x

    # x = int(input("Ingresar una opcion: "))     # 2
    #  x = 2            == 2 = x
    # return x     # 2


def principal():
    # v_objeto

    # Variables del enunciado
    n1 = int(input("Ingresar numero 1: "))
    n2 = int(input("Ingresar numero 2: "))

    op = 1
    while op != 0:            # mientras

        op = menu()             # 2                 # Devuelve Menu, valor del input que ingresamos

        if op == 1:
            prom = calcular_promedio(n1, n2)        # p
            print("El promedio es:", prom)

        elif op == 2:
            # una funcion para calcular un producto
            mult = mult_num(n1, n2)     # mult = res = 25
            print("El resultado de la multiplicacion es:", mult)

        elif op == 3:
            # Cambiar numeros
            n1, n2 = cambiar_nums()

        elif op == 4:
            cadena = hola_mundo_op()
            print(cadena)

        # salir del menu
        elif op == 0:
            print("Salio del menu.")

        else:
            print("Elija una opcion correcta.")





if __name__ == '__main__':
    principal()

