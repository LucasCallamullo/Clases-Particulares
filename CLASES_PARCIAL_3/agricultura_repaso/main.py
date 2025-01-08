from funciones import *

# ctrl x





def main():

    # Variables
    v_t = list()


    # Bandera / bools
    g_cargado = False

    op = -1
    while op != 0:

        op = int(input("ingresar opcion: "))

        if not g_cargado:
            if op == 1:
                n = int(input("Cuantos trabajos va a cargar: "))
                cargar_vector(v_t, n)
                mostrar_datos(v_t)
                g_cargado = True
            elif op == 0:
                print("Gracias por usar el pgroama")
            else:
                print("Debe primero utilizar la opcion 1.")

        else:
            if op == 1:
                print("El arreglo proyecto ya esta creado.")

            elif op == 2:
                sort(v_t)
                num = int(input("Ingresar numero a comparar: "))
                cant_personas(v_t, num)

            elif op == 3:
                v_cont = contador_trabajos(v_t)
                for i in range(len(v_cont)):
                    if v_cont[i] > 0:
                        print("Existen:", v_cont[i], " trabajos del tipo de trabajo:", i)

            elif op == 4:
                prom = calcular_promedio(v_t)
                mostrar_datos_op4(v_t, prom)
                print("el promedio es:", prom)

            elif op == 9:
                for i in v_t:
                    print(i)



if __name__ == '__main__':
    main()
