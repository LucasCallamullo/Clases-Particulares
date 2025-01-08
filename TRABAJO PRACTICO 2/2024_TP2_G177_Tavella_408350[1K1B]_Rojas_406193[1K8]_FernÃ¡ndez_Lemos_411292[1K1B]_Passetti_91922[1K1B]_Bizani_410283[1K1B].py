# Respuesta 14
def promedio(envios, total_envios):
    if total_envios == 0:
        return 0

    promedio = envios / total_envios
    return int(promedio)


# Respuesta 13
def calc_porcentaje(total_envios, envios_exterior):
    if total_envios == 0:
        return 0
    porc = (envios_exterior * 100) / total_envios
    return int(porc)


# Respuesta 8
def mayor_cantidad_cartas(carta_simple, carta_certificada, carta_expresa):
    tipo_mayor = None
    if carta_simple >= carta_certificada and carta_simple >= carta_expresa:
        tipo_mayor = "Carta Simple"
    if carta_certificada >= carta_expresa and carta_certificada > carta_simple:
        tipo_mayor = "Carta Certificada"
    if carta_expresa > carta_certificada and carta_expresa > carta_simple:
        tipo_mayor = "Carta Expresa"

    return tipo_mayor


# RESPUESTA 4
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


def obtener_cp_pais(cadena):
    n = len(cadena)
    if cadena[0:5].isdigit() and cadena[5:6] == "-" and cadena[6:9].isdigit():
        return "Brasil"

    elif cadena[0:1].isalpha() and cadena[1:5].isdigit() and cadena[5:8].isalpha() and n == 8 and cadena[0] != 'I' and cadena[0] != 'O':
        return "Argentina"

    elif cadena[0:7].isdigit() and n == 7:
        return "Chile"

    elif cadena[0:6].isdigit() and n == 6:
        return "Paraguay"

    elif cadena[0:5].isdigit() and n == 5:
        return "Uruguay"

    elif cadena[0:4].isdigit() and n == 4:
        return "Bolivia"

    else:
        return "Otro"


# RESPUESTA 2
def validar_direccion(subcadena_direcc):
    mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZÑ"
    numeros = "0123456789"
    tiene_mayus = False

    for i in subcadena_direcc:
        # estoy dentro de una palabra
        if i != " " and i != ".":
            # tiene dos mayusculas seguidas
            if tiene_mayus and "A" <= i <= "Z":
                return False

            elif "A" <= i <= "Z":
                tiene_mayus = True

            else:
                tiene_mayus = False

            # para verificar que sean solo numeros y letras
            if not "a" <= i.lower() <= "z" and not "0" <= i <= "9":
                return False


        # termino una palabra
        else:
            tiene_mayus = False

    return True
'''
            if i.upper() not in mayus and i not in numeros:
                return False

            if i in mayus and not tiene_mayus:
                tiene_mayus = True
            elif tiene_mayus and i in mayus:
                return False
            else:
                tiene_mayus = False
                '''

# RESPUESTA 1
def validar_si_es_hc_o_sc(linea):
    tiene_h = False
    tiene_hc = False
    tiene_s = False
    tiene_sc = False

    for i in linea:

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
        return "Hard Control"

    if tiene_sc:
        return "Soft Control"


def principal():
    archivo = "envios.txt"
    archivo = "envios25.txt"
    m = open(archivo, "r")  # read (leer)

    # respuesta 1
    primera_linea = True
    control = ""

    # respuesta 2
    cedvalid = 0

    # respuesta 3
    cedinvalid = 0

    # respuesta 4
    imp_acu_total = 0

    # respuesta 5
    ccs = 0

    # respuesta 6
    ccc = 0

    # respuesta 7
    cce = 0

    # respuesta 9
    primer_cp = ""
    contador_lineas = 0

    # respuesta 10
    cant_primer_cp = 0

    # respuesta 11
    menimp = None

    # respuesta 12
    mencp = None

    # respuesta 13
    contador_total_exterior = 0

    # respuesta 14
    cont_envios_BA = 0
    importe_final_BA = 0

    for linea in m:
        if primera_linea:
            # Respuesta 1
            # return Hard Control o Soft Control
            control = validar_si_es_hc_o_sc(linea)
            primera_linea = False
        else:
            cp = linea[0:9].strip()
            direccion = linea[9:29].rstrip()
            destino_pais = obtener_cp_pais(cp)
            tipo_envio = int(linea[29:30])
            forma_pago = int(linea[30:31])

            # Estoy en Hard Control
            if control == "Hard Control":
                es_direccion_valida = validar_direccion(direccion)

                if es_direccion_valida:
                    # Respuesta 2
                    cedvalid += 1

                    # Respuesta 5 carta simple
                    if tipo_envio == 0 or tipo_envio == 1 or tipo_envio == 2:
                        ccs += 1
                    # Respuesta 6 carta certificada
                    if tipo_envio == 3 or tipo_envio == 4:
                        ccc += 1
                    # Respuesta 7 carta expresa
                    if tipo_envio == 5 or tipo_envio == 6:
                        cce += 1

                    # Respuesta 4
                    importe = calcular_importe(destino_pais, tipo_envio, cp, forma_pago)
                    imp_acu_total += importe

                    # Respuesta 13
                    if destino_pais != "Argentina":
                        contador_total_exterior += 1

                    # Respuesta 14
                    if destino_pais == "Argentina" and cp[0] == "B":
                        cont_envios_BA += 1
                        importe_final_BA += importe

                # Direccion No Validas
                else:
                    # Respuesta 3
                    cedinvalid += 1

                    # Respuesta 10
                    importe = calcular_importe(destino_pais, tipo_envio, cp, forma_pago)

            # estoy En Soft Control
            else:
                # Respuesta 2
                cedvalid += 1

                # Respuesta 4
                importe = calcular_importe(destino_pais, tipo_envio, cp, forma_pago)
                imp_acu_total += importe

                # Respuesta 5 carta simple
                if tipo_envio == 0 or tipo_envio == 1 or tipo_envio == 2:
                    ccs += 1
                # Respuesta 6 carta certificada
                if tipo_envio == 3 or tipo_envio == 4:
                    ccc += 1
                # Respuesta 7 carta expresa
                if tipo_envio == 5 or tipo_envio == 6:
                    cce += 1

                # Respuesta 13
                if destino_pais != "Argentina":
                    contador_total_exterior += 1

                # Respuesta 14
                if destino_pais == "Argentina" and cp[0] == "B":
                    cont_envios_BA += 1
                    importe_final_BA += importe

            # Estoy fuera de HC y SC

            if destino_pais == "Brasil":
                if menimp is None or importe < menimp:

                    # respuesta 11
                    menimp = importe

                    # respuesta 12
                    mencp = cp

                    # respuesta 9
            if contador_lineas == 1:
                primer_cp = cp

                    # respuesta 10
            if primer_cp == cp:
                cant_primer_cp += 1

        contador_lineas += 1



    m.close()

    # Respuesta 8
    tipo_mayor = mayor_cantidad_cartas(ccs, ccc, cce)

    # Respuesta 13
    envios_totales = cedvalid + cedinvalid
    porc = calc_porcentaje(envios_totales, contador_total_exterior)

    # Respuesta 14
    prom = promedio(importe_final_BA, cont_envios_BA)

    # RESULTADOS
    print(' (r1) - Tipo de control de direcciones:', control)
    print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
    print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
    print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
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


if __name__ == '__main__':
    principal()