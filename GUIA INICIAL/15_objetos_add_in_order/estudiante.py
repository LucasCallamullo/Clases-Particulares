

import random


# clase, objeto, registro
class Estudiante:
    # constructor
    # edad (18, 25)     ; notas (0, 10)
    def __init__(self, nombre, edad, nota1, nota2, nota3):
        self.nombre = nombre                    # ctrl + d
        self.edad = edad
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def __str__(self):
        prom = calcular_promedio(self.nota1, self.nota2, self.nota3)

        cadena = "Nombre: " + self.nombre
        cadena += " | Edad: " + str(self.edad)
        cadena += " | Nota1: " + str(self.nota1)
        cadena += " | Nota2: " + str(self.nota2)
        cadena += " | Nota3: " + str(self.nota3)
        cadena += " | Promedio: " + str(prom)
        # cadena += " | Curso: " + "1K" + str(self.curso)
        return cadena


def calcular_promedio(nota1, nota2, nota3):
    p = (nota1 + nota2 + nota3) / 3
    return p


# ==================================================================
#                           Opcion 1
# ==================================================================
def validar_n():
    n = int(input("Cantidad de Estudiantes a cargar: "))
    while n <= 0:       # mientras n sea menor a 0
        n = int(input("Cantidad de Estudiantes a cargar(Debe ser un valor positivo): "))
    return n


def cargar_arreglo(v_est, n):

    nombres = "ABCDEF"
    # edad (18, 25)     ; notas (0, 10)
    # def __init__(self, nombre, edad, nota1, nota2, nota3):
    for i in range(n):      # 0 1   2           3
        nombre = random.choice(nombres)
        edad = random.randint(18, 25)
        nota1 = random.randint(0, 10)
        nota2 = random.randint(0, 10)
        nota3 = random.randint(0, 10)
        estudiantito = Estudiante(nombre, edad, nota1, nota2, nota3)
        v_est.append(estudiantito)
        # v_est = [ E, E, E ]


# ==================================================================
#                           Opcion 2
# ==================================================================
def mostrar_datos(v_est):
    #   v_est = [ E, E, E ]
    for i in v_est:
        # i = E
        print(i)





def menu():
    print("=" * 50)
    # alt + 92 = \
    print(" 1 - Cargar arreglo."
          "\n 2 - Mostrar datos."
          "\n 3 - "
          "\n 4 - "
          "\n 5 - ")

    return int(input("Ingresar opcion: "))


def principal():

    # vector / arreglo / lista principal
    v_est = list()          # []

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_est, n)

        elif op == 2:
            mostrar_datos(v_est)

        elif op == 3:
            pass

        elif op == 4:
            pass

        elif op == 5:
            pass







if __name__ == '__main__':
    principal()
