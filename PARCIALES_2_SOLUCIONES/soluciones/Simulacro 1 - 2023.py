

# r3
def validar_consonantes(i):
    return i.lower() in "bcdfghjklmnpqrstvwxyz"


# r4
def validar_vocales(i):
    if i.lower() in "aeiou":
        return True
    else:
        return False


# r1
def validar_minusculas(i):
    if "a" <= i <= "z":
        return True
    else:
        return False


def validar_digitos_impares(i):
    if i in "13579":
        return True
    else:
        return False


def principal():

    fd = "entrada.txt"
    m = open(fd, "rt")
    linea = m.readline()

    ''' 1 - Determinar la cantidad de palabras comienzan con un dígito impar, pero tales que el resto de sus
caracteres son letras en minúsculas 

# la logica es que despues del primer caracter yo voy a afirmar que son todas letras minusculas hasta que
demuestre lo contario, o sea cuando no me toque una minuscula voy a apagar la bandera, es decir para que 
cumpla la condicion al final cuando salgo de la palabra la bandera se tuvo que haber mantenido prendida.
'''
    r1 = 0  # hace referencia a la respuesta
    r1_cont_caracteres = 0
    r1_empieza_digito_impar = False
    r1_todas_minusculas = True

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más larga entre aquellas que
comienzan con una vocal y contenga al menos una letra "b" (mayúscula o minúscula) '''
    r2 = None
    r2_cont_caracteres = 0
    r2_comienza_vocal = False
    r2_tiene_b = False

    ''' 3 - Determinar el promedio entero de caracteres por palabra entre las palabras que tienen más
consonantes que vocales, pero no contienen ninguna "m" ni tampoco ninguna "a".'''
    r3 = 0  # hace referencia a la respuesta
    r3_acum_total = 0
    r3_cont_total = 0
    r3_cont_caracteres = 0
    r3_cont_cons = 0
    r3_cont_vocal = 0
    r3_tiene_m_a = False

    ''' 4 - Determinar cuántas palabras incluyen dos o más veces la expresión que conforman la letra "d"
mas una vocal (con cualquiera de sus letras en minúscula o mayúscula) pero de tal forma que la
palabra termine además con una vocal. '''
    r4 = 0      # hace referencia a la respuesta
    r4_tiene_d = False
    r4_tiene_d_vocal = False
    r4_cont_d_vocal = 0
    r4_ultima_letra = ""

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # ===================================================================
            #                       Punto 1
            # ===================================================================
            r1_cont_caracteres += 1

            # recuerden que cuando se cumplia este if, simboliza que era el comienzo de una palabraa
            if r1_cont_caracteres == 1:
                es_dgito_impar_r1 = validar_digitos_impares(i)
                if es_dgito_impar_r1:
                    r1_empieza_digito_impar = True

            # este else hace referencia a cuando no estoy al comienzo de la palabra o sea r1_cont_Caractes != 1
            # lo cual simboliza que se refiere al resto de la palabra
            else:
                es_minuscula_r1 = validar_minusculas(i)
                # es decir si me toco algun caracter que NO fue una minuscula significa que ya no cumple la condicion
                # de ser todas minusuclas o sea apago la bandera
                if not es_minuscula_r1:
                    r1_todas_minusculas = False

            # r2
            r2_cont_caracteres += 1

            if r2_cont_caracteres and validar_vocales(i):
                r2_comienza_vocal = True

            if i.lower() == "b":
                r2_tiene_b = True

            # r3
            r3_cont_caracteres += 1

            if validar_vocales(i):
                r3_cont_vocal += 1

            if validar_consonantes(i):
                r3_cont_cons += 1

            if i.lower() == "m" or i.lower() == "a":
                r3_tiene_m_a = True

            # ===================================================================
            #                       Punto 4
            # ===================================================================
            r4_ultima_letra = i

            es_vocal_r4 = validar_vocales(i)
            if r4_tiene_d and es_vocal_r4:
                r4_tiene_d_vocal = True
            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

            # aca la logica es que cuando esta bandera se ponga en True dentro de la palabra significa
            # que encontr la sigla dentro de la palabra o sea que puedo contar que lo encontre una vez
            # el tema es que debo apagarlo porque sino la proxima vuelta contaria de vuelta una mas, por
            # eso al apagar la bandera paso depender de que prenda de vuelta la bandera para poder sumar al
            # contador_d_vocal
            if r4_tiene_d_vocal:
                r4_cont_d_vocal += 1
                r4_tiene_d_vocal = False

        # Termino una palabra
        else:
            # ===================================================================
            #                       Punto 1
            # ===================================================================
            # si se mantuvo prendida todas minusculas durante la palabra significa que nunca se puso en False
            # o sea cumplio
            if r1_empieza_digito_impar and r1_todas_minusculas:
                r1 += 1

            # r2
            if r2_comienza_vocal and r2_tiene_b:
                if r2 is None or r2_cont_caracteres > r2:
                    r2 = r2_cont_caracteres

            # r3
            if not r3_tiene_m_a and r3_cont_cons > r3_cont_vocal:
                r3_acum_total += r3_cont_caracteres
                r3_cont_total += 1

            # ===================================================================
            #                       Punto 4
            # ===================================================================
            # aca recuerden estuve guardando en memoria la ultima letra para usarlo ahora en el espacio en blanco
            es_vocal_ultima_letra = validar_vocales(r4_ultima_letra)

            # aca corresponde usar el cont de vocales para afirmar que tuve la sigla, ya que el tiene d_vocal lo
            # durante dentro de la palabra y eso causa que siempre quede en False, pero el cont d vocal si sumo
            # significa que yo encontre esa siglaa
            if r4_cont_d_vocal >= 2 and es_vocal_ultima_letra:
                r4 += 1

            # Apagar Banderas / Reiniciar Contadores , etc
            # r1
            r1_cont_caracteres = 0
            r1_empieza_digito_impar = False
            r1_todas_minusculas = True

            # r3
            r3_cont_cons = 0
            r3_cont_vocal = 0
            r3_tiene_m_a = False
            r3_cont_caracteres = 0

            # r4
            r4_tiene_d = False
            r4_tiene_d_vocal = False
            r4_cont_d_vocal = 0
            r4_ultima_letra = ""

    # Fuera del ciclo
    m.close()

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()