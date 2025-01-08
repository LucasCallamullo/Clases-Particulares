# =================================================================
#                          PUNTO 14
# =================================================================
def calcular_promedio(r14_acum_importes, r14_cont_importes):
    # Promedio = Suma de cosass (un acumulador) // cantidad de cosas que sumamos (contador)
    prom = 0
    if r14_cont_importes > 0:
        prom = r14_acum_importes / r14_cont_importes
    return int(prom)


def validar_provincia(subcadena_cp):
    if subcadena_cp[0] == "B":
        return True
    return False


# =================================================================
#                          PUNTO 13
# =================================================================
def calcular_porcentaje(r13_cont_total_exterior, r13_cont_total_envios):
    #   Cont_Total  ---- 100
    #   Cont_algo   ---- x = cont_algo * 100 / cont_total
    porc = 0
    if r13_cont_total_exterior > 0:
        porc = (r13_cont_total_exterior * 100) / r13_cont_total_envios
    return int(porc)


# =================================================================
#                          PUNTO 8
# =================================================================
def validar_tipo_carta_mayor(ccs, ccc, cce):
    if ccs >= ccc and ccs >= cce:
        cadena = "Carta Simple"
    elif ccc > ccs and ccc >= cce:
        cadena = "Carta Certifcada"
    else:
        cadena = "Carta Expresa"
    return cadena


# =================================================================
#                          PUNTO 5, 6, 7
# =================================================================
def validar_tipo_carta(tipo_envio):
    if 0 <= tipo_envio <= 2:
        ccs_suma, ccc_suma, cce_suma = 1, 0, 0
    elif 3 <= tipo_envio <= 4:
        ccs_suma, ccc_suma, cce_suma = 0, 1, 0
    # elif 5 <= tipo_envio <= 6:
    else:
        ccs_suma, ccc_suma, cce_suma = 0, 0, 1
    return ccs_suma, ccc_suma, cce_suma


# =================================================================
#                          PUNTO 4
# =================================================================
def calcular_importe(imp, forma_pago, porc):
    # imp = imp + (imp * porc / 100)
    imp += (imp * porc) / 100

    if forma_pago == 1:
        imp -= (imp * 10) / 100

    return int(imp)


def calcular_porcentaje_pais_region(subcadena_cp, cod_postal):
    # uruguay montevideo
    if (cod_postal == 4 and subcadena_cp[0] == "1") or cod_postal == 3 or cod_postal == 5:
        porc = 20

    elif cod_postal == 4 or cod_postal == 2:
        porc = 25

    # elif cod_postal == 0 and (subcadena_cp[0] == "8" or subcadena_cp[0] == "9"):
    elif cod_postal == 0 and subcadena_cp[0] in "89":
        porc = 20

    # elif cod_postal == 0 and ("0" <= subcadena_cp[0] <= "3"):
    elif cod_postal == 0 and subcadena_cp[0] in "0123":
        porc = 25

    # elif cod_postal == 0 and ("4" <= subcadena_cp[0] <= "7"):
    elif cod_postal == 0 and subcadena_cp[0] in "4567":
        porc = 30

    else:
        porc = 50
    return porc

def obtener_cp_pais(subcadena_cp):
    # Brasil = 0
    if subcadena_cp[5:6] == "-" and subcadena_cp[:5].isdigit() and subcadena_cp[6:9].isdigit():
        return 0

    # Argentina = 1
    elif subcadena_cp[:1].isalpha() and subcadena_cp[1:5].isdigit() and subcadena_cp[5:8].isalpha() and len(
            subcadena_cp) == 8:
        return 1

    # Chile
    elif subcadena_cp[:7].isdigit() and len(subcadena_cp) == 7:
        return 2

    # Paraguay
    elif subcadena_cp[:6].isdigit() and len(subcadena_cp) == 6:
        return 3

    # Uruguay
    elif subcadena_cp[:5].isdigit() and len(subcadena_cp) == 5:
        return 4

    # Bolivia
    elif subcadena_cp[:4].isdigit() and len(subcadena_cp) == 4:
        return 5

    else:
        return 6


def precio_tipo_envio(tipo_envio):
    #                   0       1       2   3   4       5       6
    lista_importes = [1100, 1800, 2450, 8300, 10900, 14300, 17900]
    return lista_importes[tipo_envio]


# =================================================================
#                          PUNTO 2 y 3
# =================================================================
def validar_direccion(cadena):
    digitos = "0123456789"
    has_mayus = False
    no_cumple = False
    palabra_solo_numeros = False

    for i in cadena:
        # estamos dentro de una palabra
        if i != " " and i != ".":
            # tiene dos mayusculas seguidas
            if has_mayus and "A" <= i <= "Z":
                no_cumple = True
                break

            else:
                has_mayus = False

            if "A" <= i <= "Z":
                has_mayus = True

            # para verificar qeu sean solo numeros y letras
            if not "a" <= i.lower() <= "z" and not "0" <= i <= "9":
                no_cumple = True
                break

            # que toda la pabra sean numeros
            if i in digitos:
                palabra_solo_numeros = True

            if palabra_solo_numeros:
                if i not in digitos:
                    no_cumple = True
                    break

        else:
            # termino una palabra
            pass

    if no_cumple:
        return False

    return True


# =================================================================
#                          PUNTO 1
# =================================================================
def obtener_hc_sc(linea):
    has_h = False
    has_s = False
    has_hc = False
    has_sc = False

    #
    # "–1HC8:15–-10/06/2020"
    for i in linea:
        # H, 8, C, -, 1, 8, :,

        # i.lower() = H  --> h
        if i.lower() == "h":
            has_h = True

        elif i.lower() == "c" and has_h:
            has_hc = True
            break

        else:
            has_h = False

        # caso de obtener SC
        if i.lower() == "s":
            has_s = True

        elif i.lower() == "c" and has_s:
            has_sc = True
            break

        else:
            has_s = False

    if has_hc:
        return True

    if has_sc:
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
    ccs = 0
    ccc = 0
    cce = 0

    # r9 / r10
    primer_cp = None
    cant_primer_cp = 0

    # r11 / r12
    menimp = None
    mencp = None

    # r13
    r13_cont_total_envios = 0
    r13_cont_total_exterior = 0

    # r14
    r14_acum_importes = 0
    r14_cont_importes = 0


    # archivo = 'envios25.txt'
    archivo = 'envios100SC.txt'
    # archivo = 'envios100HC.txt'
    m = open(archivo, 'r')

    for linea in m:

        if primera_linea:
            primera_linea = False
            linea_limpia = linea.strip()

            # Para saber si estamos leyendo un HC(True) o SC(False)
            bandera_HC = obtener_hc_sc(linea_limpia)  # True o False

            if bandera_HC:
                control = "Hard Control"

            else:
                control = "Soft Control"

        else:

            # Obtener la subcadena del índice 0 al 8 que correspondeal codigo postal
            subcadena_cp = linea[0:9].strip()

            # Devuelve el pais segun un numero asignado (ver funcion para cada asignacion) (int)
            cod_postal = obtener_cp_pais(subcadena_cp)

            # obtener la subcadena indice 9:28 a la direccion
            subcadena_direcc = linea[9:29].rstrip()

            # obtener el caracter 29 que es el tipo de envio del 0 al 6 en str lo paso a int
            tipo_envio = int(linea[29:30])

            # obtener el caracter 30 que es la forma de pago 1-efectivo ; 2-tarjeta, # descuento 10% para efectivo
            forma_pago = int(linea[30:31])

            # Hard Control
            if bandera_HC:
                es_valida_la_direccion = validar_direccion(subcadena_direcc)  # True o False

                if es_valida_la_direccion:
                    # r2
                    cedvalid += 1

                    # r4
                    # Porcentaje de Argentina era 0 ; su codigo postal = 1
                    if cod_postal == 1:
                        porc = 0
                    else:
                        porc = calcular_porcentaje_pais_region(subcadena_cp, cod_postal)

                    precio_envio = precio_tipo_envio(tipo_envio)
                    importe = calcular_importe(precio_envio, forma_pago, porc)
                    imp_acu_total += importe

                    # r5 / r6 / r7
                    ccs_suma, ccc_suma, cce_suma = validar_tipo_carta(tipo_envio)
                    ccs += ccs_suma     # 1
                    ccc += ccc_suma     # 0
                    cce += cce_suma     # 0

                    # r13
                    if cod_postal != 1:
                        r13_cont_total_exterior += 1

                    # r14
                    es_bs_as = validar_provincia(subcadena_cp)      # return True o False, dependiendo si es bs as o no
                    if es_bs_as and cod_postal == 1:
                        r14_cont_importes += 1
                        r14_acum_importes += importe

                else:
                    # r2
                    cedinvalid += 1

                    # r10 / r11 , nos sirve para hacer el calcula del importe que nos pide para este punto
                    if cod_postal == 1:
                        porc = 0
                    else:
                        porc = calcular_porcentaje_pais_region(subcadena_cp, cod_postal)

                    precio_envio = precio_tipo_envio(tipo_envio)
                    importe = calcular_importe(precio_envio, forma_pago, porc)

            # Soft Control
            else:
                # r2
                cedvalid += 1

                # r4
                if cod_postal == 1:
                    porc = 0
                else:
                    porc = calcular_porcentaje_pais_region(subcadena_cp, cod_postal)

                precio_envio = precio_tipo_envio(tipo_envio)
                importe = calcular_importe(precio_envio, forma_pago, porc)
                imp_acu_total += importe

                # r5 / r6 / r7
                ccs_suma, ccc_suma, cce_suma = validar_tipo_carta(tipo_envio)
                ccs += ccs_suma  # 1
                ccc += ccc_suma  # 0
                cce += cce_suma  # 0

                # r13
                if cod_postal != 1:
                    r13_cont_total_exterior += 1

                # r14
                es_bs_as = validar_provincia(subcadena_cp)  # return True o False, dependiendo si es bs as o no
                if es_bs_as and cod_postal == 1:
                    r14_cont_importes += 1
                    r14_acum_importes += importe

            # Aca estamos fuera de HC O SC
            # r9 / r10
            if primer_cp is None:
                primer_cp = subcadena_cp
                cant_primer_cp += 1
            else:
                if primer_cp == subcadena_cp:
                    cant_primer_cp += 1

            # r11 / r12
            if cod_postal == 0:     # o sea Brasil
                if menimp is None or importe < menimp:
                    menimp = importe
                    mencp = subcadena_cp

            # r13
            r13_cont_total_envios += 1

    # FUERA DEL CICLO FOR
    tipo_mayor = validar_tipo_carta_mayor(ccs, ccc, cce)

    # r13
    porc = calcular_porcentaje(r13_cont_total_exterior, r13_cont_total_envios)

    # r14
    prom = calcular_promedio(r14_acum_importes, r14_cont_importes)

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
    m.close()


if __name__ == '__main__':
    main()