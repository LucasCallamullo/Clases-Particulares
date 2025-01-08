CABINAS = ("ARGENTINA", "BOLIVIA", "BRASIL", "PARAGUAY", "URUGUAY")
TIPOS = ("MOTO", "AUTO", "CAMIÓN")
PAISES = ("ARGENTINA", "BOLIVIA", "BRASIL", "PARAGUAY", "URUGUAY", "CHILE", "OTRO")


class Ticket:
    def __init__(self, cod, pat, tipo, pago, cab, d, imp):
        self.codigo = cod
        self.patente = pat
        self.tipo_vehiculo = tipo
        self.forma_pago = pago
        self.cabina = cab
        self.distancia = d
        self.imp_final = imp

    def __str__(self):
        cad = "Código: {:^9} | Patente: {:^8} | País: {:^10} | Vehículo: {:^6} | Forma de pago: {:^10} | Cabina: {" \
              ":^9} | Distancia recorrida: {:^3}km"
        return cad.format(self.codigo, self.patente, patente(self.patente), TIPOS[self.tipo_vehiculo], definir_pago(self.forma_pago), CABINAS[self.cabina], self.distancia)


def patente(pat):
    if pat[0:2].isalpha() and pat[5:7].isalpha() and pat[2:5].isnumeric():
        return "ARGENTINA"
    elif pat[0:2].isalpha() and pat[2:7].isnumeric():
        return "BOLIVIA"
    elif pat[0:3].isalpha() and pat[3].isnumeric() and pat[4].isalpha() and pat[5:7].isnumeric():
        return "BRASIL"
    elif pat[0:4].isalpha() and pat[4:7].isnumeric() and len(pat) == 7:
        return "PARAGUAY"
    elif pat[0:3].isalpha() and pat[3:7].isnumeric():
        return "URUGUAY"
    elif pat[0] == " " and pat[1:5].isalpha() and pat[5:7].isnumeric():
        return "CHILE"
    elif pat[0:4].isalpha() and pat[4].isnumeric() and pat[5].isnumeric() and len(pat) == 6:
        return "CHILE"
    else:
        return "OTRO"


def definir_pago(pago):
    if pago == 1:
        return "MANUAL"
    elif pago == 2:
        return "TELEPEAJE"
