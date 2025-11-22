class Tubo:

    # cod_prod Entero, diametro_pulg, tipo_apli (1, 20), gramaje, ingnifugo
    def __init__(self, cod_prod, diam_pulg, tipo_apli, gramo, igni):
        self.cod_prod = cod_prod
        self.diam_pulg = diam_pulg
        self.tipo_apli = tipo_apli
        self.gramo = gramo
        self.igni = igni

    def __str__(self):
        cadena = "Codigo: " + str(self.cod_prod)
        cadena += " | Diamentro: " + str(self.diam_pulg)
        cadena += " | Aplicacion: " + str(self.tipo_apli)
        cadena += " | Gramaje: " + str(self.gramo)
        cadena += " | Ignifugo:" + str(self.igni)
        return cadena

