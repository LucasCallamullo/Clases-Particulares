
def principal():

    fd = "expresiones.txt"
    # fd = "archivo.txt"

    m = open(fd, "rt")

    # indice       0   1    2
    aperturas = ["{", "(", "["]

    #           0     1     2
    clausura = ["}", ")", "]"]

    pila = []

    for linea in m:
        print(linea.strip())

        termino_antes = False
        # {[(a+4)*(x-t)+w]/5}*(r/3)

        for i in linea:
            # i = {, [, (, ..., ), (, ),

            # i = ")", (

            if i in aperturas:
                # pila = [ { ]
                pila.append(i)

            elif i in clausura:

                if len(pila) == 0:
                    print("Sobran Cierres")
                    termino_antes = True
                    break

                else:
                    ultimo_indice = len(pila) - 1       # 2
                    ult_valor_pila = pila.pop(ultimo_indice)    # retorna el ultimo valor
                    # ult_valor_pila = (

                    indice = None
                    for k in range(len(aperturas)):     # ["{", "(", "["]
                        # k = 0, 1, 2
                        if ult_valor_pila == aperturas[k]:
                            indice = k
                            break

                    # indice = 1
                    # clausura = ["}", ")", "]"]
                    # if ")" != ")"
                    if clausura[indice] != i:
                        print("Desequilibrio interno")
                        termino_antes = True
                        break

        #
        # despues de leer una linea
        if not termino_antes:
            if len(pila) > 0:
                print("Sobran Aperturas")

            else:
                print("ok")

        termino_antes = False
        print()
        print()

    m.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    principal()