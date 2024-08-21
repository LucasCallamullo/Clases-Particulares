

# PUNTO 14
def calcular_promedio(acum_importe_ba, cont_envios_ba):
    prom = 0
    if cont_envios_ba > 0:
        prom = int(acum_importe_ba / cont_envios_ba)
    return prom


# PUNTO 13
def calcular_porcentaje(envios_totales, cont_envios_exterior):
    porc = 0
    if envios_totales > 0:
        porc = (cont_envios_exterior * 100) / envios_totales
    return int(porc)


# PUNTO 8
def calcular_tipo_mayor(ccs, ccc, cce):
    if ccs >= ccc and ccs >= cce:
        tipo_mayor = "Carta Simple"

    elif ccc > ccs and ccc >= cce:
        tipo_mayor = "Carta Certificada"

    else:
        tipo_mayor = "Carta Expresa"
    return tipo_mayor


# Punto 4
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


def obtener_destino_pais(cp):
    size = len(cp)
    if cp[0:5].isdigit() and cp[5:6] == "-" and cp[6:9].isdigit():
        return "Brasil"
    elif cp[0].isalpha() and cp[1:5].isdigit() and cp[5:8].isalpha() and size == 8 and cp[0] != 'I' and cp[0] != 'O':
        return "Argentina"
    elif cp[0:7].isdigit() and size == 7:
        return "Chile"
    elif cp[0:6].isdigit() and size == 6:
        return "Paraguay"
    elif cp[0:5].isdigit() and size == 5:
        return "Uruguay"
    elif cp[0:4].isdigit() and size == 4:
        return "Bolivia"
    else:
        return "Otro"


# PUNTO 2 / PUNTO 3
def validar_direccion(direccion):
    valido = True
    una_mayus = False
    # direccion = "Atlantico 123." es un str
    for i in direccion:
        if i != " " and i != ".":
            if not "A" <= i.upper() <= "Z" and not "0" <= i <= "9":
                valido = False

            if una_mayus and "A" <= i <= "Z":
                valido = False
            elif "A" <= i <= "Z":
                una_mayus = True
            else:
                una_mayus = False
    return valido


# PUNTO 1
def analizar_hc_sc(linea):
    tiene_h = False
    tiene_s = False
    tiene_hc = False

    for i in linea:
        # Obtener SC
        if tiene_s and i == "C":
            tiene_hc = False
            break
        elif i == "S":
            tiene_s = True
        else:
            tiene_s = False

        # Obtener HC
        if tiene_h and i == "C":
            tiene_hc = True
            break
        elif i == "H":
            tiene_h = True
        else:
            tiene_h = False

    if tiene_hc:
        return "Hard Control"
    else:
        return "Soft Control"


def principal():
    fd = "envios25.txt"                 # file description
    # fd = "envios100HC.txt"            # file description
    # fd = "envios100SC.txt"            # file description
    # fd = "envios500b.txt"            # file description
    m = open(fd, "rt")                  # read text ; leer texto

    # Punto 1
    cont_lineas = 0
    control = ""

    # Punto 2 / Punto 3
    cedvalid = 0
    cedinvalid = 0

    # Punto 4
    imp_acu_total = 0

    # Punto 5 / 6 / 7
    ccs = 0
    ccc = 0
    cce = 0

    # Punto 9 / 10
    primer_cp = None
    cant_primer_cp = 0

    # Punto 11 / 12
    menimp = None
    mencp = None

    # Punto 13
    cont_envios_exterior = 0

    # Punto 14
    cont_envios_ba = 0
    acum_importe_ba = 0

    for linea in m:
        cont_lineas += 1

        if cont_lineas == 1:
            control = analizar_hc_sc(linea)     #
        else:

            cp = linea[0:9].strip()
            destino = obtener_destino_pais(cp)
            direccion = linea[9:29].rstrip()
            tipo_envio = int(linea[29])
            forma_pago = int(linea[30])

            # Estoy en Hard Control
            if control == "Hard Control":
                es_valida_direc = validar_direccion(direccion)

                # Direccion Valida
                if es_valida_direc:
                    # Punto 2
                    cedvalid += 1

                    # Punto 4
                    importe = calcular_importe(destino, tipo_envio, cp, forma_pago)
                    imp_acu_total += importe

                    # Punto 5 / 6 / 7
                    if tipo_envio == 0 or tipo_envio == 1 or tipo_envio == 2:
                        ccs += 1
                    elif tipo_envio == 3 or tipo_envio == 4:
                        ccc += 1
                    elif tipo_envio == 5 or tipo_envio == 6:
                        cce += 1

                    # Punto 13
                    if destino != "Argentina":
                        cont_envios_exterior += 1

                    # Punto 14
                    if destino == "Argentina" and cp[0] == "B":
                        cont_envios_ba += 1
                        acum_importe_ba += importe

                # Direccion NO Validas
                else:
                    # Punto 3
                    cedinvalid += 1

                    # Punto 10
                    importe = calcular_importe(destino, tipo_envio, cp, forma_pago)

            # Estoy en Soft Control
            else:

                # Punto 2
                cedvalid += 1

                # Punto 4
                importe = calcular_importe(destino, tipo_envio, cp, forma_pago)
                imp_acu_total += importe

                # Punto 5
                if tipo_envio == 0 or tipo_envio == 1 or tipo_envio == 2:
                    ccs += 1
                # Punto 6
                elif tipo_envio == 3 or tipo_envio == 4:
                    ccc += 1
                # Punto 7
                elif tipo_envio == 5 or tipo_envio == 6:
                    cce += 1

                # Punto 13
                if destino != "Argentina":
                    cont_envios_exterior += 1

                # Punto 14
                if destino == "Argentina" and cp[0] == "B":
                    cont_envios_ba += 1
                    acum_importe_ba += importe

            # Fuera de HC y SC
            # Punto 9 / 10
            if primer_cp is None:
                primer_cp = cp
                cant_primer_cp += 1
            else:
                if primer_cp == cp:
                    cant_primer_cp += 1

            # Punto 11 / 12
            if destino == "Brasil":
                if menimp is None or importe < menimp:
                    menimp = importe
                    mencp = cp

    m.close()

    # Punto 8
    tipo_mayor = calcular_tipo_mayor(ccs, ccc, cce)

    # Punto 13
    envios_totales = cedvalid + cedinvalid  # obtenemos el total a partir de los contadores de validos e invalidos
    porc = calcular_porcentaje(envios_totales, cont_envios_exterior)

    # Punto 14
    prom = calcular_promedio(acum_importe_ba, cont_envios_ba)

    # =================================================================
    #                          RESULTADOS
    # =================================================================
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


if __name__ == "__main__":
    principal()

