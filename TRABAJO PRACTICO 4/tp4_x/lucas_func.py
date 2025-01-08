class Ticket:
    def __init__(self, codigo, patente, tipo, forma_pago, pais_cabina, distancia):
        self.codigo = codigo
        self.patente = patente
        self.tipo = tipo
        self.forma_pago = forma_pago
        self.pais_cabina = pais_cabina
        self.distancia = distancia

    def __str__(self):
        return 'Codigo: ' + str(self.codigo) + ' - Patente: ' + str(self.patente) + ' - Tipo de vehículo: ' + str(self.tipo) + ' - Forma de pago: ' + str(self.forma_pago) + ' - País de la cabina: ' + str(self.pais_cabina) + ' - Distancia: ' + str(self.distancia)


def crear(linea):
    token = linea.split(',')
    codigo = int(token[0])
    patente = token[1]
    tipo = int(token[2])
    forma_pago = int(token[3])
    pais_cabina = int(token[4])
    distancia = int(token[5])
    return Ticket(codigo, patente, tipo, forma_pago, pais_cabina, distancia)


