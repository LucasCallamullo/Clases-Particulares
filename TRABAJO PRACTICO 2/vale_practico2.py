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
    for i in direccion:
        if i != " " and i != ".":

            if not "A" <= i.upper() <= "Z" and not "0" <= i <= "9":
                valido = False

            # dos mayusculas seguidas
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

    for i in linea:
        # Obtener HC
        if tiene_h and i == "C":
            return "Hard Control"

        elif i == "H":
            tiene_h = True
        else:
            tiene_h = False

        # Obtener SC
        if tiene_s and i == "C":
            return "Soft Control"
        elif i == "S":
            tiene_s = True
        else:
            tiene_s = False


def calc_prom(acum_importe_bsas,  cont_env_bsas):
    prom = 0
    if cont_env_bsas > 0:
        prom = acum_importe_bsas / cont_env_bsas
    return int(prom)


def calc_porcentaje(total_env, Cant_env_exterior):
    porc = 0
    if total_env > 0:
        porc = (Cant_env_exterior * 100) / total_env
    return int(porc)


def carta_mas_enviada(cart_simple, cart_cert, cart_expresa):
    if cart_simple > cart_cert and cart_simple > cart_expresa:
        mayor_envio = "Carta Simple"
    elif cart_cert > cart_expresa:
        if cart_cert == cart_simple:
            mayor_envio = "Carta Simple"
        else:
            mayor_envio = "Carta Certificada"
    else:
        if cart_expresa == cart_simple:
            mayor_envio = "Carta Simple"
        elif cart_expresa == cart_cert:
            mayor_envio = cart_cert
        else:
            mayor_envio = "Carta Expresa"
    return mayor_envio


def obtener_primercp(cp, primer_cp):
    cant_primer_cp = 0
    # r9
    if primer_cp is None:
        primer_cp = cp
    # r10
    if cp == primer_cp:
        cant_primer_cp += 1

    return primer_cp, cant_primer_cp


def principal():
    fd = "envios.txt"
    # fd = "envios25.txt"
    # fd = "envios100HC.txt"
    # fd = "envios100SC.txt"
    # fd = "envios500b.txt"
    m = open(fd, "rt")

    # Punto 1
    cont_lineas = 0
    control = ""

    # Punto 2 / Punto 3
    cedvalid = 0
    cedinvalid = 0

    # Punto 4
    imp_acu_total = 0
    cart_simple = 0
    cart_cert = 0
    cart_expresa = 0
    menor_import = None
    codigop_brasil = None
    Cant_env_exterior = 0
    primer_cp = None
    cant_primer_cp = 0
    cont_env_bsas= 0
    acum_importe_bsas = 0

    for linea in m:
        cont_lineas += 1

        if cont_lineas == 1:
            control = analizar_hc_sc(linea)  #

        else:
            # Datos direcciones
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
                    # P2
                    cedvalid += 1

                    # P4
                    importe = calcular_importe(destino, tipo_envio, cp, forma_pago)
                    imp_acu_total += importe

                    if tipo_envio == 0 or tipo_envio == 1 or tipo_envio == 2:
                        cart_simple += 1

                    elif tipo_envio == 3 or tipo_envio == 4:
                        cart_cert += 1

                    elif tipo_envio == 5 or tipo_envio == 6:
                        cart_expresa += 1

                    if destino != "Argentina":
                        Cant_env_exterior += 1

                    if destino == "Argentina" and cp[0] == "B":
                        cont_env_bsas += 1
                        acum_importe_bsas += importe

                # Direc NO Valida
                else:
                    # P3
                    cedinvalid += 1

                    # P10
                    importe = calcular_importe(destino, tipo_envio, cp, forma_pago)

            # Estoy en Soft Control
            else:

                # P2
                cedvalid += 1

                # P4
                importe = calcular_importe(destino, tipo_envio, cp, forma_pago)
                imp_acu_total += importe

                if tipo_envio == 0 or tipo_envio == 1 or tipo_envio == 2:
                    cart_simple += 1

                elif tipo_envio == 3 or tipo_envio == 4:
                    cart_cert += 1

                elif tipo_envio == 5 or tipo_envio == 6:
                    cart_expresa += 1

                if destino != "Argentina":
                    Cant_env_exterior += 1

                if destino == "Argentina" and cp[0] == "B":
                    cont_env_bsas += 1
                    acum_importe_bsas += importe

                # 11 y 12
            if destino == "Brasil":
                if menor_import is None or importe < menor_import:
                    menor_import = importe
                    codigop_brasil = cp

            primer_cp, aparece_cp = obtener_primercp(cp, primer_cp)
            cant_primer_cp += aparece_cp

    mayor_envio = carta_mas_enviada(cart_simple, cart_cert, cart_expresa)
    total_env = cedvalid + cedinvalid
    porc = calc_porcentaje(total_env, Cant_env_exterior)
    prom = calc_prom(acum_importe_bsas, cont_env_bsas)

    # =================================================================
    #                          RESULTADOS
    # =================================================================
    print(' (r1) - Tipo de control de direcciones:', control)
    print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
    print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
    print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
    print(' (r5) - Cantidad de cartas simples:', cart_simple)
    print(' (r6) - Cantidad de cartas certificadas:', cart_cert)
    print(' (r7) - Cantidad de cartas expresas:', cart_expresa)
    print(' (r8) - Tipo de carta con mayor cantidad de envios:', mayor_envio)
    print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp)
    print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
    print('(r11) - Importe menor pagado por envios a Brasil:', menor_import)
    print('(r12) - Codigo postal del envio a Brasil con importe menor:', codigop_brasil)
    print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
    print('(r14) - Importe final promedio de los envios Buenos Aires:', prom)


if __name__ == "__main__":
    principal()