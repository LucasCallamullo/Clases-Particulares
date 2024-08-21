# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import pickle
import random


class Consumo:
    # hora (0, 23), tipo(1, 3) , importe
    def __init__(self, numero, hora, tipo, importe):
        self.numero = numero
        self.hora = hora
        self.tipo = tipo
        self.importe = importe

    def __str__(self):
        # tipo          1-1           2           3
        # indice        0           1           2
        tipos_desc = ["SMS", "Llamada", "Uso de datos"]

        cad = "Numero: " + self.numero
        cad += " | Hora: " + str(self.hora)
        cad += " | Tipo: " + tipos_desc[self.tipo-1]
        cad += " | Importe: " + str(self.importe)
        return cad


# =====================================================
#               Opcion 1
# =====================================================
def validar_n():
    n = int(input("Ingresar cantidad de Consumos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de Consumos a cargar(debe ser positivo): "))
    return n


def validar_numero(v_consumo, numero):
    # Funcion para Validar que no se repitan los numeros.
    for i in v_consumo:
        if i.numero == numero:
            return True
    return False


def cargar_arreglo(v_consumo, n):
    numeros = "ABC"
    for i in range(n):          # n = 3 :   0       1       2

        numero = random.choice(numeros)
        # numero = random.choice(numeros) + str(random.randint(0, 9))
        # while validar_numero(v_consumo, numero):
        #    numero = random.choice(numeros) + str(random.randint(0, 9))

        hora = random.randint(0, 23)
        tipo = random.randint(1, 3)
        importe = round(random.uniform(0.1, 10), 2)
        consu = Consumo(numero, hora, tipo, importe)
        add_in_order(v_consumo, consu)


def add_in_order(v_consumo, consu):
    izq, der = 0, len(v_consumo) - 1    # primera vuelta:   len(v) = 0  ;  C1.numero = C
                                        # segunda vuelta:   len(v) = 1  ;  C2.numero = B

    while izq <= der:
        c = (izq + der) // 2
        if v_consumo[c].numero == consu.numero:
            pos = c
            break
        elif v_consumo[c].numero > consu.numero:        # vector >   ordenado menor a mayor
            der = c - 1                                 # objeto >   ordenado mayor a menor
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    #               0    1
    # v_consumo = [ C2,  C1  ]
    v_consumo[pos:pos] = [consu]


# =====================================================
#               Opcion 2
# =====================================================
def mostrar_datos(v_consumo, t):
    # v_consumo = [ C,  C,  C , C
    for i in v_consumo:
        # i = C
        if i.importe > t:
            print(i)


def generar_matriz(v_consumo):
    # hora (0, 23), tipo(1, 3)
    filas = 3
    columnas = 24

    matriz = [[0] * columnas for i in range(filas)]
    # matriz = [ 0,   0,    0 ]
    #          [ 0,    0,    0]
    #          [ 0,    0,    0]
    for i in v_consumo:
        matriz[i.tipo-1][i.hora] += i.importe


    tipos_desc = ["SMS", "Llamada", "Uso de datos"]
    for f in range(len(matriz)):    # f = 0, 1, 2
        # f = 1
        for c in range(len(matriz[0])):     # c = 0, 1 ,2, ... , 23
            if matriz[f][c] != 0 and 0 <= c <= 12:
                print("El acumulado de los Tipo", tipos_desc[f], "y en la hora:", c)
                print("El importe acumulado es:", matriz[f][c])
                print("=" * 50)


# =====================================================
#               Opcion 4
# =====================================================
def generar_archivo(v_consumo, fd, t):
    m = open(fd, "wb")
    se_creo = False
    for i in v_consumo:
        if i.numero == t and (i.tipo == 1 or i.tipo == 2):
            pickle.dump(i, m)
            m.flush()
            se_creo = True

    if se_creo:
        print("Se encontraron coincidencias con el numero buscado y se genero el archivo.")
    else:
        print("No se genero un nuevo archivo.")

    m.close()


# =====================================================
#               Opcion 5
# =====================================================
def mostrar_archivo(fd):
    if os.path.exists(fd):
        m = open(fd, "rb")
        tam = os.path.getsize(fd)       # obtiene el tamaño en bytes del archivo    # 186

        cont = 0
        acum = 0

        # vector = [ C, C, C ]
        # fd =      [ C1             C2 ]
        #           0       93         186

        while m.tell() < tam:
            consu = pickle.load(m)
            print(consu)

            # supongamos que te pidieran solo informar al final la promedio que fueron por tipo SMS == 1
            if consu.tipo == 1:
                cont += 1
                acum += consu.importe


        if cont > 0:
            prom = acum / cont
            print("La cantidad Promedio de Consumos por TIPO SMS mostrados fue:", prom)

        m.close()
    else:
        print("Primero debe ingresar por la opcion 4.")


# =====================================================
#               Opcion 6
# =====================================================
def busqueda_binaria(v_consumo, num):
    izq, der = 0, len(v_consumo) - 1
    while izq <= der:
        c = (izq + der) // 2
        if v_consumo[c].numero == num:
            return c
        elif v_consumo[c].numero > num:        # vector >   buscar menor a mayor
            der = c - 1                                 # objeto >   buscar mayor a menor
        else:
            izq = c + 1
    return -1


def busqueda_secuencial(v_consumo, h):
    acum = 0
    for i in range(len(v_consumo)):
        if v_consumo[i].hora == h:
            print("importe:", v_consumo[i].importe)
            acum += v_consumo[i].importe

    if acum > 0:
        print("El acumulado total es:", acum)
    else:
        print("No se encontro consumos en la hora:", h)


def menu():
    print("=" * 50)
    print(" 1 - Cargar arreglo."
          "\n 2 -")
    return int(input("Ingrese una opcion: "))


def main():

    # arreglo/vector/lista principal
    v_consumo = []          # len vacio = 0

    # archivo principal
    fd = "consumos.dat"

    # bandera para comprobar que paso por la op 1
    ingreso_op1 = False

    # archivo csv para recuperar datos
    name_csv = "Consumos.csv"

    op = -1
    while op != 0:

        op = menu()

        if not ingreso_op1:
            if op == 1:
                n = validar_n()
                cargar_arreglo(v_consumo, n)
                ingreso_op1 = True
            else:
                print("Debe ingresar primero por la opcion 1.")

        else:
            if op == 1:
                n = validar_n()
                cargar_arreglo(v_consumo, n)

            elif op == 2:
                # que supere los importes t un valor ingresado por teclado
                t = float(input("Ingresar importe a superar: "))
                mostrar_datos(v_consumo, t)

            elif op == 3:
                generar_matriz(v_consumo)

            elif op == 4:
                t = input("Ingresar numero de telefono(A, F): ")
                generar_archivo(v_consumo, fd, t)

            elif op == 5:
                mostrar_archivo(fd)

            elif op == 6:
                for i in v_consumo:
                    print(i)

            elif op == 7:
                num = input("ingresar numero: ")
                pos = busqueda_binaria(v_consumo, num)
                if pos >= 0:
                    print(v_consumo[pos])
                    # si es sms o llamada que muestre opcion recomendada.
                    if v_consumo[pos].tipo == 1 or v_consumo[pos].tipo == 2:
                        print("Opcion recomendada.")

                    # modifiques el importe que aumente un 10
                    # modifiques por un valor t ingresado por el usuario
                    v_consumo[pos].importe = v_consumo[pos].importe + v_consumo[pos].importe * 0.1
                    print(v_consumo[pos])

                else:
                    print("El numero buscado no existe.")

            elif op == 8:
                # buscar y mostrar todos los importes iguales a una hora h donde h es unvalor
                # ingresado por teclado, y al final mostrar la suma total de esos importes
                # si existe mas de uno debe mostrar todos, si no existe informar.
                h = int(input("Ingresar hora a buscar(0, 23): "))
                busqueda_secuencial(v_consumo, h)


# NO VA
def cargar_desde_csv(v_consumo, name_csv):
    archivo = open(name_csv, 'rt')
    consumos = archivo.readlines()

    primer_renglon = True
    for i in consumos:
        if primer_renglon:
            primer_renglon = False
        else:
            linea = i.split("-")
            numero = linea[0]
            hora = int(linea[1])
            tipo = int(linea[2])
            importe = float(linea[3])
            consu = Consumo(numero, hora, tipo, importe)
            add_in_order(v_consumo, consu)

    archivo.close()


if __name__ == '__main__':
    main()
