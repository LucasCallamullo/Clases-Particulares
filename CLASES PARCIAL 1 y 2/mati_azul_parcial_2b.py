

# r1
def validar_mayusculas(i):
    if "A" <= i <= "Z":
        return True
    return False


def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    return False


# r2
def calcular_promedio(r2_total_acum, r2_total_cant):
    prom = 0
    if r2_total_cant != 0:
        prom = r2_total_acum // r2_total_cant
    return prom


def validar_vocales(i):
    if i.lower() in "aeiou":
        return True
    return False


def principal():

    fd = "entrada.txt"
    m = open(fd, "rt")
    linea = m.readline()

    ''' 1 - Determinar la cantidad de palabras que tienen un dígito en la segunda y en la cuarta
posición, pero de tal forma que el resto de sus caracteres son letras mayúsculas '''
    r1 = 0      # hace referencia a la respuesta
    r1_cont_caracteres = 0
    r1_tiene_digito_pos2_pos4 = True
    r1_todas_mayusculas = True

    ''' 2 - Determinar el promedio entero de caracteres por palabra, de las palabras que tienen 
    solo una vez una 'r' y dos o más veces una 'e' (ambas en minúsculas o mayúsculas).
        # Promedio = Acumulado de cosas / Cantidad de cosas que acumulamos
        prom = acum_total // cont_total
    '''
    r2 = 0
    r2_total_acum = 0
    r2_total_cant = 0
    r2_cont_caracteres = 0
    r2_cont_r = 0
    r2_cont_e = 0

    ''' 3 - Determinar cuántas palabras empiezan con una vocal y terminan con una vocal pero
    distinta de la primera (ambas en minúscula o en mayúscula en forma indistinta). '''
    r3 = 0  # hace referencia a la respuesta
    r3_cont_caracteres = 0
    r3_empieza_vocal = False
    r3_primera_letra = ""
    r3_ultima_letra = ""

    ''' 4 - Determinar cuántas palabras incluyen la expresión "di" (con cualquiera de sus 
letras en minúscula o mayúscula) pero de tal forma que a su vez no comiencen con la expresión "di". '''
    r4 = 0                  # hace referencia a la respuesta
    r4_tiene_d = False
    r4_tiene_di = False
    r4_cont_caracteres = 0
    r4_empieza_di = False

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # r1
            r1_cont_caracteres += 1

            if r1_cont_caracteres == 2 or r1_cont_caracteres == 4:
                es_digito_r1 = validar_digitos(i)       # return True si es digito , False si no lo es
                if not es_digito_r1:        # si "es_digito_r1" esta en False
                    r1_tiene_digito_pos2_pos4 = False
            else:
                es_mayuscula_r1 = validar_mayusculas(i)
                if not es_mayuscula_r1:
                    r1_todas_mayusculas = False

            # r2
            r2_cont_caracteres += 1
            if i.lower() == "r":
                r2_cont_r += 1
            if i.lower() == "e":
                r2_cont_e += 1

            # r3
            r3_cont_caracteres += 1
            es_vocal = validar_vocales(i)
            if r3_cont_caracteres == 1 and es_vocal:
                r3_empieza_vocal = True
                r3_primera_letra = i.lower()

            r3_ultima_letra = i.lower()

            # r4
            r4_cont_caracteres += 1

            if r4_tiene_d and i.lower() == "i":
                r4_tiene_di = True

                if r2_cont_caracteres == 2:
                    r4_empieza_di = True

            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

            ''' si tiene "t" antes de la sigla '''
            if i.lower() == "t" and not r4_tiene_di:
                pass

            ''' si tiene "t" despues de la sigla '''
            if i.lower() == "t" and r4_tiene_di:
                pass

            ''' dos o mas veces la sigla '''
            if r4_tiene_di:
                # r4_cont_di += 1
                # r4_tiene_di = False
                pass

        # Termino una palabra
        else:
            # r1
            if r1_tiene_digito_pos2_pos4 and r1_todas_mayusculas:
                r1 += 1

            # r2
            if r2_cont_e >= 2 and r2_cont_r == 1:
                r2_total_acum += r2_cont_caracteres
                r2_total_cant += 1

            # r3
            es_vocal_ultima = validar_vocales(r3_ultima_letra)
            if r3_empieza_vocal and es_vocal_ultima and r3_ultima_letra != r3_primera_letra:
                r3 += 1

            # r4
            if r4_tiene_di and not r4_empieza_di:
                r4 += 1
            # if r4_cont_di >= 2 and not r4_empieza_di:

            # Apagar Banderas / Reiniciar Contadores , etc
            # r1
            r1_cont_caracteres = 0
            r1_tiene_digito_pos2_pos4 = True
            r1_todas_mayusculas = True

            # r2
            r2_cont_caracteres = 0
            r2_cont_r = 0
            r2_cont_e = 0

            # r3
            r3_cont_caracteres = 0
            r3_empieza_vocal = False
            r3_primera_letra = ""
            r3_ultima_letra = ""

            # r4
            r4_tiene_d = False
            r4_tiene_di = False
            r4_cont_caracteres = 0
            r4_empieza_di = False

    # Fuera del ciclo
    m.close()

    # r2
    r2 = calcular_promedio(r2_total_acum, r2_total_cant)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()