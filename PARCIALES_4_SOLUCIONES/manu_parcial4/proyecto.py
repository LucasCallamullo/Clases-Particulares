class Lote:
    """
Una empresa que comercializa terrenos necesita registrar los detalles de los lotes vendidos en un emprendimiento.
Por cada lote se conoce: Nombre y apellido del propietario (una cadena), número de manzana (entero entre 1 y
35), número de lote dentro de la manzana (entero entre 1 y 20), orientación del terreno (1: Norte, 2: Sur, 3: Este, 4:
Oeste), superficie del terreno (número de m2) y finalmente el monto por el que se vendió el lote. Se pide definir la
calse Lote y desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las
siguientes tareas:
    """
    # nom_ape "ABCDEF", num_man (1, 35), num_lote (1, 20), ori_terreno (1, 4), sup_terreno, monto (1, 10)
    def __init__(self, nom_ape, num_man, num_lote, ori_terreno, sup_terreno, monto):

        self.nom_ape = nom_ape
        self.num_man = num_man
        self.num_lote = num_lote
        self.ori_terreno = ori_terreno
        self.sup_terreno = sup_terreno
        self.monto = monto

    def __str__(self):
        tupla_terreno = ("Norte", "Sur", "Este", "Oeste")

        cadena = " Nombre Apellido: " + str(self.nom_ape)
        cadena += " | Numero Manzana: " + str(self.num_man)
        cadena += " | Numero Lote: " + str(self.num_lote)
        cadena += " | Orientacion Terreno: " + tupla_terreno[self.ori_terreno - 1]
        cadena += " | Superficie Terreno: " + str(self.sup_terreno)
        cadena += " | Monto: " + str(self.monto)
        return cadena