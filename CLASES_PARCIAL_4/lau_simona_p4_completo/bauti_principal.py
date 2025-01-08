

import bauti_registro
import random

def validar(inf):
    n = int(input("ingrese un numero mayor a " + str(inf) + "porfavor"))
    while n <= inf:
        n = int(input("error... el numero debe ser mayor a " + str(inf) + "vuelva a ingresar porfavor"))
    return n

def add_in_order(v,libro):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if libro.numero == v[c].numero:
            pos = c
            break
        else:
            if libro.numero < v[c].numero:
                der = c - 1
            else:
                izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [libro]



def cargar():
    n = validar(0)
    v = []
    tit1 = ("guerra","cuentos","luchas","tesoros")
    tit2 = ("frias","oscuros","perdidas","alegres")
    nombres = ("bautidta","aurelio","juan")
    apellidos = ("perez","gonzalez","agyuire")

    for i in range(n):
        num = random.randint(1000000000000,9999999999999)
        tit = random.choice(tit1) + " " + random.choice(tit2)
        aut = random.choice(nombres) + " " + random.choice(apellidos)
        cod = random.randint(1,5)
        pre = round(random.uniform(7000,20000), 2)
        libro = bauti_registro.Libro(num,tit,aut,cod,pre)
        add_in_order(v,libro)
    print("arreglo generado")
    print()
    return v


def mostrar(v):
    n = len(v)
    print("listado es...")
    for i in range(n):
        print(v[i])
    print()

def principal():
    v = []
    fd = "libros.dat"
    op = -1
    while op != 6:
        print("1-cargar arreglo")
        print("2-mostrar arreglo")
        print("3-buscar libro")
        print("4-generar archivo")
        print("5-mostrar archivo")
        print("6-salir")
        op = int(input("ingrese una opcion del menu: "))
        if op == 1:
            v = cargar()

        elif op == 2:
            if v:
                mostrar(v)
            else:
                print("el vector no fue cargado...")
                print()
        elif op == 3:
            if v:
                pass
            else:
                pass
        elif op == 4:
            if v:
                pass
            else:
                pass
        elif op == 5:
            if v:
                pass
            else:
                pass
        elif op == 6:
            print("hasta pronto...")



if __name__ == '__main__':
    principal()






