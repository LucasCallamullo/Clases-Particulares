import os.path
import pickle
import random


class Articulo:
    # genero (1, 4) 1:estadistica, 2:datos, 3:ciencia, 4:investigacion; autor(100, 103)
    def __init__(self, codigo, titulo, nombre, genero, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.nombre = nombre
        self.genero = genero
        self.autor = autor

    def __str__(self):
        generos = ("estadistica", "datos", "ciencia", "investigacion")
        cadena = "Codigo: " + str(self.codigo)
        cadena += " | Titulo: " + self.titulo
        cadena += " | Nombre: " + self.nombre
        cadena += " | Genero: " + generos[self.genero-1]
        cadena += " | Autor: " + str(self.autor)
        return cadena


# ================= Opcion 1 ==========================
def validar_n():
    n = int(input("Ingresar cantidad de Mascotas a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de Mascotas a cargar(Debe ser positivo): "))
    return n


def cargar_arreglo(v_arti, n):
    titulos = ("Datos.", "Personas.", "Enfermedades.", "Animales.")
    nombres = "ABCDEF"

    for i in range(n):      # n = 3             0           1
        codigo = random.randint(1, 15)
        titulo = "La investigacion de " + random.choice(titulos)
        nombre = random.choice(nombres)
        genero = random.randint(1, 4)
        autor = random.randint(100, 103)
        arti = Articulo(codigo, titulo, nombre, genero, autor)
        add_in_order(v_arti, arti)


def add_in_order(v_arti, arti):
    izq, der = 0, len(v_arti) - 1
    while izq <= der:
        c = (izq + der) // 2
        if v_arti[c].codigo == arti.codigo:
            pos = c
            break
        elif v_arti[c].codigo > arti.codigo:       # si se come al vector esta de menor a mayor
            der = c - 1                                 # si se come al objeto esta de mayor a menor
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_arti[pos:pos] = [arti]


def mostrar_datos(v_arti):
    for i in v_arti:
        print(i)


'''
Recorra el archivo que generó en el punto 3, y genere a partir de él un arreglo unidimensional de 
valores de tipo float, que contenga en cada casilla solo el monto de producción de los eventos del 
archivo cuyo tipo de evento sea mayor o igual a 5. Muestre el arreglo generado de esta forma, y al
 final del listado agregue una línea adicional indicando el promedio de los montos mostrados.
'''
def buscar_en_un_archivo(fd, pos):

    if os.path.exists(fd):
        m = open(fd, "rb")
        v_acum = [0.0] * 15     # cantidad de tipos de eventos

        #           0  1  2  3     5
        # v_acum = [0, 0, 0, 0, 0, 0 ]

        # matriz = [[0] * 15 for i in range(1)]
        tam = os.path.getsize(fd)
        cont = acum = 0
        while m.tell() < tam:
            arti = pickle.load(m)
            if arti.tipo >= 5:
                v_acum[arti.tipo] += arti.importe
                cont += 1
                acum += arti.importe


def busqueda_binaria(v_arti, cod):
    izq, der = 0, len(v_arti) - 1
    while izq <= der:
        c = (izq + der) // 2
        if v_arti[c].codigo == cod:
            return c
        elif v_arti[c].codigo > cod:       # si se come al vector esta de menor a mayor
            der = c - 1                    # si se come al objeto esta de mayor a menor
        else:
            izq = c + 1

    return -1


def busqueda_secuencial(v_arti, cod):
    for i in range(len(v_arti)):
        # i = 0 1 2 3  ...
        if v_arti[i].codigo == cod:
            return i
    return -1


def analizar_cadena(cadena_op5):
    print("La cadena a analizar es:", cadena_op5)

    #         12340123450
    cadena = "Aola Ataud2."
    print(cadena)


    indice = 0

    empieza_con_a = False
    cont_empieza_a = 0

    mayuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    numeros = "0123456789"
    tiene_numero = False

    vocales = "aeiou"

    for i in cadena:
        # i = H, o, l, a,  , M, u,


        if i != " " and i != ".":

            # el original era este
            indice += 1
            if indice == 1 and i.lower() == "a":
                empieza_con_a = True
                
            # si aparte tenia un numero dentro de la palabra
            if i in numeros:
                tiene_numero = True
            
            # if "0" <= i <= "9": 
            

            # si te piden que tenga al menos una vocal
            if i.lower() in vocales:
                pass
                 
            # si nos pidiera comprobar si empieza con mayuscula
            if indice == 1 and "A" <= i <= "Z": # i.isupper():
                pass

        else:
            if empieza_con_a and tiene_numero:
                cont_empieza_a += 1

            # apagar todo
            indice = 0
            empieza_con_a = False


    print("La cantidad de palabras que empieza con a es:", cont_empieza_a)


def analizar_cadena_2(cadena_op5):
    cadena = "Aola Ataud2."
    print(cadena)

    # cadena = "animal lucas"
    cadena = "empanada emprendedor"

    # supongamos que tenemos que contar todas las palabras que tienen mas vocales que consonantes
    vocales = "aeiou"

    cont_vocales = 0
    cont_consonantes = 0

    cant_palabras_cumplen = 0


    # banderas
    tiene_m = False
    tiene_mp = False

    palabra = ""
    indice = 0
    ult_caracter = ""
    for i in cadena:

        if i != " " and i != ".":

            if i.lower() in vocales:
                cont_vocales += 1

            else:
                if "a" <= i.lower() <= "z":
                    cont_consonantes += 1

            # que si tiene una m seguida de una p
            if tiene_m:
                if i.lower() == "p":
                    tiene_mp = True
                else:
                    tiene_m = False

            if i.lower() == "m":
                tiene_m = True


            indice += 1
            palabra += i

            if indice == 1 and ult_caracter == i:
                pass

        else:
            ult_caracter = palabra[:-1]


            if cont_vocales > cont_consonantes:
                cant_palabras_cumplen += 1

            if tiene_mp:
                pass # contador_palabras += 1

            cont_vocales = 0
            cont_consonantes = 0


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

    v_arti = []


    validar_op5 = False



    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            v_arti = []
            n = validar_n()
            cargar_arreglo(v_arti, n)

        elif op == 2:
            mostrar_datos(v_arti)


        elif op == 5:
            c = int(input("Ingresar codigo a buscar: "))
            pos = busqueda_binaria(v_arti, c)
            # pos = busqueda_secuencial(v_arti, c)

            if pos >= 0:
                print(v_arti[pos])

                # que te pidan cambiar el numero del autor por un autor t
                # t = int(input("Ingresar nuevo autor a modificar: "))
                # v_arti[pos].autor = t

                # aumentar su importe un 10 por ciento
                # v_arti[pos].importe = v_arti[pos].importe + v_arti[pos].importe * 0.1

                # si el genero fuera datos mostrar un mensaje adicional que diga recomendado
                # if v_arti[pos].genero == 3:
                #    print("Recomendado!")

                # datos actualizados
                # print(v_arti[pos])

                cadena_op5 = v_arti[pos].titulo

                validar_op5 = True

            else:
                print("Articulo inexistente!")

        elif op == 6:
            if validar_op5:
                analizar_cadena(cadena_op5)

            else:
                print("Primero debe ingresar a la opcion 5")




if __name__ == '__main__':
    main()
