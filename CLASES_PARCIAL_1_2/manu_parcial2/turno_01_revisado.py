# r3
def validar_digito(caracter):
    if caracter in "0123456789":
        return True
    return False


def principal():
    m = open("archivo.txt", "rt")
    linea = m.readline()
    m.close()

    # r1
    """
    1- Determinar la cantidad de palabras que tienen una "x" en la segunda posición.
    """
    r1 = 0
    indice = 0
    r1_tiene_x_pos2 = False

    """
    2- Determinar la longitud de la palabra más larga del texto. 
    """
    r2 = None
    r2_cont_caracter = 0        # podes reutilizar el indice en vez de hacer otro cont caracteres

    """
    3- Determinar el promedio entero de caracteres por palabra, de las palabras que tienen algún dígito en
    cualquier lugar.

    prom = sumatoria de caracteres / cantidad de palabras
    """
    r3 = 0
    r3_acum_contador = 0
    r3_cont_palabras = 0

    r3_tiene_digito = False

    """
    4- Determinar cuántas palabras incluyen la expresión "te" en cualquier lugar. Por ejemplo, en el texto: "En
    este tejado no se atienen a las normas.
    """
    r4 = 0
    r4_tiene_t = False
    r4_tiene_te = False

    for caracter in linea:
        if caracter != " " and caracter != ".":

            indice += 1
            # r1
            if caracter.lower() == "x" and indice == 2:
                r1_tiene_x_pos2 = True

            # r2
            # como no te pide condiciones extra realmente no tenías que hacer nada dentro de la palabra

            # if caracter > indice:     # NOTA siempre mira las variables que comparas, estas comparando
            #                           el caracter es decir una letra es decir un STR, con un indice
            #                           que indica posicion, que se va incrementando, que es un numero,
            #                           que es un entero un INT, es decir no se pueden ni comparar un INT con STR
            #                           cuando quieras plantear una condicion siempre preguntate que estas comparando
            #   r2_cont_caracter = True

            # r3
            es_digito = validar_digito(caracter)
            if es_digito is True:
                r3_tiene_digito = True

            # r4
            if r4_tiene_t is True and caracter.lower() == "e":
                r4_tiene_te = True
            elif caracter.lower() == "t":
                r4_tiene_t = True
            else:
                r4_tiene_t = False

        else:
            # r1
            if r1_tiene_x_pos2 is True:
                r1 += 1

            # r2
            if r2 is None or r2 > indice:   # esto esta perfecto es lo unico que tenias que poner del r2 realmente
                r2 = indice

            # r3
            if r3_tiene_digito is True:
                r3_acum_contador += indice
                r3_cont_palabras += 1

            # r4
            if r4_tiene_te is True:
                r4 += 1

            # reiniciar banderas/ contadores
            # r1
            indice = 0
            r1_tiene_x_pos2 = False

            # r2
            # r2_cont_mas_larga = 0   # esta variable no existe acordate de copiar y pegar desde donde las creaste
                                    # en este caso solo hay "r2" asique no lo tenias que reiniciar

            # r3
            r3_tiene_digito = False

            # r4
            r4_tiene_t = False
            r4_tiene_te = False

    if r3_cont_palabras > 0:
        r3 = r3_acum_contador // r3_cont_palabras

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()