

# Clase resgistro objeto
class Envio:
    # cod_postal STR ; direccion STR ; tipo_envio(0, 6) ; forma_pago(1, 2)
    def __init__(self, cod_postal, direccion, tipo_envio, forma_pago):
        self.cod_postal = cod_postal
        self.direccion = direccion
        self.tipo_envio = tipo_envio
        self.forma_pago = forma_pago

    def __str__(self):
        # .format <20:

        # Si una variable esta igualada a una funcion es porque esperas que la funcion retorne algun valor
        destino_str = obtener_destino_pais(self.cod_postal)

        cadena = "Cod Postal: " + self.cod_postal
        cadena += " | Destino: " + destino_str
        cadena += " | Direccion: " + self.direccion
        cadena += " | Tipo de Envio: " + str(self.tipo_envio)
        cadena += " | Forma de Pago: " + str(self.forma_pago)
        return cadena


def obtener_destino_pais(cp):
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
