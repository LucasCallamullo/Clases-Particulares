
import soporte


# Esto es para los cuestionarios 5 6 7
def main2():
    op = 2
    n = 300000

    # op = 1 Version de Cuestionario         op != 1 version de prueba
    if op == 1:
        v = soporte.vector_known_range(n)
        v_cont = [0] * n
    # Ejemplo para ver como funciona
    else:
        v = [5, 2, 3, 4, 5, 5, 2, 1, 6]
        print("Vector de prueba:", v)
        v_cont = [0] * 10


    # contador
    cont = 0
    # v = [5, 2, 3, 4, 5, 5, 2, 1, 6]

    # c = [0  0  1  1  1  2  0  0  0  0
    for i in v:
        # i = 5, 2, 3, 4, 5
        v_cont[i] += 1

        if v_cont[i] == 1:
            cont += 1


    print(v_cont)


    may, numero = 0, 0
    modal_unico = False
    for i in range(len(v_cont)):
        # 0 1 2 3 4 5
        if v_cont[i] > may:
            may = v_cont[i]     # 3
            numero = i
            modal_unico = True

        elif v_cont[i] == may:
            modal_unico = False

    # print("Vector Conteo: ", v_cont)
    # Cuestionario 5
    print("Cantidad de numeros diferentes: ", cont)

    # Cuestionario 6 y 7
    if modal_unico:
        print("El valor modal es:", numero, "Y su total de aparicion es:", may)
    else:
        print("No existe un unico valor modal.")


# Esto es para los cuestionarios 1 2 3
def main():
    # op = 1 Version de Cuestionario         op != 1 version de prueba
    op = 1
    # Ejemplo para ver como funciona
    vec = [5, 2, 3, 4, 5, 5, 2, 1, 6, 2]   # 5 = modal      # Modal tenia que ser unico

    # Arreglos paralelos
    v_cont = []
    v_num = list()

    if op == 1:
        n = 300000
        v = soporte.vector_unknown_range(n)
    else:
        print("Vector de prueba:", vec)
        v = vec

    # Con esto creamos nuestros vectores sin conocer la cantidad
    # [5, 2, 5, 3, 4, 5, 2, 1, 6, 2]
    # bandera de control
    encontro = False

    for i in v:
        # v_num  [ 5, 2
        # v_cont [ 2, 1
        for j in range(len(v_cont)):
            if v_num[j] == i:
                encontro = True
                v_cont[j] += 1
                break

        if not encontro:
            v_num.append(i)
            v_cont.append(1)

        encontro = False

    print("Vector numeros:", v_num)
    print("Vector Conteo: ", v_cont)

    # Cuestionario 1
    print("Cantidad de numeros diferentes: ", len(v_num))

    # Cuestionario 2 y 3
    may, modal = 0, 0
    modal_unico = False
    for i in range(len(v_num)):
        # i = 0 1 2 3 4

        # Vector numeros: [5, 2, 3, 4, 1, 6]        objeto.numero , .contador
        # Vector Conteo:  [3, 2, 1, 1, 1, 1]
        if v_cont[i] > may:
            may = v_cont[i]     # 3
            modal = v_num[i]    # 5
            modal_unico = True

        elif v_cont[i] == may:
            modal_unico = False

    if modal_unico:
        print("El valor modal es:", modal, "Y su total de aparicion es:", may)
    else:
        print("No existe un unico valor modal.")


if __name__ == '__main__':
    # main()
    main2()
