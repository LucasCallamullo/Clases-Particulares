
# Película: Define una clase Película con atributos como título, presupuesto, duración (1m , 180m), genero es un valor
# entre 1, 4 donde 1 = drama, 2= accion, 3= animada, 4= comedia en pantalla se debe mostrar el genero y no el numero.
# 1) crear una opcion donde el usuarrio cargue peliculas al arreglo segun una cantidad n, donde n es un valor ingresado
# por el usuario
# 2) Mostrar todos los datos ordenados por duracion de menor a mayor,


import random


class Pelicula:
    # dura (1, 180)
    def __init__(self, titulo, presupuesto, dura, gen):
        self.titulo = titulo            # Ctrl + d
        self.presupuesto = presupuesto
        self.dura = dura
        self.gen = gen

    def __str__(self):
        gen_str = gen_to_str(self.gen)
        cadena = "Titulo: " + self.titulo
        cadena += " | Presupuesto: " + str(self.presupuesto)        # Ctrl D
        cadena += " | Duración: " + str(self.dura)
        cadena += " | Genero: " + gen_str
        return cadena


def gen_to_str(gen):
    #             0        1          2          3
    generos = ["Drama", "Acción", "Animada", "Comedia"]
    # self.gen = 1, 2, 3, 4
    return generos[gen-1]


# ================================================================
#                       Opcion 1
# ================================================================
def cargar_arreglo(v_peli, n):
    tit = ("Shrek", "Nemo", "Polly", "Madagascar")

    for i in range(n):
        titulo = random.choice(tit)
        presupuesto = round(random.uniform(1, 10), 2)
        dura = random.randint(1, 180)       # Incluye a los numeroes que delimitan el intervalo
        gen = random.randint(0, 3)
        peli = Pelicula(titulo, presupuesto, dura, gen)
        v_peli.append(peli)


# ================================================================
#                       Opcion 2
# ================================================================
# i >  va a estar ordenado de menor a mayor
#   < j         Va a estar ordenado de mayor a menor
def ordenar(v_peli):
    n = len(v_peli)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_peli[i].dura > v_peli[j].dura:
                v_peli[i], v_peli[j] = v_peli[j], v_peli[i]


def mostrar_datos(v_peli):
    # v_peli [ PELI, PELI, PELI]
    for i in v_peli:
        print(i)




def menu():
    # alt + 92 = \
    print("=" * 50)
    print("1 - Cargar Arreglo."     # Ctrl + d 
          "\n 2 - Mostrar Datos."      
          "\n 3 -  "      
          "\n 4 -  "      
          "\n 5 - "     
          "\n 0 - Salir.")

    return int(input("Ingresar opcion: "))


def principal():

    # Nuestro vector con el que vamos a trabajar todo el programa
    v_peli = []

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = int(input("Ingresar cantidad de Peliculas a cargar: "))
            cargar_arreglo(v_peli, n)

        elif op == 2:
            ordenar(v_peli)
            mostrar_datos(v_peli)

        elif op == 3:
            pass

        elif op == 4:
            pass

        elif op == 5:
            pass

        elif op == 6:
            for i in v_peli:
                print(i)


if __name__ == '__main__':
    principal()
