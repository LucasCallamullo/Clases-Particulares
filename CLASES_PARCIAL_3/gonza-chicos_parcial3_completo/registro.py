

# clases - registro - objetos
class Figurita:

    # tupla_posiciones = ("Arquero", "Defensor", "Volante", "Delantero")

    # pais(1, 32) INT, num_jug(1, 19) INT, nombre STR, posicion(1, 4), importe > 0 FLOAT

    # funcion constructora o inicializadora
    def __init__(self, pais, num_jug, nombre, posicion, importe):
        # ctrl + d
        self.pais = pais
        self.num_jug = num_jug
        self.nombre = nombre
        self.posicion = posicion
        self.importe = importe

    # funcion que reemplaza al print
    def __str__(self):
        # posicion(1, 4)        1           2           3           4
        # indices               0           1           2           3
        tupla_posiciones = ("Arquero", "Defensor", "Volante", "Delantero")

        cadena = (f"Pais: {self.pais}"
                  f" | Num_Jug: {self.num_jug}"
                  f" | Nombre: {self.nombre}"
                  f" | Posicion: {tupla_posiciones[self.posicion-1]}"
                  f" | Importe: {self.importe}")
        return cadena
