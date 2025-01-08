
# Tele: marca, precio/importe > 0 , pulgadas(32, 50), sistema op, año(2000, 2022)


# 1) crear una opcion donde el usuarrio cargue peliculas al arreglo segun una cantidad n, donde n es un valor ingresado
# por el usuario
# 2) Mostrar todos los datos ordenados por algun atributo (elegi el atributo)(menor a mayor; o mayor a menor elegi),
import random


class Tele:

    # constructor del objeto
    #  precio/importe > 0 ; pulgadas(32, 50) ; año(2000, 2022)
    def __init__(self, marca, importe, pulgada, sist_op, year):
        self.marca = marca            # ctrl + d
        self.importe = importe
        self.pulgada = pulgada
        self.sist_op = sist_op
        self.year = year

    # la funcion que nos devuelve un print del objeto
    def __str__(self):
        cadena = "Marca: " + self.marca
        cadena += " | Importe: " + str(self.importe)        # ctrl d
        cadena += " | Pulgada: " + str(self.pulgada)
        cadena += " | Sist Op: " + self.sist_op
        cadena += " | Año: " + str(self.year)
        return cadena


# opcion 1
def validar_n():
    n = int(input("Ingresar cantidad de Teles a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de Teles a cargar (Por favor ingrese un numero positivo): "))
    return n


def cargar_arreglo(v_tele, n):
    marcas = ("Lg", "Hitachi", "Samsung", "Sony")
    sistemas = ("A", "B", "C", "D")
    for i in range(n):  # 5
        marca = random.choice(marcas)
        # para los valores flotanes se usa uniform
        importe = round(random.uniform(0.1, 10), 2)
        pulgada = random.randint(33, 49)
        sist_op = random.choice(sistemas)
        year = random.randint(2000, 2022)
        tv = Tele(marca, importe, pulgada, sist_op, year)
        # v_tele = [ T, T, T, T, T ]
        v_tele.append(tv)


# opcion 2
def ordenar(v_tele):
    n = len(v_tele)
    for i in range(n-1):
        for j in range(i+1, n):
            # lo unico que cambia es la condicion que depende del atributo que quieras ordenar
            if v_tele[i].marca > v_tele[j].marca:
                v_tele[i], v_tele[j] = v_tele[j], v_tele[i]


def mostrar_datos(v_tele, x, t):
    # for i in range(len(v_tele)):
    #    print(v_tele[i])

    for i in v_tele:
        # i = T ,T ; T
        if i.importe > x and i.sist_op != t.upper():
            print(i)



def menu():
    print("=" * 50)
    # alt + 92 = \          ;           \n salto de linea
    # print(" 1 - Cargar .")        # con ctrl + d copias la linea en la que esta el mouse
    # print(" 2 -  .")
    # print(" 3 -  .")
    # print(" 4 -  .")
    print(" 1 - Cargar arreglo."
          "\n 2 - Mostrar datos"
          "\n 3 - "
          "\n 4 - ")
    op = int(input("Ingresar opcion: "))
    return op


def main():

    # vector ( arreglo / lista ) etc principal con el que vamos a trabajar.
    v_tele = []         # list()


    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_tele, n)

        elif op == 2:
            ordenar(v_tele)

            # importe a superar
            x = float(input("Ingresar importe a superar: "))
            # Sistemas distinto a t
            t = input("Ingresar Sistemas que no es: ")

            mostrar_datos(v_tele, x, t)

        elif op == 3:
            pass

        elif op == 4:
            pass

        elif op == 6:
            # v_tele = [ T, T, T, T, T ]
            for i in v_tele:
                # i = T, T, T
                print(i)







# si pones main se agrega la condicion
if __name__ == '__main__':
    main()
