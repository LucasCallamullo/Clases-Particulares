from modulo_tp3_2023 import *


def mostrar_menu():
    print("**" * 100)
    print('\n---MENU DE OPCIONES---')
    print()
    print('\t* 1 borrar archivos  ')
    print('\t* 2 carga datos nuevos ')
    print('\t* 3 Mostrar todos los registros ')
    print('\t* 4 Buscar si existe en el arreglo un registro cuya patente sea igual a P ')
    print('\t* 5 Buscar si existe en el arreglo un registro cuyo código de ticket sea igual a C ')
    print('\t* 6 Determinar la cantidad de vehículos de cada país que pasaron por las cabinas ')
    print('\t* 7 Determinar el importe acumulado por pagos de tickets ')
    print('\t* 8 vehículo con mayor monto acumulado ')
    print('\t* 9 Distancia promedio desde la última cabina recorrida ')
    print('\t* 0 Salir\n')
    opcion = int(input('\t* Ingrese opción: '))
    print("--" * 100)
    print()
    return opcion


# Estas funciones no se si las usas creeria que no las vi
def clase_vehiculo(linea):
    if linea == 0:
        m = "MOTO"
        return m
    if linea == 1:
        a = "AUTO"
        return a
    if linea == 2:
        c = "CAMION"
        return c


def manu_tele(linea):
    if linea == 1:
        man = "MANUAL"
        return man
    if linea == 2:
        tele = "TELEPEAJE"
        return tele


def lu_cabina_pais(linea):
    if linea == 0:
        return "ARGENTINA"
    if linea == 1:
        return "BOLIVIA"
    if linea == 2:
        return "BRASIL"
    if linea == 3:
        return "PARAGUAY"
    if linea == 4:
        return "URUGUAY"


def obtener_idioma(linea):
    if "ES" in linea:
        return "Español"
    if "PT" in linea:
        return "Portugués"


def abrir_archivo(opcion):
    m = open("peajes-tp3.txt", "rt")
    if opcion == 3:
        m = open("peajes-tp3.txt", "rt")
        m.close()
    return m


# =================================================================================
#                               OPCION 1
# =================================================================================
def borrar_archivo(vec):
    # No se porque te tira este warning pero también podrias usar el if len(vec) == 0: ; else:
    if vec == []:
        print("NO HAY ARCHIVOS CARGADOS")
        print()
    else:
        carga = input("desea borrar los archivos cargados?, (s)i / (n)o : ").lower()
        while not (carga == "s" or carga == "n"):
            carga = input("desea borrar los archivos cargados?, (s)i / (n)o : ").lower()
            print()

        if carga == "s":
            vec.clear()
            print("se borraron los archivos para cargar nuevamente selecione opocion 3 del menu")
            print()

        elif carga == "n":
            print("no se borro ningun archivo")
            print()


# def validar_mayor(minimo, mensage='Ingrese un valor: '):
#     numero = minimo
#     while numero <= minimo:
#         numero = int(input(mensage))
#         if numero < minimo:
#             print('Valor incorrecto!!! Debe se mayor a ', minimo)
#     return numero
#

# def validar_rango(minimo, maximo, mensage='Ingrese un valor: '):
#     numero = minimo - 1
#     while numero <= minimo or numero > maximo:
#         numero = int(input(mensage))
#         if numero <= minimo or numero > maximo:
#             print('Valor incorrecta!!! El valor debe estar comprendido entre', minimo, 'y', maximo)
#     return numero
#
#
# def validate(inf):
#     n = inf
#     while n <= inf:
#         n = int(input('Ingrese cantidad de elementos (mayor a ' + str(inf) + ' por favor): '))
#         if n <= inf:
#             print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
#
#     return n


# =================================================================================
#                               OPCION 2
# =================================================================================
def cargar_manual_ticket(vec):
    codigoid = validar_entre(0, 9999999999, mensaje="Ingrese el código identificador del ticket: ")
    pate = input("Ingrese la patente del vehículo: ")
    patente = (pate.upper())
    vehiculo = validar_entre(0, 2, mensaje="Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): ")
    tipo_pago = validar_entre(1, 2, mensaje="Ingrese la forma de pago (1: manual, 2: telepeaje): ")
    pais = validar_entre(0, 4,
                         mensaje="Ingrese el país de la cabina (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay): ")
    km = validacion(0, mensaje="Ingrese los kilómetros recorridos desde la última cabina: ")
    print("-" * 100)
    cab_pa = int(pais)
    tipo_pa = forma_pago(cab_pa)
    tipo = pago_de_vehiculo(int(vehiculo), tipo_pa)
    pago = manual_telepeaje(int(tipo_pago), tipo)

    ticket_02 = Ticket(codigoid, patente, vehiculo, tipo, tipo_pago, pago, pais, km)
    vec.append(ticket_02)


def validacion(inf, mensaje):
    num = int(input(mensaje))
    while num <= inf:
        num = int(input("ERROR " + mensaje))
    return num


def validar_entre(inf, sup, mensaje):
    num = int(input(mensaje))
    while num < inf or num > sup:
        num = int(input("ERROR " + mensaje))
    return num


# =================================================================================
#                               OPCION 3
# =================================================================================
def carga_vector(vec, fd, cont_carga):
    if cont_carga == 0:
        m = open(fd, "rt")
        primera_01 = True
        for linea in m:
            if primera_01:
                primera_01 = False
            else:
                codigoid = int(linea[0:10])
                patente = (linea[10:17])
                vehiculo = int(linea[17:18])
                tipo_pago = (int(linea[18:19]))
                cabina_pais = linea[19:20]
                pais = (int(linea[19:20]))
                kilometro = int(linea[20:23])
                cab_pa = int(cabina_pais)
                tipo_pa = forma_pago(cab_pa)
                tipo = pago_de_vehiculo(int(linea[17:18]), tipo_pa)
                pago = manual_telepeaje(int(linea[18:19]), tipo)
                # Registro
                ticket = Ticket(codigoid, patente, vehiculo, tipo, tipo_pago, pago, pais, kilometro)
                # grabar vec
                vec.append(ticket)


def forma_pago(pais):
    # monto base para Bolivia
    if pais == 1:
        base = 200
        return base
    # monto base para Brasil
    elif pais == 2:
        base = 400
        return base
    #  monto base para Argentina, Chile, Paraguay, Uruguay
    else:
        base = 300
        return base


# Recorda que te conviene usar if y elif, else en caso de ser necesario; los tenes que corregir a estos multiples if,
# funciona pero conceptualmente te pueden bajar puntos por esto
def pago_de_vehiculo(tipo, base):
    basico = base
    if tipo == 0:
        # es una moto
        basico = base // 2
        return basico
    if tipo == 1:
        # es un auto
        return basico
    if tipo == 2:
        # es un camión
        basico = int(1.6 * base)
        return basico


# Recorda que te conviene usar if y elif, else en caso de ser necesario; los tenes que corregir a estos multiples if,
# funciona pero conceptualmente te pueden bajar puntos por esto
def manual_telepeaje(pago, basico):
    final = basico
    if pago == 1:
        return final
    if pago == 2:
        final = int(0.9 * basico)
        return final


# En este caso estas usando la misma funcion para hacer lo mismo deberías, reutilizarla.
def mostrar_vector_02(v):
    for i in range(len(v)):
        var = str(v[i].codigoid)
        if len(var) < 10:
            numeros_faltantes = 10 - len(var)
            numero_completo = '0' * numeros_faltantes + var
            v[i].codigoid = numero_completo
            print(v[i])
            print("--" * 100)
        else:
            print(v[i])
            print("--" * 100)


def mostrar_vector(v):
    orden(v)            # Esta funcion orden(v) debería ir en el menu principal previo a usar mostrar_vector(v)
    for i in range(len(v)):
        var = str(v[i].codigoid)
        if len(var) < 10:
            numeros_faltantes = 10 - len(var)
            numero_completo = '0' * numeros_faltantes + var
            v[i].codigoid = numero_completo
            print(v[i])
            print("--" * 100)

        else:
            print(v[i])
            print("--" * 100)


def orden(vec):
    n = len(vec)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if str(vec[i].codigoid) > str(vec[j].codigoid):
                vec[i], vec[j] = vec[j], vec[i]


# =================================================================================
#                               OPCION 6
# =================================================================================
# opcion 06: reutilizo determinar_procedencia de las opcion 2 y 3 que esta en el modulo registro
def vec_conteo(vec):
    v_conteo = [0] * 7
    v_pais = [" "] * 7
    for i in range(len(vec)):                           #    1   , 0
        v_lista = determinar_procedencia(vec[i].pat)    # ["PAIS", 2]
        v_conteo[v_lista[1]] += 1
        v_pais[v_lista[1]] = v_lista[0]
    return v_conteo, v_pais


# =================================================================================
#                               OPCION 4
# =================================================================================
def comp_patente(p, x, vec):
    for i in range(len(vec)):
        if (vec[i].pat == p) and (vec[i].paiscabi == x):
            return i
    return -1


# =================================================================================
#                               OPCION 5
# =================================================================================
"""
Buscar si existe en el arreglo un registro cuyo código de ticket sea igual a c, 
siendo c una valor que se carga por teclado. Si existe, cambiar el valor del campo forma de pago, 
de forma que pase a valer el valor contrario (si valía 1, que pase a valer 2, y viceversa), 
y luego mostrar el registro completo modificado. Si no existe indicar con un mensaje. La búsqueda debe 
detenerse al encontrar el primer registro que coincida con el criterio pedido.
"""
def verificar_entre(a, b, mensaje):
    x = int(input(mensaje))
    while x < a or x > b:
        x = int(input(mensaje))
    return str(x)


def buscar_modif_tipo_pago(v_id, c):
    n = len(v_id)
    find = False
    for i in range(n):
        if v_id[i].codigoid == c:
            print("Se encontro el proyecto numero", c)
            print("-"*100)
            print(v_id[i].manutele)
            print("-"*100)
            cab_pa = int(v_id[i].paiscabi)
            tipo_pa = forma_pago(cab_pa)
            line = verificar_entre(1, 2, "forma de pago manual o telepeaje: ")
            tipo = pago_de_vehiculo(int(v_id[i].tipovehiculo), tipo_pa)
            v_id[i].total_pago = manual_telepeaje(int(line), tipo)
            str(v_id[i].codigoid)
            v_id.append(v_id[i].total_pago)
            print("-"*100)
            find = True
            return i

    if not find:
        print("No se encontro id con el numero", c)


def principal():
    fd = "peajes-tp3.txt"
    vec = []
    contador = 0
    opcion = -1

    while opcion != 0:

        opcion = mostrar_menu()

        if opcion == 1:
            borrar_archivo(vec)
            print("cantidad de registros cargados : ", len(vec))
            print()
            contador = 0

        elif opcion == 2:
            cargar_manual_ticket(vec)
            mostrar_vector_02(vec)
            print("cantidad de registros cargados : ", len(vec))
            print("-" * 100)

        elif opcion == 3:
            carga_vector(vec, fd, contador)
            # Aca deberías llamar la funcion orden(vec)
            mostrar_vector(vec)
            print("cantidad de registros cargados : ", len(vec))
            contador += 1
        elif opcion == 4:
            p = input("cargue patente :")
            x = int(input("Ingrese el país de la cabina (0:Argentina, 1:Bolivia, 2:Brasil, 3:Paraguay, 4:Uruguay): "))
            pos = comp_patente(p, x, vec)
            if pos >= 0:
                print(vec[pos])
            else:
                print("no se encontro el registro")

        elif opcion == 5:
            c = input("Ingrese numero de id: ")
            pos_01 = buscar_modif_tipo_pago(vec, c)
            print(vec[pos_01])


        elif opcion == 6:
            v_conteo, pos = vec_conteo(vec)
            for i in range(len(pos)):
                print("La cantidad de autos que pasaron en", pos[i], ":", v_conteo[i])
        elif opcion == 7:
            pass
        elif opcion == 8:
            pass
        elif opcion == 9:
            pass


if __name__ == '__main__':
    principal()
