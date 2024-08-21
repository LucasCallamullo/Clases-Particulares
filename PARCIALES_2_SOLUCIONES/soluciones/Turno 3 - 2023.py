
# r1
def validar_minusculas(i):
    if "a" <= i <= "z":
        return True
    else:
        return False


def validar_digitos(i):
    if "0" <= i <= "9":
        return True
    else:
        return False


# r4
def validar_consonantes(i):
    if i in "bcdfghjklmnpqrstvwxyz":
        return True
    else:
        return False


def principal():

    fd = "entrada.txt"
    m = open(fd, "rt")
    linea = m.readline()

    ''' Determinar la cantidad de palabras que tienen un solo dígito y además todo el resto de sus 
    caractres son minúsculas.
    
    # la logica va a ser yo afirmo que son todas minusculas hasta que demuestre lo contrario pero voy a 
    omitir a los digitos porque van a ser parte de otra condicion, la cual va a ser tener 1 digito o menos
    osea voy a hacer una condicion propia para esto
    '''
    r1 = 0  # hace referencia a la respuesta
    r1_cont_digitos = 0
    r1_todas_minusculas = True

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más corta de aquellas que
tienen al menos un dígito.'''
    r2 = None
    r2_cont_caracteres = 0
    r2_tiene_digito = False

    ''' 3 - Determinar cuántas palabras tienen tienen exactamente dos "n" en cualquier lugar (seguidas o no,
mayúsculas o minúsculas) y al menos una "a" (mayúscula o minúscula) pero de forma que esa "a" esté
entre los cuatro primeros caracteres '''
    r3 = 0  # hace referencia a la respuesta
    r3_cont_n = 0
    r3_cont_caracteres = 0
    r3_tiene_a_pos4menos = False

    ''' 4 - Determinar cuántas palabras incluyen la expresión "se" (con cualquiera de sus letras en minúscula o
mayúscula) pero de tal forma que la palabra comience con esa expresión y termine con una consonante
cualquiera (en minúscula o mayúscula) '''

    r4 = 0      # hace referencia a la respuesta
    r4_cont_caracteres = 0
    r4_tiene_s = False
    r4_tiene_se = False
    r4_ult_letra = ""

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # ===================================================================
            #                       Punto 1
            # ===================================================================
            es_digito_r1 = validar_digitos(i)
            if es_digito_r1:
                r1_cont_digitos += 1

            # este else me indica cuando "es_digito_r1" esta en False, o sea cuando no es un digito como dije
            # en la logica no iba a tomar en consideracion a los digitos para analizar si eran todas minusculas
            # el resto de los caracteres de la palabra
            else:
                es_minuscula_r1 = validar_minusculas(i)
                # si no leyera una minuscula digo que ya no son todas minsuculas
                if not es_minuscula_r1:
                    r1_todas_minusculas = False

            # r2
            r2_cont_caracteres += 1
            es_digito_r2 = validar_digitos(i)
            if es_digito_r2:
                r2_tiene_digito = True

            # r3
            r3_cont_caracteres += 1

            if i.lower() == "n":
                r3_cont_n += 1
            if i.lower() == "a" and r3_cont_caracteres <= 4:
                r3_tiene_a_pos4menos = True

            # ===================================================================
            #                       Punto 4
            # ===================================================================
            # para solo hacer que empiece con esta sigla si o si la "s" debe ser el primer caracter
            # y deberiamos agregar esa condicion en el elif
            r4_cont_caracteres += 1

            if r4_tiene_s and i.lower() == "e":
                r4_tiene_se = True
            elif i.lower() == "s" and r4_cont_caracteres == 1:
                r4_tiene_s = True
            else:
                r4_tiene_s = False

            # recuerden que la forma de obtener la ultima letra era esta es decir cada vuelta de ciclo
            # nos guardamos el valor que nos toque como i para despues usarlo cuando termina la palabra
            r4_ult_letra = i

        # Termino una palabra
        else:
            # ===================================================================
            #                       Punto 1
            # ===================================================================
            # si se mantuvo en True todas_minusculas durante la palabra cumple porque la parte de cuantos
            # digitos tuve esta dado por el contador de digitos
            if r1_todas_minusculas and r1_cont_digitos == 1:
                r1 += 1

            # r2
            if r2_tiene_digito:
                if r2 is None or r2_cont_caracteres < r2:
                    r2 = r2_cont_caracteres

            # r3
            if r3_cont_n == 2 and r3_tiene_a_pos4menos:
                r3 += 1

            # ===================================================================
            #                       Punto 4
            # ===================================================================
            # en este caso le mando a que me pregunte si la ultima letra que me guarde previo a entrar en " "
            # es una consonante o no
            es_consonante_r4 = validar_consonantes(r4_ult_letra)
            if es_consonante_r4 and r4_tiene_se:
                r4 += 1

            # Apagar Banderas / Reiniciar Contadores , etc
            # r1
            r1_cont_digitos = 0
            r1_todas_minusculas = True

            # r2
            r2_cont_caracteres = 0
            r2_tiene_digito = False

            # r3
            r3_cont_n = 0
            r3_cont_caracteres = 0
            r3_tiene_a_pos4menos = False

            # r4
            r4_cont_caracteres = 0
            r4_tiene_s = False
            r4_tiene_se = False
            r4_ult_letra = ""

    # Fuera del ciclo
    m.close()

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()