
def porcentaje(total, envios_internacionales):
    porcent = 0
    if total > 0:
        porcent = (envios_internacionales * 100) / total
    return porcent
def calcular_promedio(acum, cont):
    promedio = 0
    if cont > 0:
        promedio = acum / cont
    return promedio
def mayor_cantidad_de_cartas(ccs, ccc, cce):
    if ccs >= ccc and ccs >= cce:
        mayor = "Carta Simple"
    elif ccc >= ccs and ccc >= cce:
        mayor = "Carta Certificada"
    else:
        mayor = "Carta Expresa"
    return mayor


def cantidad_cartas_por_tipo_envio(tipo_envio):
    cant_cs = cant_cc = cant_ce = 0
    if 0 <= tipo_envio <= 2:
        cant_cs = 1, 0, 0
    elif 3 <= tipo_envio <= 4:
        cant_cc = 0, 1, 0
    elif 5 <= tipo_envio <= 6:
        cant_ce = 0, 0, 1

    return cant_cs, cant_cc, cant_ce

#Punto 4
def importe_por_destino_mas_porcentaje(destino, tipo, cp, pago):
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


def obtener_cod_postal_pais(cp):
    long_cp = len(cp)
    if cp[0:5].isdigit() and cp[5:6] == "-" and cp[6:9].isdigit():
        return "Brasil"

    elif cp[0:1].isalpha() and cp[1:5].isdigit() and cp[5:8].isalpha() and long_cp == 8 and cp[0] != 'I' and cp[
        0] != 'O':
        return "Argentina"

    elif cp[0:4].isdigit() and long_cp == 4:
        return "Bolivia"

    elif cp[0:5].isdigit() and long_cp == 5:
        return "Uruguay"

    elif cp[0:6].isdigit() and long_cp == 6:
        return "Paraguay"

    elif cp[0:7].isdigit() and long_cp == 7:
        return "Chile"

    else:
        return "Otro"


# Punto 2
def validar_direcciones(direccion):
    mayus = "ABCDEFGHIJKLOMNÑOPQRSTUVWXYZ"
    digitos = "0123456789"
    tenemos_mayus = False
    tenemos_num = False

    for i in direccion:

        if i != " " and i != ".":

            if not i.upper() in "0123456789ABCDEFGHIJKLOMNÑOPQRSTUVWXYZ":
                return False

            if i in mayus and tenemos_mayus:
                return False
            elif i in mayus:
                tenemos_mayus = True
            else:
                tenemos_mayus = False

            # tiene un solo digito
            if i in digitos:
                tenemos_num = True

            if tenemos_num and i not in digitos:
                return False

        # termina la palabra
        else:
            tenemos_num = False
            tenemos_mayus = False

    return True

#Punto 1
def validar_control(linea):

    tenemos_h = False
    tenemos_hc = False
    tenemos_s = False

    for car in linea:

        if car != " " and car != ".":

            if car == "H":
                tenemos_h = True

            elif car == "S":
                tenemos_s = True

            elif car == "C" and tenemos_s:
                tenemos_hc = False

            elif car == "C" and tenemos_h:
                tenemos_hc = True

            else:
                tenemos_h = False
                tenemos_s = False

        # estamos fuera de una palabra
        else:
            tenemos_h = False

    if tenemos_hc:
        return "Hard Control"

    else:
        return "Soft Control"



def principal():

    archivo = "envios.txt"
    # archivo = "envios100HC.txt"
    # archivo = "envios25.txt"
    # archivo = "envios100HC.txt"
    # archivo = "envios100SC.txt"

    m = open(archivo, "rt")

    contadorLinea = 0
    control = ""

    cedvalid = 0
    cedinvalid = 0
    ccs = ccc = cce = 0
    tipo_mayor = None
    imp_acu_total = 0
    primer_cp = None
    importe = 0
    cant_primer_cp = 0
    menimp = None
    mencp = None
    envios_b = 0
    importes_b = 0
    envios_exterior = 0
    prom = porc = 0

    for linea in m:

        contadorLinea += 1
        if contadorLinea == 1:
            control = validar_control(linea)

        else:

            # Codigo postal
            cad_cod_postal = linea[0:9].strip()

            pais_destino = obtener_cod_postal_pais(cad_cod_postal)

            # Direccion
            direccion = linea[9:29].rstrip()

            #Tipo de envio del 0 al 6 en str lo paso a int
            tipo_envio = int(linea[29:30])

            # Forma de pago 1-efectivo ; 2-tarjeta, # descuento 10% para efectivo
            forma_pago = int(linea[30:31])

            #HC
            if control == "Hard Control":
                es_direcc_valida = validar_direcciones(direccion)  # return True es valida, si es False no es valida

                if es_direcc_valida:

                    cedvalid += 1

                    importe = importe_por_destino_mas_porcentaje(pais_destino, tipo_envio, cad_cod_postal, forma_pago)
                    imp_acu_total += importe

                    if cantidad_cartas_por_tipo_envio(tipo_envio):

                        if tipo_envio == 0 or tipo_envio == 1 or tipo_envio == 2:
                            ccs += 1
                        elif tipo_envio == 3 or tipo_envio == 4:
                            ccc += 1
                        elif tipo_envio == 5 or tipo_envio == 6:
                            cce += 1

                        if pais_destino != "Argentina":
                            envios_exterior += 1

                        if pais_destino == "Argentina" and cad_cod_postal[0] == "B":
                            envios_b += 1
                            importes_b += importe

                else:
                    cedinvalid += 1
                    importe = importe_por_destino_mas_porcentaje(pais_destino, tipo_envio, cad_cod_postal, forma_pago)
            # Estamos en Soft Control
            else:

                cedvalid += 1

                importe = importe_por_destino_mas_porcentaje(pais_destino, tipo_envio, cad_cod_postal, forma_pago)
                imp_acu_total += importe

                if cantidad_cartas_por_tipo_envio(tipo_envio):

                    if tipo_envio == 0 or tipo_envio == 1 or tipo_envio == 2:
                        ccs += 1
                    elif tipo_envio == 3 or tipo_envio == 4:
                        ccc += 1
                    elif tipo_envio == 5 or tipo_envio == 6:
                        cce += 1

                if pais_destino != "Argentina":
                    envios_exterior += 1

                if pais_destino == "Argentina" and cad_cod_postal[0] == "B":
                    envios_b += 1
                    importes_b += importe

            if primer_cp is None and contadorLinea == 2:
                primer_cp = cad_cod_postal
                cant_primer_cp += 1
            else:
                if primer_cp == cad_cod_postal:
                    cant_primer_cp += 1

            if pais_destino == "Brasil":
                if menimp is None or importe < menimp:
                    menimp = importe
                    mencp = cad_cod_postal

    m.close()
    # Salimos del ciclo
    tipo_mayor = mayor_cantidad_de_cartas(ccs, ccc, cce)
    cantidad_envios_totales = cedvalid + cedinvalid

    porc = int(porcentaje(cantidad_envios_totales, envios_exterior))

    prom = int(calcular_promedio(importes_b, envios_b))
   #Resultados

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

if __name__ == "__main__":
    principal()