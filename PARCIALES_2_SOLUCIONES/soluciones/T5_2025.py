# función para determinar si un caracter es un digito.
def es_digito(car):
    return "0" <= car <= "9"


# función para determinar si un caracter es una vocal.
def es_vocal(car):
    return car in "aeiouáéíóúAEIOUÁÉÍÓÚ"


# función para determinar si un caracter es una consonante.
def es_consonante(car):
    return car in "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"


# función para determinar si un caracter es una minúscula...
def es_minuscula(car):
    return car in "aábcdeéfghiíjklmnñoópqrstyuúvwxyz"


# función para determinar si un caracter es una minúscula...
def es_mayuscula(car):
    return car in "AÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚVWXYZ"


# función para calcular el porcentaje entero entre sus parámetros.
def calcular_porcentaje(contador_parcial, contador_total):
    porcentaje = 0
    if contador_total != 0:
        porcentaje = contador_parcial * 100 // contador_total
    return porcentaje


# función principal del programa.
def principal():
    # inicialización de variables de resultados..
    r1 = r3 = r4 = 0
    r2 = None

    # contador de letras en una palabra...
    contador_letras = 0

    # item 1: contador de mayusculas y de letras A...
    cant_mayusculas = cant_A = 0

    # item 2: contador de minusculas y variable para el caracter anterior...
    cant_minusculas = 0
    anterior = " "

    # item 3: acumuladores, contadores y flags para r3...
    cant_palabras_mas_digitos_que_consonantes = cantidad_palabras = cant_digitos = cant_consonantes = 0

    # item 4: flags para b, ba y t...
    tiene_d = tiene_da = tiene_s = tiene_se = False

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # texto = "La seda se adapta mejor sin darse cuenta en la diadema."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if contador_letras > 0:
                # item 1...
                if cant_mayusculas == contador_letras and cant_A == 0:
                    r1 += 1

                # item 2...
                if cant_minusculas == contador_letras and es_vocal(anterior):
                    if r2 is None or contador_letras < r2:
                        r2 = contador_letras

                # item 3...
                cantidad_palabras += 1
                if cant_digitos > cant_consonantes:
                    cant_palabras_mas_digitos_que_consonantes += 1

                # item 4...
                if tiene_da and tiene_se:
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            contador_letras = 0

            # item 1...
            cant_mayusculas = cant_A = 0

            # item 2...
            cant_minusculas = 0
            anterior = " "

            # item 3...
            cant_digitos, cant_consonantes = False, 0

            # item 4...
            tiene_d = tiene_da = tiene_s = tiene_se = False

        else:
            # caracter dentro de la palabra... contarlo...
            contador_letras += 1

            # item 1...
            if es_mayuscula(car):
                cant_mayusculas += 1
            if car == "A":
                cant_A += 1

            # item 2...
            anterior = car

            if es_minuscula(car):
                cant_minusculas += 1

            # item 3...
            if es_digito(car):
                cant_digitos += 1
            elif es_consonante(car):
                cant_consonantes += 1

            # item 4...
            if car in "dD":
                tiene_d = True
            else:
                if tiene_d and car in "aáAÁ":
                    tiene_da = True
                tiene_d = False

            if car in "sS":
                tiene_s = True
            else:
                if tiene_s and car in "eéEÉ":
                    tiene_se = True
                tiene_s = False

    # cálculo del porcentaje para r3...
    r3 = calcular_porcentaje(cant_palabras_mas_digitos_que_consonantes, cantidad_palabras)

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()
