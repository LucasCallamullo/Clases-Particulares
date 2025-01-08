class Ticket:
    def __init__(self, codigo_id, patente, tipo_vehiculo, m_base, manu_tele, t_pago, pais_cab, km):
        self.codigoid = codigo_id
        self.pat = patente
        self.tipovehiculo = tipo_vehiculo
        self.monto_base = m_base
        self.manutele = manu_tele
        self.total_pago = t_pago
        self.paiscabi = pais_cab
        self.kilometros = km

    def __str__(self):
        patente_pais = determinar_procedencia(self.pat)
        cad = "El ID es: " + str(self.codigoid)
        cad += '{:<30}'.format(" | La patente es: " + str(self.pat) + " es de " + patente_pais[0])
        vehiculo = ["MOTOCICLETA", "AUTOMOVIL", "CAMION"][self.tipovehiculo]
        cad += '{:<38}'.format(" | El tipo de vehiculo es: " + vehiculo)
        cad += '{:<9}'.format(" -p/base $ " + str(self.monto_base))
        formapago = ["MANUAL", "TELEPEAJE"][(self.manutele - 1)]
        cad += '{:<33}'.format(" | El tipo de pago es: " + formapago)
        cad += '{:<13}'.format(" -total $ " + str(self.total_pago))
        pais = ["ARGENTINA", "BOLIVIA", "BRASIL", "PARAGUAY", "URUGUAY"][self.paiscabi]
        cad += '{:<32}'.format(" | cabina es del pais: " + pais)
        cad += '{:<32}'.format(" | Los kilometros recorridos son: " + str(self.kilometros)) + "|"
        return cad


def determinar_procedencia(patente):
    if len(patente) != 7:
        return "OTRO", 6
    else:
        modelo = ""
        for car in patente:
            if "A" <= car <= "Z":
                modelo += "L"
            elif car == " ":
                modelo += " "
            else:
                modelo += "N"

        if modelo == "LLNNNLL":
            return "ARGENTINA", 0
        elif modelo == "LLLNLNN":
            return "BRASIL", 1
        elif modelo == "LLNNNNN":
            return "BOLIVIA", 2
        elif modelo == "LLLLNNN":
            return "PARAGUAY", 3
        elif modelo == "LLLNNNN":
            return "URUGUAY", 4
        elif modelo[0] == " " and modelo == " LLLLNN":
            return "CHILE", 5
        else:
            return "OTRO", 6
