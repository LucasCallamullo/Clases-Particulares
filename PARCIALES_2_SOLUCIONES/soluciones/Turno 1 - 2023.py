

# r2
def calcular_promedio(r2_total_acum, r2_total_cant):
    prom = 0
    if r2_total_cant != 0:
        prom = r2_total_acum // r2_total_cant
    return prom


# r1
def validar_vocales(i):
    if i.lower() in "aeiou":
        return True
    else:
        return False


def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    else:
        return False


def principal():

    fd = "entrada.txt"
    fd = "mi_entrada.txt"
    m = open(fd, "rt")
    linea = m.readline()

    ''' 1. Determinar la cantidad de palabras que tienen exactamente seis caracteres de largo e incluyen 
    una o dos vocales (en mayúscula o minúscula) y uno o más dígitos. '''
    r1 = 0      # hace referencia a la respuesta
    r1_cont_caracteres = 0
    r1_cont_vocales = 0
    r1_tiene_digito = False

    ''' 2 - Determinar el promedio entero de caracteres por palabra, de las palabras que tienen solo 
    una vez una 'r' y dos o más veces una 'e' (ambas en minúsculas o mayúsculas). 
        # Promedio = Acum ( acumulador de caracteres ) / cantidad de veces que sume en el acumulador.
    '''
    r2 = 0
    r2_total_acum = 0
    r2_total_cant = 0
    r2_cont_caracteres = 0
    r2_cont_r = 0
    r2_cont_e = 0

    ''' 3 - Determinar cuántas palabras empiezan con una vocal y terminan con una vocal pero distinta de la 
    primera (ambas en minúscula o en mayúscula en forma indistinta) '''
    r3 = 0      # hace referencia a la respuesta
    r3_cont_caracteres = 0
    r3_empieza_vocal = False
    r3_ultima_letra = ""
    r3_primera_letra = ""

    ''' 4 - Determinar cuántas palabras incluyen la expresión "fi" (con cualquiera de sus letras en minúscula 
    o en mayúscula) y también contienen una "n" o una "t". '''
    r4 = 0      # hace referencia a la respuesta
    r4_tiene_f = False
    r4_tiene_fi = False
    r4_tiene_n_t = False



    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":
            # r1
            r1_cont_caracteres += 1

            es_vocal_r1 = validar_vocales(i)
            if es_vocal_r1:
                r1_cont_vocales += 1

            es_digito_r1 = validar_digitos(i)
            if es_digito_r1:
                r1_tiene_digito = True

            # r2
            r2_cont_caracteres += 1

            if i.lower() == "r":
                r2_cont_r += 1

            elif i.lower() == "e":
                r2_cont_e += 1

            # r3
            r3_cont_caracteres += 1
            r3_ultima_letra = i.lower()

            es_vocal_r3 = validar_vocales(i)
            if r3_cont_caracteres == 1 and es_vocal_r3:
                r3_empieza_vocal = True
                r3_primera_letra = i.lower()

            # r4
            if r4_tiene_f and i.lower() == "i":
                r4_tiene_fi = True
            elif i.lower() == "f":
                r4_tiene_f = True
            else:
                r4_tiene_f = False

            if i.lower() in "nt":
                r4_tiene_n_t = True

        # Termino una palabra
        else:
            # r1
            if r1_cont_caracteres == 6 and 1 <= r1_cont_vocales <= 2 and r1_tiene_digito:
                r1 += 1

            # r2
            if r2_cont_r == 1 and r2_cont_e >= 2:
                r2_total_acum += r2_cont_caracteres
                r2_total_cant += 1

            # r3
            es_vocal_ultima_r3 = validar_vocales(r3_ultima_letra)
            if r3_empieza_vocal and r3_primera_letra != r3_ultima_letra and es_vocal_ultima_r3:
                r3 += 1

            # r4
            if r4_tiene_fi and r4_tiene_n_t:
                r4 += 1

            # Apagar Banderas / Reiniciar Contadores , etc
            # r1
            r1_cont_caracteres = 0
            r1_cont_vocales = 0
            r1_tiene_digito = False

            # r2
            r2_cont_caracteres = 0
            r2_cont_r = 0
            r2_cont_e = 0

            # r3
            r3_cont_caracteres = 0
            r3_empieza_vocal = False
            r3_ultima_letra = ""
            r3_primera_letra = ""

            # r4
            r4_tiene_f = False
            r4_tiene_fi = False
            r4_tiene_n_t = False

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