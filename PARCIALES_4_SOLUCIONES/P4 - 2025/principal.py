import os.path
import pickle
import random

# Use la forma de importación que prefiera.
# Comente una y descomente la otra, a su gusto.
import clases
# from clases import *


# Muestra las opciones, y carga y retorna la que elija el usuario.
def menu():
    print("1. Cargar (con inserción ordenada")
    print("2. Mostrar (de acuerdo a lo requerido")
    print("3. Conteo o Búsqueda (según sea requerido)")
    print("4. Generar archivo binario (de acuerdo a lo requerido")
    print("5. Mostrar archivo binario (de acuerdo a lo requerido")
    print("6. Salir del programa.")
    return int(input("Ingrese la opción: "))


# Carga y retorna un número, validando que sea mayor al valor inf que entra como parámetro.
def validar(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Error... Se pidio mayor a ' + str(inf) + '... Cargue de nuevo: '))
    return n


# Función principal o de arranque.
def principal():
    random.seed(13715)
    fd = "archivo.dat"
    v = []
    op = -1
    while op != 6:
        op = menu()
        if op == 1:
            pass

        elif op == 2:
            if v:
                pass
            else:
                print("el vector no fue cargado todavía...")

        elif op == 3:
            if v:
                pass
            else:
                print("El vector no fue cargado todavía...")

        elif op == 4:
            if v:
                pass
            else:
                print("El vector no fue cargado todavía...")

        elif op == 5:
            if os.path.exists(fd):
                pass
            else:
                print("El archivo", fd, "no existe...")

        elif op == 6:
            print()
            print("Programa terminado... Hasta la vista baby...")
            print()


if __name__ == "__main__":
    principal()
