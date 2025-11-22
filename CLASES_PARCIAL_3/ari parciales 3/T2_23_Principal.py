import random
from T2_23_Clase import *
# cada ticket se conoce: el código del vuelo (una cadena), el número de identificación del pasajero que compró el
    # ticket, el país de destino del vuelo (un valor entre 1 y 20), el número de asiento asignado,
    # y el importe pagado por ese ticket.

#### 1 #################################################################################################################
def cargar_arreglo():
    n = int(input("Ingrese tickets a cargar:"))
    v_ticket = [None] * n
    for i in range(n):
        cod = ("A", "B", "C", "D")
        codigo = random.choice(cod)
        ide = random.randint(1,600)
        destino = random.randint(1,20)
        asiento = random.randint(1,100)
        importe = round(random.uniform(1,100),2)
        obj = Ticket(codigo, ide, destino, asiento, importe)
        v_ticket[i] = obj
    return v_ticket

#### 2 #################################################################################################################

def ordenar_arreglo(v_ticket):
    n = len(v_ticket)
    for i in range(n - 1):
        for j in range(i+1, n):
            if v_ticket[i].codigo > v_ticket[j].codigo:
                v_ticket[i], v_ticket[j] = v_ticket[j], v_ticket[i]

def mostrar_arreglo(v_ticket, num):
    for i in v_ticket:
        if i.asiento > num:
            print(i)

#### 3 #################################################################################################################
def vector_acum(v_ticket, t):
    v_acum = [0] * 20

    for i in v_ticket:
        v_acum[i.destino - 1] += i.importe

    for i in range(len(v_acum)):
        if v_acum[i] > t:
            print("Destino", i+1, "el acumulad del importe es:", v_acum[i])


#### 4 #################################################################################################################
def busqueda_secuencial(v_ticket, id):

    for i in range(len(v_ticket)):
        if v_ticket[i].ide == id:
            print("El numero de asiento es: ", v_ticket[i].asiento, "El destino del vuelo es: ", v_ticket[i].destino)
            break
    else:
        print("No se encontraron coincidencias :(")

########################################################################################################################
def menu():
    print("_______________________")
    print("1 - Cargar tickets.")
    print("2 - Mostrar tickets.")
    print("3 - Contar tickets.")
    print("4 - Buscar tickets.")
    print("0 - Salir.")
    print("_______________________")
    op = int(input("Ingrese su opcion: "))
    print("_______________________")
    return op

def principal():
    v_ticket = []
    op = -1

    while op != 0:
        op = menu()
        if op == 1:
            v_ticket = cargar_arreglo()
        elif op == 2:
            ordenar_arreglo(v_ticket)
            num = int(input("Numero de asiento a superar: "))
            mostrar_arreglo(v_ticket, num)

        elif op == 3:
            t = int(input("Ingrese importe a superar: "))
            vector_acum(v_ticket, t)

        elif op == 4:
            id = int(input("Ingrese numero de identifiacion a buscar: "))
            busqueda_secuencial(v_ticket, id)
        elif op > 4:
            print("Elija un opcion valida !!")
        elif op == 0:
            print("Gracias por usar el menu :)")

if __name__ == "__main__":
    principal()