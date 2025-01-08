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
    n = len(cp)
    if cp[0:5].isdigit() and cp[5:6] == "-" and cp[6:9].isdigit():
        return "Brasil"

    elif cp[0].isalpha() and cp[1:5].isdigit() and cp[5:8].isalpha() and n == 8 and cp[0] != 'I' and cp[0] != 'O':
        return "Argentina"

    elif cp[0:7].isdigit() and n == 7:
        return "Chile"

    elif cp[0:6].isdigit() and n == 6:
        return "Paraguay"

    elif cp[0:5].isdigit() and n == 5:
        return "Uruguay"

    elif cp[0:4].isdigit() and n == 4:
        return "Bolivia"

    else:
        return "Otro"

def tipo_control(primera_linea):
    control = None
    FH = False
    FS = False
    for linea in primera_linea:
        if linea == 'H':
            FH = True
        elif linea == 'C' and FH:
            control = 'Hard Control'
            FH = False
        elif linea == 'S':
            FS = True
        elif linea == 'C' and FS:
            control = 'Soft Control'
            FS = False
    return control



# r5, 6 y 7
def tipo_carta(lineas):
    if lineas[29] in ['0', '1', '2']:
        return 'ccs'
    elif lineas[29] in ['3', '4']:
        return 'ccc'
    elif lineas[29] in ['5', '6']:
        return 'cce'

# r8
def mayor_cantidad_de_envios(ccs, ccc, cce):
    # Función para determinar el tipo de carta con mayor cantidad de envíos
    if ccs >= ccc and ccs >= cce:
        return 'Cartas Simples'
    elif ccc >= ccs and ccc >= cce:
        return 'Cartas Certificadas'
    else:
        return 'Cartas Expresas'


def actualizar_menor_importe_brasil(menimp, mencp, final, cp):
    if menimp is None or final < menimp:
        return final, cp
    return menimp, mencp


def validar_direcciones(direccion):
    mayuscula = False
    valida = True
    for car in direccion:
        if car != " " and car != ".":
            if 'A' <= car <= 'Z':
                if mayuscula:
                    valida = False
                    break
                mayuscula = True
            else:
                mayuscula = False

            if not 'a' <= car.lower() <= 'z' and not '0' <= car <= '9':
                valida = False
                break
    # if valida and (any(car.isalpha() for car in direccion)):
    return valida


def principal():
    # m = open("envios.txt", "rt")
    # m = open('envios25.txt', 'rt')
    # m = open('envios100HC.txt', 'rt')
    # m = open('envios100SC.txt', 'rt')
    m = open('envios500b.txt', 'rt')
    primera_linea = m.readline()
    control = tipo_control(primera_linea)  # Determina el tipo de control desde la primera línea
    cedvalid = 0
    cedinvalid = 0
    primer_cp = None
    cant_primer_cp = 0
    ccs = 0
    ccc = 0
    cce = 0
    imp_acu_total = 0
    menimp = None
    mencp = None
    total_envios = 0
    envios_exterior = 0
    acum_importe_ba = 0
    cant_envios_ba = 0
    lineas = m.readline()

    while lineas:

        total_envios += 1

        cp = lineas[0:9].strip()
        destino = obtener_destino_pais(cp)
        direccion = lineas[9:29].rstrip()
        tipo = int(lineas[29])
        pago = int(lineas[30])
        final = calcular_importe(destino, tipo, cp, pago)

        if not primer_cp:
            primer_cp = lineas[:9].strip()

        if primer_cp in lineas:
            cant_primer_cp += 1

        # Hard Control
        if control == 'Hard Control':

            es_direccion_valida = validar_direcciones(direccion)
            # Direccion Valida
            if es_direccion_valida:
                cedvalid += 1

                tipo = tipo_carta(lineas)
                if tipo == 'ccs':
                    ccs += 1
                elif tipo == 'ccc':
                    ccc += 1
                elif tipo == 'cce':
                    cce += 1

                imp_acu_total += final

                if destino != 'Argentina':
                    envios_exterior += 1

                if destino == "Argentina" and cp[0] == "B":
                    cant_envios_ba += 1
                    acum_importe_ba += final

            # Direccion NO Valida
            else:
                cedinvalid += 1

        # Soft Control
        else:
            cedvalid += 1
            tipo = tipo_carta(lineas)
            if tipo == 'ccs':
                ccs += 1
            elif tipo == 'ccc':
                ccc += 1
            elif tipo == 'cce':
                cce += 1

            imp_acu_total += final

            if destino != 'Argentina':
                envios_exterior += 1

            if destino == "Argentina" and cp[0] == "B":
                cant_envios_ba += 1
                acum_importe_ba += final

        if destino == 'Brasil':
            menimp, mencp = actualizar_menor_importe_brasil(menimp, mencp, final, cp)

        lineas = m.readline()
    m.close()
    tipo_mayor = mayor_cantidad_de_envios(ccs, ccc, cce)
    porc = int((envios_exterior / total_envios) * 100)
    if cant_envios_ba != 0:
        prom = int(acum_importe_ba / cant_envios_ba)
    else:
        prom = 0

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