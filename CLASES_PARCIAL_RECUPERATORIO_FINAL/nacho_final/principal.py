


from soporte import *
from funciones import *


def busqueda_binaria(vec, nom):
    izq, der = 0, len(vec) - 1

    while der >= izq:
        c = (izq + der) // 2
        if vec[c].nombre == nom:
            return c
        elif vec[c].nombre > nom:
            der = c - 1  # 1
        else:
            izq = c + 1  # 2

    return -1


def menu():
    print('----------------------- Menú de opciones - Becas de Estudio -------------------------')
    print('1. Cargar arreglo (ordenado por nombre)')
    print('2. Mostrar arreglo completo')
    print('3. Buscar por dni (Busqueda Secuencial')
    print('4. Conteo por tipo de beca y carrera ( MAtriz)')
    print('5. Generar archivo con condición de filtro( Archivo Binario )')
    print('6. Mostrar archivo (incluir promedio al final)')
    print('7. Busqueda Binaria')
    print('0. Salir')
    print('--------------------------------------------------------------------------------------------')
    return int(input('Ingrese número de opción: '))


def principal():
    vec = []    # list()            # vector, lista, arreglo

    # Punto archivos
    fd = "becas.dat"        # file description ; nombre del archivo

    opcion = -1
    while opcion != 0:

        opcion = menu()

        if opcion == 1:
            vec = cargar_arreglo()      # 5
            print("Carga finalizada - Arreglo generado")
            print()

        elif opcion == 2:
            if not vec:     # pregunta si vec = []
                print('El arreglo no ha sido cargado todavía..')
            else:
                mostrar_arreglo(vec)
                print()

        elif opcion == 3:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                # TAREA del estudiante...
                d = int(input("Dni a busar: "))
                pos = busqueda_secuencial(vec, d)         # retoorne un valor

                if pos >= 0:
                    print("Datos Originales:", vec[pos])

                    monto = float(input("Ingresar nuevo monto: "))
                    vec[pos].monto = monto

                    # incrementes un 25%
                    # vec[pos].monto = vec[pos].monto + vec[pos].monto * 25 / 1000
                    # vec[pos].monto += 0.25 * vec[pos].monto

                    print("Datos Modificados:", vec[pos])

                else:
                    print("No se encontro")

        elif opcion == 4:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                # TAREA del estudiante...
                t = int(input("cantidad a superar en la matriz: "))
                generar_matriz(vec, t)

        elif opcion == 5:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                # TAREA del estudiante...
                m = float(input("Ingresar monton a superar: "))
                generar_archivo_binario(vec, fd, m)

        elif opcion == 6:
            # TAREA del estudiante...
            mostrar_archivo_binario(fd)

        elif opcion == 7:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                # TAREA del estudiante...
                """
                Buscar por nombre y mostrar solamente su dni, y su monto
                """
                nom = int(input("Nombre a busar: "))
                pos = busqueda_binaria(vec, nom)  # retoorne un valor

                if pos >= 0:
                    print("DNI:", vec[pos].dni, "Monto:", vec[pos].monto)

                else:
                    print("No se encontro")



if __name__ == '__main__':      # condicion de control
    principal()
