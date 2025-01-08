
 # Estudiante: Crea una clase Estudiante con atributos como nombre, edad, calificaciones(nota1 y nota2).
 # por opciones cargar arreglo segun n donde n es un valor ingresado por el usuario,
 # calcular el promedio y mostrar información personal.


 # De todos los objetos  su constructor, su propia funcion de print
 # De todos hacer un menu con 2 opciones, Cargar arreglo, Mostrar datos




import random


class Estudiante:
    # constructor
    def __init__(self, nombre, edad, nota1, nota2):
        self.nombre = nombre                # Ctrl + d
        self.edad = edad
        self.nota1 = nota1
        self.nota2 = nota2

    # su propia funcion de print
    def __str__(self):
        cadena = "Nombre: " + self.nombre
        cadena += "| Edad: " + str(self.edad)
        cadena += "| Nota1: " + str(self.nota1)
        cadena += "| Nota2: " + str(self.nota2)
        return cadena


# =========================================
# Opcion 1
def cargar_arreglo(v_est, n):
    nombres = ("Lucas", "Matias", "Tomas", "Jere")
    for i in range(n):
        nombre = random.choice(nombres)
        edad = random.randint(18, 25)
        nota1 = random.randint(1, 10)
        nota2 = random.randint(1, 10)
        est = Estudiante(nombre, edad, nota1, nota2)
        v_est.append(est)


# ==================================
# opcion 2
def calcular_prom(v_est):
    # v_est = [est, est, est]
    for i in v_est:
        prom = (i.nota1 + i.nota2) / 2
        print(i)
        print("Su promedio es:", prom)
        print("=" * 50)


# ==================================
# opcion 3
def mostrar_datos(v_est):
    for i in v_est:
        # if i.edad > 20:
        print(i)


def menu():
    print("=" * 50)
    print(" 1 - Cargar Estudiantes."
          "\n 2 - Calcular Promedio."
          "\n 3 - Mostrar Datos."
          "\n 0 - Salir.")
    return int(input("Ingresar opcion: "))


def main():

    # Nuestro Vector con el que vamos a trabajar durante el programa
    v_est = []


    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            n = int(input("Cantidad de estudiantes a cargar: "))
            cargar_arreglo(v_est, n)

        elif op == 2:
            calcular_prom(v_est)

        elif op == 3:
            mostrar_datos(v_est)


if __name__ == '__main__':
    main()
