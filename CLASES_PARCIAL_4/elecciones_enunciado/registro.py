


class Eleccion:
    def __init__(self, candidato, provincia, votante, votos):
        self.candidato = candidato
        self.provincia = provincia
        self.votante = votante
        self.votos = votos

    def __str__(self):
        # candidato =  1-1            2           3
        #               0           1           2
        candidatos = ["Massa", "Bullrich", "Milei"]
        # candidatos_str = candidatos_to_str(self.candidato)

        cad = "Candidato: " + candidatos[self.candidato-1]
        cad += " | Provincia: " + str(self.provincia)
        cad += " | Votante: " + str(self.votante)
        cad += " | Votos: " + str(self.votos)
        return cad


def candidatos_to_str(candidato):
    candidatos = ["Massa", "Bullrich", "Milei"]
    return candidatos[candidato-1]
