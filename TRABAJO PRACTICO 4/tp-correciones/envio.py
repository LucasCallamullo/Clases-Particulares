class Envio:
    def __init__(self, cod, dp, tip, fp):
        self.codigo = cod
        self.direccion = dp
        self.tipo = tip
        self.pago = fp

    def __str__(self):
        cad = 'Código postal: {:<10} | Direccion: {:<20} | Pais: {:<12} | Tipo de envio: {:<2} | Forma de pago: {:<3} | Importe total: {:<3}'
        cad = cad.format(self.codigo, self.direccion, self.country(), self.tipo, self.pago, self.final_amount())
        return cad

    def country(self):
        cp = self.codigo
        n = len(cp)
        if n < 4 or n > 9:
            return 'Otro'

        # ¿es Argentina?
        if n == 8:
            if cp[0].isalpha() and cp[0] not in 'IO' and cp[1:5].isdigit() and cp[5:8].isalpha():
                return 'Argentina'
            else:
                return 'Otro'

        # ¿es Brasil?
        if n == 9:
            if cp[0:5].isdigit() and cp[5] == '-' and cp[6:9].isdigit():
                return 'Brasil'
            else:
                return 'Otro'

        if cp.isdigit():
            # ¿es Bolivia?
            if n == 4:
                return 'Bolivia'

            # ¿es Chile?
            if n == 7:
                return 'Chile'

            # ¿es Paraguay?
            if n == 6:
                return 'Paraguay'

            # ¿es Uruguay?
            if n == 5:
                return 'Uruguay'

        # ...si nada fue cierto, entonces sea lo que sea, es otro...
        return 'Otro'

    def check_dir(self):
        cl = cd = 0
        td = False
        ant = " "
        for car in self.direccion:
            if car in " .":
                # fin de palabra...
                # un flag si la palabra tenia todos sus caracteres digitos...
                if cl == cd:
                    td = True

                # resetear variables de uso parcial...
                cl = cd = 0
                ant = " "

            else:
                # en la panza de la palabra...
                # contar la cantidad de caracteres de la palabra actual...
                cl += 1

                # si el caracter no es digito ni letra, la direccion no es valida... salir con False...
                if not car.isdigit() and not car.isalpha():
                    return False

                # si hay dos mayusculas seguidas, la direccion no es valida... salir con False...
                if ant.isupper() and car.isupper():
                    return False

                # contar digitos para saber si hay alguna palabra compuesta solo por digitos...
                if car.isdigit():
                    cd += 1

                ant = car

        # si llegamos acá, es porque no había dos mayusculas seguidas y no habia caracteres raros...
        # ... por lo tanto, habria que salir con True a menos que no hubiese una palabra con todos digitos...
        return td

    def final_amount2(self):
        # determinación del importe inicial a pagar.
        importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
        monto = importes[self.tipo]

        if self.country() == 'Argentina':
            inicial = monto
        else:
            if self.country() == 'Bolivia' or self.country() == 'Paraguay' or (self.country() == 'Uruguay' and self.codigo[0] == '1'):
                inicial = int(monto * 1.20)
            elif self.country() == 'Chile' or (self.country() == 'Uruguay' and self.codigo[0] != '1'):
                inicial = int(monto * 1.25)
            elif self.country() == 'Brasil':
                if self.codigo[0] == '8' or self.codigo[0] == '9':
                    inicial = int(monto * 1.20)
                else:
                    if self.codigo[0] == '0' or self.codigo[0] == '1' or self.codigo[0] == '2' or self.codigo[0] == '3':
                        inicial = int(monto * 1.25)
                    else:
                        inicial = int(monto * 1.30)
            else:
                inicial = int(monto * 1.50)

        # determinación del valor final del ticket a pagar.
        # asumimos que es pago en tarjeta...
        final = inicial

        # ... y si no lo fuese, la siguiente será cierta y cambiará el valor...
        if self.pago == 1:
            final = int(0.9 * inicial)

        return final


    def final_amount(self):
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

def generar_objeto(linea):
    partes = linea.split(',')
    cp = partes[0]
    de = partes[1]
    te = int(partes[2])
    fp = int(partes[3])
    obj = Envio(cp, de, te, fp)
    return obj