class Venta:
    """
    Una tienda de delicatessen necesita un programa que permita llevar un control de las ventas de los
    productos queposee. Por cada Venta se conoce: código de venta, nombre del producto que se vendió, el tipo
    de producto (un entero 1 y 5; Ej.: 1: Snacks, 2: Vinos, 3: Aderezos, 4: Embutidos, 5: Whiskies),
    origen (un entero entre 0 y 2; Ej.: 0 – Importado, 1 – Nacional, 2 - Mercosur) y el monto total
    de esa venta. Se pide definir la clase Venta y desarrollar un
    programa en Python controlado por menú de opciones, que permita realizar las siguientes tareas:
    """
    # codigo INT, nombre STR, tipo tupla(1, 5), origen tupla(0, 2), monto FLOAT

    def __init__(self, codigo, nombre, tipo, origen, monto):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.origen = origen
        self.monto = monto

    def __str__(self):
        tupla_tipo = ("Snacks", "Vinos", "Aderezo", "Embutidos", "Whiskies")
        tupla_origen = ("Importado", "Nacional", "Mercosur")

        cadena = " Codigo de venta: " + str(self.codigo)
        cadena += " | Nombre producto: " + str(self.nombre)
        cadena += " | Tipo producto: " +  tupla_tipo[self.tipo - 1]
        cadena += " | Origen: " + tupla_origen[ self.codigo - 1]
        cadena += " | Monto total: "+ str(self.monto)
        return cadena
