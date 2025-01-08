

from funciones import *


def menu():
    # ctrl + d
    print("1 - Cargar Arreglo")
    print("2 - Mostrar Arreglo")
    print("3 - Vector de conteo/acum")
    print("4 - Busqueda Secuencial")
    print("0 - Salir.")
    x = int(input("Ingresar una opcion: "))     # 1
    return x        # devolver, retornar algun valor


def principal():

    # lista/vector/arreglo de trabajo
    v_figus = []

    op = -1
    while op != 0:      # mientras op sea distinto de cero, ingreso al ciclo

        # si una variable esta igualada a una funcion, es porque espero que la funcino me devuelva algo
        op = menu()     # vale lo que retorna menu = 1

        if op == 1:
            n = validar_n()
            """
            1 - Cada vez que se ingrese a esta opcion el arreglo debe ser creado nuevamente.
            """
            v_figus = []
            cargar_arreglo(v_figus, n)

        elif op == 2:
            """ 
            2 - Mostrar las figuritas ordenadas por nombre de menor a mayor
            - Solo mostrar los que sean de un páis superior a "p" que se carga por teclado
            
            """
            ordenar_arreglo(v_figus)

            p = int(input("Ingresar pais a superar: "))  # 10
            mostrar_arreglo(v_figus, p)

        elif op == 3:
            """
                3 - Determinar y mostrar la cantidad de figuritas por pais(1, 32), 32 contadores
                - Solo mostrar los contadores que superen una cantidad "m" que se ingresa por teclado.
            """
            m = int(input("Ingresar cantidad a superar: "))
            generar_vector_conteo(v_figus, m)

        elif op == 4:
            """
                4 - Determinar si existe una figurita cuyo nombre sea igual "nom" y que sea de la 
                posicion "Defesor" o "Arquero"
                que se carga por teclado
                - Si No existe Informar
                - Detenga al primer resultado
                
                - Si existe modificar el importe por un valor "imp" que se carga por teclado
                mostrar los datos modificados
            """
            nom = input("Ingresar nombre a buscar: ")
            pos = busqueda_secuencial(v_figus, nom)

            if pos >= 0:

                print("Datos Sin Modificar:", v_figus[pos])

                imp = float(input("Ingresar importe nuevo: "))
                v_figus[pos].importe = imp

                print("Datos Modificados:", v_figus[pos])

                # Aumentar el importe un 10%
                v_figus[pos].importe += v_figus[pos].importe * 0.1

                # Solo mostrar su pais y su num  jug
                print("Pais:", v_figus[pos].pais, "Y su Num Jug:", v_figus[pos].num_jug)

            else:
                print("No existe.")


if __name__ == '__main__':
    principal()
