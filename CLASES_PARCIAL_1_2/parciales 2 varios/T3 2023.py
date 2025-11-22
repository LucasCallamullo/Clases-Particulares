




def validar_digitos(i):
    if i in "0123456789":
        return True
    else:
        return False


def principal():
    m = open("entrada.txt", "r")
    linea = m.readline()

    # 1. Determinar la cantidad de palabras que tienen unn solo dígito y además todo el resto de sus caractres
    # son minúsculas. Por ejemplo, en el texto: "El Aer11T2 e2s un cod3igo de in3gre2so CASI i2gual a Aer12T2."
    # hay tres palabras que cumplen: "e2s", "cód3igo" e "i2gual". Las demás no cuentan porque tienen cero o
    # más de un dígito o tienen alguna mayúscula.
    r1 = 0
    cant_digito = 0
    caracteres_min = True

    # 2. Determinar la longitud (en cantidad de caracteres) de la palabra más corta de aquellas que tienen al
    # menos un dígito. Por ejemplo, en el texto: "La salida23 aparece marcada en el item92 y en el cuadrante4."
    # Hay tres palabras con al menos un dígito ("salida23", "item92" y "cuadrante4") y la menor longitud de
    # entre esas tres, es de 6 caracteres (en la palabra "item92").

    for i in linea:
        if i != " " and i != ".":

            un_digito = validar_digitos(i)

            if un_digito:
                cant_digito += 1

            if i in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
                caracteres_min = False












        else:
            if un_digito == 1:
                r1 += 1

            if caracteres_min:
                r1 += 1




            #Apagar
            caracteres_min = True
            cant_digito = 0



    print("Primer resultado:", r1)
    #print("Segundo resultado:", r2)
    #print("Tercer resultado:", r3)
    #print("Cuarto resultado:", r4)

    # 3. Determinar cuántas palabras tienen tienen exactamente dos "n" en cualquier lugar (seguidas o no,
    # mayúsculas o minúsculas) y al menos una "a" (mayúscula o minúscula) pero de forma que esa "a" esté
    # entre los cuatro primeros caracteres. Por ejemplo, en el texto "La constante None es antagonista de Null."
    # Hay una palabra que cumple: "antagonista". Las palabras "constante" y "None" no cuentan porque no
    # tienen una "a" entre los primeros cuatro caracteres (aunque cumplen con tener exactamente dos "n").

    # 4. Determinar cuántas palabras incluyen la expresión "se" (con cualquiera de sus letras en minúscula o
    # mayúscula) pero de tal forma que la palabra comience con esa expresión y termine con una consonante
    # cualquiera (en minúscula o mayúscula). Por ejemplo, en el texto: "Sepan que a los semestres los sienten
    # seguros." Hay tres palabras que cumplen: "Sepan", "semestres" y "seguros". La palabra "sienten"
    # obviamente no cuenta porque no empieza con "se".

if __name__ == "__main__":
    principal()