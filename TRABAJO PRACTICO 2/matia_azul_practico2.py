

def calcular_promedio(acum_importe_bsas, cont_envios_bsas):
    if cont_envios_bsas > 0:
        prom = acum_importe_bsas / cont_envios_bsas
        return int(prom)
    else:
        return 0


def calcular_porc(cont_envios_exterior, envios_totales):
    porc = 0
    if envios_totales > 0:
        porc = (cont_envios_exterior * 100) / envios_totales
    return int(porc)


def obtengo_datos(linea):
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


def validacion_direccion(dato):
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

# Resolviendo requerimientos
def r1(linea):
    car_ant = None
    for i in linea:
        if (car_ant == "H" or car_ant == "h") and (i == "C" or i == "c"):
            return True
        car_ant = i


"""def r4(total_envios, tipo_de_envio):

    if total_envios == -1:
        valor = precios(tipo_de_envio)
        total_envios += valor +1
    else:
        valor = precios(tipo_de_envio)
        total_envios += valor

    return total_envios"""


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


def mayor_cant_envios(a, b, c):
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


# ===========================================================
#                           PUNTO 4
# ===========================================================
# Punto 4       - Funcion Valerio TP 1
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

'''
def precios(tipo_de_envio):
    valor = 0
    if tipo_de_envio == "0":
        valor = 1100
    elif tipo_de_envio == "1":
        valor = 1800
    elif tipo_de_envio == "2":
        valor = 2450
    elif tipo_de_envio == "3":
        valor = 8300
    elif tipo_de_envio == "4":
        valor = 10900
    elif tipo_de_envio == "5":
        valor = 14300
    else:
        valor = 17900
    return valor

def pais(cp):
 destino = None
 cp_length = len(cp)
 region = None
 uru = None
 if cp[-1].isdigit():
       if cp_length == 4 and cp[-2].isdigit() and cp[-3].isdigit() and cp[-4].isdigit():
            destino = "Bolivia"
 elif cp_length == 6 and cp[-2].isdigit() and cp[-3].isdigit() and cp[-4].isdigit() and cp[-5].isdigit() and cp[
     -6].isdigit():
       destino = "Paraguay"
 elif cp_length == 5 and cp[-2].isdigit() and cp[-3].isdigit() and cp[-4].isdigit() and cp[-5].isdigit():
        destino = "Uruguay"
        if cp[0] == "1":
            uru = "Uruguay (Montevideo)"
        else:
            uru = "Uruguay (No Montevideo)"
 elif cp_length == 7 and cp[-2].isdigit() and cp[-3].isdigit() and cp[-4].isdigit() and cp[-5].isdigit() and cp[
     -6].isdigit():
       destino = "Chile"
 elif cp_length == 9 and cp[-2].isdigit() and cp[-3].isdigit() and cp[-4] == "-" and cp[-5].isdigit() and cp[
     -6].isdigit() and cp[-8].isdigit() and cp[-9].isdigit():
        destino = "Brasil"
        if cp[0] == "1":
            region = '1'
        elif cp[0] == "2":
            region = "2"
        elif cp[0] == "3":
            region = '3'
        elif cp[0] == "4":
            region = '4'
        elif cp[0] == "5":
            region = '5'
        elif cp[0] == "6":
            region = '6'
        elif cp[0] == "7":
            region = '7'
        elif cp[0] == "8":
            region = '8'
        elif cp[0] == "9":
            region = '9'
        else:
            region = '0'
 else:
     destino = "Otro"
 if cp[-1].isalpha() and cp[-2].isalpha() and cp[-3].isalpha() and cp[-4].isdigit() and cp[-5].isdigit() and cp[
     -6].isdigit() and cp[-7].isdigit() and cp[-8].isalpha() and cp[0] != "I" and cp[0] != "Ñ" and cp[0] != "O":
       destino = "Argentina"

 else:
    destino = "Otro"

 return destino, region, uru

# CALCULAMOS INTERESES
def interes(destino, region, uru, inicial, pago):
    # print('valores de funcion interes: ',destino,region,uru,inicial,pago)

    if pago == '1' and destino == "Argentina":
        final = inicial - ((inicial * 10) / 100)
    else:
        final = inicial
    if destino == "Bolivia" or destino == "Paraguay" or uru == "Uruguay (Montevideo)":
        inicial = inicial + ((inicial * 20) / 100)
        if pago == '1':
            final = inicial - ((inicial * 10) / 100)
        else:
            final = inicial
    elif destino == "Chile" or uru == "Uruguay (No Montevideo)":
        inicial = inicial + ((inicial * 25) / 100)
        if pago == '1':
            final = inicial - ((inicial * 10) / 100)
        else:
            final = inicial
    elif region == '8' or region == '9':
        inicial = inicial + ((inicial * 20) / 100)
        if pago == '1':
            final = inicial - ((inicial * 10) / 100)
        else:
            final = inicial
    elif region == '0' or region == '1' or region == '2' or region == '3':
        inicial = inicial + ((inicial * 25) / 100)
        if pago == '1':
            final = inicial - ((inicial * 10) / 100)
        else:
            final = inicial

    elif region == '4' or region == '5' or region == '6' or region == '7':
        inicial = inicial + ((inicial * 30) / 100)
        if pago == '1':
            final = inicial - ((inicial * 10) / 100)
        else:
            final = inicial
    elif destino == "Otro":
        inicial = inicial + ((inicial * 50) / 100)
        final = inicial
 
        # if pago == '1':
         #  final = inicial - ((inicial * 10) / 100)
        # else:
    # print('importe con interes: ',final)
    return int(final)





def porcentaje(et, ee):  # et es envíos totales y ee es envíos al exterior
    if et == 0:
        porcentaje = 0
    else:
        porcentaje = int(ee * 100 / et)

    return porcentaje
'''


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

    fd = "envios.txt"
    # fd = "envios25.txt"
    # fd = "envios100HC.txt"
    # fd = "envios100SC.txt"

    # texto = open("envios25.txt")
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
            codigo_postal, direccion_fisica, tipo_de_envio, forma_de_pago = obtengo_datos(linea)
            destino = obtener_destino_pais(codigo_postal)


            if contador == 2:
                primer_cp = codigo_postal
            if codigo_postal == primer_cp:
                cant_primer_cp += 1

            # HARD CONTROL
            if HC:
                # DIRECCION VALIDA
                if validacion_direccion(direccion_fisica):

                    direcciones_validas += 1

                    '''
                    # inicial = precios(tipo_de_envio)
                    # destino, region, uru = pais(codigo_postal)
                    # valor = interes(destino, region, uru, inicial, forma_de_pago)
                   
                    if tipo_de_envio >= "0" and tipo_de_envio <= "6":
                        if total_envios == -1:
                            total_envios += valor + 1
                        else:
                            valor = precios(tipo_de_envio)
                            total_envios += valor
                    else:
                        print("El valor debe estar en el rango de 0 a 6") '''
                    importe = calcular_importe(destino, tipo_de_envio, codigo_postal, forma_de_pago)
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

                # DIRECCION NO VALIDA
                else:
                    direcciones_invalidas += 1
                    importe = calcular_importe(destino, tipo_de_envio, codigo_postal, forma_de_pago)

            # ESTOY EN SOFT CONTROL
            else:
                direcciones_validas += 1

                importe = calcular_importe(destino, tipo_de_envio, codigo_postal, forma_de_pago)
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

                '''
                if tipo_de_envio >= "0" and tipo_de_envio <= "6":
                   if total_envios == -1:
                        valor = precios(tipo_de_envio)
                        total_envios += valor + 1
                   else:
                        valor = precios(tipo_de_envio)
                        total_envios += valor
                else:
                    print("El valor debe estar en el rango de 0 a 6")
                '''

            # ES CUANDO NO ESTOY NI EN SOFT NI EN HARD CONTROL
            if destino == "Brasil":
                if menimp is None or importe < menimp:
                    menimp = importe
                    mencp = codigo_postal

    texto.close()

    envios_totales = direcciones_validas + direcciones_invalidas
    porc = calcular_porc(cont_envios_exterior, envios_totales)

    prom = calcular_promedio(acum_importe_bsas, cont_envios_bsas)

    tipo_mayor = mayor_cant_envios(ccs, ccc, cce)

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
