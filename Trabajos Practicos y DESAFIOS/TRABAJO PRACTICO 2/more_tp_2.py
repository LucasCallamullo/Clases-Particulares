

# =================================================================
#                          PUNTO 4
# =================================================================
def calcular_importe(destino, tipo, cp, pago):
    importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    monto = importes[tipo]

    if destino == 'Argentina':
        inicial = monto
    else:
        if destino == 'Bolivia' or destino == 'Paraguay' or (destino == 'Uruguay' and cp[0] == '1'):
            inicial = int(monto * 1.20)
        elif destino == 'Chile' or (destino == 'Uruguay' and cp[0] != '1'):
            inicial = int(monto * 1.25)
        elif destino == 'Brasil':
            if cp[0] == '8' or cp[0] == '9':
                inicial = int(monto * 1.20)
            else:
                if cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3':
                    inicial = int(monto * 1.25)
                else:
                    inicial = int(monto * 1.30)
        else:
            inicial = int(monto * 1.50)

    # 4. Determinación del valor final del ticket a pagar.
    # asumimos que es pago en tarjeta...
    final = inicial

    # ... y si no lo fuese, la siguiente será cierta y cambiará el valor...
    if pago == 1:
        final = int(0.9 * inicial)

    return final


def obtener_cod_postal_pais(cp):
    long_cp = len(cp)
    if cp[0:5].isdigit() and cp[5:6] == "-" and cp[6:9].isdigit():
        return "Brasil"

    elif cp[0:1].isalpha() and cp[1:5].isdigit() and cp[5:8].isalpha() and long_cp == 8 and cp[0] != 'I' and cp[0] != 'O':
        return "Argentina"

    elif cp[0:4].isdigit() and long_cp == 4:
        return "Bolivia"

    elif cp[0:5].isdigit() and long_cp == 5:
        return "Uruguay"

    elif cp[0:6].isdigit() and long_cp == 6:
        return "Paraguay"

    elif cp[0:7].isdigit() and long_cp == 7:
        return "Chile"

    else:
        return "Otro"


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
        if i != " " and i != ".":

            # upper() transforma tod0 a  mayusculas, y el lower() tod0 a minusculas
            # if not ("A" <= i.upper() <= "Z" or i.lower() == "ñ") or not "0" <= i <= "9":
            # if not i.upper() in "0123456789ABCDEFGHIJKLOMNÑOPQRSTUVWXYZ":  # si no esta
            if i.upper() not in mayus and i not in digitos:
                return False  # si no es numero o letra no es valida la direccion

            # si tiene dos mayusculas seguidas no es valida la direccion
            if i in mayus and has_mayus:
                return False
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

    return True  # es cuando sali de la cadena significa que cumplio todas las condiciones


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


def principal():
    # archivo = "envios25.txt"
    # archivo = "envios100HC.txt"
    archivo = "envios100SC.txt"

    # m = open("envios25.txt", "rt", encoding="utf-8")
    m = open(archivo, "rt")  # read text

    # r1
    contadorlinea = 0
    control = ""

    # r2 / r3
    cedvalid = 0
    cedinvalid = 0

    # r4
    imp_acu_total = 0

    for linea in m:
        contadorlinea += 1

        # "Estoy en la primera linea"
        if contadorlinea == 1:
            control = validar_control(linea)  # "Hard Control"

        # "No Estoy en la primera linea"
        else:

            # sub-cadena indice 0:8 referencia a  codigo postal
            cad_cod_postal = linea[0:9].strip()

            # Devuelve el pais segun un numero asignado (ver funcion para cada asignacion) (int)
            pais_destino = obtener_cod_postal_pais(cad_cod_postal)

            # sub-cadena indice 9:28 referencia a la direccion
            direccion = linea[9:29].rstrip()

            # sub-cadena caracter 29 referencia a la tipo de envio 0 al 6
            tipo_envio = int(linea[29:30])

            # sub-cadena caracter 29 referencia a la forma de pago 1-efectivo ; 2-tarjeta; descuento 10% para efectivo
            forma_pago = int(linea[30:31])

            # Estamos en HC
            if control == "Hard Control":
                es_direcc_valida = validar_direcciones(direccion)  # return True es valida, si es False no es valida

                if es_direcc_valida:
                    # r2
                    cedvalid += 1

                    # r4
                    importe = calcular_importe(pais_destino, tipo_envio, cad_cod_postal, forma_pago)
                    imp_acu_total += importe

                else:
                    cedinvalid += 1

            # Estamos en Soft Control
            else:
                # r2
                cedvalid += 1

                # r4
                importe = calcular_importe(pais_destino, tipo_envio, cad_cod_postal, forma_pago)
                imp_acu_total += importe

            print("No estoy en la primera linea")

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