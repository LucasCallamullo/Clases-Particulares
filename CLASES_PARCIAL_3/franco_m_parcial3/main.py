

class Estudiante:
    # Legajo , Nombre (str) , Carrera ( 1, 4 ), cuota importe ( float )
    def __init__(self, legajo, nombre, carrera, importe):         # funcion constructor o inicializadora de la clase
        # ctrl + d
        self.legajo = legajo
        self.nombre = nombre
        self.carrera = carrera
        self.importe = importe

    def __str__(self):
        # alt + 92
        # indices              0        1           2            3
        # valores              1        2           3            4
        tupla_carreras = ("Sistemas", "Civil", "Industrial", "Quimica")

        # cadena = (f"Legajo: {self.legajo} | "
        #          f"Nombre: ")
        cadena = "Legajo: " + str(self.legajo)
        cadena += " | Nombre: " + self.nombre
        cadena += " | Carrera: " + tupla_carreras[self.carrera-1]
        cadena += " | Importe: " + str(self.importe)
        return cadena


def principal2():
    # creamos el objeto y lo igualamos a la variable est1
    est1 = Estudiante(1, "lucas", 2, 10.0)
    est2 = Estudiante(2, "franco", 3, 15.0)

    # est1.legajo = 3
    print(est1)
    print(est2)


def principal():

    # listas vacías
    listas = []         # lista vacía
    listas = list()     # lista vacia

    # listas arreglos arrays vectores
    tupla = ("a", "b", "c")         # variable no mutable

    #          0    1    2
    listas = ["a", "b", "c"]        # variable mutable
    listas[0] = "a"
                  # 3
    listas.append("d")      #

    print("tupla:", tupla)

    print("lista:", listas)

    # ["a", 'b', 'c', 'd']
    for i in listas:
        # i = a, b, c, d
        print(i)

    vueltas = len(listas)       # el tamaño de la lista se refiera a la cantidad de elementos que tenga la lista
    for i in range(vueltas):        # 4
        # i = 0, 1, 2, 3
        print(i)







if __name__ == '__main__':
    principal2()
