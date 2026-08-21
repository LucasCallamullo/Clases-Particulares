import os
import pickle
import registro


def mostrar_menu():
    cadena = "Menu de Opciones\n"
    cadena += f'{"-" * 70}\n'
    cadena += '1 ---- Cargar Seguros\n'
    cadena += '2 ---- Mostrar Seguros\n'
    cadena += '3 ---- Buscar Seguros por Nombr\n'
    cadena += '4 ---- Generar Archivo de Seguros\n'
    cadena += '5 ---- Mostrar Archivo de Seguros\n'
    cadena += '0 ---- Salir\n'
    cadena += 'Ingrese su opcion: '
    return int(input(cadena))


def principal():
    opcion = -1
    seguros = []
    FD = "seguros.dat"

    while opcion != 0:
        opcion = mostrar_menu()
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass


if __name__ == '__main__':
    principal()
