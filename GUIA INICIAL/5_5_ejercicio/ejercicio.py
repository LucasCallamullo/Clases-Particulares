
'''
Ejercicio 3: Calculadora de Descuentos

Escribe un programa que calcule el precio final de todos los precios de productos que ingrese el
usario hasta que no quiera ingresar mas, y después aplicar un descuento ingresado por el usuario.
El programa debe mostrar el precio total, el descuento y el precio final.
'''


def calcular_precio(desc, precio_final):
    precio_total = precio_final - desc
    return precio_total


def calcular_porc(porc, precio_final):
    desc = precio_final * porc / 100
    return desc




def main():

    # acum
    precio_final = 0

    op = -1
    while op != 0:

        precio = float(input("Ingresar precio del producto: "))
        print("El precio cargado es:", precio)
        precio_final += precio

        preg = input("Desea seguir cargando productos? S/N: ")
        # preg = A B C D E
        while preg != "S" and preg != "N":
            preg = input("Desea seguir cargando productos? S/N (INGRESE S O N): ")

        if preg == "S":
            op = 1
        elif preg == "N":
            op = 0

    porc = float(input("Ingrese un porcentaje de descuento: "))
    desc = calcular_porc(porc, precio_final)
    precio_total = calcular_precio(desc, precio_final)


    print("El Precio final es:", precio_final)
    print("El Porcentaje de Descuento es:", desc)
    print("El Precio Total es:", precio_total)













if __name__ == "__main__":
    main()
