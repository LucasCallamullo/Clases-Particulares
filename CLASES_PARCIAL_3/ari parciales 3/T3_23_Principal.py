import random
from T3_23_Clase import *
    # . Por cada Servicio de alarma vendido a un cliente se tiene un código identificatorio (un número entero), el
    # nombre del cliente (una cadena), un valor entre 1 y 10 que indica el tipo de servicio prestado,
    # y el importe a pagar por mes por ese servicio.

#### 1 #################################################################################################################
def cargar_arreglo():
    n = int(input("Cantidad de servicios: "))
    v_servicio = [None] * n
    for i in range(n):
        nombre = ("Lucas", "Ariana", "Lucario")
        ide = random.randint(1,600)
        nombre = random.choice(nombre)
        tipo = random.randint(1,10)
        importe = round(random.uniform(1,40000),2)
        obj = Servicio(ide, nombre, tipo, importe)
        v_servicio[i] = obj
    return v_servicio

#### 2 #################################################################################################################

def ordenar_arreglo(v_servicio):
    n = len(v_servicio)
    for i in range(n - 1):
        for j in range(i+1, n):
            if v_servicio[i].ide > v_servicio[i].ide:
                v_servicio[i], v_servicio[j] = v_servicio[j], v_servicio[i]

def mostrar_arreglo(v_servicio, i1, i2):
    cont = 0
    for i in v_servicio:
        if i1 < i.importe < i2:
            print(i)
            cont += 1
    print("Se mostraron", cont, "servicios.")


#### 3 #################################################################################################################
def generar_acum(v_servicio):
    v_cont = [0] * 10
    for i in v_servicio:
        v_cont[i.tipos - 1] += 1

    for i in range(len(v_cont)):
        if v_cont[i] > 0:
            print("Servicios para cada tipo: ", i+1, "cantidad:", v_cont[i])

#### 4 #################################################################################################################
def busqueda_secuencial(v_servicio, nom):

    for i in range(len(v_servicio)):
        if v_servicio[i].nombre == nom:
            print("Datos viejos: ", v_servicio[i])

            v_servicio[i].importe += 2000
            print("Datos nuevos: ", v_servicio[i])
            break

        else:
            print("No se encontraron coincidencias :(")

########################################################################################################################


def menu():
    print("1 - Cargar arreglo: ")
    print("2 - Mostrar arreglo: ")
    print("3 - Contar arreglo: ")
    print("4 - Buscar arreglo: ")
    print("0 - Salir")
    op = int(input("Ingrese su opcion: "))
    return op

def principal():
    op = -1
    v_servicio = []

    while op != 0:
        op = menu()
        if op == 1:
            v_servicio = cargar_arreglo()
        elif op == 2:
            ordenar_arreglo(v_servicio)
            i1 = int(input("Ingrese valor minimo de importe: "))
            i2 = int(input("Ingrese valor maximo de importe: "))
            mostrar_arreglo(v_servicio, i1, i2)
        elif op == 3:
            generar_acum(v_servicio)
        elif op == 4:
            nom = input("Ingrese nombre: ")
            busqueda_secuencial(v_servicio, nom)

        elif op > 4:
            print("Ingrese una opcion valida !!")
        elif op == 0:
            print("Gracias por usar el menu :)")




if __name__ == "__main__":
    principal()














