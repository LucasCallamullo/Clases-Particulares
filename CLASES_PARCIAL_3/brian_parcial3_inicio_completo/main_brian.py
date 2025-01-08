

from funciones import *


def menu():
    print(" 1 - Cargar arreglo. ")
    print(" 2 - Mostrar arreglo. ")
    print(" 3 - vectores de conteo/acumulacion. ")
    print(" 4 - busqueda secuencial o binaria. ")
    print(" 0 - Salir. ")
    op = int(input("Elija su opción: "))
    return op


def principal():

    v_est = []      # inicia vacía

    validar_op1 = False

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            """
            Cargar arreglo, con la cantidad n indicada por el usuario,
            Cada vez que se ingrese a la opcion se debe crear un nuevo arreglo
            """
            n = validar_n()
            v_est = []
            cargar_arreglo(n, v_est)
            validar_op1 = True

        # Cuando esta en True
        if validar_op1:

            if op == 2:
                """ 
                Mostrar arreglo pero que este ordenado por legajo de menor a mayor
                """
                t = int(input("Ingrese edad a superar: "))

                ordenar_arreglo(v_est)
                mostrar_arreglo(v_est, t)

            elif op == 3:
                """
                #Edad ( 18 a 25)
    
                Determinar el total de cuotas por estudiante que recaudó por cada edad que fue registrado
                (8 acumuladores en total en un vector de acumulación). Debe solamente mostrar los valores
                de los importes acumulados que esten en el intervalo de los valores "c" y "x"
                 ingresados por teclado
                
                """
                c = float(input("Ingrese el importe inferior: "))
                x = float(input("Ingrese el importe superior: "))
                generar_vector_acum(v_est, c, x)

            elif op == 4:
                """
                Buscar si existe un estudiante con  un legajo "z" donde z es un valor ingresado por teclado
                Si existe mostrar sus datos, si no existe informar, debe detenerse la busqueda en el primer
                resultado
                """
                z = int(input("Legajo a buscar: "))
                pos = busqueda_secuencial(v_est, z)

                if pos >= 0:
                    # Significa que encontre un valor

                    # Mostrar los del estudiante encontrado
                    print(v_est[pos])

                    # Mostrar solo el nombre y su cuota
                    print("Nombre:", v_est[pos].nombre, "Cuota:", v_est[pos].cuota_importe)

                    # Mostrar los datos del estudiante encontrado y luego Modificar el valor de la
                    # cuota por un valor "imp" que se ingresa por teclado y despues mostrar los nuevos
                    # datos actualizados
                    print(v_est[pos])           # datos viejos
                    imp = float(input("Ingresar neuva cuota:"))
                    v_est[pos].cuota_importe = imp
                    print("Datos actualizados:", v_est[pos])

                    # Agregar un %10 de aumento a la cuota
                    v_est[pos].cuota_importe += 0.1 * v_est[pos].cuota_importe

                else:
                    print("No existe ese legajo.")

        elif op == 0:
            print("gracias por usar el programa")

        else:
            print("debe ingresar una opcion valida.")


if __name__ == '__main__':
    principal()
