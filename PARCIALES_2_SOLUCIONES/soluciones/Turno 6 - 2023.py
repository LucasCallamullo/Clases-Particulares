

# r1
def validar_consonantes(i):
    if i.lower() in "bcdfghjklmnpqrstvwxyz":
        return True
    return False


# r3
def calcular_promedio(r3_total_acum, r3_total_cont):
    prom = 0
    if r3_total_cont != 0:
        prom = r3_total_acum // r3_total_cont
    return prom


def validar_digitos(i):
    return "0" <= i <= "9"


# r4
def validar_vocales(i):
    if i.lower() in "aeiou":
        return True
    return False


def principal():

    fd = "entrada.txt"
    m = open(fd, "rt")
    linea = m.readline()

    ''' 1 - Determinar la cantidad de palabras cuya longitud sea impar, y que tengan solo una consonante
(minúscula o mayúscula) '''
    r1 = 0  # hace referencia a la respuesta
    r1_cont_caracteres = 0
    r1_cont_consonantes = 0

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más corta entre aquellas que
tienen una vocal (mayúscula o minúscula) en la segunda posición y no tienen ninguna "n"
(minúscula o mayúscula) en ninguna parte '''
    r2 = None
    r2_cont_caracteres = 0
    r2_tiene_vocal_pos2 = False
    r2_tiene_n = False

    ''' 3 - Determinar el promedio entero de caracteres por palabra entre las palabras que tienen una "g"
(minúscula o mayúscula) en la segunda posición y no tienen ningún dígito.'''
    r3 = 0  # hace referencia a la respuesta
    r3_total_acum = 0
    r3_total_cont = 0
    r3_cont_caracteres = 0
    r3_tiene_g_pos2 = False
    r3_tiene_digito = False

    ''' 4 - Determinar cuántas palabras incluyen la expresión "pe" (con cualquiera de sus letras en
minúscula o mayúscula) pero de tal forma que la palabra además no comience con una vocal
(mayúscula o minúscula). '''
    r4 = 0      # hace referencia a la respuesta
    r4_tiene_p = False
    r4_tiene_pe = False
    r4_cont_caracteres = 0
    r4_comienza_vocal = 0

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # r1
            r1_cont_caracteres += 1
            es_consonante_r1 = validar_consonantes(i)
            if es_consonante_r1:
                r1_cont_consonantes += 1

            # r2
            r2_cont_caracteres += 1

            es_vocal_r2 = validar_vocales(i)
            if es_vocal_r2:
                r2_tiene_vocal_pos2 = True

            if i.lower() == "n":
                r2_tiene_n = True

            # r3
            r3_cont_caracteres += 1

            if i.lower() == "g" and r3_cont_caracteres == 2:
                r3_tiene_g_pos2 = True

            es_digito_r3 = validar_digitos(i)
            if es_digito_r3:
                r3_tiene_digito = True

            # r4
            if r4_tiene_p and i.lower() == "e":
                r4_tiene_pe = True
            elif i.lower() == "p":
                r4_tiene_p = True
            else:
                r4_tiene_p = False

            r4_cont_caracteres += 1
            es_vocal_r4 = validar_vocales(i)
            if r4_cont_caracteres == 1 and es_vocal_r4:
                r4_comienza_vocal = True

        # Termino una palabra
        else:
            # r1
            if r1_cont_consonantes == 1 and r1_cont_caracteres % 2 != 0:
                r1 += 1

            # r2
            if not r2_tiene_n and r2_tiene_vocal_pos2:
                if r2 is None or r2_cont_caracteres < r2:
                    r2 = r2_cont_caracteres

            # r3
            if not r3_tiene_digito and r3_tiene_g_pos2:
                r3_total_acum += r3_cont_caracteres
                r3_total_cont += 1

            if r4_tiene_pe and not r4_comienza_vocal:
                r4 += 1

            # Apagar Banderas / Reiniciar Contadores , etc
            # r1
            r1_cont_caracteres = 0
            r1_cont_consonantes = 0

            # r2
            r2_cont_caracteres = 0
            r2_tiene_vocal_pos2 = False
            r2_tiene_n = False

            # r3
            r3_cont_caracteres = 0
            r3_tiene_g_pos2 = False
            r3_tiene_digito = False

            # r4
            r4_tiene_p = False
            r4_tiene_pe = False
            r4_cont_caracteres = 0
            r4_comienza_vocal = 0

    # Fuera del ciclo
    m.close()

    r3 = calcular_promedio(r3_total_acum, r3_total_cont)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()