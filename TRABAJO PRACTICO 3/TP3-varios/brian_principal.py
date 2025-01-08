

from brian_modulo import *

def validar_opciones(lim_inferior, lim_superior, mensaje="ingrese la opcion deseada"):
    n = int(input(mensaje))
    while n < lim_inferior or n > lim_superior:
        print("El valor dabe estar entre", lim_inferior, "y", lim_superior)
        n = int(input(mensaje))

    return n




def menu_de_opciones():
        print("1. Cargar envíos desde archivo")
        print("2. Cargar un envío manualmente")
        print("3. Mostrar envíos ordenados por código postal")
        print("4. Buscar envío por dirección y tipo")
        print("5. Cambiar forma de pago según código postal")
        print("6. Determinar cantidad de envíos válidos (HC) o totales (SC)")
        print("7. Determinar importe final acumulado por tipo de envío")
        print("8. Determinar tipo de envío con mayor importe final acumulado")
        print("9. Calcular promedio de importes y cuántos envíos están por debajo")
        print("0. Salir")
        op = validar_opciones(0, 9, "ingrese la opcion deseada: ")
        return op

def main():
    op = -1
    envios = []
    op_1_2 = False
    tc = "HC"
    fd = "envios-tp3.txt"
    while op != 0:
        op = menu_de_opciones()
        if op == 1:
            envios, tc = opcion1(envios, tc, fd)
            op_1_2 = True
        elif op == 2:
            cargar_envio_manual(envios)
            op_1_2 = True
        if op_1_2:
            if op == 3:
                mostrar_arreglo(envios)
            elif op == 4:
                d = str(input("Ingrese la dirección a buscar: "))
                e = int(input("Ingrese el tipo de envió a buscar: "))
                pos = busqueda_secuencial_p4(envios, d, e)
                if pos > 0:
                    print(envios[pos])
                else:
                    print("No existe esa direccion y no existe el tipo de envio.")
            elif op == 5:
                cp = input("Ingrese el codigo postal a buscar: ")
                pos = busqueda_secuencial_p5(envios, cp)
                if pos >= 0:
                    print("se encontro el codigo postal a buscar", envios[pos])

                    if envios[pos].forma_pago == 2:
                        envios[pos].forma_pago = 1

                    else:
                        envios[pos].forma_pago = 2
                    print("Forma de pago modificado:", envios[pos])
                else:
                    print("No existe el codigo postal.")
            elif op == 6:
                vec_cont_hc = vector_acum_hc(envios)
                vec_cont_sc = vector_acum_sc(envios)
                mostrar_conteo_hc(vec_cont_hc)
                mostrar_conteo_sc(vec_cont_sc)

            elif op == 7:
                vec_acum_hc = vector_acum_hc_p_7(envios)
                vec_acum_sc = vector_acum_sc_p_7(envios)
                mostrar_conteo_hc_p7(vec_acum_hc)
                mostrar_conteo_sc_p7(vec_acum_sc)

            elif op == 8:
                if vec_acum_hc is None or vec_acum_sc is None:
                    print("Los vectores de acumulación HC y SC no han sido generados. Por favor, ejecute el punto 7 primero.")
                else:
                    may = encontrar_mayor_monto(vec_acum_hc, vec_acum_sc)
                    print("el mayor monto acumulado es: ", may)
                    res = calcular_porcentaje_mayor(vec_acum_hc, vec_acum_sc, may)
                    print("el porcentaje (ustedes pongalo bonito)", res)
            elif op == 9:
                pass
        elif op == 0:
            print("Saliendo del programa...")
        else:
            print("Cargue primero en la opcion 1 o opcion 2")



if __name__ == '__main__':
    main()