

def validar_mayusculas(car):
    if "A" <= car <= "Z" or car == "Ñ":
        return True
    return False


def calcular_porcentaje(r2_total_palabras, r2_palabras_que_cumplan):
    if r2_total_palabras > 0:
        return r2_palabras_que_cumplan * 100 // r2_total_palabras
    return 0


def validar_consonantes(car):
    # consonantes = "bcdefghjklmnpqrstvwxyz"
    if "a" <= car.lower() <= "z" or car.lower() == "ñ":
        if not car.lower() in "aeiou":          # si no esta en
            return True
    return False


def validar_digitos(car):
    return "0" <= car <= "9"
    #if "0" <= car <= "9":
    #    return True
    #return False


def validar_vocales(car):  # A - > a
    # .lower() es transformar al caracter en una minuscula  / .upper() es transformar al caracter en una mayuscula
    if car.lower() in "aeiou":  # si el car esta in algunas de las siguientes letras "aeiou"
        return True
    else:
        return False
    # return car in "aeiou"



def principal():

    fd = "entrada.txt"          # file descripttion # descripcion del archivo
    m = open(fd, "rt", encoding="utf-8")          # rt , read text, leer texto

    # forma 1
    linea = m.readline()

    ''' 1 - Determinar la cantidad de palabras que empiezan con una vocal (mayúscula o minúscula) e
incluyen dos o más dígitos. 
    Anexo 1 si termina con vocal '''
    r1 = 0          # a un contador de la cantidad de palabras que cumplan las condiciones
    r1_indice = 0
    r1_empieza_vocal = False
    r1_cont_digitos = 0
    r1_anexo_ult_letra = None

    # para evitar dos espacios seguidos
    es_palabra = False
    cont_palabras = 0

    ''' 2 - Determinar el porcentaje entero de palabras (con respecto al total de palabras del texto), de las
palabras que tienen al menos dos consonantes seguidas 
    porc = 
    total_palabras --- 100%
    palabras_cumplen ---- X = palabras_cumplen * 100 / total_palabras
'''
    # ds sd ss dd
    r2 = 0      # respuesta de r2 o sea el porcentaje
    r2_total_palabras = 0
    r2_palabras_que_cumplan = 0
    r2_tiene_consonante = False
    r2_tiene_dos_consonantes = False

    ''' 3 - Determinar cuántas palabras tienen más de dos caracteres pero menos de siete, y presentan una
vocal en la posición 3, una consonante en la posición 5 y una mayúscula cualquiera en la posición
6. '''
    #     4     5
    # 12340123450
    # Hola Mundo.
    r3 = 0              # a un contador de la cantidad de palabras que cumplan las condiciones
    r3_cont_caracteres = 0
    r3_vocal_pos3 = False
    r3_cons_pos5 = False
    r3_mayus_pos6 = False


    ''' 4 - Determinar cuántas palabras incluyen la expresión “so” (con cualquiera de sus letras en minúscula
o mayúscula) pero de tal forma que antes de esa expresión haya aparecido una ‘p’ en cualquier
lugar '''
    r4 = 0         # a un contador de la cantidad de palabras que cumplan las condiciones
    r4_tiene_s = False
    r4_tiene_so = False
    r4_tiene_p = False


    for car in linea:

        # esta dentro de una palabra
        if car != " " and car != ".":

            # r1
            r1_indice += 1
            es_vocal_r1 = validar_vocales(car)
            if r1_indice == 1 and es_vocal_r1:
                r1_empieza_vocal = True

            es_digito_r1 = validar_digitos(car)     # return True si es un digito, que retorne False si no lo es
            if es_digito_r1:
                r1_cont_digitos += 1

            # r1 anexo
            r1_anexo_ult_letra = car

            # para evitar dos espacios seguidos
            es_palabra = True

            # r2
            es_consonante = validar_consonantes(car)
            if r2_tiene_consonante and es_consonante:
                r2_tiene_dos_consonantes = True
            elif es_consonante:
                r2_tiene_consonante = True
            else:
                r2_tiene_consonante = False

            # r3
            r3_cont_caracteres += 1
            es_vocal_r3 = validar_vocales(car)
            es_cons_r3 = validar_consonantes(car)
            es_mayus_r3 = validar_mayusculas(car)

            if es_vocal_r3 and r3_cont_caracteres == 3:
                r3_vocal_pos3 = True

            if es_cons_r3 and r3_cont_caracteres == 5:
                r3_cons_pos5 = True

            if es_mayus_r3 and r3_cont_caracteres == 6:
                r3_mayus_pos6 = True

            # r4
            if r4_tiene_s and car.lower() == "o":
                r4_tiene_so = True
            elif car.lower() == "s":
                r4_tiene_s = True
            else:
                r4_tiene_s = False

            if car.lower() == "p" and not r4_tiene_so:          # r4_tiene_so = false
                r4_tiene_p = True

        # termino una palabra
        else:
            if es_palabra:
                cont_palabras += 1

                # r1
                if r1_empieza_vocal and r1_cont_digitos >= 2:
                    r1 += 1

                # r1 anexo
                es_vocal_r1_anexo = validar_vocales(r1_anexo_ult_letra)
                if es_vocal_r1_anexo:
                    pass

                # r2
                r2_total_palabras += 1
                if not r2_tiene_dos_consonantes:
                    r2_palabras_que_cumplan += 1

                # r3
                if r3_vocal_pos3 and r3_cons_pos5 and r3_mayus_pos6:
                    r3 += 1

                # r4
                if r4_tiene_so and r4_tiene_p:
                    r4 += 1


            # Apagar banderas, reiniciar contadores etc
            # r1
            r1_indice = 0
            r1_empieza_vocal = False
            r1_cont_digitos = 0
            r1_anexo_ult_letra = None

            es_palabra = False

            # r2
            r2_tiene_consonante = False
            r2_tiene_dos_consonantes = False

            # r3
            r3_cont_caracteres = 0
            r3_vocal_pos3 = False
            r3_cons_pos5 = False
            r3_mayus_pos6 = False

            # r4
            r4_tiene_s = False
            r4_tiene_so = False
            r4_tiene_p = False


    # significa que sali del ciclo for
    m.close()

    r2 = calcular_porcentaje(r2_total_palabras, r2_palabras_que_cumplan)

    print("Resultados 1:", r1)
    print("Resultados 2:", r2)
    print("Resultados 3:", r3)
    print("Resultados 4:", r4)

    print("Cantidad de palabras:", cont_palabras)






if __name__ == '__main__':
    principal()


    # forma 2
    # for linea in m:
    #    for car in linea:
    #        pass
