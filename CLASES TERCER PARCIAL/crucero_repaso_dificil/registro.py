

class Pasaje:
    # destino(100, 103)  (100: Bahamas, 101: Bermudas: 102: Puerto Rico, 103: República Dominicana)
    # pasaporte = str   ; clase (1, 10)
    def __init__(self, pasaporte, nombre, destino, clase, importe):
        self.pasaporte = pasaporte          # ctrl + d
        self.nombre = nombre
        self.destino = destino
        self.clase = clase
        self.importe = importe

    def __str__(self):
        destino_str = destino_to_str(self.destino)

        cadena = "Pasaporte: " + self.pasaporte
        cadena += " | Nombre: " + self.nombre
        cadena += " | Destino: " + destino_str
        cadena += " | Clase: " + str(self.clase)
        cadena += " | Importe: " + str(self.importe)
        return cadena


def destino_to_str(destino):
    # destino(100, 103)   100-100      101-100      102-100             103-100
    # indices                 0           1           2                   3
    paises =             ["Bahamas", "Bermudas", "Puerto Rico", "República Dominicana"]
    dest = paises[destino-100]
    return dest



def mostrardatosop2(vector):
    acum = 0
    for i in vector:
        if i:
        # if (condición que te pida a comparar en caso de que te pidan comparar):
            print(i)
            acum = i.importe
    print("El total acumulado de los que se mostraron fue:", acum)
