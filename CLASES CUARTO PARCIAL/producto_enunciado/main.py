import os.path
import pickle
import random



class Producto:
    # marca (55, 60)    ; categoría (1: Electrónica, 2: Ropa, 3: Alimentos).
    def __init__(self, nombre, id, precio, marca, categoria):
        self.nombre = nombre
        self.id = id
        self.precio = precio
        self.marca = marca
        self.categoria = categoria

    def __str__(self):
        # self.categoria(1,3) 1-1        2-1         3-1
        # indices               0           1           2
        desc_categorias = ("Electronica", "Ropa", "Alimentos")

        cad = "Nombre: " + self.nombre
        cad += " | ID: " + str(self.id)
        cad += " | precio: " + str(self.precio)
        cad += " | marca: " + str(self.marca)
        cad += " | categoria: " + desc_categorias[self.categoria-1]

        # cad += " | Curso: " + "1K" + str(self.curso)
        return cad


# ================= Opcion 1 ==========================
def validar_n():
    n = int(input("Ingresar cantidad de Casos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de Casos a cargar(Debe ser positivo): "))
    return n


def cargar_arreglo(v_prod, n):
    descripciones = "ABCDEF"
    for i in range(n):          # 3         0       1       2
        nombre = random.choice(descripciones) + random.choice(descripciones)
        id = random.randint(1, 15)
        precio = round(random.uniform(0.1, 10), 2)
        marca = random.randint(55, 60)
        categoria = random.randint(1, 3)
        prod = Producto(nombre, id, precio, marca, categoria)
        add_in_order(v_prod, prod)


def add_in_order(v_prod, prod):             # primera vuelta  len = 0   prod.id = 5
    izq, der = 0, len(v_prod) - 1           # segunda vuelta  len = 1  prod.id = 3

    while izq <= der:
        c = (izq + der) // 2
        if v_prod[c].id == prod.id:
            pos = c
            break
        elif v_prod[c].id > prod.id:            # si se come al vector esta de menor a mayor
            der = c - 1                         # se se come al objeto esta de mayor a menor
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    #            0      1
    # v_prod = [ P2,    P1     ]

    v_prod[pos:pos] = [prod]


# ================= Opcion 2 ==========================
def mostrar_datos(v_prod):
    # for i in range(len(v_prod)):
    # i = 0 , 1 , 2 ,3 ... print(v_prod[i])

    for producto in v_prod:
        # i = P1, P2, P3 ..
        print(producto)


def generar_matriz(v_prod):
    # crear matriz con 0
    # marca (55, 60)    ; categoría (1: Electrónica, 2: Ropa, 3: Alimentos).
    filas = 3   # categoria
    columnas = 6    # marca
    matriz_conteo = [[0] * columnas for i in range(filas)]
    # [ [0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0, 0] ]

    # indices               0                       1                       2
    # matriz_conteo =  [ [0, 0, 0, 0, 0, 0],     [0, 0, 0, 0, 0, 0],     [0, 0, 0, 0, 0, 0] ]


    # rellenar la matriz
    for i in v_prod:
        matriz_conteo[i.categoria-1][i.marca-55] += 1

    # mostrar matriz
    desc_categorias = ("Electronica", "Ropa", "Alimentos")
    for f in range(len(matriz_conteo)):              # f = 0 1 2 3 4 5
        for c in range(len(matriz_conteo[0])):           # c = 0 1 2
            if matriz_conteo[f][c] > 0 and c+55 > 57:
                print("La cantidad por Marca:", c+55, "Y Categorias:", desc_categorias[f])
                print("La cantidad total es:", matriz_conteo[f][c])


# ================= Opcion 4 ==========================
def generar_archivo(fd, v_prod, x):

    # with open(fd, "wb") as file:
    file = open(fd, "wb")
    cont = 0
    for i in v_prod:
        if i.precio > x and (i.categoria == 3 or i.categoria == 1):
            pickle.dump(i, file)
            file.flush()       # no es necesario
            cont += 1

    print("Se cargaron la cantidad de productos de:", cont)
    file.close()    # ES NECESARIO


# ================= Opcion 5 ==========================
def mostrar_archivo(fd):
    if os.path.exists(fd):
        m = open(fd, "rb")
        tam = os.path.getsize(fd)

        cont = acum = 0

        while m.tell() < tam:
            prod = pickle.load(m)
            print(prod)
            if prod.marca <= 57:
                cont += 1
                acum += prod.precio

        if cont > 0:
            prom = acum / cont
            print("El promedio de las marcas menos o iguales a 57 es:", prom)
        else:
            print("No se encontraron marcas menos a 57")

        m.close()
    else:
        print("No existe el archivo:", fd, "Por favor ingrese primero por la opcion 4.")


# ================= Opcion 6 ==========================
def busqueda_secuencial(v_prod, cat):
    se_encontro = False

    for i in range(len(v_prod)):
        if v_prod[i].categoria == cat:
            print(v_prod[i])
            se_encontro = True

    if not se_encontro:         # es false
        print("No se encontro ningun objeto de esa categoria")


# ================= Opcion 7 ==========================
def busqueda_binaria(v_prod, x):
    izq, der = 0, len(v_prod) - 1
    while izq <= der:
        c = (izq + der) // 2
        if v_prod[c].id == x:
            return c
        elif v_prod[c].id > x:            # si se come al vector esta de menor a mayor
            der = c - 1                   # se se come al objeto esta de mayor a menor
        else:
            izq = c + 1
    return -1



def menu():
    print("=" * 50)
    print(" 1 - Cargar arreglo"
          "\n 2 - Mostrar dats"
          "\n 3 - Matriz"
          "\n 4 - Generar Archivo"
          "\n 5 - Mostrar Archivo"
          "\n 6 - Busqueda secuencial."
          "\n 7 - Busqueda binaria.")

    return int(input("Ingresar opcion: "))


def main():

    # arreglo principal
    v_prod = []

    # nombre del archivo principal
    fd = "productos.dat"


    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_prod, n)

        elif op == 2:
            mostrar_datos(v_prod)

        elif op == 3:
            generar_matriz(v_prod)

        elif op == 4:
            x = float(input("Precio a supérar para guardar en el archivo: "))
            generar_archivo(fd, v_prod, x)

        elif op == 5:
            mostrar_archivo(fd)

        elif op == 6:
            cat = int(input("Ingresar categoria a buscar: "))
            busqueda_secuencial(v_prod, cat)

        elif op == 7:
            x = int(input("Ingresar id a buscar: "))
            pos = busqueda_binaria(v_prod, x)
            if pos >= 0:
                print(v_prod[pos])
                # print(v_prod[pos].categoria, v_prod[pos].precio)

                if v_prod[pos].categoria == 1:
                    print("Opcion no ecologica.")

                t = float(input("Ingrese nuevo valor a modificar: "))
                v_prod[pos].precio = t

                # ponerle un recargo del 10%
                v_prod[pos].precio = v_prod[pos].precio * 1.1

                # datos actualizados
                print(v_prod[pos])

            else:
                print("No se encontro el id buscado.")




if __name__ == '__main__':
    main()

