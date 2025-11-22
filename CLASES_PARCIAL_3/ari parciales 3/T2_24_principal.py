import random
from T2_24_clase import *
# el código de producto (un entero),
# el diámetro en pulgadas,
# el tipo de aplicación del tubo (un entero del 1 al 20; Ej. 1-Agua sanitaria, 2-Electricidad, etc.),
# cantidad de gramos de PVC utilizados para su fabricación
# y un campo más para indicar si es ignífugo o no (1: sí, 2: no).


######## 1 #############################################################################################################
def cargar_arreglo():
    n = int(input("Ingrese cant de tubos a cargar: "))
    v_tubos = [None] * n

    for i in range(n):
        codigo = random.randint(1, 1000)
        diametro = random.randint(1, 50)
        aplicacion = random.randint(1,20)
        gramos = round(random.uniform(1, 200), 2)
        ignifugo = random.randint(1,2)
        tubito = Tubo(codigo, diametro, aplicacion, gramos, ignifugo)
        v_tubos[i] = tubito
    print("Se cargaron", n, "Tubos")
    return v_tubos


####### 2 ##############################################################################################################
def ordenar_arreglo(v_tubos):
    n = len(v_tubos)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if v_tubos[i].diametro < v_tubos[j].diametro:
                v_tubos[i], v_tubos[j] = v_tubos[j], v_tubos[i]

def mostrar_datos(v_tubos):
    cont = 0
    acum = 0

    for i in v_tubos:
        # i = T1, T2, T3
        if i.ignifugo == 1:
            cont += 1
            acum += i.gramos
            print(i)

    prom = 0
    if cont > 0:
        prom = acum / cont
    print("El promedio de gramos es: ", prom)

##### 3 ################################################################################################################
def generar_vector(v_tubos, a):
    v_acum = [0] * 20

    for i in v_tubos:
        # i = T1, T2
        v_acum[i.aplicacion - 1] += 1

    # v_acum --> vector de contadores --> lista
    for i in range(len(v_acum)):
        # i = 0, 1, 2, ...    --> a un indice del vector de conteo
        # v_acum[i] --> a cada contador/acumulador
        if v_acum[i] > a:
            print("Para el tipo de aplicacion", i+1, "- tiene cantidad: ", v_acum[i])

        # mostrar solo los tipo de aplicacion entre 4 y 6:
        # i + 1 --> representa al tipo de aplicacion
        # if (i+1 == 4 or i+1 == 5 or i+1 == 6):

        # mostrar los tipos que superen un tipo de aplicacion a cargada por teclado
        #if i + 1 > a:
            #pass

##### 4 ################################################################################################################
def busqueda_secuencial(v_tubos, prod):
    """
    Determinar si existe un tubo cuyo código de producto sea igual a prod. Si se encuentra, mostrar el tipo
    de aplicación y su diámetro. Si no se encuentra, indicar con un mensaje que no existe.
    Debe mostrar los datos del
primero que encuentre y detener en ese momento la búsqueda (sin importar si hay más de un registro con el
mismo código).
    """
    for i in range(len(v_tubos)):
        # i = 0, 1, 2, ...
        # v_tubos[i]  --> cada objeto del tipo tubo
        if prod == v_tubos[i].codigo:

            print("Tipo de aplicacion: ", v_tubos[i].aplicacion, "Su diametro", v_tubos[i].diametro)

            # aumentar los gramos un 10% si es descuento va menos
            v_tubos[i].gramos += 0.1 * v_tubos[i].gramos

            # cambiar el valor de los gramos por un valor que se carga por teclado
            print("Datos vejos:", v_tubos[i])
            v_tubos[i].gramos = int(input("Ingrese valor: "))
            print("Datos nuevos:", v_tubos[i])

            return      # cortar la funcion

    print("No existe")

########################################################################################################################
def menu():
    print("1 - Cargar cant de tubos: ")
    print("2 - Mostrar cant de tubos ignífugos: ")
    print("3 - Contar tubos que se fabrican: ")
    print("4 - Buscar cuyo código de producto sea igual a prod: ")
    print("0 - Salir ")
    op = int(input("Ingrese su opcion: "))
    return op

def principal():
    v_tubos = []
    op = -1

    while op != 0:
        op = menu()
        if op == 1:
            v_tubos = cargar_arreglo()

        elif op == 2:
            ordenar_arreglo(v_tubos)
            mostrar_datos(v_tubos)

        elif op == 3:
            a = int(input("Valor minimo de acum: "))
            generar_vector(v_tubos, a)

        elif op == 4:
            prod = int(input("Ingresar producto a buscar: "))
            busqueda_secuencial(v_tubos, prod)

        elif op == 5:
            for i in v_tubos:
                print(i)

        elif op == 0:
            print("Gracias por usar el menu")

if __name__ == "__main__":
    principal()