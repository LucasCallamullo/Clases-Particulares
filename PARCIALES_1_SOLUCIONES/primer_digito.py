


import random
random.seed(23)

n = 10
for i in range(n):
    num = random.randint(1, 100)


    print("El numero es:", num)

    # para reconocer el primer digito
    primer_digito = int(str(num)[0])

    # solo printeo la linea extra cuandl de los numeros que empiezan con 1 ejemplo
    if primer_digito == 1:
        print("su primer digito es:", primer_digito)


    # para saber su ultimo numero, y solo voy a printear una linea extra cuando termine en 8
    # ejemplo 36 / 10 = 10 * 3 + 6, este resto coincide con su ultimo digito
    ult_digito = num % 10

    if ult_digito == 8:
        print("El ultimo digito es:", ult_digito)