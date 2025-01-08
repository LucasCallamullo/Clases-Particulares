

# Una emppresa de viajes desea almacenar en un arreglo llamado Viajes, viajes con los siguiente atributos
# destino, precio, cant de vuelos vendidos tiene que ser mayor a 0 , cant de asientos vacios(0, 19)


# De todos los objetos  su constructor, su propia funcion de print
# De todos hacer un menu con 2 opciones, Cargar arreglo, Mostrar datos
# 1 ) Cargar arreglo,
# 2) Mostrar datos

import random


# \ [] > < = ! | () " "
class Viajes:
    # Constructor del objeto,
    # cant_vendidos > 0         ;      cant_vacios (0, 19)
    def __init__(self, destino, importe, cant_vendidos, cant_vacios):
        self.destino = destino              # ctrl + d
        self.importe = importe
        self.cant_vendidos = cant_vendidos
        self.cant_vacios = cant_vacios

    def __str__(self):
        cadena = "Destino: " + self.destino
        cadena += " | Importe: " + str(self.importe)        # ctrl + d
        cadena += " | Cant_ven: " + str(self.cant_vendidos)
        cadena += " | Cant_vac: " + str(self.cant_vacios)
        return cadena


def cargar_arreglo(v_viaje, n):

    # le pedi por teclado el destino
    paises = ("A", "B", "C")

    for i in range(n):      # 10
        # cant_vendidos > 0         ;      cant_vacios (0, 19)
        # def __init__(self, destino, importe, cant_vendidos, cant_vacios):

        destino = random.choice(paises)
        # Esta es la forma de crear random flotantes
        importe = random.uniform(0.1, 10)
        cant_vendidos = random.randint(1, 19)
        cant_vacios = random.randint(0, 19)

        viajecito = Viajes(destino, importe, cant_vendidos, cant_vacios)
        v_viaje.append(viajecito)


def mostrar_datos(v_viaje):
    #               0         1
    # v_viaje = [ Viajes, Viajes, Viajes, Viajes]
    for i in v_viaje:
        print(i)


def main():

    # Este es nuestro arreglo / vector / lista principal con la que vamos a trabajar.
    v_viaje = []

    op = -1
    while op != 0:
        # op = menu()
        op = int(input("ingresa opcion: "))

        if op == 1:
            n = int(input("Cantidad de arreglos a cargar: "))       # 10
            cargar_arreglo(v_viaje, n)

        elif op == 2:
            mostrar_datos(v_viaje)

        elif op == 3:
            pass

        elif op == 4:
            pass


# main
if __name__ == '__main__':
    main()
