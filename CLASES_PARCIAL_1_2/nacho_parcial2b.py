
def calcular_promedio(r5_acum_total, r5_cant_total):
    prom = 0
    if r5_cant_total != 0:
        prom = r5_acum_total // r5_cant_total
    return prom


def validar_mayusculas(i):
    if "A" <= i <= "Z":
        return True
    return False


def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    return False



def validar_vocales(i):
    # return i.lower() in "aeiou"
    if i.lower() in "aeiou":
        return True
    return False


def principal():

    fd = "entrada.txt"
    m = open(fd, "rt")
    linea = m.readline()

    r1 = 0  # hace referencia a la respuesta

    ''' 2 -
    Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que
    comienzan con una vocal y contenga al menos una letra "b" (mayúscula o minúscula). 
    '''
    r2 = None
    r2_cont_caracteres = 0
    r2_empieza_vocal = False
    r2_tiene_b = False


    r3 = 0  # hace referencia a la respuesta

    ''' 4 -         
    da de di do du              incluyenn
    Determinar cuántas palabras incluyen dos o más veces la expresión que conforman la letra "d"
mas una vocal (con cualquiera de sus letras en minúscula o mayúscula) pero de tal forma que la
palabra termine además con una vocal. '''
    r4 = 0      # hace referencia a la respuesta
    r4_tiene_d = False
    r4_tiene_d_vocal = False
    r4_cont_d_vocal = 0
    r4_ultima_letra = ""

    ''' 5 -       12345678
    Determinar el promedio de caracteres de las palabras que tienen un dígito en la segunda y en la 
cuarta posición, pero de tal forma que el resto de sus caracteres son letras mayúsculas 
    # promedio = una suma de cosas / la cantidad de cosas que suamamos
'''
    r5 = 0
    r5_acum_total = 0
    r5_cant_total = 0
    r5_cont_caracteres = 0
    r5_tiene_digitos = True
    r5_tiene_mayusculas = True

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # r1

            # r2
            r2_cont_caracteres += 1

            es_vocal = validar_vocales(i)
            if r2_cont_caracteres == 1 and es_vocal:
                r2_empieza_vocal = True

            if i.lower() == "b":
                r2_tiene_b = True

            # r4
            es_vocal_r4 = validar_vocales(i)
            if r4_tiene_d and es_vocal_r4:
                r4_tiene_d_vocal = True
            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

            if r4_tiene_d_vocal:
                r4_cont_d_vocal += 1
                r4_tiene_d_vocal = False

            r4_ultima_letra = i

            # r5
            r5_cont_caracteres += 1

            if r5_cont_caracteres == 2 or r5_cont_caracteres == 4:
                es_digito = validar_digitos(i)
                if not es_digito:
                    r5_tiene_digitos = False

            else:
                es_mayuscula = validar_mayusculas(i)
                if not es_mayuscula:
                    r5_tiene_mayusculas = False

        # Termino una palabra
        else:

            # r2
            if r2_empieza_vocal and r2_tiene_b:
                if r2 is None or r2_cont_caracteres > r2:
                    r2 = r2_cont_caracteres

            # r4
            es_vocal_ult = validar_vocales(r4_ultima_letra)
            if r4_cont_d_vocal >= 2 and es_vocal_ult:
                r4 += 1

            # r5
            if r5_tiene_mayusculas and r5_tiene_digitos:
                r5_acum_total += r5_cont_caracteres
                r5_cant_total += 1

            # Apagar Banderas / Reiniciar Contadores , etc
            # r2
            r2_cont_caracteres = 0
            r2_empieza_vocal = False
            r2_tiene_b = False

            # r4
            r4_tiene_d = False
            r4_tiene_d_vocal = False
            r4_cont_d_vocal = 0
            r4_ultima_letra = ""

            # r5
            r5_cont_caracteres = 0
            r5_tiene_digitos = True
            r5_tiene_mayusculas = True

    # Fuera del ciclo
    m.close()

    r5 = calcular_promedio(r5_acum_total, r5_cant_total)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)
    print("Quinto resultado:", r5)


if __name__ == '__main__':
    principal()