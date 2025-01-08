

# clase / registro / objeto
class Parlante:

    # id > 0, descripcion STR, marca(1, 5), peso(200, 220) INT, importe > 0 FLOAT,

    # funcion constructora o inicializadora
    def __init__(self, id, descripcion, marca, peso, importe):
        # ctrl + d
        self.id = id
        self.descripcion = descripcion
        self.marca = marca
        self.peso = peso
        self.importe = importe

    # la funcion que reemplaza al print
    def __str__(self):
        # ctrl + d
        cadena = "ID: " + str(self.id)
        cadena += " | Desripcion: " + self.descripcion
        cadena += " | Marca: " + str(self.marca)
        cadena += " | Peso: " + str(self.peso)
        cadena += " | Importe: " + str(self.importe)
        return cadena
