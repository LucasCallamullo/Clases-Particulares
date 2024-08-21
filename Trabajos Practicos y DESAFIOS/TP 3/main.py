from funciones import *


def menu(first_time):
    print("=" * 50)
    if first_time:
        print("1 - Cargar Proyectos por Primera Vez.")
    else:
        print("1 - Agregar más Proyectos.")
    print("2 - Ordenar y Mostrar Datos.")
    print("3 - Actualizar Proyecto Num X.")
    print("4 - Resumen por lenguaje.")
    print("5 - Resumen por año.")
    print("6 - Filtrar lenguaje.")
    print("7 - Productividad.")
    return int(input("Ingrese una opción: "))


def main():
    gProyecto = list()
    op = -1
    # Para verificar que cargaron datos
    first_time = True
    # Porque la opcion 7 depende de la opcion 5, recicla una lista que se crea en opcion 5.
    indep_de_op5 = False

    while op != 0:
        # Menu
        op = menu(first_time)

        if first_time:
            if op == 1:
                n = int(input("Cantidad de Proyectos a cargar: "))
                cargar_datos(gProyecto, n)
                first_time = False
            else:
                print("Debe 'Cargar Proyectos por Primera Vez' para ejecutar las demás opciones.")
        else:
            if op == 1:
                n = int(input("Cantidad de Proyectos a agregar: "))
                cargar_datos(gProyecto, n)
                # Se apaga la bandera en este caso porque se agregarian mas proyectos, debera pasar de nuevo
                # por la op 5 si desea usar la op 7
                indep_de_op5 = False
            elif op == 2:
                sort(gProyecto, op)
                show_datos(gProyecto)
            elif op == 3:
                x = int(input("Buscar Proyecto Numero: "))
                existe = validar_num_proyecto(gProyecto, x)
                menu_opcion3(existe, gProyecto, x)
            elif op == 4:
                acum_op4 = acumuladores_op4(gProyecto)
                show_op4(acum_op4)
            elif op == 5:
                cont_op5 = contadores_op5(gProyecto)
                show_op5(cont_op5)
                indep_de_op5 = True
            elif op == 6:
                lista_lenguajes = obtener_lista_op6()
                ln = Validar_lenguaje_op6(lista_lenguajes)
                lista_ln = obtener_lista_ln_op6(gProyecto, ln)
                sort(lista_ln, op)
                show_datos(lista_ln)
            elif op == 7:
                if indep_de_op5:
                    may_op7 = calcular_may_op7(cont_op5)
                    show_op7(may_op7)
                else:
                    print("Necesita realizar 'Resumen por Año' primero. (Opción 5)")


if __name__ == "__main__":
    main()
