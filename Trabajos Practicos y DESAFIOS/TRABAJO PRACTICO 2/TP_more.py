
#R8 funcion para identificar cual tipo de cartas fue mas enviada
def promedio(envios, total_envios):
    if envios <= total_envios:
        promedio = envios / total_envios
    return promedio


def mayor_cantidad_cartas(carta_simple, carta_certificada, carta_expresa):
    tipo_mayor = None
    if carta_simple >= carta_certificada and carta_simple >= carta_expresa:
        tipo_mayor = "carta simple"
    if carta_certificada >= carta_expresa and carta_certificada > carta_simple:
        tipo_mayor = "carta certificada"
    if carta_expresa > carta_certificada and carta_expresa > carta_simple:
        tipo_mayor = "carta expresa"

    return tipo_mayor


#RESPUESTA 4

def calcular_importe_final(precio_envio, porc, forma_pago):
    importe = precio_envio + (precio_envio * porc) / 100

    if forma_pago == 1:     # significa que era efectivo y un %10 de descuento
        importe = importe - (importe * 10) / 100

    return int(importe)


def precio_tipo_envio(tipo_envio):
    monto = 0
    if tipo_envio == 0:
        monto = 1100
    elif tipo_envio == 1:
        monto = 1800
    elif tipo_envio == 2:
        monto = 2450
    elif tipo_envio == 3:
        monto = 8300
    elif tipo_envio == 4:
        monto = 10900
    elif tipo_envio == 5:
        monto = 14300
    elif tipo_envio == 6:
        monto = 17900
    return monto


def calcular_porcentaje_pais_region(subcadena_cp, cod_postal):
    # uruguay montevideo
    if (cod_postal == 4 and subcadena_cp[0] == "1") or cod_postal == 3 or cod_postal == 5:
        porc = 20

    elif cod_postal == 4 or cod_postal == 2:
        porc = 25

    elif cod_postal == 0 and (subcadena_cp[0] == "8" or subcadena_cp[0] == "9"):
        porc = 20

    elif cod_postal == 0 and ("0" <= subcadena_cp[0] <= "3"):
        porc = 25

    elif cod_postal == 0 and ("4" <= subcadena_cp[0] <= "7"):
        porc = 30

    else:
        porc = 50

    return porc


def obtener_cp_pais(subcadena_cp):
    # Brasil = 0
    if subcadena_cp[5:6] == "-" and subcadena_cp[0:5].isdigit() and subcadena_cp[6:9].isdigit():
        return 0

    # Argentina = 1
    if subcadena_cp[0:1].isalpha() and subcadena_cp[1:5].isdigit() and subcadena_cp[5:8].isalpha() and len(
            subcadena_cp) == 8:
        return 1

    # Chile
    if subcadena_cp[:7].isdigit() and len(subcadena_cp) == 7:
        return 2

    # Paraguay
    if subcadena_cp[:6].isdigit() and len(subcadena_cp) == 6:
        return 3

    # Uruguay
    if subcadena_cp[:5].isdigit() and len(subcadena_cp) == 5:
        return 4

    # Bolivia
    if subcadena_cp[:4].isdigit() and len(subcadena_cp) == 4:
        return 5

    # Otro pais
    return 6





#RESPUESTA 2

def validar_direccion(subcadena_direcc):
    letras = "abcdefghijklmnopqrstuvwxyzñ"
    numeros = "0123456789"

    tiene_mayus = False
    mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZÑ"

    palabra_solo_numeros = False

    for i in subcadena_direcc:
        # estoy dentro de una palabra
        if i != " " and i != ".":

            # if not "a" <= i.lower() <= "z" and not "0" <= i <= "9":
            if i.lower() not in letras and i not in numeros:     # si la i.lower() no esta dentro de letras
                return False            # significa que no cumple

            # para saber dops mayusculas seguidas
            # ABV
            if i in mayus and not tiene_mayus:
                tiene_mayus = True
            elif tiene_mayus and i in mayus:
                return False
            else:
                tiene_mayus = False

            # que toda la pabra sean numeros
            if i in numeros:
                palabra_solo_numeros = True

            if palabra_solo_numeros:
                if not i.isdigit():
                    return False

        # termino una palabra
        else:
            tiene_mayus = False
            palabra_solo_numeros = False

    return True             # si salio del ciclo for significa que es una direc valida







#RESPUESTA 1

def validar_si_es_hc_o_sc(linea):
    # linea = omitir esta lineaHC.
    # Reconocer si la linea/cadena contiene un HC o SC

    tiene_h = False
    tiene_hc = False

    tiene_s = False
    tiene_sc = False

    for i in linea:
        # i = o m i t i, r, H, , C,  ,e sta  linea.
        # i = H C
        # estoy dentro de una palabra
        if i != " " and i != ".":

            # tiene hc
            if i.lower() == "h":
                tiene_h = True

            elif tiene_h and i.lower() == "c":
                tiene_hc = True

            else:
                tiene_h = False

            # tiene sc
            if i.lower() == "s":
                tiene_s = True

            elif tiene_s and i.lower() == "c":
                tiene_sc = True

            else:
                tiene_s = False

        # termino una palabra
        else:
            tiene_s = False
            tiene_h = False

    if tiene_hc:
        return True

    if tiene_sc:
        return False
    return False




def principal():

    archivo = "envios25.txt"
    #archivo = "envios100HC.txt"
    #archivo = "envios100SC.txt"
    m = open(archivo, "r")          # read o sea leer

    # r1
    primera_linea = True
    control = ""

    # r2
    cedvalid = 0

    # r3
    cedinvalid = 0

    # r4
    imp_acu_total = 0

    # r5
    ccs = 0

    # r6
    ccc = 0

    # r7
    cce = 0

    # r14
    cont_envios_BA = 0


    for linea in m:
        if primera_linea:

            # r1
            es_hc = validar_si_es_hc_o_sc(linea)    # Si es True es HC, si es False es SC

            if es_hc:
                control = "Hard Control"
            else:
                control = "Soft Control"

            # algo vamos a hacer
            primera_linea = False

        else:

            # r2
            # obtener la subcadena indice 9:28 a la direccion
            subcadena_direcc = linea[9:29].rstrip()

            # Obtener la subcadena del índice 0 al 8 que correspondeal codigo postal
            subcadena_cp = linea[0:9].strip()

            # Devuelve el pais segun un numero asignado (ver funcion para cada asignacion)
            cod_postal = obtener_cp_pais(subcadena_cp)

            # obtener el caracter 29 que es el tipo de envio del 0 al 6 en str lo paso a int
            tipo_envio = int(linea[29:30])

            # obtener el caracter 30 que es la forma de pago 1- efectivo ; 2- tarjeta, # descuento 10% para efectivo
            forma_pago = int(linea[30:31])

            # Estoy en Hard Control
            if es_hc:
                # r2
                es_valida_direcc = validar_direccion(subcadena_direcc)  # Si Es True es valido, si es False no es valida

                if es_valida_direcc:
                    # r2
                    cedvalid += 1

                    # r5 carta simple
                    if tipo_envio == 0 or tipo_envio == 1 or tipo_envio == 2 :
                        ccs += 1
                    # r6 carta certificada
                    if tipo_envio == 3 or tipo_envio == 4:
                        ccc += 1
                    # r7 carta expresa
                    if tipo_envio == 5 or tipo_envio == 6:
                        cce += 1

                    # r4
                    # Argentina = 1 no cobra porcentaje
                    if cod_postal == 1:
                        porc = 0
                    else:
                        porc = calcular_porcentaje_pais_region(subcadena_cp, cod_postal)

                    precio_envio = precio_tipo_envio(tipo_envio)

                    importe = calcular_importe_final(precio_envio, porc, forma_pago)
                    imp_acu_total += importe


                else:
                    # r3
                    cedinvalid += 1

            # estoy En Soft Control
            else:

                # r2
                cedvalid += 1

                # r4
                # Argentina = 1 no cobra porcentaje
                if cod_postal == 1:
                    porc = 0
                else:
                    porc = calcular_porcentaje_pais_region(subcadena_cp, cod_postal)

                precio_envio = precio_tipo_envio(tipo_envio)

                importe = calcular_importe_final(precio_envio, porc, forma_pago)
                imp_acu_total += importe

                # r5 carta simple
                if tipo_envio == 0 or tipo_envio == 1 or tipo_envio == 2:
                    ccs += 1
                # r6 carta certificada
                if tipo_envio == 3 or tipo_envio == 4:
                    ccc += 1
                # r7 carta expresa
                if tipo_envio == 5 or tipo_envio == 6:
                    cce += 1

        #r8 El mayor tipo de carta enviadas
        tipo_mayor = mayor_cantidad_cartas(ccs, ccc, cce)















    #RESULTADOS

    print(' (r1) - Tipo de control de direcciones:', control)
    print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
    print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
    print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
    print(' (r5) - Cantidad de cartas simples:', ccs)
    print(' (r6) - Cantidad de cartas certificadas:', ccc)
    print(' (r7) - Cantidad de cartas expresas:', cce)
    print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)

    ''' 
    total -- 100
    calcular -- calcular * 100 / total
    

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