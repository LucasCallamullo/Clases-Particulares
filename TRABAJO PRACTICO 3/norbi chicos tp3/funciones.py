

# =====================================================================
#                       Opcion 3
# =====================================================================
def ordenar_arreglo(v_envios):
    n = len(v_envios)
    # indices       0   1   2
    # v_envios = [ E2, E1, E3 ]
    for i in range(n-1):        # 2
        # i = 0             , 1

        for j in range(i+1, n):     # 3
            # i = 0
            # j = 1, 2
            # menor a mayor o mayor  a menor
            if v_envios[i].cod_postal > v_envios[j].cod_postal:
                v_envios[i], v_envios[j] = v_envios[j], v_envios[i]


def shell_sort(v_envios):
    n = len(v_envios)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = v_envios[i]
            j = i

            while j >= gap and v_envios[j - gap].cod_postal > temp.cod_postal:
                v_envios[j] = v_envios[j - gap]
                j -= gap

            v_envios[j] = temp

        gap //= 2


def mostrar_datos(v_envios):

    # Indices       0   1   2
    # v_envios = [ E1, E2, E3, ..., ]
    for i in v_envios:
        # i = E1, E2, E3
        print(i)