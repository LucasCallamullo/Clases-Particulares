

# Clase Objeto
class Venta:
    # tipo_perf es un entero (1, 4)
    def __init__(self, num_f, importe, tipo_f, apellido, tipo_perf):
        self.num_f = num_f      # ctrl + D
        self.importe = importe
        self.tipo_f = tipo_f
        self.apellido = apellido
        self.tipo_perf = tipo_perf


    def __str__(self):
        marca = tipo_perf_to_str(self.tipo_perf)

        cadena = "Num de Factura: " + str(self.num_f)
        cadena += "| Importe: " + str(self.importe)
        cadena += "| Tipo de Fact: " + self.tipo_f
        cadena += "| Apellido: " + self.apellido
        cadena += "| Marca: " + marca
        return cadena


def tipo_perf_to_str(tipo_perf):
    #               0           1             2       3
    perfumes = ["Channel", "Paco Rabanne", "Polo", "Tomy"]
    # tipo_perf (1, 4)
    return perfumes[tipo_perf-1]
