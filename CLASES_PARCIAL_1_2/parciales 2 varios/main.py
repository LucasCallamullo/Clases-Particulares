


def principal():

     m = open('entrada.txt', 'r', encoding='utf-8')
     cadena = m.readline()   # str --> "Hola mundo."

     for i in cadena:
         # i = H, o, l, a, .

        # dentro de una palabra
        if i != " " and i != ".":
            pass

        # fuera dela palabra
        else:
            pass

            # reiniciar contadores y/o banderas


if __name__ == "__main__":
    principal()
