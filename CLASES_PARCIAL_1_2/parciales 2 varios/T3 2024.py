


def validar_mayusculas(i):
    if i in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
            return True
    else:
        return False
def validar_digitos(i):
    if i in "0123456789":
        return True
    else:
        return False
def principal():
    m = open("entrada.txt", "r")
    linea = m.readline()
    m.close()

    # 1. Determinar la cantidad de palabras que comienzan con mayúscula y tienen un dígito en la cuarta posición.
    # Por ejemplo, en el texto: "El civ6 es mejor que el Civ5 y el FIFA24 es mejor que el PES24." hay dos palabras
    # que cumplen: "Civ5" y "PES24".
    r1 = 0
    indice = 0
    mayuscula = False
    digito_4 = False

    # 2. Determinar la longitud de la palabra más larga entre las que tienen una "p" o una "n". Por ejemplo, en el
    # texto: "Le pasan la pelota al genio." hay tres palabras con "p" o con "n" ("pasan", "pelota" y "genio") y la
    # mayor longitud de entre esas tres (el resultado pedido), es de 6 caracteres (en la palabra "pelota").
    r2 = None
    tienep_n = False

    # 3. Determinar el promedio entero de caracteres por palabra entre las que tienen dos o más veces un dígito
    # en cualquier lugar y además tienen una vocal en cualquier lugar. Por ejemplo, en el texto: "Las rutas A2 y
    # R1513 son las mas transitadas despues de las rutas Ead513 y TAfg814." hay 2 palabras que cumplen: "
    # Ead513" y " TAfg814". Entre las tres suman 13 caracteres, y por lo tanto el promedio entero es 6.

    r3 = 0
    tiene_digito = 0
    tiene_vocal = False
    acum_c = 0
    cont_c = 0

    # 4. Determinar cuántas palabras incluyen la expresión "fa" (con cualquiera de sus letras en minúscula o
    # mayúscula) pero de tal forma que además comiencen con una vocal. Por ejemplo, en el texto: "Las familias
    # afamadas no conocen Antofagasta ni leen a Mafalda pero se afianzan." Hay dos palabras que cumplen:
    # "afamadas", y "Antofagasta".
    r4 = 0
    tiene_f = False
    tiene_fa = False
    r4_tiene_vocal = False




    for i in linea:
        if i != " " and i != ".":
            indice += 1


            #PUNTO 1
            com_mayuscula = validar_mayusculas(i)
            es_digito = validar_digitos(i)

            if com_mayuscula and indice == 1:
                mayuscula = True

            if es_digito and indice == 4:
                digito_4 = True

            #PUNTO 2
            if i == "p" or i == "n":
                tienep_n = True

            #PUNTO 3
            if i in "0123456789":
                tiene_digito += 1

            if i.lower() in "aeiou":
                tiene_vocal = True

            # PUNTO 4

            if i.lower() in "aeiou" and indice == 1:
                r4_tiene_vocal = True

            if tiene_f and i.lower() == "a":
                tiene_fa = True
                tiene_f = False
            elif i.lower() == "f":
                tiene_f = True
            else:
                tiene_f = False


        else:
            #1
            if mayuscula and digito_4:
                r1 += 1
            # 2
            if tienep_n:
                if r2 is None or r2 < indice:
                    r2 = indice

            # 3
            if tiene_vocal and tiene_digito >= 2:
                acum_c += indice
                cont_c += 1

            # 4
            if r4_tiene_vocal and tiene_fa:
                r4 += 1

            #APAGAR
            indice = 0
            mayuscula = False
            digito_4 = False
            tienep_n = False
            #3
            tiene_digito = 0
            tiene_vocal = False
            #4
            tiene_f = False
            tiene_fa = False
            r4_tiene_vocal = False

    prom = 0
    if cont_c > 0:
        prom = acum_c // cont_c

    r3 = prom

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)



if __name__ == "__main__":
    principal()

""" 
  sigla   =   fa

  tiene_f = False
  tiene_fa = False

  # dentro de la palabra
      if tiene_f and i.lower() == "a":
          tiene_fa = True
      elif i.lower() == "f":
          tiene_f = True   
      else: 
          tiene_f = False    
  """