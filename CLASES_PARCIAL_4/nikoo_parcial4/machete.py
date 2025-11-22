

def add_in_order(v_pant, pant):

    izq, der = 0, len(v_pant) - 1

    while izq <= der:
        c = (izq + der) // 2

        if v_pant[c].codigo == pant.codigo:
            pos = c
            break
        elif v_pant[c].codigo > pant.codigo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_pant[pos:pos] = [pant]



def generar_matriz(v_peli):
    # generar la matriz en 0
    filas = 20     # id_pais = random.randint(500, 519)
    columnas = 5   # tipo = random.randint(1, 5)
    matriz = [[0] * columnas for i in range(filas)]

    # [ [3.0, 0, 0 ] ,
    #   [0, 2.5, 0 ] ,
    #   [0, 0, 0 ] ,
    #   [0, 0, 0 ]  ]

    # rellenar la matriz
    for i in v_peli:
        # i = P ,   P
        # matriz[i.tipo-1][i.id_pais-500] += 1
        matriz[i.id_pais-500][i.tipo-1] += i.importe

    # supongamos que te piden ademas mostrar los valores que sean de un id pais superior o igual a 510.

    # TIPOS = ("Acción", "Comedia", "Drama", "Thriller", "Romantico")
    # mostrar la matriz:
    for f in range(len(matriz)):            #  f = 0, 1, 2, ..., 19
        for c in range(len(matriz[0])):     # c = 0, 1, ..., 4
            if matriz[f][c] > 0 and f+500 >= 510:
                print("=" * 50)
                print("La cantidad por tipo:", TIPOS[c], "y por Id Pais:", f+500)
                print("La cantidad total es:", matriz[f][c])