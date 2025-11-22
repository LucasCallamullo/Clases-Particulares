import random
from T4_23_clase import *
# Juicio se conoce su código de expediente (un número entero), la descripción o carátula del juicio (una cadena), el
    # tipo de juicio (un entero entre 1 y 15), el nombre del cliente defendido,
    # y el monto de honorarios a cobrar por ese juicio.


#### 1 #################################################################################################################

def cargar_arreglo(v_jucio):
    n = int(input("Cantidad de juicios: "))
    v_jucio = [None] * n

    tupla = (True, False)
    for i in range(n):
        nombres = ("Ariana", "Lucas", "Lucario")
        caratula = ("A", "B", "C", "D")
        codigo = random.randint(1, 800)
        desc = random.choice(caratula)
        desc = random.choice(tupla)
        tipo = random.randint(1, 15)
        nombre = bool(nombres)
        monto = round(random.uniform(1,8000))
        obj = Juicio(codigo, desc, tipo, nombre, monto)
        v_jucio[i] = obj
    return v_jucio

#### 2 #################################################################################################################
def ordenar_arreglo(v_jucio):
    n = len(v_jucio)
    for i in range(n - 1):
        for j in range(i+1, n):
            if v_jucio[i].desc > v_jucio[j].desc:
                v_jucio[i], v_jucio[j] = v_jucio[j], v_jucio[i]

def mostrar_arreglo(v_jucio, mon):
    cont = 0
    for i in range(len(v_jucio)):

        if v_jucio[i].monto > mon:
            print(v_jucio[i])
            cont += 1
    print("Se mostraron", cont,"juicios.")


#### 3 #################################################################################################################

def vector_conteo(v_jucio, c):
    v_cont = [0] * 20
    for i in v_jucio:
        v_cont[i.tipo - 1] += 1

    for i in range(len(v_cont)):
        if v_cont[i] > c:
            print("Para el tipo", i+1,"tiene la cantidad de:", v_cont[i])

#### 4 #################################################################################################################
def buscar_arreglo(v_jucio, cod):

    for i in range(len(v_jucio)):
        if v_jucio[i].codigo == cod:
            print("Datos viejos: ", v_jucio[i])
            num = int(input("Ingrese nuevo monto: "))
            v_jucio[i].monto = num
            False
            print("Datos nuevos", v_jucio[i])
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
    op = int(input("Elija su opcion: "))
    return op

def principal():
    op = -1
    v_jucio = []

    while op != 0:
        op = menu()
        if op == 1:
            v_jucio = cargar_arreglo(v_jucio)

        elif op == 2:
            ordenar_arreglo(v_jucio)
            mon = int(input("Numero de asiento a superar:"))
            mostrar_arreglo(v_jucio, mon)

        elif op == 3:
            vector_conteo(v_jucio, c)
            c = ("Valor de contador a superar:")
        elif op == 4:
            cod = int(input("Expediente a buscar: "))
            buscar_arreglo(v_jucio, cod)
        elif op > 4:
            print("Elija la opcion correcta !!")
        elif op == 0:
            print("Gracias por usar el menu :)")

if __name__ == "__main__":
    principal()