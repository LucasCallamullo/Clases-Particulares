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


if __name__ == "__main__":
    e1 = Envio("98176-453", "Pele 2536.", 4, 2)
    p1 = e1.country()
    print("Pais:", p1)
    print("Direccion valida?:", e1.check_dir())
    print(e1)

    e2 = Envio("76543", "Independencia 374", 2, 1)
    print(e2)
