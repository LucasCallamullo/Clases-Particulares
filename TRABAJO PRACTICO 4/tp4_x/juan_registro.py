

class Ticket:
    def __init__(self, codigo, patente, tipo, forma_de_pago, pais_cabina, km_recorridos, pais_patente):
        self.codigo = codigo
        self.patente = patente
        self.tipo = tipo
        self.forma_de_pago = forma_de_pago
        self.pais_cabina = pais_cabina
        self.km_recorridos = km_recorridos
        self.pais_patente = pais_patente

    def __str__(self):
        vehiculos_str = vehiculo_to_str(self.tipo)
        cabinas_str = cabina_to_str(self.pais_cabina)
        pago_str = pago_to_str(self.forma_de_pago)

        cad = 'Código: {:<13} | Patente: {:<10} | Pais: {:<10} | Tipo: {:<14} | Forma pago: {:<10} | Cabina: {:<10} | Distancia: {:>5}km'
        cad = cad.format(self.codigo, self.patente, self.pais_patente, vehiculos_str, pago_str, cabinas_str, self.km_recorridos)
        return cad


def vehiculo_to_str(tipo):
    tipos_vehiculo = ("Motocicleta", "Automóvil", "Camión")
    return tipos_vehiculo[tipo]


def cabina_to_str(pais_cabina):
    cabinas = ("Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay")
    return cabinas[pais_cabina]


def pago_to_str(forma_de_pago):
    formas_pago = ("Manual", "Telepeaje")
    return formas_pago[forma_de_pago-1]


# Esta funcion la reutilizamos de la solucion del tp3 que subio el profe, y modificamos algunas partes
def pais_patente_identificado(pat):
    lp = len(pat)

    # ...si tiene menos de 6 o más de 7 caracteres, es otro pais...
    if lp < 6 or lp > 7:
        return "Otro"

    # ...si tiene 6 caracteres, es de Chile o es de otro pais...
    if lp == 6:
        # ...Chile...
        if pat[0:4].isalpha() and pat[4:6].isdigit():
            return "Chile"

        # ...Otro...
        else:
            return "Otro"

    # ...si llegó hasta acá, tiene 7 caracteres...
    # ...Argentina...
    if pat[0:2].isalpha() and pat[2:5].isdigit() and pat[5:7].isalpha():
        return "Argentina"

    # ...Bolivia...
    if pat[0:2].isalpha() and pat[2:7].isdigit():
        return "Bolivia"

    # ...Brasil...
    if pat[0:3].isalpha() and pat[3].isdigit() and pat[4].isalpha() and pat[5:7].isdigit():
        return "Brasil"

    # ...Paraguay...
    if pat[0:4].isalpha() and pat[4:7].isdigit():
        return "Paraguay"

    # ...Uruguay...
    if pat[0:3].isalpha() and pat[3:7].isdigit():
        return "Uruguay"

    # ...si ninguno fue cierto, entonces es Otro...
    return "Otro"


# MENÚ DE OPCIONES
def menu():
    linea = "-=" * 50
    print(linea)
    print(" MENÚ DE OPCIONES")
    print(linea)
    print("1. Cargar archivo con objetos desde el .csv.")
    print("2. Cargar ticket individual por teclado al archivo.")
    print("3. Mostrar listado de tickets dentro del archivo.")
    print("4. Buscar y mostrar ticket/s por patente.")
    print("5. Buscar y mostrar ticket por codigo de ticket.")
    print("6. Generar matriz de conteo por pais de cabina y tipo de vehiculo.")
    print("7. Mostrar cantidad total por pais cabina y tipo vehiculo.")
    print("8. Generar un arreglo y Mostrar datos de menor a mayor por km recorridos.")
    print()
    print("0. Salir")
    print(linea)
    return int(input("Ingrese una opción: "))
