

def calcular_importe(destino, tipo, cp, pago):
    #             0     1       2   3   4       5       6
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


def obtener_destino_cod_postal(cp):
    tam = len(cp)
    if cp[0:5].isdigit() and cp[5:6] == "-" and cp[6:9].isdigit():
        return "Brasil"

    elif cp[0:1].isalpha() and cp[1:5].isdigit() and cp[5:8].isalpha() and tam == 8 and (cp[0] != 'I' and cp[0] != 'O'):
        return "Argentina"

    elif cp[0:7].isdigit() and tam == 7:
        return "Chile"

    elif cp[0:6].isdigit() and tam == 6:
        return "Paraguay"

    elif cp[0:5].isdigit() and tam == 5:
        return "Uruguay"

    elif cp[0:4].isdigit() and tam == 4:
        return "Bolivia"

    else:
        return "Otro"


def validar_direcciones(cadena_direccion):
    # cadena_direccion = Atlantico 123.
    # consonantes = "abcdefghijklmnopqrstuvwxyzñ"
    # numeros = "0123456789"

    tiene_mayus = False
    solo_numeros = False
    direccion_valida = True     # una direccion valida hasta que se demuestra lo contrario

    for i in cadena_direccion:
        # estamos dentro den una palabra
        if i != " " and i != ".":

            # para que todos sean letras y numeros
            # if i.lower() not in consonantes and i not in numeros:
            if not "a" <= i.lower() <= "z" and not "0" <= i <= "9":
                direccion_valida = False
                # break

            # si tengo dos mayusculas seguidas
            if tiene_mayus and "A" <= i <= "Z":
                direccion_valida = False
                # break

            elif "A" <= i <= "Z":
                tiene_mayus = True

            else:
                tiene_mayus = False

            # que toda la pabra sean numeros
            if i in "0123456789":
                solo_numeros = True

            if solo_numeros:
                if i not in "0123456789":
                    direccion_valida = False
                    # break

    if direccion_valida:
        return True
    else:
        return False


# =============================================================
#                         Punto 1
# =============================================================
def analizar_linea_control(linea):
    '''
    if "HC" in linea:
        return "Hard Control"

    if "SC" in linea:
        return "Soft Control" '''
    tiene_h = False
    tiene_hc = False

    tiene_s = False
    tiene_sc = False

    # linea = "HC – 18:15 SC – 10/06/2020" esto lo toma como un str/ cadena
    for i in linea:

        # detectar HC
        if i == "H":
            tiene_h = True

        elif tiene_h and i == "C":
            tiene_hc = True
            break
            # return "Hard Control"

        else:
            tiene_h = False

        # detectar SC
        if i == "S":
            tiene_s = True

        elif tiene_s and i == "C":
            tiene_sc = True
            # break
            # return "Soft Control"

        else:
            tiene_s = False

    if tiene_hc:
        return "Hard Control"

    if tiene_sc:
        return "Soft Control"


def principal():

    # archivo = "envios25.txt"
    archivo = "envios100SC.txt"
    # archivo = "envios100HC.txt"
    # archivo = "envios500b.txt"

    m = open(archivo, "rt")             # read text, leer texto

    # r1
    control = ""
    cont_lineas = 0

    # r2 / r3
    cedvalid = cedinvalid = 0

    # r4
    imp_acu_total = 0

    for linea in m:
        # linea =  "HC – 18:15 – 10/06/2020" es un str
        cont_lineas += 1

        # significa que estoy en la primera linea
        if cont_lineas == 1:
            control = analizar_linea_control(linea)     # return Hard control o Soft control segun corresponda

        else:
            # Para obtener la cadena que corresponde al codigo postal
            # subcadena_cp = "  03X3076"                                Atlantico 123.      01
            cadena_cod_postal = linea[0:9].strip()                  # quita los espacios en blanco a la izq

            # Devuelve el pais segun un numero asignado (ver funcion para cada asignacion) (int)
            cod_postal = obtener_destino_cod_postal(cadena_cod_postal)

            # Para obtener la cadena que corresponde a la direccion
            cadena_direccion = linea[9:29].rstrip()             # quita los espacios en blanco a la derecha

            # Para obtener el numero que corresponde a tipo_envio ( 0 al 6 )
            tipo_envio = int(linea[29:30])

            # obtener el caracter 30 que es la forma de pago 1-efectivo ; 2-tarjeta, # descuento 10% para efectivo
            forma_pago = int(linea[30:31])

            # Estoy en Hard Control HC
            if control == "Hard Control":

                es_direccion_valida = validar_direcciones(cadena_direccion)     # return True si es valida, False si no es valida

                # Cuando la direccion valida
                if es_direccion_valida:
                    # r2
                    cedvalid += 1

                    # r4
                    importe = calcular_importe(cod_postal, tipo_envio, cadena_cod_postal, forma_pago)
                    imp_acu_total += importe

                # Cuando la direccion NO es valida
                else:
                    # r3
                    cedinvalid += 1

                    # r11 / r12
                    importe = calcular_importe(cod_postal, tipo_envio, cadena_cod_postal, forma_pago)
                    imp_acu_total += importe

            # Estoy en Soft Control SC
            else:
                # r2
                cedvalid += 1

                # r4
                importe = calcular_importe(cod_postal, tipo_envio, cadena_cod_postal, forma_pago)
                imp_acu_total += importe

            #No estoy ni en Hc ni en SC

    # SALI DEL ARCHIVO
    m.close()


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



if __name__ == '__main__':
    principal()


