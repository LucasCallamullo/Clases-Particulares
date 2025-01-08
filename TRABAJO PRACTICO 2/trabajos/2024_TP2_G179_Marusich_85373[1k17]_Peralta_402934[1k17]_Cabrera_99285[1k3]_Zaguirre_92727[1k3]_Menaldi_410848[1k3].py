def r1(linea):
    car_ant = None
    for i in linea:
        if (car_ant == "H" or car_ant == "h") and (i == "C" or i == "c"):
            return True
        car_ant = i

def datos(linea):
    codigo_postal = linea[0:9].strip()
    direccion_fisica = linea[9:28].rstrip()
    valid = True
    for car in codigo_postal:
        if car == " " or car.isdigit():
            pass
        else:
            valid = False
            break
    tipo_de_envio = int(linea[29])
    forma_de_pago = int(linea[30])

    return codigo_postal, direccion_fisica, tipo_de_envio, forma_de_pago

def calcular_promedio(acum_importe_bsas, cont_envios_bsas):
    if cont_envios_bsas > 0:
        prom = acum_importe_bsas / cont_envios_bsas
        return int(prom)
    else:
        return 0


def porcentaje(cont_envios_exterior, envios_totales):
    porc = 0
    if envios_totales > 0:
        porc = (cont_envios_exterior * 100) / envios_totales
    return int(porc)



def direccion(dato):
    valid = True
    mayus_anterior = False
    for i in dato:
        if valid == False:
            break
        if i.isalpha() or i.isdigit() or i == " " or i == ".":
            if mayus_anterior == True and i >= 'A' and i <= 'Z':
                valid = False
            elif i >= 'A' and i <= 'Z':
                mayus_anterior = True
            else:
                mayus_anterior = False
        else:
            valid = False
    return valid


def r5(tipo_de_envio):
    carta_simple = False
    carta_certificada = False
    carta_expresa = False

    if 0 <= tipo_de_envio <= 2:
        carta_simple = True
    elif tipo_de_envio == 3 or tipo_de_envio == 4:
        carta_certificada = True
    else:
        carta_expresa = True
    return carta_simple, carta_certificada, carta_expresa


def mayor_cantidad_envios(a, b, c):
    if a > b and a > c:
        return 'Carta Simple'
    elif a == b or a == c:
        return 'Carta Simple'
    elif b == c:
        return 'Carta Certificada'
    elif b > c:
        return 'Carta Certificada'
    else:
        return 'Carta expresa'



def importe(destino, tipo, cp, pago):
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


    if pago == 1:
        final = int(0.9 * inicial)

    return final


def obtener_destino(cp):
    n = len(cp)
    if cp[0:5].isdigit() and cp[5:6] == "-" and cp[6:9].isdigit():
        return "Brasil"
    elif cp[0].isalpha() and cp[1:5].isdigit() and cp[5:8].isalpha() and n == 8 and cp[0] != 'I' and cp[0] != 'O':
        return "Argentina"
    elif cp[0:4].isdigit() and n == 4:
        return "Bolivia"
    elif cp[0:5].isdigit() and n == 5:
        return "Uruguay"
    elif cp[0:6].isdigit() and n == 6:
        return "Paraguay"
    elif cp[0:7].isdigit() and n == 7:
        return "Chile"
    else:
        return "Otro"


def porcentaje(et, ee):
    if et == 0:
        porcentaje = 0
    else:
        porcentaje = int(ee * 100 / et)

    return porcentaje

def principal():
    contador = 0
    direcciones_validas = 0
    direcciones_invalidas = 0
    HC = False
    ccs, ccc, cce = 0, 0, 0
    primer_cp = ''
    cant_primer_cp = 0

    menimp = None
    mencp = ""

    # fd = "envios.txt"
    fd = "envios100HC.txt"
    texto = open(fd, "rt")


    total_envios = 0
    num_anter = False
    carc_tanter = False
    validos = False
    invalidos = False
    basado = True

    cont_envios_exterior = 0

    cont_envios_bsas = 0
    acum_importe_bsas = 0


    while True:
        linea = texto.readline()
        contador += 1

        if linea == "":
            break

        if contador == 1:
            HC = r1(linea)

            if HC:
                control = "Hard Control"
            else:
                control = "Soft Control"


        else:
            codigo_postal, direccion_fisica, tipo_de_envio, forma_de_pago = datos(linea)
            destino = obtener_destino(codigo_postal)


            if contador == 2:
                primer_cp = codigo_postal
            if codigo_postal == primer_cp:
                cant_primer_cp += 1


            if HC:

                if direccion(direccion_fisica):

                    direcciones_validas += 1


                    importe = importe(destino, tipo_de_envio, codigo_postal, forma_de_pago)
                    total_envios += importe

                    carta_simple, carta_certificada, carta_expresa = r5(tipo_de_envio)

                    if carta_simple == True:
                        ccs += 1
                    elif carta_certificada == True:
                        ccc += 1
                    else:
                        cce += 1

                    if destino != "Argentina":
                        cont_envios_exterior += 1

                    if destino == "Argentina" and codigo_postal[0] == "B":
                        cont_envios_bsas += 1
                        acum_importe_bsas += importe


                else:
                    direcciones_invalidas += 1
                    importe = importe(destino, tipo_de_envio, codigo_postal, forma_de_pago)


            else:
                direcciones_validas += 1

                importe = importe(destino, tipo_de_envio, codigo_postal, forma_de_pago)
                total_envios += importe

                carta_simple, carta_certificada, carta_expresa = r5(tipo_de_envio)

                if carta_simple == True:
                    ccs += 1
                elif carta_certificada == True:
                    ccc += 1
                else:
                    cce += 1

                if destino != "Argentina":
                    cont_envios_exterior += 1

                if destino == "Argentina" and codigo_postal[0] == "B":
                    cont_envios_bsas += 1
                    acum_importe_bsas += importe

                if destino == "Brasil":

                    if menimp is None or importe < menimp:
                        menimp = importe
                        mencp = codigo_postal

    texto.close()

    envios_totales = direcciones_validas + direcciones_invalidas
    porc = porcentaje(cont_envios_exterior, envios_totales)

    prom = calcular_promedio(acum_importe_bsas, cont_envios_bsas)

    tipo_mayor = mayor_cantidad_envios(ccs, ccc, cce)

    # Print de requerimientos
    print(' (r1) - Tipo de control de direcciones:', control)
    print(' (r2) - Cantidad de envios con direccion valida:', direcciones_validas)
    print(' (r3) - Cantidad de envios con direccion no valida:', direcciones_invalidas)
    print(' (r4) - Total acumulado de importes finales:', total_envios)
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
