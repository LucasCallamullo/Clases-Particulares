



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

    # donde vaya esta funcion

    importe = importe_total(destino, cp, tipo, pago)
    impo_Acumulado += importe