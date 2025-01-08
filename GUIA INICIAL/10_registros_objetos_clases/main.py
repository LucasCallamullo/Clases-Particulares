
'''
'''
import random



class Estudiante:
    def __init__(self, leg, nom, n1, n2, n3):
        self.legajo = leg
        self.nombre = nom
        self.nota1 = n1
        self.nota2 = n2
        self.nota3 = n3
        self.prom = calcular_promedio(n1, n2, n3)


    def __str__(self):      # self.nombre = (1 , 10)
        nombre_real = nombre_to_str(self.nombre)

        cadena = " Legajo: " + str(self.legajo) + \
                 "\n Nombre: " + nombre_real + \
                 "\n Nota1: " + str(self.nota1) + \
                 "\n Nota2: " + str(self.nota2) + \
                 "\n Nota3: " + str(self.nota3) + \
                 "\n Promedio: " + str(self.prom)

        return cadena


def calcular_promedio(n1, n2, n3):
    prom = (n1 + n2 + n3) / 3
    return prom


def nombre_to_str(nombre):
    nombres = ("Lucas", "Matias", "")
    return nombres[nombre-1]




def cargar_arreglo(v_est, n):
    nombres = ("Lucas", "Matias")
    for i in range(n):
        legajo = random.randint(0, 100)
        nombre = random.choice(nombres)
        n1 = random.randint(0, 10)
        n2 = random.randint(0, 10)
        n3 = random.randint(0, 10)

        est = Estudiante(legajo, nombre, n1, n2, n3)
        v_est.append(est)



def main():
    v_est = list()

    n = int(input("Cuantos elementos carga? "))
    cargar_arreglo(v_est, n)



    print(v_est[0])


    op = -1
    while op != -1:
        pass




if __name__ == '__main__':
    main()

