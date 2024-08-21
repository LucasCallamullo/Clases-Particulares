

class Trabajo:
    # tipo_t = un valor de 0 a 3,
    # id e importe > 0
    # Constructor
    def __init__(self, id, desc, tipo_t, importe, cant_p):
        self.id = id        # ctrl + d
        self.desc = desc
        self.tipo_t = tipo_t
        self.importe = importe
        self.cant_p = cant_p

    def __str__(self):
        # Ejemplo : Te podrian que tipo_t sea un intervalo de (1, 4) pero que en pantalla debe mostrarse lo siguiente
        # 1:interior, 2:exterior, 3:piletas, 4:tapizados segun corresponda.
        # print("El numero del tipo es: ", self.tipo_t)           #  self.tipo_t = 2

        tipo_t_str = tipo_t_to_str(self.tipo_t)     # self.tipo_t = 2       ;   tipo_t_str = "Piletas"

        cadena = "ID: " + str(self.id)
        cadena += " | Desc: " + self.desc
        cadena += " | tipo_t: " + tipo_t_str
        cadena += " | importe: " + str(self.importe)
        cadena += " | cant_p: " + str(self.cant_p)
        return cadena


def tipo_t_to_str(tipo_t): # tipo_t = 2
    # tipo_t(1,4)   1           2           3           4
    #               0           1           2           3
    trabajos = ["Interior", "Exterior", "Piletas", "Tapizados"]

    # tipo_t 1
    t_str = trabajos[tipo_t-1]     # Str - string - "Piletas"
    return t_str        # "Piletas"
