


def calcular_importe_punto4(precio_envio, porc, forma_pago):
    # precio                --- 100
    # X = porc * precio envio / 100   ---  porc
    importe = precio_envio + (porc * precio_envio) / 100

    if forma_pago == 1:         # efectivo 10% de descuento
        # importe                     --- 100%
        #  importe * 10 / 100 =     X  ---   10%
        importe = importe - (importe * 10) / 100

    return int(importe)


def calcular_porcentaje_punto4(cadena, cod_postal):
    # uruguay montevideo
    if (cod_postal == 4 and cadena[0] == "1") or cod_postal == 3 or cod_postal == 5:
        porc = 20

    elif cod_postal == 4 or cod_postal == 2:
        porc = 25

    # elif cod_postal == 0 and (subcadena_cp[0] == "8" or subcadena_cp[0] == "9"):
    elif cod_postal == 0 and cadena[0] in "89":
        porc = 20

    # elif cod_postal == 0 and ("0" <= subcadena_cp[0] <= "3"):
    elif cod_postal == 0 and cadena[0] in "0123":
        porc = 25

    # elif cod_postal == 0 and ("4" <= subcadena_cp[0] <= "7"):
    elif cod_postal == 0 and cadena[0] in "4567":
        porc = 30

    else:
        porc = 50
    return porc


def obtener_cod_postal_pais(cadena):
    # Brasil = 0
    if cadena[5:6] == "-" and cadena[0:5].isdigit() and cadena[6:9].isdigit():
        return 0

    # Argentina = 1
    elif cadena[0:1].isalpha() and cadena[1:5].isdigit() and cadena[5:8].isalpha() and len(
            cadena) == 8:
        return 1

    # Chile
    elif cadena[0:7].isdigit() and len(cadena) == 7:
        return 2

    # Paraguay
    elif cadena[0:6].isdigit() and len(cadena) == 6:
        return 3

    # Uruguay
    elif cadena[0:5].isdigit() and len(cadena) == 5:
        return 4

    # Bolivia
    elif cadena[0:4].isdigit() and len(cadena) == 4:
        return 5

    else:
        return 6


def precio_por_tipo_envio(tipo_envio):
    #                   0     1    2    3      4       5       6
    tupla_importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    return tupla_importes[tipo_envio]


# ==================================================================
#                   Punto 2
# ==================================================================
def validar_direcciones(direccion):
    mayus = "ABCDEFGHIJKLOMNÑOPQRSTUVWXYZ"
    digitos = "0123456789"
    has_mayus = False
    has_numbers = False

    for i in direccion:
        # estamos dentro de la palabra
        # direccion = Da Porto 987.
        # i = D, O,  , P
        if i != " " and i != ".":

            # upper() transforma tod0 a  mayusculas, y el lower() tod0 a minusculas
            # if not ("A" <= i.upper() <= "Z" or i.lower() == "ñ") or not "0" <= i <= "9":
            if not i.upper() in "0123456789ABCDEFGHIJKLOMNÑOPQRSTUVWXYZ":       # si no esta
                return False            # si no es numero o letra no es valida la direccion

            if i in mayus and has_mayus:
                return False         # si tiene dos mayusculas seguidas no es valida la direccion
            elif i in mayus:
                has_mayus = True
            else:
                has_mayus = False

            # tiene un solo digito
            if i in digitos:
                has_numbers = True

            if has_numbers and i not in digitos:
                return False

        # termina la palabra
        else:
            has_numbers = False
            has_mayus = False

    return True         # es cuando sali de la cadena significa que cumplio todas las condiciones




# ==================================================================
#                   Punto 1
# ==================================================================
def validar_control(linea):
    # validar si es HC o SC
    # linea =  "HoC – 18:15 – 10/06/2020."
    has_h = False
    has_hc = False
    has_s = False

    for car in linea:
        # car = H,  , C,  , - ,  , 1
        # estamos dentro de una palabra
        # if not car in " .":
        if car != " " and car != ".":

            if car == "H":
                has_h = True

            elif car == "S":
                has_s = True

            elif car == "C" and has_s:
                has_hc = False

            elif car == "C" and has_h:
                has_hc = True

            else:
                has_h = False
                has_s = False

        # estamos fuera de una palabra
        else:
            has_h = False

    if has_hc:
        return "Hard Control"

    else:
        return "Soft Control"


'''
def direccionValida(linea):
    hayPalabraConDigitos = False
    caractAntMayor = False
    hayEspacioNum = False
    cantDigitos = 0

    for caracter in linea[9:28]:

        # estamos
        if caracter != " " and caracter != ".":
            pass

        # if ("A" <= caracter.upper() <= "Z" or caracter.lower() == "ñ") or "0" <= caracter <= "9":
        if caracter.upper() in "0123456789ABCDEFGHIJKLOMNÑOPQRSTUVWXYZ .":
            # if ("A" <= caracter <= "Z" or caracter == "ñ")
            if caracter in "ABCDEFGHIJKLOMNÑOPQRSTUVWXYZ":
                if caractAntMayor:
                    return False
                caractAntMayor = True
            else:
                caractAntMayor = False

            if caracter == " ":
                hayEspacioNum = True

            if hayEspacioNum:
                if caracter in "0123456789":
                    cantDigitos += 1
                elif caracter in " ." and cantDigitos >= 1:
                    hayPalabraConDigitos = True
                else:
                    cantDigitos = 0
        else:
            return False
    if hayPalabraConDigitos:
        return True
    else:
        return False
'''




def principal():

    # archivo = "envios25.txt"
    archivo = "envios100HC.txt"
    # archivo = "envios100SC.txt"

    # m = open("envios25.txt", "rt", encoding="utf-8")
    m = open(archivo, "rt")      # read text

    # r1
    contadorLinea = 0
    control = ""

    # r2 / r3
    cedvalid = 0
    cedinvalid = 0

    # r4
    imp_acu_total = 0


    for linea in m:

        contadorLinea += 1

        # "Estoy en la primera linea"
        if contadorLinea == 1:
            control = validar_control(linea)        # "Hard Control"

        # "No Estoy en la primera linea"
        else:

            # Obtener la subcadena del índice 0 al 8 que correspondeal codigo postal
            cad_cod_postal = linea[0:9].strip()

            # Devuelve el pais segun un numero asignado (ver funcion para cada asignacion) (int)
            cod_postal = obtener_cod_postal_pais(cad_cod_postal)

            # obtener la subcadena indice 9:28 a la direccion
            direccion = linea[9:29].rstrip()

            # obtener el caracter 29 que es el tipo de envio del 0 al 6 en str lo paso a int
            tipo_envio = int(linea[29:30])

            # obtener el caracter 30 que es la forma de pago 1-efectivo ; 2-tarjeta, # descuento 10% para efectivo
            forma_pago = int(linea[30:31])



            # Estamos en HC
            if control == "Hard Control":
                es_direcc_valida = validar_direcciones(direccion)       # return True es valida, si es False no es valida

                if es_direcc_valida:
                    # r2
                    cedvalid += 1

                    # r4
                    # argentina no cobra porcentaje por envio internacional
                    if cod_postal == 1:
                        porc = 0
                    else:
                        porc = calcular_porcentaje_punto4(cad_cod_postal, cod_postal)

                    precio_envio = precio_por_tipo_envio(tipo_envio)
                    importe = calcular_importe_punto4(precio_envio, porc, forma_pago)
                    imp_acu_total += importe


                else:
                    cedinvalid += 1



            # Estamos en Soft Control
            else:
                # r2
                cedvalid += 1

                # argentina no cobra porcentaje por envio internacional
                if cod_postal == 1:
                    porc = 0
                else:
                    porc = calcular_porcentaje_punto4(cad_cod_postal, cod_postal)

                precio_envio = precio_por_tipo_envio(tipo_envio)
                importe = calcular_importe_punto4(precio_envio, porc, forma_pago)
                imp_acu_total += importe




            print("No estoy en la primera linea")


        # for i in linea:
            # i = h,  , S, C,  , -  , 1

            ''' 
    while True:
        linea = m.readline()        #

        print(linea, end="")

        if contadorLinea == 0:
            contadorLinea += 1
            if "HC" in linea:
                control = "Hard Control"

            if "SC" in linea:
                control = "Soft Control"

        else:
            if control == "Hard Control":
                print(direccionValida(linea[0:31]))

            if not linea:
                break
    '''

    m.close()
    # Salimos del ciclo for del archivo

    # =================================================================
    #                          RESULTADOS
    # =================================================================
    print(' (r1) - Tipo de control de direcciones:', control)
    print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
    print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
    print(' (r4) - Total acumulado de importes finales:', imp_acu_total)

    ''' 
    print(' (r5) - Cantidad de cartas simples:', ccs)
    print(' (r6) - Cantidad de cartas certificadas:', ccc)
    print(' (r7) - Cantidad de cartas expresas:', cce)
    print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)
    print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp)
    print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
    print('(r11) - Importe menor pagado por envios a Brasil:', menimp)
    print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
    print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
    print('(r14) - Importe final promedio de los envios Buenos Aires:', prom)
    '''
    m.close()


if __name__ == '__main__':
    principal()