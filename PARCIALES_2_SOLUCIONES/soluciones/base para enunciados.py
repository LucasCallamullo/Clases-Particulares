





def principal():

    fd = "entrada.txt"
    m = open(fd, "rt")
    linea = m.readline()

    r1 = 0  # hace referencia a la respuesta

    r2 = 0

    r3 = 0  # hace referencia a la respuesta

    r4 = 0      # hace referencia a la respuesta

    for i in linea:

        # Estoy dentro de una palabra
        if i != " " and i != ".":
            pass

        # Termino una palabra
        else:
            pass

            # Apagar Banderas / Reiniciar Contadores , etc

    # Fuera del ciclo
    m.close()

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()