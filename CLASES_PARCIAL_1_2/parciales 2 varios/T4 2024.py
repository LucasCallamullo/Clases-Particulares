

def validar_vocales(i):
    if i.lower() in "aeiou":
        return True
    else:
        return False


def validar_digitos(i):
    if i in "0123456789":
        return True
    else:
        return False

def principal():

    m = open("entrada.txt", "r")
    linea= m.readline()
    m.close()

    # 1. Determinar la cantidad de palabras que tienen más dígitos que vocales, pero solo una consonante. Por
    # ejemplo, en el texto: "R23A es un robot similar a R2D2 y C256 pero muy distinto de U57E3." hay dos
    # palabras que cumplen: "R23A" y "C256".
    r1 = 0
    r1_cont_vocales = 0
    r1_cont_digitos = 0
    r1_tiene_consonante = 0


    # 2. Determinar la longitud de la palabra más corta entre aquellas que tienen al menos una "s" o al menos una
    # "c" (minúsculas o mayúsculas). Por ejemplo, en el texto: "Antes de anclar cae el ocaso." Hay cuatro palabras
    # que cumplen ("Antes", "anclar", "cae" y "ocaso"), y la menor longitud entre esas palabras es de 3
    # caracteres (en la palabra "cae").
    indice = 0
    r2 = None
    r2_tiene_nos = False

    # 3. Determinar el porcentaje entero que representan las palabras que no tienen dígitos sobre el total del
    # palabras del texto. Por ejemplo, en el texto "Estamos en la zona X3 o en la T5." hay 9 palabras en total, y 7
    # de ellas no tienen dígitos. Por lo tanto, el porcentaje entero pedido es del 77 por ciento. Aclaración: al
    # calcular el porcentaje, haga primero la multiplicación y luego la división.
    r3 = 0
    r3_tiene_digito = False
    r3_cantnodig = 0
    r3_cantidad_palabras = 0

    # 4. Determinar cuántas palabras empiezan con la expresión "vi" (con cualquiera de sus letras en minúscula o
    # mayúscula) y tengan además una "n" en cualquier lugar. Por ejemplo, en el texto: "Aviso el viernes envia
    # su mensaje a AVEIT." hay una palabra que cumple: "viernes".
    r4 = 0
    r4_tiene_v = False
    r4_tiene_vi = False
    r4_letra_n = False


    for i in linea:
        if i != " " and i != ".":
            indice += 1

            # PUNTO 1
            es_vocal = validar_vocales(i)
            es_digito = validar_digitos(i)

            if es_vocal:
                r1_cont_vocales += 1
            if es_digito:
                r1_cont_digitos += 1
            if i.lower() in "bcdfghjklmnñpqrstvwxyz":
                r1_tiene_consonante += 1

            # PUNTO 2
            if i.lower() == "s" or i.lower() == "c":
                r2_tiene_nos = True

            # PUNTO 3
            if i in "0123456789":
                r3_tiene_digito = True

            # PUNTO 4

            if i.lower() == "n":
                r4_letra_n = True

            if r4_tiene_v and i.lower() == "i":
                r4_tiene_vi = True
                r4_tiene_v = False

            elif i.lower() == "v" and indice == 1:
                r4_tiene_v = True
            else:
                r4_tiene_v = False


        else:
            #1
            if r1_tiene_consonante == 1 and r1_cont_digitos > r1_cont_vocales:
                r1 += 1
            #2
            if r2_tiene_nos:
                if r2 is None or r2 > indice:
                    r2 = indice
            #3
            r3_cantidad_palabras += 1
            if not r3_tiene_digito:
                r3_cantnodig += 1

            #4
            if r4_letra_n and r4_tiene_vi:
                r4 += 1


            #APAGAR
            indice = 0
            r1_cont_vocales = 0
            r1_cont_digitos = 0
            r1_tiene_consonante = 0
            r2_tiene_nos = False
            r3_tiene_digito = False
            r4_tiene_v = False
            r4_tiene_vi = False
            r4_letra_n = False


    porc = 0
    if r3_cantidad_palabras > 0:
        porc = (r3_cantnodig * 100) // r3_cantidad_palabras
    r3 = porc


    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    principal()