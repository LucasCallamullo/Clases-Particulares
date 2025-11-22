

def add_in_order(v_libros, nuevo_libro):

    izq, der = 0, len(v_libros) - 1

    while izq <= der:
        c = (izq + der) // 2

        # el atributo por el que les pidan ordenar es lo que cambian
        if v_libros[c].isbn == nuevo_libro.isbn:
            pos = c
            break

        # la boquita ">" determinar si esta de menor a mayor o mayor a menor
        elif v_libros[c].isbn > nuevo_libro.isbn:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_libros[pos:pos] = [nuevo_libro]