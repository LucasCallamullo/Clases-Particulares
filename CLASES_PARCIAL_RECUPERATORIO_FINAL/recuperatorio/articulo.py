class Articulo:
    def __init__(self, codigo, titulo, nombre_autor):
        self.codigo = codigo
        self.titulo = titulo
        self.nombre_autor = nombre_autor

    def __str__(self):
        sep = '-'
        cadena = '| {:<10} | {:<100} | {:<20} |\n{:<135}'
        return cadena.format(self.codigo, self.titulo, self.nombre_autor, sep * 140)