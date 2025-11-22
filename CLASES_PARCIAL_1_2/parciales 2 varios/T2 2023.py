




def validar_digitos(i):
    if i in "0123456789":
        return True
    else:
        return False

def validar_consonantes(i):
    if i.lower() in "bcdfghjklmnñpqrstvwxyz":
        return True
    else:
        return False


def principal():
    m = open("entrada.txt", "r")
    linea = m.readline()
    m.close()

    # 1. Determinar la cantidad de palabras que tienen un dígito en la segunda o en la tercera posición y además
    # incluyen dos o más consonantes pero a partir de la cuarta posición, incluida la cuarta (en minúscula o
    # mayúscula). Por ejemplo, en el texto: "Ax1efDa es una password aceptable pero 12r3aei no lo es."
    # Respuesta: hay solo una palabra que cumple: "Ax1efDa". La palabra "123aei" tiene los dígitos pedidos pero
    # no tiene ninguna consonante a partir de la cuarta posición, por lo que no cuenta.
    r1 = 0
    indice = 0
    tiene_digito23 = False
    tiene_consonante4 = 0


    # 2. Determinar el porcentaje entero de palabras (con respecto al total de palabras del texto), de las palabras
    # que tienen al menos una vocal (en minúscula o mayúscula) y finalizan con un dígito. Por ejemplo, en el
    # texto: "Con los procesos pr1ae8 y gri78x9 no era posible pero lo es a partir del trA2j." hay dos palabras que
    # cumplen el criterio: "pr1ae8" y "gri78x9". Como hay 16 palabras en total, el porcentaje entero pedido es
    # del 12 por ciento (aclaración: en el cálculo del porcentaje haga primero la multiplicación y luego la
    # división)



    for i in linea:

        if i != " " and i != ".":
            indice += 1

            posee_dig = validar_digitos(i)
            tiene_cons = validar_consonantes(i)

            if posee_dig and (indice == 2 or indice == 3):
               tiene_digito23 = True
            if tiene_cons and indice >= 4:
               tiene_consonante4 += 1






        else:

            if tiene_digito23 and tiene_consonante4 >= 2:
                r1 += 1

            #Apagar banderas
            indice = 0
            tiene_digito23 = False
            tiene_consonante4 = 0

    print("Primer resultado:", r1)
    #print("Segundo resultado:", r2)
    #print("Tercer resultado:", r3)
    #print("Cuarto resultado:", r4)


if __name__ == "__main__":
    principal()





