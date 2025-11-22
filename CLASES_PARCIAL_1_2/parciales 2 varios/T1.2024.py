
def principal():
    m = open("../entrada.txt", "r")
    linea = m.readline()

    m.close()

    #1. Determinar la cantidad de palabras que tienen una "x" en la segunda posición. Por ejemplo,
    # en el texto: "El expresidente es también exjugador y no es xenófobo." hay 2 palabras que cumplen:
    # "expresidente" y"exjugador". La palabra "xenófobo" tiene una "x" pero no cumple porque la tiene en primera
    r1 = 0
    indice = 0
    x_posicion2 = False

    #2. Determinar la longitud de la palabra más larga del texto. Por ejemplo, en el texto "La verdad se devela
    #tarde o temprano." la palabra más larga es "temprano", con 8 caracteres. Por lo tanto, la respuesta para
    #este ejemplo es 8.
    r2 = None

    #3. Determinar el promedio entero de caracteres por palabra, de las palabras que tienen algún dígito en
    #cualquier lugar. Por ejemplo, en el texto: "El sector SDR3 acusa un error de la forma E83PC." hay dos
    #palabras con al menos un dígito("SDR3" y "E83PC"). Entre las dos suman 9 caracteres, por lo que el
    #promedio entero pedido es 4 caracteres por palabra (promedio = acumulado de la cantidad de letras entre
    #las palabras que cumplen // cantidad de palabras que cumplen).
    r3 = 0
    tiene_digito = False
    acum_pd = 0
    cont_pd = 0

    #4. Determinar cuántas palabras incluyen la expresión "te" en cualquier lugar. Por ejemplo, en el texto:
    # "Eneste tejado no se atienen a las normas." hay dos palabras que cumplen: "este" y "tejado". La palabra
    #"atienen" no cuenta ya que hay una "i" entre la "t" y la "e".
    r4 = 0
    tiene_t = False
    tiene_te = False



    for i in linea:
        if i != " " and i != ".":
            indice += 1
            # PUNTO 1
            if i.lower() == "x" and indice == 2:
                x_posicion2 = True

            # PUNTO 3
            if i in "0123456789":
                tiene_digito = True

            # PUNTO 4

            if tiene_t and i.lower() == "e":
                tiene_te = True
            elif i.lower() == "t":
                tiene_t = True
            else:
                tiene_t = False



        else:
            # 1
            if x_posicion2:
                r1 += 1
            # 2
            if r2 is None or r2 < indice:
                r2 = indice
            # 3
            if tiene_digito:
                acum_pd += indice
                cont_pd += 1
            # 4
            if tiene_te:
                r4 += 1

            #APAGAR
            indice = 0
            x_posicion2 = False
            tiene_digito = False
            tiene_t = False
            tiene_te = False

    prom = 0
    if cont_pd > 0:
        prom = acum_pd // cont_pd
    r3 = prom

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)
















if __name__ == "__main__":
    principal()