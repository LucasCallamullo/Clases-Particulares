# =================================================================
#                          PUNTO 14
# =================================================================
def calcular_promedio(acum_imp_14, cont_imp_14):
    prom = 0
    if cont_imp_14 > 0:
        prom = int(acum_imp_14 / cont_imp_14)
    return prom


def validar_provincia(subcadena_cp):
    if subcadena_cp[0] == "B":
        return True
    return False


# =================================================================
#                          PUNTO 13
# =================================================================
def calcular_porcentaje(cont_inter_13, cont_total_13):
    porc = 0
    if cont_total_13 > 0:
        porc = (cont_inter_13 * 100) / cont_total_13
    return int(porc)


# =================================================================
#                          PUNTO 8
# =================================================================
def obtener_tipo_mayor(ccs, ccc, cce):
    if ccs >= ccc and ccs >= cce:
        tipo_mayor = "Carta Simple"

    elif ccc > ccs and ccc >= cce:
        tipo_mayor = "Carta Certificada"

    else:
        tipo_mayor = "Carta Expresa"

    return tipo_mayor


# =================================================================
#                          PUNTO 5 , 6, 7
# =================================================================
def contadores_cartas(tipo_envio):
    ccs, ccc, cce = 0, 0, 0
    if 0 <= tipo_envio <= 2:
        ccs += 1
    elif 3 <= tipo_envio <= 4:
        ccc += 1
    elif 5 <= tipo_envio <= 6:
        cce += 1
    return ccs, ccc, cce


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


def obtener_cod_postal_pais(cadena):
    n = len(cadena)
    if cadena[0:5].isdigit() and cadena[5:6] == "-" and cadena[6:9].isdigit():
        return "Brasil"

    elif cadena[0:1].isalpha() and cadena[1:5].isdigit() and cadena[5:8].isalpha() and n == 8 and (cadena[0] != 'I' and cadena[0] != 'O'):
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


# =================================================================
#                          PUNTO 2 y 3
# =================================================================



def validar_direccion(cadena):
    has_mayus = False
    palabra_solo_numeros = False

    for i in cadena:
        # estamos dentro de una palabra
        if i != " " and i != ".":
            # tiene dos mayusculas seguidas
            if has_mayus and "A" <= i <= "Z":
                return False

            elif "A" <= i <= "Z":
                has_mayus = True

            else:
                has_mayus = False

            # para verificar que sean solo numeros y letras
            if not "a" <= i.lower() <= "z" and not "0" <= i <= "9":
                return False

            # que toda la pabra sean numeros
            if i.isdigit():
                palabra_solo_numeros = True

            if palabra_solo_numeros:
                if not i.isdigit():
                    return False

    return True


# =================================================================
#                          PUNTO 1
# =================================================================
def obtener_hc_sc(linea):
    has_h = False
    has_s = False

    for i in linea:
        car = i.lower()
        # caso de obtener HC
        if car == "h":
            has_h = True
        # caso de obtener SC
        elif car == "s":
            has_s = True

        elif car == "c" and has_h:
            return True

        elif car == "c" and has_s:
            return False

        else:
            has_h = False
            has_s = False

    return False


def main():
    # r1
    primera_linea = True

    # r2
    cedvalid = 0

    # r3
    cedinvalid = 0

    # r4
    imp_acu_total = 0

    # r5 / r6 / r7
    ccs, ccc, cce = 0, 0, 0

    # r9 / r10
    primer_cp = None
    cant_primer_cp = 0

    # r11 / r12
    menimp = None
    mencp = None

    # r13
    cont_total_13, cont_inter_13 = 0, 0

    # r14
    acum_imp_14, cont_imp_14 = 0, 0

    archivo = 'envios25.txt'
    # archivo = 'envios100SC.txt'
    # archivo = 'envios100HC.txt'
    archivo = 'envios500b.txt'
    m = open(archivo, 'r')

    for linea in m:
        if primera_linea:
            primera_linea = False
            linea_limpia = linea.strip()

            # Devuelve True para HC / Devuelve False para SC
            bandera_HC = obtener_hc_sc(linea_limpia)
            if bandera_HC:
                control = "Hard Control"
            else:
                control = "Soft Control"

        else:
            # Obtener la subcadena del índice 0 al 8 que correspondeal codigo postal
            subcadena_cp = linea[0:9].strip()

            # Devuelve el pais segun un numero asignado (ver funcion para cada asignacion)
            cod_postal = obtener_cod_postal_pais(subcadena_cp)

            # obtener la subcadena indice 9:28 a la direccion
            subcadena_direcc = linea[9:29].rstrip()

            # obtener el caracter 29 que es el tipo de envio del 0 al 6 en str lo paso a int
            tipo_envio = int(linea[29:30])

            # obtener el caracter 30 que es la forma de pago 1- efectivo ; 2- tarjeta, # descuento 10% para efectivo
            forma_pago = int(linea[30:31])

            # HARD CONTROL
            if bandera_HC:
                # Devuelve True si es valida la direccion, devuelve False si no es valida
                es_valida_la_direccion = validar_direccion(subcadena_direcc)
                if es_valida_la_direccion:
                    # r2
                    cedvalid += 1

                    # r4
                    importe = calcular_importe(cod_postal, tipo_envio, subcadena_cp, forma_pago)
                    imp_acu_total += importe

                    # r5 / r6 / r7
                    ccs_dato, ccc_dato, cce_dato = contadores_cartas(tipo_envio)
                    ccs += ccs_dato
                    ccc += ccc_dato
                    cce += cce_dato

                    # r13
                    if cod_postal != "Argentina":
                        cont_inter_13 += 1

                    # r14 - se puede hacer bloque if else, pero solo fue otro if para comentar mejor el archivo
                    if cod_postal == "Argentina":
                        es_prov_bsas = validar_provincia(subcadena_cp)
                        if es_prov_bsas:
                            cont_imp_14 += 1
                            acum_imp_14 += importe

                # direccion no validas en HC
                else:
                    # r2
                    cedinvalid += 1

                    # r11 / r12
                    # duda hay que hacer un nuevo importe? porque los hc no validos tienen importes pero no serian validos..?
                    importe = calcular_importe(cod_postal, tipo_envio, subcadena_cp, forma_pago)

            # SOFT CONTROL
            else:
                # r2
                cedvalid += 1

                # r4
                importe = calcular_importe(cod_postal, tipo_envio, subcadena_cp, forma_pago)
                imp_acu_total += importe

                # r5 / r6 / r7
                ccs_dato, ccc_dato, cce_dato = contadores_cartas(tipo_envio)
                ccs += ccs_dato
                ccc += ccc_dato
                cce += cce_dato

                # r13
                if cod_postal != "Argentina":
                    cont_inter_13 += 1

                # r14 - se puede hacer bloque if else, pero solo fue otro if para comentar mejor el archivo
                if cod_postal == "Argentina":
                    es_prov_bsas = validar_provincia(subcadena_cp)
                    if es_prov_bsas:
                        cont_imp_14 += 1
                        acum_imp_14 += importe

            # Indpendientemente de si es valida o no la direccion. es decir fuera de HC o SC
            # r9 / r10
            if primer_cp is None:
                primer_cp = subcadena_cp
                cant_primer_cp += 1
            else:
                if primer_cp == subcadena_cp:
                    cant_primer_cp += 1

            # r11 / r12
            if cod_postal == "Brasil":
                if menimp is None:
                    menimp = importe
                    mencp = subcadena_cp
                elif importe < menimp:
                    menimp = importe
                    mencp = subcadena_cp

            # r13
            cont_total_13 += 1

    # Fuera del ciclo for, es decir una vez tenemos todos los contadores totalizados
    m.close()

    # r5 / r6 / r7
    tipo_mayor = obtener_tipo_mayor(ccs, ccc, cce)

    # r13
    porc = calcular_porcentaje(cont_inter_13, cont_total_13)

    # r14
    prom = calcular_promedio(acum_imp_14, cont_imp_14)

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
    main()
