
# r3
def validar_vocales_sin_u(i):
    return i.lower() in "aeio"


# r1
def validar_mayusculas(i):
    if "A" <= i <= "Z":
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
    m = open(fd, "rt")
    linea = m.readline()

    ''' 1 - Determinar la cantidad de palabras que tienen un dígito en la segunda y en la cuarta posición, 
pero de tal forma que el resto de sus caracteres son letras mayúsculas.

    # la logica va a ser que voy a afirmar que son todas mayusculas hasta que demuestre lo contrario
    aunque obvio tenemos que omitir cuando el contador valga 2 y 4 porque tienen que ser digitos en esas 
    posiciones a su vez necesitamos un cont, para contar que efectivamente tuvimos los dos digitos de
    esas posiciones
'''
    r1 = 0  # hace referencia a la respuesta
    r1_cont_caracteres = 0
    r1_cont_cumple_digitos = 0
    r1_todas_mayus = True

    ''' 2 - Determinar la longitud (en cantidad de caracteres) de la palabra más corta entre aquellas que comienzan
con una "t" (minúscula o mayúscula). '''
    r2 = None
    r2_cont_caracteres = 0
    r2_comienza_t = False

    ''' 3 - Determinar cuántas palabras están conformadas solo por vocales (minúsculas o mayúsculas), pero no
contienen ninguna "u" (minúscula o mayúscula). '''
    r3 = 0  # hace referencia a la respuesta
    r3_todas_vocales = True

    ''' 4 - Determinar cuántas palabras incluyen la expresión "di" (con cualquiera de sus letras en 
minúscula o mayúscula) pero de tal forma que a su vez no comiencen con la expresión "di". '''
    r4 = 0      # hace referencia a la respuesta
    r4_cont_caracteres = 0
    r4_tiene_d = False
    r4_tiene_di = False

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":

            # ===================================================================
            #                       Punto 1
            # ===================================================================
            r1_cont_caracteres += 1

            # esto lo declare de esta forma para que cumpla la condicion de ser 2 o 4 pos
            if r1_cont_caracteres == 2 or r1_cont_caracteres == 4:
                es_digito_r1 = validar_digitos(i)
                if es_digito_r1:
                    r1_cont_cumple_digitos += 1

            # este else toma la condicion de cuando el r1_contcaracteres sea distinto de 2 y 4
            else:
                # si me tocara algo que no fuera una mayuscula o sea cuando es_mayuscula me devuelva un
                # False quiero que mi bandera que dice que son todas mayus se apague
                es_mayuscula_r1 = validar_mayusculas(i)
                if not es_mayuscula_r1:
                    r1_todas_mayus = False

            # r2
            r2_cont_caracteres += 1
            if i.lower() == "t" and r2_cont_caracteres == 1:
                r2_comienza_t = True

            # r3
            es_vocal_r3 = validar_vocales_sin_u(i)
            if not es_vocal_r3:
                r3_todas_vocales = False

            # ===================================================================
            #                       Punto 4
            # ===================================================================
            # la logica para que no comience con la sigla es que simplemente la d no puede ser la primera letra
            r4_cont_caracteres += 1

            if r4_tiene_d and i.lower() == "i":
                r4_tiene_di = True
            elif i.lower() == "d":
                r4_tiene_d = True
            else:
                r4_tiene_d = False

        # Termino una palabra
        else:
            # ===================================================================
            #                       Punto 1
            # ===================================================================
            # se supone que cumplimos lo de los digitos si efectivamente fueron 2
            # y si la bandera todas_mayus se mantuvo en True significa que fueron todas mayus
            if r1_cont_cumple_digitos == 2 and r1_todas_mayus:
                r1 += 1

            # r2
            if r2_comienza_t:
                if r2 is None or r2_cont_caracteres < r2:
                    r2 = r2_cont_caracteres

            # r3
            if r3_todas_vocales:
                r3 += 1

            # r4
            if r4_tiene_di:
                r4 += 1

            # Apagar Banderas / Reiniciar Contadores , etc
            # r1
            r1_cont_caracteres = 0
            r1_cont_cumple_digitos = 0
            r1_todas_mayus = True

            # r2
            r2_cont_caracteres = 0
            r2_comienza_t = False

            # r3
            r3_todas_vocales = True

            # r4
            r4_cont_caracteres = 0
            r4_tiene_d = False
            r4_tiene_di = False

    # Fuera del ciclo
    m.close()

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()