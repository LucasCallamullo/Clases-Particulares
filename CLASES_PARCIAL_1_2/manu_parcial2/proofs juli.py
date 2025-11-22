


def validar_mayusculas(i):
    if i in "QWERTYUIOPASDFGHJKLÑZXCVBNM":
        return True
    return False

def validar_digitos(ultima):
    if ultima in "0123456789":
        return True
    return False

def principal():
    m = open("archivo.txt", "rt")
    linea= m.readline()
    m.close()
    linea = "La fila f34 parece completa pero la columna C3 y el sector x4g5 no."


    r1 = r2 = r3 = r4 = 0

    """1- Determinar la cantidad de palabras que terminan con un dígito pero no tienen ninguna mayúscula"""

    r1ultima = ""
    r1_no_tiene_mayus = True
    r1_termina_digito = False


    for i in linea:

        #estoy adentro de la palabra
        if i != " " and i != ".":

            #r1
            es_mayuscula = validar_mayusculas(i)
            if es_mayuscula:
                r1_no_tiene_mayus = False

            r1ultima = i

        #estoy fuera de la palabra
        else:
            es_digito = validar_digitos(r1ultima)
            if es_digito:
                r1_termina_digito = True

            if r1_termina_digito and r1_no_tiene_mayus:
                r1 += 1

            #REINICIAR CONTADORES, APAGAR BANDERAS
            r1ultima = ""
            r1_no_tiene_mayus = True
            r1_termina_digito = False

    #estoy fuera del ciclo for
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__ == '__main__':
    principal()