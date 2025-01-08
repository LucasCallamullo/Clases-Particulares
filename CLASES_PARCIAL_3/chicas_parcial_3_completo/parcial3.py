

from funciones import *


def menu():
    print("=" * 50)  # ===========================================================
    print("1 - Cargar arreglo.")
    print("2 - Mostrar arreglo.")
    print("3 - Vector de conteo/acumulacion arreglo.")
    print("4 - Busqueda secuencial en el arreglo.")
    print("0 - Salir.")
    op = int(input("Ingrese una opcion: "))  # 2
    return op   # regresar, retornar op


def principal():

    # listas / arreglo / arrays / vector

    # punto 1       - Crear una lista vacía
    v_paseos = []   # ó list()

    op = -1
    while op != 0:      # mientras op sea distinto de cero

        #
        op = menu()     # 2

        if op == 1:
            n = int(input("Ingrese la cantidad de paseos a generar: "))  # 5
            cargar_arreglo(v_paseos, n)

        elif op == 2:
            """ 2- solo mostrar los paseos que superan un importe "t" ingresado por teclado,
             - Muestre el arreglo ordenado por ID 
             
             """

            ordenar_arreglo(v_paseos)

            t = float(input("Ingrese importe a superar: "))
            mostrar_arreglo(v_paseos, t)

        elif op == 3:
            """ 
             3 - Determinar y mostrar cuantos paseos hay por cada tipo de destino posible (un vector con 3 contadores)
             , 
             Solo mostrar los destinos que tengan un contaodr mayor "x", x es un valor ingresado por telcado
                
            """
            x = int(input("supera un valor de contador: "))
            generar_vector_conteo(v_paseos, x)


        elif op == 4:
            """
                4 - Determianr si existe un pais cuyo ID "t" que se ingresa por teclado,
                que sea del destino "Montañas" o "Lago",
                
            """
            t = int(input("Ingresar ID a buscar: "))

            pos = busqueda_secuencial(v_paseos, t)

            if pos >= 0:

                print("Datos viejos:", v_paseos[pos])

                # si existe, modifique el precio por un valor "imp" que se carga por teclado
                imp = float(input("Ingresar nuevo precio: "))
                v_paseos[pos].importe = imp

                print("Datos Actulizados:", v_paseos[pos])

                # aumentarle un 10% el valor de importe
                v_paseos[pos].importe += 0.1 * v_paseos[pos].importe

                # Solo muestre el nombre y el destino
                print("Nombbre", v_paseos[pos].nombre, "Precio:", v_paseos[pos].importe)

            else:       # pos  < 0  cuando sea -1
                print("No se encontro ningun resultado")

        elif op == 0:
            print("Gracias por usar el menu")



    print("Sali del ciclo while")


if __name__ == '__main__':
    principal()

