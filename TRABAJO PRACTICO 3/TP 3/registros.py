

class Proyecto:
    def __init__(self, Num_P, Titulo, Dia, Mes, Year, Lenguaje, Cant_lineas):
        self.num_p = Num_P
        self.titulo = Titulo
        self.dia = Dia
        self.mes = Mes
        self.year = Year
        self.lenguaje = Lenguaje
        self.cant_lineas = Cant_lineas


# Funcion write() generica del teorico
def show_datos(gLista):
    for i in range(len(gLista)):
        m_lenguaje = mostrar_lenguajes(gLista[i].lenguaje)
        Cadena_Fecha = str(gLista[i].dia) + "-" + str(gLista[i].mes) + "-" + str(gLista[i].year)
        print("Núm de Proyecto:", gLista[i].num_p, "| Titulo:", gLista[i].titulo, "| Fecha Act:",
              Cadena_Fecha, "| Lenguaje:", m_lenguaje, "| Cant. Lineas:", gLista[i].cant_lineas)


def mostrar_lenguajes(lenguaje):
    gLenguajes = list()
    lenguajes = ("Python", "Java", "C++", "Javascript", "Shell", "HTML", "Ruby", "Swift", "C#", "VB", "Go")
    for i in lenguajes:
        gLenguajes.append(i)

    for j in range(len(gLenguajes)):
        if lenguaje == j:
            x = gLenguajes[j]
            return x
