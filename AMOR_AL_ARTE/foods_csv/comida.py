class Comida:
    
    def __init__(self, name, proteins, carbohydrates, category):
        self.name = name
        self.proteins = proteins
        self.carbohydrates = carbohydrates
        self.category = category
        self.precio = 100
        self.descuento = 10

    def __str__(self):
        cad = f"Nombre: {self.name} - Proteínas: {self.proteins} - Carbohidratos: {self.carbohydrates}"
        cad += f" - Category: {self.category} - Total {self.calcular_total()}"
        return cad

    def calcular_total(self):
        total = self.precio - self.precio * 0.1
        return total