

# Punto 14
def calc_promedio(acum_importe_BA, cont_envios_BA):
    prom = 0
    if cont_envios_BA > 0:
        prom = acum_importe_BA / cont_envios_BA
    return int(prom)


# Punto 13
def calc_porcentaje(cant_envios_totales, cont_envios_exterior):
    porc = 0
    if cant_envios_totales > 0:
        porc = (cont_envios_exterior * 100) / cant_envios_totales
    return int(porc)


# Punto 8
def calc_tipo_carta_mayor(ccs, ccc, cce):
    if ccs >= ccc and ccs >= cce:
        return "Carta Simple"
    if ccc >= cce and ccc > ccs:
        return "Carta Certificada"
    if cce > ccc and cce > ccs:
        return "Carta Expresa"


# Punto 4 - Funcion Valerio TP1
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
    tamanio = len(cadena)
    if cadena[0:5].isdigit() and cadena[5:6] == "-" and cadena[6:9].isdigit():
        return "Brasil"
    elif cadena[0].isalpha() and cadena[1:5].isdigit() and cadena[5:8].isalpha() and tamanio == 8 and cadena[0] != 'I' and cadena[0] != 'O':
        return "Argentina"
    elif cadena[0:4].isdigit() and tamanio == 4:
        return "Bolivia"
    elif cadena[0:5].isdigit() and tamanio == 5:
        return "Uruguay"
    elif cadena[0:6].isdigit() and tamanio == 6:
        return "Paraguay"
    elif cadena[0:7].isdigit() and tamanio == 7:
        return "Chile"
    else:
        return "Otro"


# Punto 2
def validar_direccion(direccion):
    tiene_mayuscula = False
    for i in direccion:
        if i != " " and i != ".":
            if not "a" <= i.lower() <= "z" and not "0" <= i <= "9":
                return False            # no cumple

            # para detectar dos mayusculas seguidas
            if tiene_mayuscula and "A" <= i <= "Z":
                return False
            elif "A" <= i <= "Z":
                tiene_mayuscula = True
            else:
                tiene_mayuscula = False
    return True


# Punto 1
def r1_analizar_timestap(linea):
    tiene_h = False
    tiene_s = False

    for i in linea:
        # para detectar HC
        if i.lower() == "h":          # convierte al caracter en minuscula
            tiene_h = True
        elif tiene_h and i.lower() == "c":
            return "Hard Control"
        else:
            tiene_h = False

        # para detectar SC
        if i.lower() == "s":  # convierte al caracter en minuscula
            tiene_s = True
        elif tiene_s and i.lower() == "c":
            return "Soft Control"
        else:
            tiene_s = False


def principal():

    archivo = "envios.txt"
    # archivo = "envios25.txt"
    # archivo = "envios100HC.txt"
    # archivo = "envios100SC.txt"

    m = open(archivo, "rt")         # read text , leer texto

    # Punto 1
    contador_lineas = 0
    control = ""

    # Punto 2 / Punto 3
    cedvalid = 0
    cedinvalid = 0

    # Punto 4
    imp_acu_total = 0

    # Punto 5 / 6 / 7
    ccs, ccc, cce = 0, 0, 0

    # Punto 9 / 10
    primer_cp = None
    cant_primer_cp = 0

    # Punto 11 / Punto 12
    menimp = None
    mencp = None

    # Punto 13
    cont_envios_exterior = 0

    # Punto 14
    cont_envios_BA = 0
    acum_importe_BA = 0

    for linea in m:
        # Punto 1
        contador_lineas += 1

        # Analizar TimeStap
        if contador_lineas == 1:
            # Punto 1
            control = r1_analizar_timestap(linea)   # "Hard Control" o "Soft Control"

        # Analizar direcciones
        else:
            cp = linea[0:9].strip()
            destino = obtener_cp_pais(cp)
            direccion = linea[9:29].rstrip()
            tipo = int(linea[29])
            pago = int(linea[30])

            # Estoy en Hard Control
            if control == "Hard Control":
                # Punto 2
                es_direccion_valida = validar_direccion(direccion)

                if es_direccion_valida:
                    # Punto 2
                    cedvalid += 1

                    # Punto 4
                    importe = calcular_importe(destino, tipo, cp, pago)
                    imp_acu_total += importe

                    # Punto 5 / 6 / 7
                    if 0 <= tipo <= 2:
                        ccs += 1
                    elif 3 <= tipo <= 4:
                        ccc += 1
                    elif 5 <= tipo <= 6:
                        cce += 1

                    # Punto 13
                    if destino != "Argentina":
                        cont_envios_exterior += 1

                    # Punto 14
                    if destino == "Argentina" and cp[0] == "B":
                        cont_envios_BA += 1
                        acum_importe_BA += importe

                # Direccion NO Valida
                else:
                    # Punto 3
                    cedinvalid += 1

                    # Punto 9 / Punto 10
                    importe = calcular_importe(destino, tipo, cp, pago)

            # Estoy en Soft Control
            else:
                # Punto 2 / Punto 3
                cedvalid += 1

                # Punto 4
                importe = calcular_importe(destino, tipo, cp, pago)
                imp_acu_total += importe

                # Punto 5 / 6 / 7
                if 0 <= tipo <= 2:
                    ccs += 1
                elif 3 <= tipo <= 4:
                    ccc += 1
                elif 5 <= tipo <= 6:
                    cce += 1

                # Punto 13
                if destino != "Argentina":
                    cont_envios_exterior += 1

                # Punto 14
                if destino == "Argentina" and cp[0] == "B":
                    cont_envios_BA += 1
                    acum_importe_BA += importe

            # Fuera de HC y SC
            # r9 / r10
            if primer_cp is None:
                primer_cp = cp
                cant_primer_cp += 1
            else:
                if primer_cp == cp:
                    cant_primer_cp += 1

            # Punto 11 / Punto 12
            if destino == "Brasil":
                if menimp is None or importe < menimp:
                    menimp = importe
                    mencp = cp

    # Salimos del archivo
    m.close()

    # Respuesta 8
    tipo_mayor = calc_tipo_carta_mayor(ccs, ccc, cce)

    # Respuesta 13
    cant_envios_totales = cedvalid + cedinvalid
    porc = calc_porcentaje(cant_envios_totales, cont_envios_exterior)

    # Respuesta 14
    prom = calc_promedio(acum_importe_BA, cont_envios_BA)

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


if __name__ == '__main__':
    principal()