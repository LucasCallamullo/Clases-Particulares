class Vehiculo:
    # marca STR , id INT, tam (1, 4), tipo(5, 9), importe FLOAT
    def __init__(self, marca, id, tam, tipo, importe):
        self.marca = marca
        self.id = id
        self.tam = tam
        self.tipo = tipo
        self.importe = importe

    def __str__(self):
        
        if self.disponible:
            mensaje = "Propietario"
        else:
            mensaje = "No Propietario"

        
        cadena = "Disponible: " + mensaje
        
        
        
        # tamaños          1-1           2           3           4
        # indices           0           1           2           3
        tupla_tams = ("Subcompacto", "Compacto", "Mediano", "Grande")

        # tipo (5, 9)   5-5         6        7          8           9
        tuplas_tipo =  ("Nafta", "Gasoil", "GNC", "Eléctrico", "Hidrógeno")

        cad = "Marca: " + self.marca
        cad += " | ID: " + str(self.id)
        cad += " | Tamaño: " + tupla_tams[self.tam-1]
        cad += " | Tipo: " + tuplas_tipo[self.tipo-5]
        cad += " | Importe: " + str(self.importe)
        return cad