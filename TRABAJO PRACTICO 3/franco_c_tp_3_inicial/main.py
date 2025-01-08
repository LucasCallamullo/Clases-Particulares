

# Clase / Registro / Objeto
class Envio:

    # funcion constrcutora o inicializadora
    def __init__(self, cod_postal, direccion, tipo_envio, forma_pago):
        self.cod_postal = cod_postal
        self.direccion = direccion
        self.tipo_envio = tipo_envio
        self.forma_pago = forma_pago

    def __str__(self):
        cadena = "Cod_Postal: " + str(self.cod_postal)
        cadena += " | Direccion: " + str(self.direccion)
        cadena += " | tipo_envio: " + str(self.tipo_envio)
        cadena += " | forma_pago: " + str(self.forma_pago)
        return cadena


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                   Opcion 1
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def cargar_arreglo(v_envio, fd):
    n = len(v_envio)        # 0

    if n != 0:
        # Menu de oopcion que diga si quiere borrar tod0 el contenido del arreglo
        # 1 Si borar todo el arreglo
        # 2 - Cancelar
        # while que solo te deje elegir esas opciones

        # Cada vez que se elija esta opción, el arreglo debe ser creado de nuevo desde cero
        v_envio = []

    # Cuando el arreglo esta vacío
    else:
        m = open(fd, "rt")          # read text

        cont_lineas = 0

        for linea in m:
            cont_lineas += 1

            if cont_lineas == 1:
                # control = analizar_hc_sc(linea)
                pass
            else:
                cod_postal = linea[0:9].strip()
                direccion = linea[9:29].rstrip()
                tipo_envio = int(linea[29])
                forma_pago = int(linea[30])
                envio_objeto = Envio(cod_postal, direccion, tipo_envio, forma_pago)
                v_envio.append(envio_objeto)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                   Opcion 2
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def cargar_un_arreglo(v_envio):
    # pero el tipo de envio este entre 0 y 6, y la forma de pago sea 1 o 2

    cod_postal = input()
    direccion = input()

    tipo_envio = int(input())

    forma_pago = int(input("Ingresar forma de pago (debe ser 1 o 2): "))
    while forma_pago != 1 and forma_pago != 2:
        forma_pago = int(input("Ingresar forma de pago (debe ser 1 o 2): "))

    envio_objeto = Envio(cod_postal, direccion, tipo_envio, forma_pago)
    v_envio.append(envio_objeto)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                   Opcion 3
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def shellsort(v_envio):
    n = len(v_envio)
    gap = n // 2  # Empieza con una gran distancia y luego reduce la distancia

    while gap > 0:
        # Realiza un ordenamiento por inserción con esta distancia.
        # Los primeros elementos gap arr[0..gap-1] ya están ordenados por distancia
        for i in range(gap, n):
            temp = v_envio[i]
            j = i
            # Mueve los elementos previamente ordenados por distancia hasta encontrar el lugar correcto para v_envio[i]
            while j >= gap and v_envio[j - gap].cod_postal > temp.cod_postal:
                v_envio[j] = v_envio[j - gap]
                j -= gap
            v_envio[j] = temp

        gap //= 2  # Reduce el tamaño de la distancia


def mostrar_arreglo(v_envio, m=0):

    cont = 0
    # v_envio = [E1, E2, E3, ]
    for i in v_envio:
        # i = E1, E2, E3, ...
        print(i)
        cont += 1

        if m != 0 and m == cont:
            break


def menu_op3(v_envio):
    op = -1
    while op != 1 and op != 2:
        print("=========================== Menu - Opcion 3 =============================")
        print("1 - Mostrar Todos")
        print("2 - Cantidad a mostrar")
        op = int(input("Ingresar su opcion: "))
        if op == 1:
            mostrar_arreglo(v_envio)
        elif op == 2:
            m = int(input("Cantidad a mostrar: "))
            mostrar_arreglo(v_envio, m)





def menu():
    # ctrl + d
    print("1 - Cargar Arreglo Desde el archivo")
    print("3 - Mostrar Arreglo")
    # aca va el resto del menu
    op = int(input("Ingresar opción: "))        # 5
    return op


def principal():

    # lista / vector / arreglo / array
    v_envio = []
    fd = "envios100HC.txt"

    op = -1
    while op != 0:      # mientras op sea distinto de cero

        # Si una variable esta igualada a una funcion es porque espera que le devuelva un valor
        op = menu()     # 5 usuario

        if op == 1:
            cargar_arreglo(v_envio, fd)

        elif op == 2:
            cargar_un_arreglo(v_envio)

        elif op == 3:
            shellsort(v_envio)
            menu_op3(v_envio)



        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            pass













if __name__ == '__main__':
    principal()
