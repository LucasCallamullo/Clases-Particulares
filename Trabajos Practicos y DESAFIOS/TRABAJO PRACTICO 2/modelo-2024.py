def check_dir(direccion):
    mayuscula = mayuscula2 = cdigito = cdigitoypalabra = False
    cantidadmayuscula2 = cl = cp = cldigito = cpdigito = 0
    for car in direccion:
        if car in " .":
            if cl != 0:
                cp += 1
            cl = 0
            if cldigito != 0:
                cpdigito += 1
            if cpdigito >= 1:
                return True
            if cdigitoypalabra:
                return False
            # final de palabra...
        else:
            cl += 1
            # panza de la palabra...
            if not car.isdigit() and not car.isalpha():
                return False
            if cl == 2 and car.isupper():
                return False
            if car.isdigit():
                cdigito = True
                cldigito += 1
            elif car.isalpha() and cdigito:
                cdigitoypalabra = True
    return True

def ordenar(n1,n2,n3):
    ccs,ccc,cce = n1,n2,n3
    if n1 == n2 and n1 == n3:
        mayor = 'Carta Simple'
    if n2 == n3:
        mayor = 'Carta Certificada'
    if n1 > n2 and n1 > n3:
        mayor = 'Carta Simple'
    else:
        if n2 > n3 and n2 > n1:
            mayor = 'Carta Certificada'
        else:
            mayor = 'Carta Express'
    return mayor

def codigo_postal(cp):
    if len(cp) == 8 and (cp[1:5].isnumeric() and cp[5:8].isalpha() and cp[0].isalpha()) and (cp[0] != 'I' and cp[0] != 'O'):
        destino = 'Argentina'
    elif len(cp) == 4 and cp[0:4].isnumeric():
        destino = 'Bolivia'
    elif len(cp) == 9 and cp[5] == '-' and cp[0:5].isnumeric() and cp[6:9].isnumeric():
        destino = 'Brasil'
    elif len(cp) == 7 and cp[0:7].isnumeric():
        destino = 'Chile'
    elif len(cp) == 6 and cp[0:6].isnumeric():
        destino = 'Paraguay'
    elif len(cp) == 5 and cp[0:5].isnumeric():
        destino = 'Uruguay'
    else:
        destino = 'Otro'
    return destino


def importe_total(cp, tipo, pago):
    if len(cp) == 8 and (cp[1:5].isnumeric() and cp[5:8].isalpha() and cp[0].isalpha()) and (cp[0] != 'I' and cp[0] != 'O'):
        destino = 'Argentina'
    elif len(cp) == 4 and cp[0:4].isnumeric():
        destino = 'Bolivia'
    elif len(cp) == 9 and cp[5] == '-' and cp[0:5].isnumeric() and cp[6:9].isnumeric():
        destino = 'Brasil'
    elif len(cp) == 7 and cp[0:7].isnumeric():
        destino = 'Chile'
    elif len(cp) == 6 and cp[0:6].isnumeric():
        destino = 'Paraguay'
    elif len(cp) == 5 and cp[0:5].isnumeric():
        destino = 'Uruguay'
    else:
        destino = 'Otro'
    if destino == 'Argentina':
        if tipo == 0:
            inicial = 1100
        elif tipo == 1:
            inicial = 1800
        elif tipo == 2:
            inicial = 2450
        elif tipo == 3:
            inicial = 8300
        elif tipo == 4:
            inicial = 10900
        elif tipo == 5:
            inicial = 14300
        elif tipo == 6:
            inicial = 17900
    elif destino == 'Bolivia' or destino == 'Paraguay' or (destino == 'Uruguay' and cp[0] == '1') or (
            destino == 'Brasil' and (cp[0] == '8' or cp[0] == '9')):
        if tipo == 0:
            inicial = 1100 + (1100 * 20) // 100
        elif tipo == 1:
            inicial = 1800 + (1800 * 20) // 100
        elif tipo == 2:
            inicial = 2450 + (2450 * 20) // 100
        elif tipo == 3:
            inicial = 8300 + (8300 * 20) // 100
        elif tipo == 4:
            inicial = 10900 + (10900 * 20) // 100
        elif tipo == 5:
            inicial = 14300 + (14300 * 20) // 100
        elif tipo == 6:
            inicial = 17900 + (17900 * 20) // 100
    elif destino == 'Chile' or (destino == 'Uruguay' and cp[0] != '1') or (destino == 'Brasil' and (cp[0] == '0' \
         or cp[0] == '1' or cp[0] == '2' or cp[0] == '3')):
        if tipo == 0:
            inicial = 1100 + (1100 * 25) // 100
        elif tipo == 1:
            inicial = 1800 + (1800 * 25) // 100
        elif tipo == 2:
            inicial = 2450 + (2450 * 25) // 100
        elif tipo == 3:
            inicial = 8300 + (8300 * 25) // 100
        elif tipo == 4:
            inicial = 10900 + (10900 * 25) // 100
        elif tipo == 5:
            inicial = 14300 + (14300 * 25) // 100
        elif tipo == 6:
            inicial = 17900 + (17900 * 25) // 100
    elif destino == 'Brasil' and (cp[0] == '4' or cp[0] == '5' or cp[0] == '6' or cp[0] == '7'):
        if tipo == 0:
            inicial = 1100 + (1100 * 30) // 100
        elif tipo == 1:
            inicial = 1800 + (1800 * 30) // 100
        elif tipo == 2:
            inicial = 2450 + (2450 * 30) // 100
        elif tipo == 3:
            inicial = 8300 + (8300 * 30) // 100
        elif tipo == 4:
            inicial = 10900 + (10900 * 30) // 100
        elif tipo == 5:
            inicial = 14300 + (14300 * 30) // 100
        elif tipo == 6:
            inicial = 17900 + (17900 * 30) // 100
    elif destino == 'Otro':
        if tipo == 0:
            inicial = 1100 + (1100 * 50) // 100
        elif tipo == 1:
            inicial = 1800 + (1800 * 50) // 100
        elif tipo == 2:
            inicial = 2450 + (2450 * 50) // 100
        elif tipo == 3:
            inicial = 8300 + (8300 * 50) // 100
        elif tipo == 4:
            inicial = 10900 + (10900 * 50) // 100
        elif tipo == 5:
            inicial = 14300 + (14300 * 50) // 100
        elif tipo == 6:
            inicial = 17900 + (17900 * 50) // 100
    if pago == 2:
        final = inicial
    else:
        final = int(inicial * 0.9)
    return final



def principal():
    # resultados r2 y r3...
    cedvalid = cedinvalid = imp_acu_total = ccs = ccc = cce = cant_primer_cp = prom = 0
    porc = envios_al_exterior = 0
    envio_buenos_aires = importe_buenos_aires = 0
    valido = validosoft = False
    primer_cp = menimp = mencp = None
    menor_importe_brasil = False
    menor_importe = 0

    fd = 'envios25.txt'
    fd = 'envios100SC.txt'
    # fd = 'envios100HC.txt'
    # fd = 'envios500b.txt'


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


        if primer_cp is None:
            primer_cp = cp
        if primer_cp == cp:
            cant_primer_cp += 1

        if control == "Hard Control":
            if check_dir(direccion):
                # direccion buena...
                cedvalid += 1
                valido = True
                if valido and tipo == 0 or tipo == 1 or tipo == 2:
                    ccs += 1
                if valido and tipo == 3 or tipo == 4:
                    ccc += 1
                if valido and tipo == 5 or tipo == 6:
                    cce += 1
                if valido:
                    tipo_mayor = ordenar(ccs, ccc, cce)
                if valido:
                    importe = importe_total(cp,tipo,pago)
                    imp_acu_total += importe
            else:
                # direccion mala...
                cedinvalid += 1

                # otros cambios
                importe = importe_total(cp, tipo, pago)

                valido = False
        else:
            # es Soft control...
            cedvalid += 1
            validosoft = True
            if validosoft and tipo == 0 or tipo == 1 or tipo == 2:
                ccs += 1
            if validosoft and tipo == 3 or tipo == 4:
                ccc += 1
            if validosoft and tipo == 5 or tipo == 6:
                cce += 1
            if validosoft:
                tipo_mayor = ordenar(ccs,ccc,cce)
            if validosoft:
                importe = importe_total(cp, tipo, pago)
                imp_acu_total += importe
#Resultado 12
        if codigo_postal(cp) == 'Brasil' and ((menimp and mencp) is None or importe < menimp):
            menimp = importe
            mencp = cp
#Resultado 14
        if (valido or validosoft) and (codigo_postal(cp) == 'Argentina' and cp[0] == 'B'):
            envio_buenos_aires += 1
            importe_buenos_aires += importe
        if (valido or validosoft) and envio_buenos_aires != 0:
            prom = int(importe_buenos_aires // envio_buenos_aires)
        else:
            prom = 0

#Resultado 13
        if (valido or validosoft) and (codigo_postal(cp) != 'Argentina'):
            envios_al_exterior += 1

        if cedvalid != 0:
            total_envios = cedvalid + cedinvalid
            porc = int((envios_al_exterior * 100) /total_envios)
        else:
            porc = 0
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
