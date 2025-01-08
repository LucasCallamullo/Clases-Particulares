# Coche: Crea una clase Coche con atributos como titular, marca(1, 4), año de fabricación(2000, 2004),
# precio que sea mayor a 0

# 1 - Cargar un arreglo de registros con los datos de n Coches (cargar n por teclado y
# validar que sea positivo), de manera que entodo momento el arreglo se mantenga ordenado
# por titular alfabeticamente. Para esto debe utilizar el algoritmo de inserción ordenada con búsqueda binaria
# ( add_in_order )

# 2 - Mostrar el arreglo uno por linea pero en marca en vez de mostrar el valor entero se debe mostrar
# marcas = (1:"Fiat", 2:"Peugot", 3:"Audi", 4:"Citroen") segun corresponda, tambien solo se deben mostrar
# los que superen un importe t ingresadop por teclado.

# 3 - MATRICES
# mostrar los importes acumulados por marca y año de fabricacion segun corresponda, pero solo debe
# mostrar los años menores o igual a 2002 y con importes acumulados distintos de 0

# 4 - A partir del arreglo generar un archivo binario donde se incluyan los datos de todos los coches
# que superen un valor/precio t ingresado por teclado

# 5 - Mostrar el archivo generado en el punto anterior indicando además al final una línea
# extra con el promedio de los precios de los autos que estaban en el archivo


# 7 - buscar a un titular p donde p es un valor que se ingresa por teclado si existe mostrar sus datos,
# y si existe ademas si la marca fuera Audi o Citroen mostrar un mensaje "marca premium"
# si no existe informar al usuario.

# 8 - buscar un año de fabricazion igual a x donde x es un valor ingresado por el usuario, si existe mostrar
# todos sus datos, si no existe debe informar al usuario. si existiera mas de uno debe mostrar todos.


import os.path
import pickle
import random


class Coche:
    # su constructor
    def __init__(self, titular, marca, year, importe):
        self.titular = titular  # ctrl + d
        self.marca = marca
        self.year = year
        self.importe = importe

    # su funcion de print
    def __str__(self):  # ctrl + d

        marca_str = marca_to_str(self.marca)  # 1 2 3 4

        cadena = "Titular: " + self.titular
        cadena += " | Marca: " + marca_str
        cadena += " | Año: " + str(self.year)
        cadena += " | Precio: " + str(self.importe)
        return cadena


def marca_to_str(marca):  # 500 503
    #        500-500    501-501   502-502  503-503
    # marca    1-1      2-1       3-1      4-1

    # indice     0       1         2         3
    marcas = ["Fiat", "Peugot", "Audi", "Citroen"]
    marca_str = marcas[marca - 1]
    return marca_str


# =========== Opcion 1 ====================
def validar_n():
    n = int(input("Ingresar cantidad de Coches a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de Coches a cargar ( Debe ser positivo ): "))
    return n


def cargar_arreglo(v_coche, n):  # 4

    nombres = "ABCDE"
    for i in range(n):
        # i = 0          1          2           3
        # def __init__(self, titular, marca, year, importe):
        titular = random.choice(nombres)
        marca = random.randint(1, 4)
        year = random.randint(2000, 2004)
        # Flotantes
        importe = round(random.uniform(1, 10), 2)
        cochecito = Coche(titular, marca, year, importe)
        add_in_order(v_coche, cochecito)


def add_in_order(v_coche, cochecito):
    izq, der = 0, len(v_coche) - 1  # = 0       cochecito.titular = C
    # = 1       cochecito.titular = B

    while izq <= der:  # mientras izq sea menor o igual a derecha
        c = (izq + der) // 2
        if v_coche[c].titular == cochecito.titular:
            pos = c
            break
        elif v_coche[c].titular > cochecito.titular:  # v[c] > es de menor a mayor
            der = c - 1  # v[c] < es de mayor a menor
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_coche[pos:pos] = [cochecito]


# =========== Opcion 2 ====================
def mostrar_datos(v_coche, t):
    # v_coche = [ C, C, C, C ]

    # Mostrar cantidad de prints al final
    cont = 0
    for i in v_coche:
        if i.importe > t:
            print(i)
            cont += 1

    print("Se mostraron", cont, "Coches.")


# =========== Opcion 4 ====================
def generar_archivo_binario(v_coche, fd, t):
    # wb = siempre crea/genera un archivo nuevo desde cero, es decir si existe lo sobreescribe desde cero
    m = open(fd, "wb")

    se_genero_archivo = False
    for i in v_coche:
        if i.importe > t:
            pickle.dump(i, m)
            m.flush()  # es opcional
            se_genero_archivo = True

    if se_genero_archivo:  #
        print("Se genero correctamente el archivo:", fd)
    else:
        print("No se genero ningun archivo esta vuelta de ciclo.")

    m.close()  # va si o si


# =========== Opcion 5 ====================
def mostrar_archivo_binario(fd):
    if os.path.exists(fd):
        m = open(fd, "rb")

        # prom = acum / cant
        cant, acum = 0, 0

        tam = os.path.getsize(fd)  # len(          ; 75 bytes
        # vector = [ 1 , 4 , 5 ]
        # fd    = [ C  ][  C ][   C ]
        #         0    25    50     75
        while m.tell() < tam:
            cochecito = pickle.load(m)
            print(cochecito)
            cant += 1
            acum += cochecito.importe

        prom = 0
        if cant > 0:
            prom = acum / cant
        print("El promedio de los importes de los coches mostrados es:", prom)

        m.close()  # va si o si

    else:
        print("No se encontro el archivo para leer, debe pasar por la opcion 4 primero.")


# =========== Opcion 7 ====================
def busqueda_binaria(v_coche, p):  # p = C         E
    # v_coche [ A , A , B , C , D ]
    #                   c , c

    izq, der = 0, len(v_coche) - 1  # izq = 3   der = 4
    while izq <= der:  # mientras izq sea menor o igual a derecha
        c = (izq + der) // 2
        if v_coche[c].titular == p:
            return c
        elif v_coche[c].titular > p:  # v[c] > es de menor a mayor
            der = c - 1  # v[c] < es de mayor a menor
        else:
            izq = c + 1
    return -1


# =========== Opcion 8 ====================
def busqueda_lineal(v_coche, x):
    se_encontro = False
    # v_coche [ C , C , C , C , C ]
    for i in range(len(v_coche)):  # tamaño del vector/lista/arreglo
        # i = 0 1 2 3
        if v_coche[i].year == x:
            print(v_coche[i])
            se_encontro = True

    if not se_encontro:  # se_encontro = False
        print("No se encontro el año ingresado.")


# marca(1, 4), año de fabricación(2000, 2004), precio que sea mayor a 0
def generar_matriz(v_coche):
    #   0,0 0,1 0,2
    # [ [0, 0, 0, 0],
    #   [0, 0, 0, 0] ]
    #   1,0 1,1

    col = 4
    filas = 5
    matriz = [[0] * col for f in range(filas)]

    # print(matriz)

    # marcas = (0:"Fiat", 1:"Peugot", 2:"Audi", 3:"Citroen")
    # marcas = (1:"Fiat", 2:"Peugot", 3:"Audi", 4:"Citroen")
    # marca(1, 4), año de fabricación(2000, 2004),
    for i in v_coche:
        # i = C , C , C, C, C
        #       FILAS       COLUMNA
        matriz[i.year - 2000][i.marca - 1] += i.importe

    # mostrar los años menores o igual a 2002 y con importes acumulados distintos de 0
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if f <= 2 and matriz[f][c] > 0:
                print("En el año:", f + 2000, "Y de la marca:", c + 1)
                print("Su importe acumulado es:", matriz[f][c])
                print("=" * 50)

    # [[8.98, 0, 0, 0],
    # [0, 7.03, 0, 0],
    # [0, 6.42, 0, 0],
    # [0, 0, 0, 0],
    # [0, 0, 6.5, 0]]

    # print(matriz)
    # f = cabinas   = 5
    # c = vehiculos = 3

    for f in range(len(matriz)):  # f = 0, 1, 2, 3, 4
        # f = 1
        acum = 0
        for c in range(len(matriz[0])):  # c = 0, 1 ,2
            acum += matriz[f][c]

        print("El acumulado de las cabinas", f, "es igual a:", acum)

    for c in range(len(matriz[0])):  # c = 0, 1 ,2
        # c = 0, 1
        acum = 0
        for f in range(len(matriz)):  # f = 0, 1, 2, 3, 4
            acum += matriz[f][c]

        print("El acumulado de las vehiculos", c, "es igual a:", acum)


def menu():
    print("=" * 50)
    # alt + 92 = \
    print(" 1 - Cargar arreglo"
          "\n 2 - "  # ctrl + d
          "\n 3 - "
          "\n 4 - "
          "\n 5 - "
          "\n 0 - Salir.")
    x = int(input("Ingresar opcion: "))
    return x


def principal():
    # vector / lista / arreglo principal
    v_coche = []

    # archivo binario principal
    fd = "datos.dat"

    op = -1
    while op != 0:
        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_coche, n)

        elif op == 2:
            t = float(input("Ingrese precio a superar: "))
            mostrar_datos(v_coche, t)

        elif op == 3:
            generar_matriz(v_coche)

        elif op == 4:
            t = float(input("Guardar los que superen el precio de: "))
            generar_archivo_binario(v_coche, fd, t)

        elif op == 5:
            mostrar_archivo_binario(fd)

        elif op == 6:
            # v_coche = [ C, C, C, C, C ]
            for i in v_coche:
                # i = C
                print(i)

        elif op == 7:
            p = input("Ingresar titular a buscar (ABCDE): ")
            pos = busqueda_binaria(v_coche, p)

            if pos >= 0:
                print(v_coche[pos])
                # if 3 <= v_coche[pos].marca <= 4:
                if v_coche[pos].marca == 3 or v_coche[pos].marca == 4:
                    print("Marca Premium")
            else:
                print("No se encontro el titular buscado.")

        elif op == 8:
            x = int(input("Ingresar año a buscar (2000-2023): "))
            busqueda_lineal(v_coche, x)


if __name__ == '__main__':
    principal()
