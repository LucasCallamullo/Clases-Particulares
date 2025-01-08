
# crea lista vacia
v_envio = []        # list()
v_envio = [5]

v_envio.append(8)

#          0   1   2
v_envio = [10, 15, 25]

v_envio[0] += 2
v_envio[1] = 8

#           0  1   2
v_envio = [12, 8, 25]  # 3

for i in v_envio:
    # i = 12, 8, 25
    print(i)

for i in range(len(v_envio)):  # 3
    # i = 0, 1, 2
    v_envio[i] += 1

    # v_envio = [13, 9, 26]