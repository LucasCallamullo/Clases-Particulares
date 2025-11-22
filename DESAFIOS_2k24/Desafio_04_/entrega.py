
def principal():

    fd = "expresiones.txt"
    m = open(fd, "rt")

    aperturas = ["{", "(", "["]
    clausuras = ["}", ")", "]"]

    pila = []

    for linea in m:
        print(linea.strip())

        termino_antes = False

        for i in linea:

            if i in aperturas:
                pila.append(i)

            elif i in clausuras:

                if len(pila) == 0:
                    print("Sobran Cierres")
                    termino_antes = True
                    break

                else:
                    ultimo_indice = len(pila) - 1
                    ult_valor_pila = pila.pop(ultimo_indice)

                    indice = None
                    for k in range(len(aperturas)):
                        if ult_valor_pila == aperturas[k]:
                            indice = k
                            break

                    if clausuras[indice] != i:
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
        pila = []
        print()
        print()

    m.close()


if __name__ == '__main__':
    principal()