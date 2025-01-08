class Envio:
    def __init__(self, cod, dp, tip, fp):
        self.codigo = cod
        self.direccion = dp
        self.tipo = tip
        self.pago = fp

    def __str__(self):
        cad = 'Código postal: {:<10} | Direccion: {:<20} | Pais: {:<12} | Tipo de envio: {:<2} | Forma de pago: {:<3}'
        cad = cad.format(self.codigo, self.direccion, self.country(), self.tipo, self.pago)
        return cad

    def country(self):
        cp = self.codigo
        n = len(cp)
        if n < 4 or n > 9:
            return 'Otro'
        if n == 8:
            if cp[0].isalpha() and cp[0] not in 'IO' and cp[1:5].isdigit() and cp[5:8].isalpha():
                return 'Argentina'
            else:
                return 'Otro'
        if n == 9:
            if cp[0:5].isdigit() and cp[5] == '-' and cp[6:9].isdigit():
                return 'Brasil'
            else:
                return 'Otro'
        if cp.isdigit():
            if n == 4:
                return 'Bolivia'
            if n == 7:
                return 'Chile'
            if n == 6:
                return 'Paraguay'
            if n == 5:
                return 'Uruguay'
        return 'Otro'

    def check_dir(self):
        cl = cd = 0
        td = False
        ant = " "
        for car in self.direccion:
            if car in " .":
                if cl == cd:
                    td = True
                cl = cd = 0
                ant = " "
            else:
                cl += 1
                if not car.isdigit() and not car.isalpha():
                    return False
                if ant.isupper() and car.isupper():
                    return False
                if car.isdigit():
                    cd += 1
                ant = car
        return td

    def calcular_importe(self):
        cp = self.codigo
        pago = self.pago
        tipo = self.tipo
        destino = self.country()

        importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
        monto = importes[tipo]

        if destino == 'Argentina':
            inicial = monto
        else:
            if destino == 'Bolivia' or destino == 'Paraguay' or (destino == 'Uruguay' and cp[0] == '1'):
                inicial = int(monto * 1.20)
            elif destino == 'Chile' or (destino == 'Uruguay' and cp[0] != '1'):
                inicial = int(monto * 1.25)
            elif destino == 'Brasil':
                if cp[0] == '8' or cp[0] == '9':
                    inicial = int(monto * 1.20)
                else:
                    if cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3':
                        inicial = int(monto * 1.25)
                    else:
                        inicial = int(monto * 1.30)
            else:
                inicial = int(monto * 1.50)

        # 4. Determinación del valor final del ticket a pagar.
        # asumimos que es pago en tarjeta...
        final = inicial

        # ... y si no lo fuese, la siguiente será cierta y cambiará el valor...
        if pago == 1:
            final = int(0.9 * inicial)

        return final


def validar_rango(inf, sup, msj):
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def validar_mayor(inf, msj):
    valor = int(input(msj))
    while valor <= inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def menu():
    print("MENÚ DE OPCIONES")
    print("-=" * 50)
    print("1. Cargar arreglos de registros desde algún archivo")
    print("2. Agregar nuevo envió por teclado")
    print("3. Mostrar listado por código postal de menor a mayor")
    print("4. Buscar arreglo por dirección y tipo de envió")
    print("5. Cambiar forma de pago mediante el código postal")
    print("6. Generar listado de cantidad de envió")
    print("7. Mostrar importe final acumulado por pagos de envió")
    print("8. Buscar el tipo de envió con mayor monto acumulado y mostrar el porcentaje")
    print("9. Mostrar el importe final promedio")
    print("10. Salir ")
    print("-=" * 50)
    opcion = int(input("Ingrese una opción: "))
    return opcion
