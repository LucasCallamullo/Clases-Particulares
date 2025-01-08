import os.path
import pickle
import random


class ImpuestoTV:
    # client(15, 20)    ;   producto(1,4)   1: TV   ,   2:Internet  , 3: Cable, 4:Cable + Internet
    def __init__(self, id, nombre, cliente, producto, importe):
        self.id = id
        self.nombre = nombre
        self.cliente = cliente
        self.producto = producto
        self.importe = importe

    def __str__(self):
        # self.producto= 1-1           2       3               4
        #   indices =     0         1           2       3
        desc_producto = ("TV", "Internet", "Cable", "Cable + Internet")

        cad = "Id: " + str(self.id)
        cad += " | Nombre: " + self.nombre
        cad += " | Cliente: " + str(self.cliente)
        cad += " | Producto: " + desc_producto[self.producto-1]
        cad += " | Importe: " + str(self.importe)
        return cad


# ==== Opcion 1
def validar_n():
    n = int(input("Ingresar cantidad de ImpuestosTV a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de ImpuestosTV a cargar (debe ser postivo): "))
    return n


# Por las dudas
def validar_id(v_impuesto, id):
    # Funcion para Validar que no se repitan los id.
    for i in v_impuesto:
        if i.id == id:
            return True
    return False


def cargar_arrreglo(v_impuesto, n):
    nombres = "ABCDEF"
    for i in range(n):

        id = random.randint(1, 20)
        while validar_id(v_impuesto, id):
            id = random.randint(1, 20)

        nombre = random.choice(nombres)
        cliente = random.randint(15, 20)
        producto = random.randint(1, 4)
        importe = round(random.uniform(0.1, 10), 2)
        impuestito = ImpuestoTV(id, nombre, cliente, producto, importe)
        add_in_order(v_impuesto, impuestito)


def add_in_order(v_impuesto, impuestito):
    izq, der = 0, len(v_impuesto) - 1

    while izq <= der:
        c = (izq + der) // 2
        if v_impuesto[c].id == impuestito.id:
            pos = c
            break
        elif v_impuesto[c].id < impuestito.id:          # si se come al vector > es de menor a mayor
            der = c - 1                                 # si se come al objeto(impuestito) > es de mayor a menor
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_impuesto[pos:pos] = [impuestito]


# ==== Opcion 2
def mostrar_datos(v_impuesto, t):
    # v_impuesto = [ I, I, I, ]
    for i in v_impuesto:
        # i = I
        if i.importe > t:
            print(i)


# ==== Opcion 3
def busqueda_binaria(v_impuesto, x):
    izq, der = 0, len(v_impuesto) - 1

    # id [ 7, 5, 3, 2, 1]
    #            3   2 1

    while izq <= der:
        c = (izq + der) // 2
        if v_impuesto[c].id == x:
            return c
        elif v_impuesto[c].id < x:          # si se come al vector > es de menor a mayor
            der = c - 1                     # si se come al objeto(impuestito) > es de mayor a menor
        else:
            izq = c + 1
    return -1


# ==== Opcion 4
def generar_matriz(v_impuesto):
    # generar la matriz
    columnas = 6    # tipo_cliente
    filas = 4       # tipo_producto
    matriz_cont = [[0] * columnas for i in range(filas)]         # [f][c]
    # matriz = [[0] * filas for i in range(columnas)]       # [c][f]

    matriz_acum = [[0] * columnas for i in range(filas)]         # [f][c]

    # completar/rellenar la matriz  ; # client(15, 20)    ;   producto(1,4)
    for i in v_impuesto:
        matriz_cont[i.producto-1][i.cliente-15] += 1
        # e ncaso de acumlar los montos facturados por tipo cliente y producto
        matriz_acum[i.producto-1][i.cliente-15] += i.importe


    # mostrar matriz
    # f =               0       1           2           3
    desc_producto = ("TV", "Internet", "Cable", "Cable + Internet")
    for f in range(len(matriz_cont)):
        for c in range(len(matriz_cont[0])):
            if matriz_cont[f][c] > 0 and c+15 >= 17:
                print("=" * 50)
                print("En tipo de cliente:", c+15, "y el tipo de producto:", desc_producto[f])
                print("La cantidad de clientes es:", matriz_cont[f][c])


# ==== Opcion 5
def generar_archivo(v_impuesto, fd, x):
    m = open(fd, "wb")
    se_genero = False
    for i in v_impuesto:
        if i.cliente == x and i.producto != 1 and i.producto != 2:
            pickle.dump(i, m)
            m.flush()       # no es necesaria de aprender
            se_genero = True

    if se_genero:
        print("Se genero correctamente el archivo:", fd)
    else:
        print("No se genero un nuevo archivo con nuevos datos.")

    m.close()       # SI ES NECESARIO


# ==== Opcion 6
def mostrar_archivo(fd):
    if os.path.exists(fd):
        m = open(fd, "rb")
        tam = os.path.getsize(fd)

        # v_imp = [ I, I, I ]
        # fd =    [ I       I       I ]
        #         0   220       440     660
        acum = 0

        while m.tell() < tam:
            imp = pickle.load(m)
            print(imp)
            if imp.producto == 4:
                acum += imp.importe

        print("El total acumulado es:", acum)
        m.close()

    else:
        print("No existe el archivo por favor ingrese primero a la opcion 4.")


def busqueda_secuencial(v_impuesto, x):
    acum, acum_total = 0, 0

    for i in range(len(v_impuesto)):
        acum_total += v_impuesto[i].importe
        if v_impuesto[i].producto == x:
            print(v_impuesto[i])
            acum += v_impuesto[i].importe

    # porcentaje        acum_total   ---   100%
    #                   acum        --- porc =

    if acum_total > 0:
        porc = acum * 100 / acum_total

        print("El acumulador del tipo de producto x:", acum)
        print("El acumulador total es:", round(acum_total, 2))
        print("Y el porcentaje que representa acum en acumtotal es:", round(porc, 2))


def menu():
    print("=" * 50)
    print(" 1 - Cargar Arreglo."
          "\n 2 - Mostrar datos."
          "\n 3 - Busqueda Binaria."
          "\n 4 - Generar y Mostrar Matriz"
          "\n 5 - Generar Archivo Binario"
          "\n 6 - Mostrar Archivo Binario")

    return int(input("Ingresar opcion: "))


def main():

    # arreglo principal
    v_impuesto = list()     # []

    # archivo bintario principal:
    fd = "impuestos.dat"

    # validar que pasamos por la opcion 1
    validar_op1 = False

    op = -1
    while op != 0:

        op = menu()

        if not validar_op1:
            if op == 1:
                n = validar_n()
                cargar_arrreglo(v_impuesto, n)
                validar_op1 = True
            else:
                print("Primero debe pasar por la opcion 1.")

        else:
            if op == 1:
                n = validar_n()
                cargar_arrreglo(v_impuesto, n)

            elif op == 2:
                t = float(input("INgresar importe a superar: "))
                mostrar_datos(v_impuesto, t)

            elif op == 3:
                x = int(input("Ingresar num id a buscar: "))
                pos = busqueda_binaria(v_impuesto, x)
                if pos >= 0:
                    print("Datos viejos")
                    print(v_impuesto[pos])

                    # reemplazes por un valor por teclado
                    imp = float(input("Ingresar impuesto con nuevo valor a modificar: "))
                    v_impuesto[pos].importe = imp

                    # que lo pongas un recargo del 10%
                    v_impuesto[pos].importe = v_impuesto[pos].importe - v_impuesto[pos].importe * 0.25

                    print("Datos actualizados")
                    print(v_impuesto[pos])

                else:
                    print("No se encontro el id buscado.")

            elif op == 4:
                generar_matriz(v_impuesto)

            elif op == 5:
                x = int(input("Ingresar tipo de cliente a guardar en archivo(15, 20): "))
                generar_archivo(v_impuesto, fd, x)

            elif op == 6:
                mostrar_archivo(fd)

            elif op == 7:
                x = int(input("Ingresar producto a buscar(1, 4): "))
                busqueda_secuencial(v_impuesto, x)


if __name__ == '__main__':
    main()
