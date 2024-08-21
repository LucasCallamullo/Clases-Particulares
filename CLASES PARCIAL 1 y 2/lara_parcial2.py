

# r2
def validar_vocales_sin_u(i):
    return i.lower() in "aeio"


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
def validar_vocales(i):
    if i.lower() in "aeiou":
        return True
    return False


def principal():

    fd = "entrada.txt"
    m = open(fd, "rt")
    linea = m.readline()

    ''' 1 - Determinar la cantidad de palabras que tienen un dígito en la segunda y en la 
cuarta posición, pero de tal forma que el resto de sus caracteres son letras mayúsculas. '''
    r1 = 0      # hace referencia a la respuesta
    r1_cont_caracteres = 0
    r1_tiene_digitos_pos2_pos4 = True
    r1_todas_mayusculas = True

    ''' 2 - Determinar cuántas palabras están conformadas solo por vocales 
(minúsculas o mayúsculas), pero no contienen ninguna "u" (minúscula o mayúscula) '''
    r2 = 0
    r2_todas_vocales = True

    #       123456789  1234567 palabrass
    ''' 3 - Determinar cuántas palabras empiezan con una vocal y terminan con una vocal 
pero distinta de la primera (ambas en minúscula o en mayúscula en forma indistinta). '''
    r3 = 0      # hace referencia a la respuesta
    r3_cont_caracteres = 0
    r3_empieza_vocal = False
    r3_ultima_letra = ""
    r3_primera_letra = ""

    ''' 4 - Determinar cuántas palabras incluyen la expresión "di" (con cualquiera de 
sus letras en minúscula o mayúscula) pero de tal forma que a su vez no comiencen con 
la expresión "di". '''
    r4 = 0      # hace referencia a la respuesta
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
                es_digito_r1 = validar_digitos(i)
                if not es_digito_r1:    # si "es_digitop" esta en false
                    r1_tiene_digitos_pos2_pos4 = False

            else:
                es_mayus_r1 = validar_mayusculas(i)
                if not es_mayus_r1:     # si "es_mayus_r1" esta en false
                    r1_todas_mayusculas = False

            # r2
            es_vocal_sin_u = validar_vocales_sin_u(i)
            if not es_vocal_sin_u:
                r2_todas_vocales = False

            # r3
            r3_cont_caracteres += 1
            es_vocal = validar_vocales(i)   # return True si es vocal, false si no lo es
            if r3_cont_caracteres == 1 and es_vocal:
                r3_empieza_vocal = True
                r3_primera_letra = i.lower()

            r3_ultima_letra = i.lower()

            # r4
            r4_cont_caracteres += 1

            if r4_tiene_d and i.lower() == "i":
                r4_tiene_di = True

                if r4_cont_caracteres == 2:
                    r4_empieza_di = True

                ''' por si queres detectar si termino con la sigla '''
                ultima_pos = r4_cont_caracteres

            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

            ''' aparecio una "t" antes de la sigla'''
            if i.lower() == "t" and not r4_tiene_di:
                pass
            ''' aparecio una "t" despues de la sigla'''
            if i.lower() == "t" and r4_tiene_di:
                pass

        # Termino una palabra
        else:

            # r1
            if r1_todas_mayusculas and r1_tiene_digitos_pos2_pos4 and r4_cont_caracteres >= 4:
                r1 += 1

            # r2
            if r2_todas_vocales:
                r2 += 1

            # r3
            es_vocal_ultima = validar_vocales(r3_ultima_letra)
            if r3_empieza_vocal and es_vocal_ultima and r3_ultima_letra != r3_primera_letra:
                r3 += 1

            # r4
            if r4_tiene_di and not r4_empieza_di:
                r4 += 1

            # Apagar Banderas / Reiniciar Contadores , etc
            # r1
            r1_cont_caracteres = 0
            r1_tiene_digitos_pos2_pos4 = True
            r1_todas_mayusculas = True

            # r2
            r2_todas_vocales = True

            # r3
            r3_cont_caracteres = 0
            r3_empieza_vocal = False
            r3_ultima_letra = ""
            r3_primera_letra = ""

            # r4
            r4_tiene_d = False
            r4_tiene_di = False
            r4_cont_caracteres = 0
            r4_empieza_di = False

    # Fuera del ciclo
    m.close()

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()
