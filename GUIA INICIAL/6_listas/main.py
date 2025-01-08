import random


def main():

    # Lista ejemplo - Variable mutable se puede modificar.
    #     Nombre    apellido edad  cursa

    #       0           1       2   3
    # tuplas = ()
    v1 = ["Lucas", "Martinez", 25, True]


    # print(v1)


    # Crear lista/vector/arreglo vacía
    v1 = list()         # tamaño = 0    len(v1)
    v2 = []             # tamaño = 0

    # Agregar elementos a la lista al final de la la lista:
    # n = int(input(" Cuantos elementos agregar a la lista: "))

    op = 2
    if op == 1:
        for i in range(5):
            # i = 0 1 2 3 4
            # v1 = [ 0, 1, 2, 3, 4 ]
            v1.append(i)

            num = random.randint(1, 8)      # numero aleatorio entre 1 y 8
            # v2 = [num, num, num, num, num]
            print("Numero: ", num)
            v2.append(num)
            print(v2)

        print("El vector final 1 es:", v1)       # ctrl + d
        print("El vector final 2 es:", v2)



    elif op == 2:
        # Modificar valores en la lista
        #         0, 1, 2, 3, 4
        #   v2 = [5, 1, 0, 7, 2]
        #        [2, 1, 1, 2, 1]



        # Estudiante(legajo, nombre, edad, nota1, nota2, nota3)
        #     0  1  2  3  4
        v2 = [5, 5, 5, 5, 5]        # 5, tamaño/size = 5
        # v_est = [E, E, E, E, E]

        #   tam = len(v2)           # = 5       # tamaño size
        print(v2)

        # v2[i] = 5

        # v2 = [5, 5, 1, 7, 2]

        cont = 0

        for i in range(len(v2)):
            # i = 0     1   2   3   4
            ''' 
            if v_est[i].legajo == leg:
                v_est[i].nota1 = int(input("Ingresar nueva nota: "))
                v_est[i].nota2 = int(input("Ingresar nueva nota: "))
                v_est[i].nota3 = int(input("Ingresar nueva nota: "))
            '''

            if v2[i] == 5:
                cont += 1
                if cont == 2:
                    v2[i] = 2
                    break


            if v2[i] > 6:
                # modificar valores
                v2[i] = 2
                # pass
            else:
                v2[i] = 1

        # v2 = [1, 2, 5, 5, 5]
        print(v2)



        # Acumulador promedio
        # [2, 1, 1, 2, 2]


        #   v1 = []
        #   e1 = Estudiante(legajo, notas1, notas2, nombre, promedio)
        #   v1 = [e1, e2, e3, e4, e5]
        #


        # v2 = [ OBJ, OBJ, OBJ, OBJ, 2 ]
        # v2 = [ OBJ, OBJ, OBJ, OBJ, 2 ]
        # print(v2)
        acum = 0

        # v2 = [1, 2, 5, 5, 5]
        for i in v2:
            # i = 1, 2, 5, 5, 5
            acum += i

        print("El total acumulado es:", acum)


if __name__ == '__main__':
    main()
