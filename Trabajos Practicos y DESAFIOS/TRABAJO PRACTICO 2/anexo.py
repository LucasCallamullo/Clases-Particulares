
from Ema_tp_2 import *



def main():
    cadena = "Hola A todos"

    for i in cadena:
        # i = H, o, l, a,  , M, u

        es_vocal = validar_vocales(i)  # return True es vocal, si return false no es vocal

        if es_vocal == True:
            print("Toco una vocal", i)


if __name__ == '__main__':
    main()