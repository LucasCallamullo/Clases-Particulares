

from funciones import *

def menu():
    print(" 1 - Cargar Arreglo.")
    print(" 2 - Mostrar Arreglo.")
    print(" 3 - Generar Matriz.")
    print(" 4 - Generar Archivo binario.")
    print(" 5 - Mostrar archivo binario")
    print(" 0 - Salir.")
    return int(input("Ingresar opcion: "))


def main():  # principal()

    # Lista, arreglo, vector de trabajo
    v_consumos = []

    # fd = file description = nombre del archivo
    fd = "consumos.dat"

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            """
            1 - cada vez que se ingrese a la opcion 1 debe construir nuevamente el arreglo
            
            """
            n = validar_n()
            v_consumos = []
            cargar_arreglo(v_consumos, n)

        elif op == 2:
            """
            2 - Mostrar arreglo, pero solo los que importe "x"
            """
            if len(v_consumos) > 0:
                x = int(input("Importe a superar: "))
                mostrar_arreglo(v_consumos, x)
            else:
                print("Primero debe pasar por la opcion 1")

        elif op == 3:
            """
            3 - A partir del arreglo generado en el punto 1, calcular el monto total acumulado por 
            hora del día y por tipo de consumo. Muestre únicamente aquellos acumulados que correspondan 
            al horario entre las "h1" y las "h2" hs
            """
            if len(v_consumos) > 0:
                h1 = int(input("Ingresar hora a superar: "))
                h2 = int(input("Ingresar hora a ser menor: "))
                generar_matriz(v_consumos, h1, h2)
            else:
                print("Primero debe pasar por la opcion 1")

        elif op == 4:
            """
            4 - Generar archivo binario, debe conservar su contenido y agregar lo nuevo al final "ab"; 
            "ab" --> crea un archivo nuevo, agrega contenido al final y conserva lo anterior
            "wb" --> crea un archivo nuevo, sobreescribe todo su contenido cada vez que usamos esta opcion 4
            
            Solo guardar los tipo de consumos SMS y Llamada y que correspondan al numero de telefono "t"
            """
            if len(v_consumos) > 0:
                t = input("numero de telefono a guardar: ")
                generar_archivo_binario(v_consumos, fd, t)
            else:
                print("Primero debe pasar por la opcion 1")

        elif op == 5:
            """
            5 - Mostrar Archivo binario generado
            - al final del listado mostrar el promedio de los importes de los tipo de consumos que eran SMS
            """
            mostrar_archivo_binario(fd)

        elif op == 6:
            """ 
            6 - Busqueda binaria:
            buscar por "num" que va a ser un numero de telefoon, si existe mostrar datos, si no existe informar
            
            """
            num = input("Buscar num_tel: ")
            pos = busqueda_binaria(v_consumos, num)

            if pos >= 0:
                pass

            else:
                print("No existe")


if __name__ == '__main__':
    main()

