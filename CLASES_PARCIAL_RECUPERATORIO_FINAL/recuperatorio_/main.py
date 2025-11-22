

import os.path
import pickle
import random

# Use la forma de importación que prefiera.
# Comente una y descomente la otra, a su gusto.
# import equipo
from equipo import Equipo


# Muestra las opciones, y carga y retorna la que elija el usuario.
def menu():
    print("1. Cargar (con inserción ordenada")
    print("2. Mostrar (de acuerdo a lo requerido")
    print("3. Conteo o Búsqueda (según sea requerido)")
    print("4. Generar archivo binario (de acuerdo a lo requerido")
    print("5. Mostrar archivo binario (de acuerdo a lo requerido")
    print("6. Analisis de cadena.")
    print("0. Salir del programa.")
    return int(input("Ingrese la opción: "))


# Carga y retorna un número, validando que sea mayor al valor inf que entra como parámetro.
def validar(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Error... Se pidio mayor a ' + str(inf) + '... Cargue de nuevo: '))
    return n


def generar_aleatorio():
    nombres = (
        "Alpha Strike.", "Crimson Vipers.", "Shadow Core.", "Echo Squad."
    )

    lista_descripciones = (
        "Descripcion uno.",
        "Descripcion dos.",
        "Frase uno."
    )

    nombre = random.choice(nombres)
    jugadores = random.randint(5, 8)
    rango = random.randint(1, 8)
    puntaje = random.randint(100, 1000)
    region = random.randint(1, 4)
    descripcion = random.choice(lista_descripciones)

    return Equipo(nombre, jugadores, rango, puntaje, region, descripcion)


# ===========================================================
# Opcion 1
# ===========================================================
def cargar_arreglo(vector, n):

    for i in range(n):
        # la variable e va a ser igual a lo que devuelva la funcion generar_aleatorio
        e = generar_aleatorio()

        add_in_order(vector, e)


def add_in_order(v, equipo):
    der = len(v) - 1
    izq = 0
    while izq <= der:
        c = (izq + der) // 2
        if v[c].nombre == equipo.nombre:
            pos = c
            break
        elif v[c].nombre > equipo.nombre:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [equipo]


# =================================================================
#           Punto 2
# ================================================================
def mostrar_arreglo(v):
    """
        Mostrar todos y al final del listado mostrar una linea que muestra la cantidad dee equipos del rango r
    """
    r1 = int(input("Ingresar rango al que debe ser igual el equipo: "))
    cont = 0

    # v = [ E1, E2, E3 ]
    for i in v:
        # i = E1,           E2, E3
        print(i)

        if i.rango == r1:
            cont += 1

    print("Contador de rango r: ", cont)


# =================================================================
#           Punto 5
# ================================================================
# Si esta ordenado por NOMBRE y nos piden buscar por NOMBRE --> BUSQUEDA BINARIA
# Si esta ordenado por NOMBRE y nos piden buscar CUALQUIER COSA QUE NO SEA EL NOMBRE --> BUSQUEDA SECUENCIAL
def busqueda_binaria(v, nom):
    """ Si encuentra equipo mostrar sus datos y retornar el nombre del mismo
     Si no existe informar por con el siguiente mensaje "Equipo no existe." y retornarlo """
    der = len(v) - 1
    izq = 0
    while izq <= der:
        c = (izq + der) // 2
        # if v[c].nombre == equipo.nombre:
        if v[c].nombre == nom:      # SIGNIFICA QUE ENCONTRAMOS UN RESULTADO VALIDO
            # El objeto -->  v[c]
            print(v[c])

            # retornar el nombre del mismo
            return v[c].nombre
            # pos = c
            # break

        # elif v[c].nombre > equipo.nombre:
        elif v[c].nombre > nom:
            der = c - 1
        else:
            izq = c + 1

    mensaje = "Equipo no existe."
    print(mensaje)
    return mensaje


# ================================================================
#           Punto 6
# ================================================================
def analizar_cadena(variable_punto_5_6):
    """
     ¿Cuál es la cantidad de palabras de esa cadena que contienen una letra "r"
    en la segunda o en la tercera posición (en mayúsculas o minúsculas) y que
    además no contenga más de 1 dígito?
    """
    # variable_punto_5_6 = cadena
    print("Cadena a analizar: ", variable_punto_5_6)
    #                  9    4
    # cl      12345678901234
    cadena = "Argentina hola."

    r1 = 0                      # 1

    # contiene o NO contiene        --> bandera
    tiene_r_pos_2_3 = False         # False
    cl = 0                          # 4

    # si habla de cantidad    --> bandera
    cont_digitos = 0

    """  Si pidiera que la ultima letra fuera vocal """
    # ultima_letra --> toma el valor de cada caracter todas las vueltas de ciclo

    #                    a
    # ultima    Argentina
    # cadena = "Argentina hola."
    ultima_letra = ""

    for i in variable_punto_5_6:        # itera sobre un str
        # i =   A, r  g,  , h     ..., .         # i --> caracter

        # Dentro de la palabra
        if i != " " and i != ".":
            cl += 1
            ultima_letra = i

            if i in "0123456789":
                cont_digitos += 1

            if (cl == 2 or cl == 3) and i.lower() == "r":
                tiene_r_pos_2_3 = True

        # fuera de la palabra o termina la palabra
        else:
            # ultima_letra = "a"
            # if ultima_letra.lower() in "aeiou":
            #    r1 += 1

            if tiene_r_pos_2_3 and cont_digitos <= 1:     #  de decir que esta en true
                r1 += 1

            # reiniciar banderas o contadores
            cl = 0
            tiene_r_pos_2_3 = False
            cont_digitos = 0

    print("La cadena tiene", r1, "palabras que cumplen.")


# Función principal o de arranque.
def main():
    random.seed(13715)
    fd = "archivo.dat"
    v = []
    op = -1

    variable_punto_5_6 = None

    while op != 0:

        op = menu()
        if op == 1:
            n = validar(0)
            cargar_arreglo(v, n)

        elif op == 2:
            if v:       # si el vector tiene contenido
                mostrar_arreglo(v)
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
            if v:
                nom = input("Ingresar nombre a buscar: ")
                # la variable_punto_5_6 va a valer lo que retorne busqueda_binaria
                variable_punto_5_6 = busqueda_binaria(v, nom)
            else:
                print("El archivo", fd, "no existe...")

        elif op == 6:
            if variable_punto_5_6 is None:
                print("Pasa por el punto 5")
            else:
                analizar_cadena(variable_punto_5_6)

            """ Analizar la descripcion del primer registro(objeto) del arreglo(lista,vector)
             generado en el punto 1"""
            #
            #         0   1    2
            # lista [ a , b ,  c ]      --> len(lista) = 3 - 1
            cadena = v[0].descripcion
            analizar_cadena(cadena)

            """ Analizar la descripcion del ultimo registro(objeto) del arreglo(lista,vector)
            generado en el punto 1"""
            ultimo = len(v) - 1
            cadena = v[ultimo].descripcion
            analizar_cadena(cadena)

            """ Analizar la descripcion del centro registro(objeto) del arreglo(lista,vector)
            generado en el punto 1"""
            centro = len(v) // 2        #   1
            cadena = v[centro].descripcion
            analizar_cadena(cadena)

        elif op == 0:
            print()
            print("Programa terminado... Hasta la vista baby...")
            print()


if __name__ == "__main__":
    main()




