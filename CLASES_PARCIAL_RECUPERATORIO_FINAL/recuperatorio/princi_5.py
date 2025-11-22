import random
import pickle
import os
from articulo import *

def menu():
    cadena_opciones = '\nMenú de Opciones:\n' + \
             '=================================================================\n' + \
             '1 - Cargar artículos en un vector.\n' \
             '2 - Mostrar el vector creado a razón de un artículo por línea.\n' \
             '3 - Crear un archivo con los artículos de un autor.\n' \
             '4 - Mostrar archivo de artículos (creado en el punto 3).\n' \
             '5 - Buscar un artículo por código.\n' \
             '6 - Analizar título.\n' \
             '0 - Salir.\n' \
             'Ingrese su opción: '
    return int(input(cadena_opciones))      # op


def cargar_articulo():
    posibles_titulos = ("Exploracion de las interacciones nanomateriales y biologicas en la medicina regenerativa.",
               "Mecanismos de resistencia antimicrobiana en patogenos emergentes.",
               "Efectos de la acidificacion oceanica en los ecosistemas marinos.",
               "Aplicaciones de la inteligencia artificial en la deteccion temprana de enfermedades cardiacas.",
               "Dinamica de poblacion y conservacion de especies en peligro de extincion.",
               "Neuroplasticidad y rehabilitacion despues de lesiones cerebrales traumaticas.",
               "Desarrollo de terapias genicas para enfermedades geneticas raras.",
               "Impacto del cambio climatico en la biodiversidad de los bosques tropicales.",
               "Tecnologias emergentes en la captura y almacenamiento de carbono.",
               "Efectos de la microbiota intestinal en la salud humana.",
               "Avances en la nanotecnologia aplicada a la medicina.",
               "Rol de la epigenetica en la regulacion de la expresion genica.")
    posibles_nombre_autores = ("Juan", "María", "Carlos", "Ana", "Antonio", "Laura", "Pedro", "Isabel", "Miguel",
                               "Carmen")
    posibles_apellidos_autores = ("García", "Rodríguez", "López", "Martínez", "Pérez", "González", "Hernández",
                                  "Sánchez", "Torres", "Fernández",)
    codigo = random.randint(10000, 100000)
    titulo = random.choice(posibles_titulos)
    nombre_autor = random.choice(posibles_apellidos_autores) + " " + random.choice(posibles_nombre_autores)

    return Articulo(codigo, titulo, nombre_autor)


def validar_mayor_que(limite, mensaje='Ingrese un número:'):
    num = limite        # num = 0
    while num <= limite:
        num = int(input(mensaje))       # 3
        if num <= limite:
            print('¡Error! El valor debe ser mayor a {}'.format(limite))
    return num      # 3


# =======================================================================
#               Opcion 1
# =======================================================================
def cargar_arreglo(vector, n):
    for i in range(n):
        # crear tus objetos a partir de la funcion que te dan
        articulo = cargar_articulo()
        add_in_order(vector, articulo)


def add_in_order(vector, articulo):
    der = len(vector) - 1
    izq = 0
    while izq <= der:
        c = (izq + der) // 2
        if vector[c].codigo == articulo.codigo:
            pos = c
            break
        elif vector[c].codigo > articulo.codigo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    vector[pos:pos] = [articulo]


# =======================================================================
#               Opcion 2
# =======================================================================
def mostrar_arreglo(vector):

    # vector = [ A1, A2, A3 ]
    for i in vector:
        # i = A1, A2
        print(i)

    # for i in range(len(vector)):        # range(3)
    #    # i = 0, 1, 2


# =======================================================================
#               Opcion 3
# =======================================================================
def generar_archivo_binario(vector, nombre_archivo):
    m = open(nombre_archivo, "wb")
    a = input("Ingresar autor: ")
    # ctrl + c --> copiar
    # ctrl + v --> para pegar

    for i in vector:
        # i = A1, A2, A3

        if i.nombre_autor == a:
            pickle.dump(i, m)

    m.close()       # OBLIGATORIO


# =======================================================================
#               Opcion 4
# =======================================================================
def mostrar_archivo_binario(nombre_archivo):

    # flag = os.path.exists(nombre_archivo)       # return True si el archivo existe, o FALSE si no existe
    # if not flag:

    if not os.path.exists(nombre_archivo):
        print("el archivo no existe:", nombre_archivo)
        return          # cortar la funcion

    #
    m = open(nombre_archivo, "rb")
    tamanio = os.path.getsize(nombre_archivo)

    # solo mostrar los articulos que tengan un codigo superior a "x" que se carga por teclado
    x = int(input("Ingresar codigo a superar: "))
    cont = 0

    while m.tell() < tamanio:
        # A1, A2, A3 ...
        art = pickle.load(m)    # retorna los objetos guardados

        if art.codigo > x:
            print(art)
            cont += 1

    print("Aparecieron registros guardados:", cont)

    m.close()


# =======================================================================
#               Opcion 5
# =======================================================================
def busqueda_binaria(vector):
    c = int(input("Ingresar codigo a buscar: "))

    der = len(vector) - 1
    izq = 0
    while izq <= der:
        centro = (izq + der) // 2
        # if vector[c].codigo == articulo.codigo:
        if vector[centro].codigo == c:

            # el objeto/articulo --> vector[c] --> A1, A2, ...
            print(vector[centro])

            # y retornar el título del mismo para utilizar luego en el ítem 6.
            return vector[centro].titulo     # string

            # pos = c
            # break
        # elif vector[c].codigo > articulo.codigo:
        elif vector[centro].codigo > c:
            der = centro - 1

        else:
            izq = centro + 1

    return "Artículo inexistente!."     # string


# =======================================================================
#               Opcion 6
# =======================================================================
def analizar_cadena(titulo_para_usar_punto_6):
    """
    ¿Cuál es la cantidad de palabras de esa cadena que comienza con la letra
    “a” (en mayúsculas o minúsculas)?

    comienza --> necesito un indice para saber donde estoy parado dentro de mi palaabra
                    o sea debe ser la posicion 1
    """
    r1 = 0
    indice = 0
    comienza_a = False

    # que termine con "u"
    ultima_letra = ""

    # cadena = "Hola Mundo."

    # titulo_para_usar_punto_6 = "Hola mundo."
    for i in titulo_para_usar_punto_6:
        # i = H, o, l, a,  , ...

        # dentro de la palabra
        if i != " " and i != ".":
            indice += 1

            if indice == 1 and i.lower() == "a":
                comienza_a = True

            # para ver con que letra termina mi palabra
            ultima_letra = i.lower()

        # fuera de la palabra o termino una palabra
        else:
            if comienza_a:      # if comienza_a == True
                r1 += 1

            if ultima_letra == "u":
                #   Cumple con esta condicion
                pass

            # apagar las banderas
            indice = 0
            comienza_a = False

    print("La cantidad de palabras que comienzan con a:", r1)


def principal():
    opcion = -1
    vector = []
    titulo_para_usar_punto_6 = None
    nombre_archivo = 'articulos_por_autor.dat'
    # fd

    while opcion != 0:
        opcion = menu()

        if opcion == 1:
            n = validar_mayor_que(0)
            vector = []
            cargar_arreglo(vector, n)

        elif opcion < 0 or opcion > 6:
            print('La opción elegida no es válida')

        elif len(vector) > 0:
            if opcion == 2:
                mostrar_arreglo(vector)

            elif opcion == 3:
                generar_archivo_binario(vector, nombre_archivo)

            elif opcion == 4:
                mostrar_archivo_binario(nombre_archivo)

            elif opcion == 5:
                titulo_para_usar_punto_6 = busqueda_binaria(vector)

            elif opcion == 6:

                if titulo_para_usar_punto_6 is None:
                    print("ingrese primero por la op 5")
                else:
                    analizar_cadena(titulo_para_usar_punto_6)

                    # analizar la cadena del titulo del primer registro del arreglo cargado en el punto 1
                    # titulo = vector[0].titulo
                    # analizar_cadena(titulo)

                    # analizar la cadena del titulo del ultimo registro del arreglo cargado en el punto 1
                    # ultimo = len(vector) - 1
                    # titulo = vector[ultimo].titulo
                    # analizar_cadena(titulo)

                    # analizar la cadena del titulo del ultimo registro del arreglo cargado en el punto 1
                    # centro = len(vector) // 2
                    # titulo = vector[centro].titulo
                    # analizar_cadena(titulo)
        else:
            print('Primero debe ejecutar la opción 1')


if __name__ == "__main__":
    principal()



# si una variable "n" esta igualada a una funcion,
# es porque espera que la funcion retorne algun valor
# n = validar_mayor_que(0)