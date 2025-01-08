import os.path
import pickle
import random


class Cliente:
    # numero 100, 120          ; importe >= 0      ; cat ( 1, 3)
    def __init__(self, nombre, numero, importe, categoria):
        self.nombre = nombre
        self.numero = numero
        self.importe = importe
        self.categoria = categoria

    def __str__(self):

        # cat(1,3)
        #              1-1         2-1         3-1
        # indices       0           1           2
        desc_cat = ("Normal", "Preferencial", "VIP")

        cadena = "Nombre: " + self.nombre
        cadena += " | Numero: " + str(self.numero)
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Categoria: " + desc_cat[self.categoria-1]
        return cadena


# =====================================================================
#                            Opcion 1
# =====================================================================
def validar_n():
    n = int(input("Ingresar cantidad de clientes a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de clientes a cargar(debe ser positivo): "))
    return n


def cargar_arreglo(v_cliente, n):
    nombres = "ABCDEF"
    for i in range(n):
        nombre = random.choice(nombres)
        numero = random.randint(100, 120)
        importe = round(random.uniform(0.1, 10), 2)             # flotantes
        categoria = random.randint(1, 3)
        clientecito = Cliente(nombre, numero, importe, categoria)
        add_in_order(v_cliente, clientecito)


def add_in_order(v_cliente, clientecito):
    izq, der = 0, len(v_cliente) - 1

    while izq <= der:
        c = (izq + der) // 2
        if v_cliente[c].numero == clientecito.numero:
            pos = c
            break
        elif v_cliente[c].numero > clientecito.numero:      # si se come al vector esta de menor a mayor
            der = c - 1                                     # si se come al objeto esta de mayor a menor
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_cliente[pos:pos] = [clientecito]


# =====================================================================
#                            Opcion 2
# =====================================================================
def mostrar_datos(v_cliente):
    # v_cliente = [ C, C, C, C ]
    for i in v_cliente:
        # i = C     ; C         ;C
        print(i)


# =====================================================================
#                            Opcion 3
# =====================================================================
def generar_matriz(v_cliente):
    # numero 100, 120             ; cat ( 1, 3)
    # crear la matriz en 0
    filas = 21          # numero
    columnas = 3        # categoria
    matriz = [[0] * columnas for i in range(filas)]

    # [ [0, 0, 0],
    #   [0, 0, 0],
    #   [0, 0, 0],
    #   [0, 0, 0] ...

    # rellenar la matriz
    for i in v_cliente:
        # i = C1, C2, C3
        matriz[i.numero-100][i.categoria-1] += 1
        # si te piden una matriz una acumlacion
        # matriz[i.numero-100][i.categoria-1] += i.importe

    # mostrar la matriz
    desc_cat = ("Normal", "Preferencial", "VIP")
    for f in range(len(matriz)):         # len = 21  ; f = 0, 1, 2, 3, ..., 21
        for c in range(len(matriz[0])):  # len = 3   ; c = 0, 1, 2
            if matriz[f][c] > 0 and f+100 > 110:
                print("La cantidad por Numero de cliente:", f+100, "Y por Categoria:", desc_cat[c])
                print("La cantidad total es:", matriz[f][c])


# =====================================================================
#                            Opcion 4
# =====================================================================
def generar_archivo(fd, v_cliente, x):
    m = open(fd, "wb")  # write binary      # "ab" append binary
    cont = 0
    for i in v_cliente:
        if i.importe < x and (i.categoria == 1 or i.categoria == 2):
            pickle.dump(i, m)
            m.flush()       # no es necesario pero agregalo
            cont += 1

    print("Se cargaron esta cantidad de clientes:", cont)
    m.close()       # SI ES NECESARIO


# =====================================================================
#                            Opcion 5
# =====================================================================
def mostrar_archivo(fd):
    if os.path.exists(fd):
        m = open(fd, "rb")  # read binary
        size = os.path.getsize(fd)      # 300   ;    0

        cont = 0
        acum = 0
        # fd = [  C       C       C  ]
        #      0     100      200     300
        while m.tell() < size:
            client = pickle.load(m)
            print(client)

            if client.categoria == 2 or client.categoria == 3:
                cont += 1
                acum += client.importe

        if cont > 0:
            prom = acum / cont
            print("El promedio total es:", prom)
        else:
            print("NO hubieron clientes vip o preferenciales en el archivo.")

        m.close()

    else:
        print("El archivo:", fd, "No existe. Primero debe pasar por la opcion 4.")


# =====================================================================
#                            Opcion 6
# =====================================================================
def busqueda_secuencial(v_cliente, nom):
    se_encontro = False
    for i in range(len(v_cliente)):
        if v_cliente[i].nombre == nom:
            print(v_cliente[i])
            se_encontro = True

    if not se_encontro:         # se encoontro esta en falso
        print("No se encontro ese cliente con ese nombre.")


# =====================================================================
#                            Opcion 7
# =====================================================================
def busqueda_binaria(v_cliente, x):
    izq, der = 0, len(v_cliente) - 1

    while izq <= der:
        c = (izq + der) // 2
        if v_cliente[c].numero == x:
            return c
        elif v_cliente[c].numero > x:      # si se come al vector esta de menor a mayor
            der = c - 1                    # si se come al objeto esta de mayor a menor
        else:
            izq = c + 1
    return -1


def menu():
    print("=" * 50)
    print(" 1 - Cargar arreglo."
          "\n 2 - Mostrar datos."
          "\n 3 - Generar matriz y mostrar"
          "\n 4 - Generar Archivo Binario."
          "\n 5 - Mostrar Archivo Binario."
          "\n 3 - ")

    return int(input("Ingresar una opcion: "))


def main():

    # vector / arreglo / lista principal
    v_cliente = []      # list()

    # nombre del archivo principal
    fd = "clientes.dat"

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_cliente, n)

        elif op == 2:
            mostrar_datos(v_cliente)

        elif op == 3:
            generar_matriz(v_cliente)

        elif op == 4:
            x = float(input("Ingresar saldo al que debe ser menor para guardarse en el archivo: "))
            generar_archivo(fd, v_cliente, x)

        elif op == 5:
            mostrar_archivo(fd)

        elif op == 6:
            nom = input("Ingresar nombre a buscar: ")
            busqueda_secuencial(v_cliente, nom)

        elif op == 7:
            x = int(input("Ingresar numero de cliente a buscar: "))
            pos = busqueda_binaria(v_cliente, x)

            if pos >= 0:
                # mostrar datos
                print(v_cliente[pos])

                # modificar por un valor t
                t = float(input("Ingresar nuevo valor a modificar: "))
                v_cliente[pos].importe = t

                # la condicion de si es preferencial o vip
                if v_cliente[pos].categoria == 2 or v_cliente[pos].categoria == 3:
                    print("Cupon de descuento")

                # datos actualizados
                print(v_cliente[pos])


            else:
                print("No se encontro un cliente con ese numero.")


if __name__ == '__main__':
    main()
