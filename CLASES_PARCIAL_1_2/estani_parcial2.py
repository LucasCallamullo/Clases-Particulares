

# r1
def validar_mayusculas(i):
    if "A" <= i <= "Z":
        return True
    return False


def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    return False


# r3
def calcular_promedio(r3_total_cant, r3_total_acum):
    prom = 0
    if r3_total_cant != 0:
        prom = r3_total_acum // r3_total_cant
    return prom


def validar_consonantes(i):
    if i.lower() in "bcdfghjklmnpqrstvwxyz":
        return True
    else:
        return False


def validar_vocales(i):      # A
    # .lower() transformar al caracter en minuscula
    if i.lower() in "aeiou":  # si la i esta en "aeiou"
        return True     # retornar devolver
    else:
        return False


def principal():

    m = open("entrada.txt", "rt")   # read text ; leer texto
    linea = m.read()                # recuperar un str
    # linea = m.readline()          # recuperar un str

    ''' 1 - Determinar la cantidad de palabras que tienen un dígito en la segunda y en 
la cuarta posición, pero de tal forma que el resto de sus caracteres son letras mayúsculas 
'''
    r1 = 0
    r1_cont_caracteres = 0
    r1_tiene_digitos_pos2_pos4 = True
    r1_todas_mayusculas = True

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más corta 
entre aquellas que comienzan con una "t" (minúscula o mayúscula). y que su longitud sea par'''
    r2 = None
    r2_cont_caracteres = 0
    r2_empieza_t = False

    #                      Promedioo
    ''' 3 -  Determinar el promedio de caracteres de las palabras que tienen exactamente dos 
consonantes en las primeras cuatro posiciones y terminan con vocal. 
    # Promedio
        prom = acumulador // la cantida de cosas que acumulamos
'''
    r3 = 0
    r3_total_acum = 0
    r3_total_cant = 0
    r3_cont_caracteres = 0
    r3_cont_cons = 0
    r3_ultima_letra = ""

    ''' 4 - Determinar cuántas palabras incluyen la expresión "di" (con cualquiera de sus
letras en minúscula o mayúscula) pero de tal forma que a su vez no comiencen con 
la expresión "di". '''
    r4 = 0
    r4_tiene_d = False
    r4_tiene_di = False
    r4_cont_caracteres = 0
    r4_comienza_di = False

    for i in linea:

        # ===================================================
        # Estoy dentro de la palabra
        # ===================================================
        if i != " " and i != ".":

            # r1
            r1_cont_caracteres += 1

            if r1_cont_caracteres == 2 or r1_cont_caracteres == 4:
                es_digito = validar_digitos(i)      # return True si es digito, False si no lo es
                if not es_digito:       # "es_digito" esta en false
                    r1_tiene_digitos_pos2_pos4 = False

            else:
                es_mayuscula = validar_mayusculas(i)    # return True si es mayus, False si no lo es
                if not es_mayuscula:    # "es_mayuscula" esta en false
                    r1_todas_mayusculas = False

            # r2
            r2_cont_caracteres += 1

            if r2_cont_caracteres == 1 and i.lower() == "t":
                r2_empieza_t = True

            # r3
            r3_cont_caracteres += 1
            es_consonante_r3 = validar_consonantes(i)   # return True si era consonante, False si no l oes

            if r3_cont_caracteres <= 4 and es_consonante_r3:
                r3_cont_cons += 1

            r3_ultima_letra = i

            # r4
            r4_cont_caracteres += 1

            if r4_tiene_d and i.lower() == "i":
                r4_tiene_di = True

                if r4_cont_caracteres == 2:
                    r4_comienza_di = True

            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

            ''' encontrar la "t" antes de la sigla '''
            if i.lower() == "t" and not r4_tiene_di:
                pass
            ''' encontrar la "t" despues de la sigla '''
            if i.lower() == "t" and r4_tiene_di:
                pass

        # ===================================================
        # Termino la palabra / Estoy fuera de la palabra
        # ===================================================
        else:
            # r1
            if r1_tiene_digitos_pos2_pos4 and r1_todas_mayusculas:
                r1 += 1

            # r2
            if r2_empieza_t and r2_cont_caracteres % 2 == 0:
                if r2 is None or r2_cont_caracteres < r2:
                    r2 = r2_cont_caracteres

            # r3
            es_vocal_r3 = validar_vocales(r3_ultima_letra)     # return True si era vocal, False si no lo era
            if r3_cont_cons == 2 and es_vocal_r3:
                r3_total_acum += r3_cont_caracteres
                r3_total_cant += 1

            # r4
            if r4_tiene_di and not r4_comienza_di:
                r4 += 1
            # ===================================================
            # Reiniciar contadores, apagar banderas
            # ===================================================
            # r1
            r1_cont_caracteres = 0
            r1_tiene_digitos_pos2_pos4 = True
            r1_todas_mayusculas = True

            # r2
            r2_cont_caracteres = 0
            r2_empieza_t = False

            # r3
            r3_cont_caracteres = 0
            r3_cont_cons = 0
            r3_ultima_letra = ""

            # r4
            r4_tiene_d = False
            r4_tiene_di = False
            r4_cont_caracteres = 0
            r4_comienza_di = False


    # Termino del ciclo
    m.close()

    r3 = calcular_promedio(r3_total_cant, r3_total_acum)        # return prom

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()