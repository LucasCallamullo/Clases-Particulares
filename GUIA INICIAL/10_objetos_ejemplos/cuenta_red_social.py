

 # Coche: Crea una clase Coche con atributos como marca es un valor entre (1 y 4) validar este valor donde 1 = Peugot
 # 2 = Citroen, 3 = Ford, 4 = Audi por pantalla se debe mostrar la marca que corresponda segun el numero,
 # nombre del modelo, año de fabricación es un valor entre 2000 y 2010, precio (1, 10)

 # 1 ) Cargar arreglo de n tamaño donde n es un numero ingresado por el usuario.
 # 2 ) Mostrar el arreglo ordenado por modelo en orden alfabetico, que tengan un precio mayor a t donde t es un valor
 # ingresado por teclado
 # 3 )


import random
# from registro import *


class Coche:
    # marca ( 1, 4)             año(2000, 2010)  precio 1, 10
    def __init__(self, marca, modelo, year, precio):
        self.marca = marca      # ctrl + d
        self.modelo = modelo
        self.year = year
        self.precio = precio

    def __str__(self):
        # self.marca = 1, 2, 3, 4
        marca_str = marca_to_str(self.marca)

        cadena = "Marca: " + marca_str         # ctrl + d
        cadena += " | Modelo: " + self.modelo
        cadena += " | Año: " + str(self.year)
        cadena += " | Precio: " + str(self.precio)
        return cadena


def marca_to_str(marca):
    # marca =           1,         2,      3,      4
    #                   0           1       2       3
    lista_marcas = ["Peugot", "Citroen", "Ford", "Audi"]
    m = lista_marcas[marca - 1]
    return m


# ==================================================
#               Opcion 1
# ==================================================
def cargar_arreglo(v_coche, n):
    # marca ( 1, 4)             año(2000, 2010)  precio 1, 10
    # def __init__(self, marca, modelo, year, precio):
    modelos_str = ("A", "B", "C", "D")

    for i in range(n):
        marca = random.randint(1, 4)
        modelo = random.choice(modelos_str)
        year = random.randint(2000, 2010)
        # Subir bien un valor flotante
        precio = round(random.uniform(1, 10), 2)
        cochecito = Coche(marca, modelo, year, precio)
        v_coche.append(cochecito)


# ==================================================
#               Opcion 2
# ==================================================
# Que este ordenado alfabeticamente por modelo
#   Si la boquita se come a la i --->           i > esta ordenado de menor a mayor
#   Si la boquita se come a la j --->           < j esta ordenado de mayor a menor
def ordenar(v_coche):
    n = len(v_coche)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_coche[i].modelo > v_coche[j].modelo:
                v_coche[i], v_coche[j] = v_coche[j], v_coche[i]


def mostrar_datos(v_coche, t):
    #   0 1 2 3 4
    #  [ C, C, C, C
    for i in v_coche:
        if i.precio > t:
            print(i)


def menu():
    print("=" * 50)
    print(" 1 - Cargar arreglo."
          "\n 2 - Mostrar datos."
          "\n 3 - ."
          "\n 4 - ."
          "\n 5 - ."
          "\n 0 - Salir.")
    return int(input("Ingresar opcion: "))


def main():

    # vector general con el que vamos a trabajar
    v_coche = []

    # validar op_1
    validar_op1 = False


    op = -1
    while op != 0:

        op = menu()

        # not validar_op1 = False
        if not validar_op1:
            if op == 1:
                n = int(input("Ingresar cantidad de coches a cargar: "))
                cargar_arreglo(v_coche, n)
                validar_op1 = True
            else:
                print("Tiene primero que elegir la opcion 1.")

        else:
            if op == 1:
                n = int(input("Ingresar cantidad de coches a cargar: "))
                cargar_arreglo(v_coche, n)

            elif op == 2:       # ctrl + d
                ordenar(v_coche)
                t = float(input("Ingresar precio a comparar: "))
                mostrar_datos(v_coche, t)

            elif op == 3:
                pass

            elif op == 4:
                pass

            elif op == 6:
                for i in v_coche:
                    print(i)


# pones main
if __name__ == '__main__':
    main()
