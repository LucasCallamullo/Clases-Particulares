'''
Ejercicio 1: Mix para poner en practica

Crear un menu en python que pida previamente dos numeros que ingresan por teclado.
Se pide un menu que posea las siguientes funciones por opciones:
Una opcion de suma entre dos numeros ingresados por teclado.
Una opcion de promedio entre 4 numeros elegidos de forma aleatoria.
Una opcion que calcule el 10% de un numero ingresado por teclado
Una opcion que te permita saber cuantas vocales tiene una cadena ingresada por teclado.
'''


from funciones_ejercicio import *


def menu():
    print("=" * 50)
    op = int(input("Ingresar opcion: "))
    return op


def main():
    n1 = int(input("Ingresar Numero1: "))       # ctrl + D
    n2 = int(input("Ingresar Numero2: "))       # ctrl + D

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            suma = sumar_numeros(n1, n2)
            print("La suma es:", suma)

        elif op == 2:
            prom = calcular_promedio()
            print("El promedio es: ", prom)

        elif op == 3:
            num = int(input("Ingresar numero: "))
            porc = porcentaje_op3(num)
            print("El porcentaje es:", porc)

        # Una opcion que te permita saber cuantas vocales tiene una cadena ingresada por teclado.
        elif op == 4:
            cad = input("Ingresar cadena: ")
            cont = cant_vocales_op4(cad)
            print("La cantidad de vocales es:", cont)


if __name__ == "__main__":
    main()
