import random


# Opcion 1
def sumar_numeros(n1, n2):
    return n1 + n2


# Opcion 2
def calcular_promedio():
    acum = 0

    # 0 1 2 3
    for i in range(4):
        num = random.randint(1, 5)
        print(num)
        acum += num

    prom = acum / 4
    return prom


# Opcion 3:
def porcentaje_op3(num):
    #  100% --- num
    #  10%  --- x = 10 * num / 100
    porc = num * 10 / 100
    return porc


# Opcion 4
def cant_vocales_op4(cad):
    # cad = hola mundo

    cont = 0
    vocales = "aeiou"   # AEIOU
    for i in cad:
        print(i)
        # i = h
        if i.lower() in vocales:
            cont += 1

    return cont
