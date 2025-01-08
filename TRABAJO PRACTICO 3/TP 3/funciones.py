import random
from registros import *


# Opcion 1
def validar_num_proyecto(gProyecto, Num_Proyecto):
    for i in gProyecto:
        if i.num_p == Num_Proyecto:
            return True
    return False


def cargar_datos(gProyecto, tam):
    Titulos = ("Alemania", "Argentina", "Australia", "Bélgica", "Brasil", "Canadá", "Catar", "Croacia",
               "Ecuador", "España", "Francia", "Ghana", "México", "Portugal", "Polonia", "Suiza", "Holanda")
    Max_Cant_Proyectos = 10
    for i in range(tam):
        Num_Proyecto = random.randint(1, Max_Cant_Proyectos)
        Titulo = random.choice(Titulos)
        Dia = random.randint(1, 31)
        Mes = random.randint(1, 12)
        Year = random.randint(2000, 2022)
        Lenguaje = random.randint(0, 10)
        Cant_lin = random.randint(100, 500)

        Num_Valido = validar_num_proyecto(gProyecto, Num_Proyecto)
        while Num_Valido:
            Num_Proyecto = random.randint(1, Max_Cant_Proyectos)
            # Este apartado se hizo para no tener limite en la carga de la cantidad de Numero de Proyectos.
            Num_Valido = validar_num_proyecto(gProyecto, Num_Proyecto)
            if Num_Valido:
                Max_Cant_Proyectos += 1

        LilProy = Proyecto(Num_Proyecto, Titulo, Dia, Mes, Year, Lenguaje, Cant_lin)
        gProyecto.append(LilProy)


# Opcion 2
def sort(gProyecto, op):
    # se incluye la variable op del Menu(), para "reciclar" la funcion que se pide ordenar en las op 2 y 6
    n = len(gProyecto)
    for i in range(n-1):
        for j in range(i+1, n):
            if op == 2:
                if gProyecto[i].titulo > gProyecto[j].titulo:
                    gProyecto[i], gProyecto[j] = gProyecto[j], gProyecto[i]
            elif op == 6:
                if gProyecto[i].num_p > gProyecto[j].num_p:
                    gProyecto[i], gProyecto[j] = gProyecto[j], gProyecto[i]


# Opcion 3:
def menu_opcion3(Existe, gProyecto, X):
    if Existe:
        while Existe:
            # Para mostrar los datos del proyecto que desea actualizar.
            print("Los Datos del Proyecto que desea modificar: ")
            Datos_Old = lista_opcion3(gProyecto, X)
            show_datos(Datos_Old)
            # Menu improvisado para la interfaz de usuario
            print("¿Desea Modificar Cantidad de Líneas de Código y/o Fecha de Actualización?")
            print("1 - Si.")
            print("2 - No.")
            opc = int(input("Ingresar Opción: "))

            if opc == 1:
                Cant_Lineas = int(input("Cantidad de Líneas a Modificar: "))
                Dia, Mes, Year = validar_datos_opcion3()
                cambiar_datos_op3(gProyecto, X, Dia, Mes, Year, Cant_Lineas)
                # Para mostrar los datos del proyecto ahora Actualizado.
                Datos_New = lista_opcion3(gProyecto, X)
                print("Los Datos del Proyecto modificado Actualizado: ")
                show_datos(Datos_New)
                break
            elif opc == 2:
                break
    else:
        print("No existe ningún Proyecto con el Número ingresado.")


# Funcion para obtener una lista y poder mostrarla con mi funcion generica de write/show_datos
def lista_opcion3(gProyecto, X):
    lista3 = list()
    for i in gProyecto:
        if i.num_p == X:
            lista3.append(i)
    return lista3


def validar_datos_opcion3():
    Dia = int(input("Ingrese Nuevo Día: "))
    while not 1 <= Dia <= 31:
        Dia = int(input("Ingrese Nuevo Día (entre 1 y 31): "))

    Mes = int(input("Ingrese Nuevo Mes: "))
    while not 1 <= Mes <= 12:
        Mes = int(input("Ingrese Nuevo Mes (entre 1 y 12): "))

    Year = int(input("Ingrese Nuevo Año: "))
    while not 2000 <= Year <= 2022:
        Year = int(input("Ingrese Nuevo Año (entre 2000 y 2022): "))

    return Dia, Mes, Year


def cambiar_datos_op3(gProyecto, X, Dia, Mes, Year, Cant_Lineas):
    for i in range(len(gProyecto)):
        if gProyecto[i].num_p == X:
            gProyecto[i].mes = Dia
            gProyecto[i].dia = Mes
            gProyecto[i].year = Year
            gProyecto[i].cant_lineas = Cant_Lineas


# Opcion 4
def acumuladores_op4(gProyecto):
    Acum = [0] * 11
    for i in gProyecto:
        Acum[i.lenguaje] += i.cant_lineas
    return Acum


def show_op4(acum_op4):
    print("=" * 50)
    print("Lenguaje", "\t Cant. Lineas de Código \n")
    for i in range(len(acum_op4)):
        X = mostrar_lenguajes(i)
        if len(X) < 3:
            Tab = "\t\t\t"
        elif len(X) > 8:
            Tab = "\t"
        else:
            Tab = "\t\t"
        print(X, Tab, acum_op4[i])
        # print("El Lenguaje", X, "tiene", acum_op4[i], "de Lineas de Código.")


# Opcion 5
def contadores_op5(gProyecto):
    Cont = [0] * 23
    for i in gProyecto:
        Cont[(i.year - 2000)] += 1
    return Cont


def show_op5(cont_op5):
    print("=" * 50)
    print("Año", "\t Cant. Proyectos \n")
    for i in range(len(cont_op5)):
        if cont_op5[i] > 0:
            print(i+2000, "\t", cont_op5[i])
            # print("El Año", i+2000, "Tiene un total de", cont_op5[i], "Proyectos de Software.")


# Opcion 6
def obtener_lista_op6():
    gLenguajes = list()
    lenguajes = ("Python", "Java", "C++", "Javascript", "Shell", "HTML", "Ruby", "Swift", "C#", "VB", "Go")
    for i in lenguajes:
        gLenguajes.append(i)
    return gLenguajes


def Validar_lenguaje_op6(Lista_Lenguajes):
    Valido = False
    while not Valido:
        show_lenguajes_op6(Lista_Lenguajes)
        ln = input("Ingrese el Lenguaje a buscar (Nombre o Número correspondiente): ")
        for i in range(len(Lista_Lenguajes)):
            # Lo hicimos para que tambien leyera valores en minuscula.
            j = Lista_Lenguajes[i].lower()
            if j == ln or str(i) == ln:
                Valido = True
                return i


def show_lenguajes_op6(Lista_Lenguajes):
    print("=" * 50)
    print("Número", "\t Lenguaje")
    for i in range(len(Lista_Lenguajes)):
        print(i, "\t\t", Lista_Lenguajes[i])


def obtener_lista_ln_op6(gProyecto, LN):
    # para crear una lista que solo cumplan ser del mismo lenguaje
    lista6 = list()
    for i in gProyecto:
        if i.lenguaje == LN:
            lista6.append(i)
    return lista6


# Opcion 7
def calcular_may_op7(acum_op5):
    may = -1
    may_list = list()
    for i in range(len(acum_op5)):
        if acum_op5[i] > may:
            may = acum_op5[i]

    for i in range(len(acum_op5)):
        if acum_op5[i] == may:
            may_list.append(i+2000)

    return may_list


def show_op7(may_op7):
    n = len(may_op7)
    if n == 1:
        print("El Año con más proyectos actualizados fue:", (may_op7[0]))
    elif n > 1:
        print("Los Años con más proyectos actualizados fueron:")
        for i in range(n):
            print("Año:", may_op7[i])
