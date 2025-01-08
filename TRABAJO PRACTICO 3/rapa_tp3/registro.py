class Envio:

    def __init__(self, cod_postal, direccion, tipo_envio, forma_pago):
        self.cod_postal = cod_postal
        self.direccion = direccion
        self.tipo_envio = tipo_envio
        self.forma_pago = forma_pago

    def __str__(self):
        cad = 'Código postal: {:<10} | Direccion: {:<20} | Pais: {:<12} | Tipo de envio: {:<2} | Forma de pago: {:<3}'
        cad = cad.format(self.cod_postal, self.direccion, self.obtener_destino_pais(), self.tipo_envio, self.forma_pago)
        return cad

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

    def calcular_importe(self):
        cp = self.cod_postal
        pago = self.forma_pago
        tipo = self.tipo_envio
        destino = self.obtener_destino_pais()

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

    def obtener_destino_pais(self):
        cp = self.cod_postal
        n = len(cp)
        if cp[0:5].isdigit() and cp[5:6] == "-" and cp[6:9].isdigit():
            return "Brasil"

        elif cp[0].isalpha() and cp[1:5].isdigit() and cp[5:8].isalpha() and n == 8 and cp[0] != 'I' and cp[0] != 'O':
            return "Argentina"

        elif cp[0:7].isdigit() and n == 7:
            return "Chile"

        elif cp[0:6].isdigit() and n == 6:
            return "Paraguay"

        elif cp[0:5].isdigit() and n == 5:
            return "Uruguay"

        elif cp[0:4].isdigit() and n == 4:
            return "Bolivia"

        else:
            return "Otro"


if __name__ == "__main__":
    e1 = Envio("98176-453", "Pele 2536.", 4, 2)
    p1 = e1.obtener_destino_pais()
    print("Pais:", p1)
    print("Direccion valida?:", e1.check_dir())
    print(e1)

    e2 = Envio("76543", "Independencia 374", 2, 1)
    print(e2)
