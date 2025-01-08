def check_dir(direccion):
    palabraynumero = False
    cl = cp = cldigito = 0
    caracter_anterior = " "
    for car in direccion:
        if car in " .":
            if cl != 0:
                cp += 1
            cl = 0
            if cldigito == cl:
                palabraynumero = True
        else:
            cl += 1
            # panza de la palabra...
            if not car.isdigit() and not car.isalpha():
                return False
            if caracter_anterior.isupper() and car.isupper():
                return False
            if car.isdigit():
                cldigito += 1
            caracter_anterior = car
    return palabraynumero

def ordenar(n1,n2,n3):
    ccs,ccc,cce = n1,n2,n3
    if n1 > n2 and n1 > n3:
        mayor = 'Carta Simple'
    else:
        if n2 > n3 and n2 > n1:
            mayor = 'Carta Certificada'
        else:
            mayor = 'Carta Express'
    if n1 == n2 and n1 == n3:
        mayor = 'Carta Simple'
    if n2 == n3:
        mayor = 'Carta Certificada'
    return mayor


def codigo_postal(cp):
    if len(cp) == 8 and (cp[1:5].isdigit() and cp[5:8].isalpha() and cp[0].isalpha()) and (cp[0] != 'I' and cp[0] != 'O'):
        destino = 'Argentina'
    elif len(cp) == 4 and cp[0:4].isdigit():
        destino = 'Bolivia'
    elif len(cp) == 9 and cp[5] == '-' and cp[0:5].isdigit() and cp[6:9].isdigit():
        destino = 'Brasil'
    elif len(cp) == 7 and cp[0:7].isdigit():
        destino = 'Chile'
    elif len(cp) == 6 and cp[0:6].isdigit():
        destino = 'Paraguay'
    elif len(cp) == 5 and cp[0:5].isdigit():
        destino = 'Uruguay'
    else:
        destino = 'Otro'
    return destino


def importe_total(destino,cp,tipo,pago):
    importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    inicial = importes[tipo]

    if destino == 'Argentina':
        inicial = importes[tipo]

    elif destino == 'Bolivia' or destino == 'Paraguay' or (destino == 'Uruguay' and cp[0] == '1') or (
            destino == 'Brasil' and (cp[0] == '8' or cp[0] == '9')):

        inicial += (inicial * 20) / 100

    elif destino == 'Chile' or (destino == 'Uruguay' and cp[0] != '1') or (destino == 'Brasil' and (cp[0] == '0' \
         or cp[0] == '1' or cp[0] == '2' or cp[0] == '3')):

        inicial += (inicial * 25) / 100

    elif destino == 'Brasil' and (cp[0] == '4' or cp[0] == '5' or cp[0] == '6' or cp[0] == '7'):

        inicial += (inicial * 30) / 100

    # elif destino == 'Otro':
    else:
        inicial += (inicial * 50) / 100

    if pago == 1:
        inicial = inicial * 0.9
    return int(inicial)


def principal():
    # resultados r2 y r3...
    cedvalid = cedinvalid = imp_acu_total = ccs = ccc = cce = cant_primer_cp = prom = porc = envios_al_exterior = 0
    envio_buenos_aires = importe_buenos_aires = imp_acu_todo_F = 0
    valido = validosoft = False
    primer_cp = menimp = mencp = None

    fd = "envios100HC.txt"
    m = open(fd, "rt")
    line = m.readline()
    # resultado 1...
    if "HC" in line:
        control = "Hard Control"
    else:
        control = "Soft Control"
    # procesar el resto de las lineas...
    while True:
        line = m.readline()
        if line == "":
            break
        cp = line[0:9].strip().upper()
        direccion = line[9:29].strip()
        tipo = int(line[29])
        pago = int(line[30])
        destino = None

        if primer_cp is None:
            primer_cp = cp
        if primer_cp == cp:
            cant_primer_cp += 1
        if control == "Hard Control":
            if check_dir(direccion):
                # direccion buena...
                cedvalid += 1
                if tipo in (0,1,2):
                    ccs += 1
                if tipo in (3,4):
                    ccc += 1
                if tipo in (5,6):
                    cce += 1
                tipo_mayor = ordenar(ccs, ccc, cce)
                destino = codigo_postal(cp)
                importe = importe_total(destino,cp,tipo, pago)
                imp_acu_total += importe
                if codigo_postal(cp) != 'Argentina':
                    envios_al_exterior += 1
                if cedvalid != 0:
                    total_envios = cedvalid + cedinvalid
                    porc = int((envios_al_exterior * 100) / total_envios)
                else:
                    porc = 0
                if codigo_postal(cp) == 'Argentina' and cp[0] == 'B':
                    envio_buenos_aires += 1
                    importe_buenos_aires += importe
                if envio_buenos_aires != 0:
                    prom = int(importe_buenos_aires // envio_buenos_aires)
                else:
                    prom = 0
            else:
                # direccion mala...
                cedinvalid += 1
                destino = codigo_postal(cp)
                importe = importe_total(destino, cp, tipo, pago)
                imp_acu_todo_F += importe
        else:
            # es Soft control...
            cedvalid += 1
            if tipo in (0,1,2):
                ccs += 1
            if tipo in (3,4):
                ccc += 1
            if tipo in (5,6):
                cce += 1
            tipo_mayor = ordenar(ccs,ccc,cce)
            destino = codigo_postal(cp)
            importe = importe_total(destino, cp, tipo, pago)
            imp_acu_total += importe
            if codigo_postal(cp) == 'Argentina' and cp[0] == 'B':
                envio_buenos_aires += 1
                importe_buenos_aires += importe
            if envio_buenos_aires != 0:
                prom = int(importe_buenos_aires // envio_buenos_aires)
            else:
                prom = 0
            if codigo_postal(cp) != 'Argentina':
                envios_al_exterior += 1
            if cedvalid != 0:
                total_envios = cedvalid
                porc = int((envios_al_exterior * 100) / total_envios)
            else:
                porc = 0

#Resultado 12
        if codigo_postal(cp) == 'Brasil' and ((menimp and mencp) is None or importe < menimp):
            menimp = importe
            mencp = cp
    m.close()

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
    print('(r14) - Importe final promedio de los envios a Buenos Aires:', prom)
principal()