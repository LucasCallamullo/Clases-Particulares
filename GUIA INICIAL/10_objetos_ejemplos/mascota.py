

# Mascota: Crea una clase Mascota con atributos como nombre, tipo de animal es un valor entre 1000, 1003 donde
# 1000 = Perro, 1001 = Gato, 1002= Loro, 1003=Conejo en pantalla no se debe mostrar el numero sino el animal que cosrresponda,
# edad, precio

# 1) Cargar arreglo, segun una cantidad n que ingrese el usuario por teclado
# 2 ) Mostrar por pantalla las mascotas ordenadas por nombre, y que se mayor a una edad t donde t es un valor ingresado
# por el usuario.
# 3 ) Buscar por nombre, validar op_2, o mas bien llamar a la funcion de orden
#
#

import random
# from registro import *


class Mascota:
    # tipo_a = 1000 = Perro, 1001 = Gato, 1002= Loro, 1003=Conejo
    def __init__(self, nombre, tipo_a, edad, precio):
        self.nombre = nombre        # Con ctrl + d ; copias la linea abajo
        self.tipo_a = tipo_a
        self.edad = edad
        self.precio = precio


    def __str__(self):
        # si fueran 5
        # int + int = 10
        # str + str = 55
        tipo_a_str = tipo_a_to_str(self.tipo_a)
        cadena = "Nombre: " + self.nombre
        cadena += " | Tipo Animal: " + tipo_a_str
        cadena += " | Edad: " + str(self.edad)
        cadena += " | Precio: " + str(self.precio)
        return cadena


def tipo_a_to_str(tipo_a):
    #               0       1       2       3
    mascotas = ["Perro", "Gato", "Loro", "Conejo"]
    # tipo_a =     1000,  1001,   1002,    1003
    animal = mascotas[tipo_a-1000]      #
    return animal


# ==============================================================================
#                           Opcion 1
# ==============================================================================
def validar_n():
    n = 0
    while n <= 0:
        n = int(input("Ingresar por teclado n: "))
    return n


def cargar_arreglo(v_masc, n):
    nombres = ["Coco", "Dante", "Fanta", "Fito"]
    for i in range(n):
        nombre = random.choice(nombres)
        tipo_a = random.randint(1000, 1003)
        edad = random.randint(1, 9)
        # Para elegir variables flotantes random con uniform
        precio = round(random.uniform(1, 10), 2)
        mascotita = Mascota(nombre, tipo_a, edad, precio)
        v_masc.append(mascotita)


# ==============================================================================
#                           Opcion 2
# ==============================================================================
#   Si la boquita se come a la i --->           i > esta ordenado de menor a mayor
#   Si la boquita se come a la j --->           < j esta ordenado de mayor a menor
def orden(v_masc):
    n = len(v_masc)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_masc[i].nombre > v_masc[j].nombre:
                v_masc[i], v_masc[j] = v_masc[j], v_masc[i]


def mostrar_datos(v_masc, t):
    # i = MASCOTA, MASCOTA, MASCOTA
    for i in v_masc:
        if i.edad > t:
            print(i)




def menu(validar_op1):
    if not validar_op1:
        print(" 1 - Cargar arreglo.")
    else:
        print("=" * 50)
        print(" 1 - Agregar mascotas al arreglo")

    print(" 2 - Mostrar datos."
          "\n 3 - ."
          "\n 4 - ."
          "\n 5 - ."
          "\n 0 - Salir.")
    return int(input("Ingresar numero: "))


def main():

    # Nuestro vector de trabajo
    v_masc = []             # list()

    # validar qe paso por opcion 1
    validar_op1 = False

    op = -1
    while op != 0:

        op = menu(validar_op1)

        # not validar_op1 esto significa si la bandera es falsa.
        if not validar_op1:
            # Con tab solo se mueve todo para adelante
            if op == 1:
                n = validar_n()
                cargar_arreglo(v_masc, n)
                validar_op1 = True

            else:
                print("Primero debe pasar por la opcion 1.")


        else:
            # preguntar si ponemos la opcion 1 en ambas banderas
            if op == 1:
                n = validar_n()
                cargar_arreglo(v_masc, n)

            elif op == 2:
                orden(v_masc)
                t = int(input("Ingresar edad a comparar: "))
                mostrar_datos(v_masc, t)


            elif op == 3:
                orden(v_masc)
                # aca hacer la busqueda binaria

            elif op == 4:
                pass

            # Crear una opcion para ver todos tus datos
            elif op == 6:
                for i in v_masc:
                    print(i)


# Si pones main se pone en automatico esta condicion
if __name__ == '__main__':
    main()
