

"""
998 // 9 = 110 con resto de 8.   * 1
110 // 9  = 12   con resto de 2.  *10
12 // 9    = 1     con resto de 3.   *100
Y como el último cociente es 1   *1000

998 = 1328
"""

# 1.) Cargar el valor en base 10 en la variable num_base_10.
num_base_10 = int(input("numero base 10: "))

# 2.) Si num_base_10 tiene tres o menos dígitos:
if -1000 < num_base_10 < 1000:

    # 2.1.) Sea str_base_9 una cadena inicialmente vacía, para ir armando el número dígito a dígito.
    str_base_9 = ""

    # 2.2.) Si num_base_10 es negativo:
    if num_base_10 < 0:
        # 2.2.1.) Sea num_base_10 el valor absoluto del mismo num_base_10.
        num_base_10 = num_base_10 * -1
        # 2.2.2.) Agregar un signo menos delante de la cadena str_base_9.
        str_base_9 = "-"

    # 2.3.) Sea cociente1 = num_base_10 // 9
    # 2.4.) Sea digito4 = num_base_10 % 9
    # 928
    cociente1 = num_base_10 // 9   # 110
    digito4 = num_base_10 % 9   # 8

    # 2.5.) Sea cociente2 = cociente1 // 9
    # 2.6.) Sea digito3 = cociente1 % 9
    cociente2 = cociente1 // 9  # 12
    digito3 = cociente1 % 9     # 2

    # 2.7.) Sea digito1 = cociente2 // 9
    # 2.8.) Sea digito2 = cociente2 %
    digito1 = cociente2 // 9    # 1
    digito2 = cociente2 % 9     # 3

    # 2.9.) Sea str_base_9 la concatenación de su valor anterior, más digito1, digito2, digito3 y digito4.
    str_base_9 += str(digito1) + str(digito2) + str(digito3) + str(digito4)
    # 2.10.) Sea num_base_9 = conversión a int de la cadena str_base_9.
    num_base_9 = int(str_base_9)
    # 2.11.) Mostrar num_base_10
    print("Base 10:", num_base_10)
    print("Base 9:", num_base_9)

# sino:
#   2.12.) Mostrar "Valor no admitido"
else:
    print("Valor no admitido")
