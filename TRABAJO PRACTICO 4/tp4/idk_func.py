import os.path
import pickle


def porcentaje(s, t):
    if t != 0:
        return (s * 100) / t


def promedio(s, t):
    if t != 0:
        return s / t
    else:
        return 0


def validar_mayor(a, n):
    n = int(n)
    while n < a:
        print("El valor debe ser mayor a: ", a)
        n = int(input("Ingrese nuevamente: "))
    return n


def validar_entre(a, b, n):
    n = int(n)
    while a > n or n > b:
        print("El valor debe estar entre: ", a, " y ", b)
        n = int(input("Ingrese nuevamente: "))
    return n


def validar_solo_num(dat):
    while not dat.isdigit():
        print("CARACTERES NO VÁLIDOS.")
        dat = input("Ingrese nuevamente (sólo números): ")
    return dat


def validar_pat(pat):
    while not pat.isdigit() or not pat.isalpha():
        print("CARACTERES NO VÁLIDOS.")
        pat = input("Ingrese nuevamente una patente (sólo letras y números): ")
    return pat


def imp_basico(cab):
    if cab == 1:
        return 200
    elif cab == 2:
        return 400
    else:
        return 300


def imp_final(tipo, forma, imp):
    if tipo == 0:
        moto = imp / 2
        if forma == 2:
            valor = moto - (moto * 0.1)
            return valor
        else:
            return moto
    if tipo == 2:
        camion = imp + (imp * 0.6)
        if forma == 2:
            valor = camion - (camion * 0.1)
            return valor
        else:
            return camion
    else:
        if forma == 2:
            valor = imp - (imp * 0.1)
            return valor
        else:
            return imp


def mostrar_datos(v):
    for i in v:
        print(i)


