

# registros / clase / objetos
class Estudiante:
    # legajo, nombre, carrera(1, 4), cuota a pagar

    # funcion constructora o inicializadora
    def __init__(self, legajo, nombre, carrera, importe):
        self.legajo = legajo
        self.nombre = nombre
        self.carrera = carrera
        self.importe = importe

    def __str__(self):
        # f"{20<: }  "
        cadena = "Legajo: " + str(self.legajo)
        cadena += " | Nombre:" + self.nombre
        cadena += " | Carrera:" + str(self.carrera)
        cadena += " | Importe:" + str(self.importe)
        return cadena


def principal():

    est1 = Estudiante(1, "Lucas", 1, 10.0)
    est2 = Estudiante(2, "Azul", 2, 20.0)

    print(est1)
    print(est2)

    est1.nombre = "Matias"
    print()
    print(est1)
    print(est2)





def principal3():

    # listas / arreglos / arrays / vectores

    # como crear una lista vacia
    v_listas = []       # list()

    # la funcion .append() : agregar contenido al final de la lista, conservando todoo el contenido previo
    v_listas.append(15)
    v_listas.append(25)
    v_listas.append(35)

    # indices      0  1   2
    # v_listas = [15, 25, 35]

    # v_listas[1] = "Lucas"
    # v_listas = [15, "Lucas", 35]

    # v_listas[2] += 15
    # v_listas = [15, "Lucas", 50]

    # recorrido que te sirve para cuando solo queres leer el contenido del arreglo

    # indices =    0   1   2
    # v_listas = [15, 25, 35]
    for i in v_listas:
        # i = 15, 25, 35
        print(i)

    # que la i toma valores de indice
    for i in range(len(v_listas)):      # 3
        # i = 0, 1, 2
        if i != 2:
            v_listas[i] += 5

    # # v_listas = [20, 30, 35]





def menu():
    # ctrl + d
    print("1 - Cargar Arreglo")
    print("2 - Mostrar Arreglo")
    print("3 - Vector de Conteo / Acum")
    print("4 - Busqueda Secuencial.")
    print("0 - Salir")

    op = int(input("Ingresar opcion:"))  # 2
    return op


def principal2():

    op = -1
    while op != 0:      # mientras op sea distinto de cero ingresa al ciclo

        op = menu()

        if op == 1:
            print("Hola 1")

        elif op == 2:
            print("hoal 2")



if __name__ == '__main__':
    principal()

