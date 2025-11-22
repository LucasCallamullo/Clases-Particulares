num_base_10= int(input("Ingrese su numero en base 10:"))

if num_base_10 <= 999 and num_base_10 >= -999:
    str_base_9 = ""
    if num_base_10 <= -1:
        str_base_9 += "-"
        num_base_10 = -1 * num_base_10

    # 998
    cociente1 = num_base_10 // 9  # 8
    digito4 = num_base_10 % 9   # 110
    cociente2 = cociente1 // 9   #   12
    digito3 = cociente1 % 9     # 2
    digito1 = cociente2 // 9    # 3
    digito2 = cociente2 % 9     # 1

    str_base_9 += str(digito1) + str(digito2) + str(digito3) + str(digito4)     # "1234"   STR
    str_base_9 = int(str_base_9)                    # 1234 INT

    print("Numero ingresado en base 9:", str_base_9)

else:
    print("Valor no admitido")

