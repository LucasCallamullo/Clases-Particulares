

# r1
def es_digito(caracter):    # 5
    if caracter in "0123456789":
        return True
    return False


# r2
def es_mayuscula(caracter):
    if caracter in "QWRTYPSDFGHJKLÑZXCVBNMAEIOU":
        return True
    return False


# r3
def es_vocal_sin_u(caracter):
    if caracter.lower() in "aeio":
        return True
    return False


def principal():

    m = open('archivo.txt', 'r')

    linea = m.readline()        # obtiene la primera linea de texto

    # indice = 123401
    # linea = "Hola Mundo."
    m.close()

    """
    1 - Determinar la cantidad de palabras que tienen un dígito en la segunda y en la cuarta 
    posición, pero de tal forma que el resto de sus caracteres son letras mayúsculas. 
    Por ejemplo, en el texto: "La pieza D3A5CED reemplaza a la a4j5TY pero no a la 234DFR." 
    hay solo una palabra que cumple: "D3A5CED". El resto de las palabras no tienen los dígitos 
    pedidos o tienen alguna minúscula.
    """
    r1 = 0      # contador

    r1_indice = 0
    r1_cont_digitos_pos2_pos4 = 0
    r1_todas_mayusculas = True

    """ 
    #  1234567890
    2. Determina la longitud (en cantidad de caracteres) de la palabra más corta entre aquellas
    que comienzan con una "t" (minúscula o mayúscula). Por ejemplo, en el texto: "Tenemos tantos 
    tios que viajan en tren." Hay cuatro palabras que comienzan con "t" (minúscula o mayúscula), 
    y la menor longitud entre esas palabras es de 4 caracteres (en la palabra "tios"). 
    """
    r2 = None       # te pide calcular la menor longitud
    r2_indice = 0
    r2_comienza_t = False

    """ 
    3. Determinar cuántas palabras están conformadas solo por vocales (minúsculas o mayúsculas), 
    pero no contienen ninguna "u" (minúscula o mayúscula). Por ejemplo, en el texto "Ea pues a 
    por ellos ue ai." hay tres palabras que cumplen: "Ea", "a" y "ai". La palabra "ue" no cumple 
    porque tiene una "u" (aunque cumple con estar formada solo por vocales).
    """
    r3 = 0      # contador
    r3_solo_vocales_sin_u = True        # False

    """ 
    4 - Determinar cuántas palabras incluyen la expresión "di" (con cualquiera de sus letras 
    en minúscula o mayúscula) pero de tal forma que a su vez no comiencen con la expresión "di". 
    Por ejemplo, en el texto: "Usted imagina doscientos videos sobre dioses que aplican sadismo 
    por lo que en un didimio los humanos lo dimos y lo perdimos todo." hay dos palabras que 
    cumplen: "sadismo" y "perdimos". Las palabras "dioses" y "dimos" no cuentan porque si bien 
    tienen "di", ambas comienzan con "di". Y note que la palabra "didimio" tampoco cuenta: tiene 
    "di" pero también comienza con "di" y eso la hace inválida.
    
    12
    didimio
    12
    adidas
    
    "DS"
    # si te pidieran dos mayusculas seguidas
    tiene_una_mayus = False
    tiene_dos_mayus = False
    
    mayus = es_mayuscula(caracter)
    
    if mayus is True and tiene_una_mayus is True:
        tiene_dos_mayus = True
        
    elif mayus is True:
        tiene_una_mayus = True
        
    else:
        tiene_una_mayus = False
    """
    r4 = 0

    r4_tiene_d = False
    r4_tiene_di = False

    r4_comienza_di = False
    r4_indice = 0

    """  
     la palabra además no comience con una vocal 
    """
    indice = 0  # --> vaya sumando cada vez que toque un caracter
    comienza_vocal = False


    for caracter in linea:
        # caracter = "H", "o", ..., "."

        # Estoy dentro de una palabra
        if caracter != " " and caracter != ".":

            # r1
            r1_indice += 1

            if r1_indice == 2 or r1_indice == 4:
                digito = es_digito(caracter)    # True o False
                if digito is True:  # if digito:
                    r1_cont_digitos_pos2_pos4 += 1

            else:       # if r1_indice != 2 and r1_indice != 4:
                mayus = es_mayuscula(caracter)      # True o False
                if mayus is False:      # if not mayus:
                    r1_todas_mayusculas = False

            # r2
            r2_indice += 1

            if r2_indice == 1 and caracter.lower() == "t":
                r2_comienza_t = True

            # r3
            vocal_sin_u = es_vocal_sin_u(caracter)
            if vocal_sin_u is False:
                r3_solo_vocales_sin_u = False

            # r4
            r4_indice += 1

            if caracter.lower() == "i" and r4_tiene_d is True:
                r4_tiene_di = True
                if r4_indice == 2:
                    r4_comienza_di = True

            elif caracter.lower() == "d":
                r4_tiene_d = True

            else:
                r4_tiene_d = False


        #
        # Fuera de una palabra
        else:

            # r1
            if r1_cont_digitos_pos2_pos4 == 2 and r1_todas_mayusculas is True:
                r1 += 1

            # r2
            if r2_comienza_t:
                if r2 is None or r2_indice < r2:       # 9
                    r2 = r2_indice      # 5

            # r3
            if r3_solo_vocales_sin_u is True:
                r3 += 1

            # r4
            if r4_tiene_di is True and r4_comienza_di is False:
                r4 += 1

            # Reiniciar contadores / banderas
            # r1
            r1_indice = 0
            r1_cont_digitos_pos2_pos4 = 0
            r1_todas_mayusculas = True

            # r2
            r2_indice = 0
            r2_comienza_t = False

            # r3
            r3_solo_vocales_sin_u = True

            # r4
            r4_indice = 0
            r4_tiene_d = False
            r4_tiene_di = False
            r4_comienza_di = False

    # resultados
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()

