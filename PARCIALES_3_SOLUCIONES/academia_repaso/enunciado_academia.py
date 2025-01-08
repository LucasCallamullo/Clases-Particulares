import random


class Alumno:
    # nivel (0 12)  ; name = nombre     ; surname = apellido
    def __init__(self, dni_alum, name, surname, dni_tut, importe, nivel):
        self.dni_alum = dni_alum
        self.name = name
        self.surname = surname
        self.dni_tut = dni_tut
        self.importe = importe
        self.nivel = nivel

    def __str__(self):
        cadena = "DNI Alum: " + str(self.dni_alum)
        cadena += " | Nombre: " + self.name
        cadena += " | Apellido: " + self.surname
        cadena += " | DNI Tut: " + str(self.dni_alum)
        cadena += " | Importe: " + str(self.importe)
        cadena += " | Nivel: " + str(self.nivel)
        return cadena


# ==============================================================
#                       Opcion 1
# ==============================================================
def validar_n():
    n = int(input("Ingresar cantidad de alumnos a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de alumnos a cargar: "))
    return n


def cargar_arreglo(v_alum, n):
    # nivel (0 12)  ; name = nombre     ; surname = apellido
    # def __init__(self, dni_alum, name, surname, dni_tut, importe, nivel):
    nombres = ("A", "B", "C", "D")
    apellidos = ("a", "b", "c", "d")

    for i in range(n):
        dni_alum = random.randint(1, 10)
        name = random.choice(nombres)
        surname = random.choice(apellidos)
        dni_tut = random.randint(1, 10)
        importe = round(random.uniform(0.1, 10), 2)
        nivel = random.randint(0, 12)

        alumnito = Alumno(dni_alum, name, surname, dni_tut, importe, nivel)
        v_alum.append(alumnito)


# ==============================================================
#                       Opcion 2
# ==============================================================
def ordenar(v_alum):
    n = len(v_alum)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_alum[i].surname > v_alum[j].surname:
                v_alum[i], v_alum[j] = v_alum[j], v_alum[i]


def mostrar_datos(v_alum):
    for i in v_alum:
        print(i)


# ==============================================================
#                       Opcion 3
# ==============================================================
def contadores_op3(v_alum):
    v_cont = [0] * 13
    for i in v_alum:
        v_cont[i.nivel] += 1

    for i in range(len(v_cont)):
        if v_cont[i] > 0:
            print("La cantidad de alumnos en el nivel", i, " Son:", v_cont[i])


# ==============================================================
#                       Opcion 4
# ==============================================================
def calcular_importe_op4(v_alum, x):
    acum = 0
    for i in v_alum:
        if i.dni_tut == x:
            acum += i.importe

    if acum > 0:
        print("La cantidad de importes total de las cuotas del DNI:", x, " es:", acum)
    else:
        print("No se encontro un dni de tutor con el numero:", x)


# ==============================================================
#                       Opcion 5
# ==============================================================
def busqueda_secuencial(v_alum, x):
    for i in range(len(v_alum)):
        if v_alum[i].dni_alum == x:
            return i
    return -1


def cambiar_cuota_importe_op5(v_alum, pos):
    if pos >= 0:
        print("Los datos viejos del alumno son:")
        print(v_alum[pos])
        print("=" * 50)
        # calcular 10% de descuento en el importe
        # v_alum[pos].importe   ==== 100%
        # v_alum[pos].importe * 10 / 100    ====  10%
        #
        # aca calculas el nuevo importe al que vamos igualar
        descuento = v_alum[pos].importe * 10 / 100
        nuevo_importe = v_alum[pos].importe - descuento

        # aca accedes al atributo que queres modificar por eso es importante el indice pos
        v_alum[pos].importe = nuevo_importe

        # aca mostramos los datos nuevos.
        print("Los datos nuevos del alumno son:")
        print(v_alum[pos])

    else:
        print("No existe un alumno con ese dni.")


def main():

    v_alum = list()     # []

    op = -1
    while op != 0:

        if op == 1:
            n = validar_n()
            cargar_arreglo(v_alum, n)

        elif op == 2:
            ordenar(v_alum)
            mostrar_datos(v_alum)

        elif op == 3:
            contadores_op3(v_alum)

        elif op == 4:
            # te pide dni del tutor
            x = int(input("Ingresar dni del tutor: "))
            calcular_importe_op4(v_alum, x)

        elif op == 5:
            # te pide busqueda secuencial por lo general el "si existe" hace referencia a eso.

            # pedimos el dni alumno como x
            x = int(input("Ingresar dni del alumno: "))

            # recuperamos un indice mediante busqueda secuencial
            pos = busqueda_secuencial(v_alum, x)

            # operaciones varias que pide el punto
            cambiar_cuota_importe_op5(v_alum, pos)


if __name__ == '__main__':
    main()
