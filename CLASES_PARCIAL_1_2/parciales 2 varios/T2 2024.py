



def validar_consonantes(i):
    if i.lower() in "bcdfghjklmnñpqrstvwxyz":
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
    linea = m.readline()
    m.close()

    # 1. Determinar la cantidad de palabras que tienen una consonante en la tercera o en la cuarta posición y
    # además tienen un dígito en cualquier parte. Por ejemplo, en el texto: "SALU4 o PAE3 son codigos malos en
    # el mercado como salTA37." Respuesta: hay dos palabras que cumplen: "SALU4" y "salTA37".
    r1 = 0
    indice = 0
    consonante_34 = False
    digito_p = False

    # 2. Determinar la longitud de la palabra más corta entre las que comienzan con "s" (minúscula o mayúscula).
    # Por ejemplo, en el texto "Salen siempre temprano las aves del sol." Hay tres palabras que empiezan con "s"("Salen", "siempre" y "sol") y la palabra más corta de esas tres es "sol", con 3 caracteres. Por lo tanto, la
    # respuesta para este ejemplo es 3.
    r2 = None
    primera_s = False

    # 3. Determinar el porcentaje entero de palabras (con respecto al total de palabras del texto), de las palabras
    # que tienen dos o más vocales. Por ejemplo, en el texto: "Andamos a los tumbos." hay dos palabras que
    # cumplen el criterio: "Andamos" y "tumbos". Como hay 4 palabras en total, el porcentaje entero pedido es
    # del 50 por ciento (aclaración: en el cálculo del porcentaje haga primero la multiplicación y luego la
    # división).
    r3 = 0
    tiene_vocal = 0
    cumplio = 0
    total_p = 0

    # 4. Determinar cuántas palabras incluyen una sola vez la expresión "ni" (con cualquiera de sus letras en
    # minúscula o mayúscula). Por ejemplo, en el texto: "Ningun navio y ninguna ninfa es lindo ni feo en Ninive."
    # hay cuatro palabras que cumplen: "Ningun", "Ninguna", "ninfa" y "ni". La palabra "Ninive" no cuenta
    # porque tiene la expresión más de una vez.
    r4 = 0
    tiene_n = False
    tiene_ni = 0

    for i in linea:
        if i != " " and i != ".":
            indice += 1


            #punto 1
            tiene_cons = validar_consonantes(i)
            tiene_dig = validar_digitos(i)

            if tiene_cons and (indice == 3 or indice ==4):
                consonante_34 = True

            if tiene_dig:
                digito_p = True

            # PUNTO 2
            if i.lower() == "s" and indice == 1:
                primera_s = True

            # PUNTO 3
            if i.lower() in "aeiou":
                tiene_vocal += 1

            # Punto 4
            # nii
            if tiene_n and i.lower() == "i":
                tiene_ni += 1
                tiene_n = False

            elif i.lower() == "n":
                tiene_n = True
            else:
                tiene_n = False

        else:
            #1
            if consonante_34 and digito_p:
                r1 += 1
            #2
            if primera_s:
                if r2 is None or r2 > indice:
                    r2 = indice
            #3
            total_p += 1
            if tiene_vocal >= 2:
                cumplio += 1

            #4
            if tiene_ni == 1:
                r4 += 1




            #apagar
            indice = 0
            consonante_34 = False
            digito_p = False
            primera_s = False
            tiene_vocal = 0
            tiene_n = False
            tiene_ni = 0

    porc = 0
    if total_p > 0:
        porc = (cumplio * 100) // total_p
    r3 = porc

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)





if __name__ == "__main__":
    principal()