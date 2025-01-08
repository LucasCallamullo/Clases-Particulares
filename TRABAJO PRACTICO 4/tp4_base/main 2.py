import funciones2


def menu():
    while True:
        print("\n\t      [MENÚ DE OPCIONES]")
        print("\n\t1. Cargar binario desde los registros provistos.")
        print("\t2. Cargar datos de envío por teclado.")
        print("\t3. Mostrar datos de registros.")
        print("\t4. Buscar registros por código postal.")
        print("\t5. Buscar registro por dirección postal.")
        print("\t6. Mostrar cantidad de envíos por posibles combinaciones.")
        print("\t7. Mostrar cantidad de envíos por tipo de envío y por forma de pago.")
        print("\t8. Calcular importe promedio pagado por envío y mostrar envíos con un importe mayor a este.")
        print("\t0. Salir")
        op = funciones2.rango(0, 8, "\nElija una opción: ")
        return op


def principal():
    fdt = "envios-tp4p2.csv"
    fdb = "envios-tp4p2.dat"
    fd_binario = "envios.bin"
    op = 420

    while op != 0:
        op = menu()

        if op == 1:
            funciones2.generar_archivo_binario(fdt, fdb)

        elif op == 2:
            funciones2.cargar_envio(fd_binario)

        elif op == 3:
            funciones2.mostrar_archivo_binario(fdb)

        elif op == 4:
            cod_buscado = input("Ingrese el código postal que desea buscar: ")
            funciones2.buscar_por_codigo(fdb, cod_buscado)

        elif op == 5:
            direccion_buscada = input("Ingrese la dirección postal que desea buscar: ")
            funciones2.buscar_por_direccion(fdb, direccion_buscada)

        elif op == 6:
            funciones2.contar_envios_por_combinaciones(fdb)

        elif op == 7:
            funciones2.totalizar_envios_por_tipo_y_pago(fdb)

        elif op == 8:
            funciones2.calcular_importe_promedio(fdb)


if __name__ == "__main__":
    principal()
