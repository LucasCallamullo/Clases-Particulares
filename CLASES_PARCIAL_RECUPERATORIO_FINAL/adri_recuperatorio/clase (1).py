class Alquiler:
    """
    nombre del juego,
    nombre de la persona que alquiló el juego,
    el tipo de juego (un entero entre 0 y 4: Ej.: 0: Acción, 1: Aventura, 2: Rol (RPG), 3: Shooter, 4: Estrategia),
    mes de publicación (1: enero, 2: febrero, etc. hasta 12: diciembre)
    y el monto del alquiler.
    """
    # nombre, persona, tipo 0 4, mes 1 12, monto
    def __init__(self, nombre, persona, tipo, mes, monto):
        self.nombre = nombre
        self.persona = persona
        self.tipo = tipo
        self.mes = mes
        self.monto = monto

    def __str__(self):
        juego = ("Acción", "Aventura", "Rol (RPG)", "Shooter", "Estrategia")
        r = " "
        r += "{:30}".format("Nombre del juego: " + self.nombre)
        r += "{:15}".format("|Persona :" + self.persona)
        r += "{:15}".format("|Tipo: " + str(self.tipo))
        r += "{:30}".format("(" + str(juego) + ")")
        r += "{:15}".format("|Mes: " + str(self.mes))
        r += "{:15}".format("|Monto: " + str(self.monto))

        return r
