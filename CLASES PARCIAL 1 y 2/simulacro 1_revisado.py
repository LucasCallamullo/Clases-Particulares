def valid_vocales(i):
    if i.lower() in "aeiou":
        return True
    else:
        return False


def valid_digito(i):
    if i in "123456789":
        return True
    else:
        return False


def r2_palabras_con_e(i):
    if i.lower() in "e":
        return True
    else:
        return False


def principal():
    m = open("entrada.txt", "rt")
    texto = m.read()
    m.close()

    # contadores y acumuladores
    ''' 1 - Determinar la cantidad de palabras que tienen exactamente seis caracteres 
    de largo e incluyen una o dos vocales (en mayúscula o minúscula) y uno o más dígitos. '''
    r1 = 0
    r1_cont_caract = 0          # bieen para contar los seis caracteres exactos
    # r1_es_vocal = False   # la bandera no indica cantidad nos pide solo una o dos
    r1_cont_vocal = 0       # contador de vocales para verificar si fue 1 o 2
    # r1_es_digito = False    # bien, en este caso podemos usar una bandera aunque la voy a renombrar
    r1_tiene_digito = False     # nos va a indicar si tuvimos digito o no, porque el enunciado dice si
                                # tuvimos al menos un digito no nos pide una canitdad exacta

    ''' 2 - Promedio entero de caracteres por palarbas de las que tienen solo una r y dos o 
    mas veces una e '''
    r2 = 0

    r2_total_acum = 0       # necesario para el promedio
    r2_total_cant = 0       # necesario para el promedio

    r2_cont_caract = 0      # se suma al acumulador necesario bien
    r2_contador_r = 0       # contador necesario porque necesitamos SOLO una r
    # r2_palabras_con_e = False
    r2_contador_e = 0       # necesitamos un contador porque nos pide cantidad de e y la bandera
                            # no indica cantidad

    # promedio = 0          # en realidad estos r2 no hace falta crear uno como tal*

    # r3

    for i in texto:

        # estoy dentro de la palabra
        if i != " " and i != ".":

            # r1
            # agrego este contador de caracteres aca porque necesitas sumar cada vez que toca
            # un caracter dentro de la palabra
            r1_cont_caract += 1

            r1_es_vocal = valid_vocales(i)  # las funnciones con variable bien
            r1_es_digito = valid_digito(i)

            # de esta forma determinamos si tuvimos un digito prendemos la bandera
            if r1_es_vocal:
                r1_tiene_digito = True
            # cada vez que toque una vocal suma una al contador
            if r1_es_digito:
                r1_cont_vocal += 1

            ''' 
            esto en realidad iria cuando termino la palabra, pero con algunos cambios
            if r1_cont_caract == 6 and r1_es_vocal <= 2 and r1_es_digito > 1:
                r1 += 1
            '''

            # r2
            ''' 
            No se hacen returns en la funcion principal y tampoco estas contando r o e aca
            r2_cont_caract += 1
            if r2_contador_r and r2_palabras_con_e >= 2:
                return True
            '''
            if i.lower() == "r":    # cada vez que toque r dentro de la palabra sumo uno al contador
                r2_contador_r += 1

            if i.lower() == "e":
                r2_contador_e += 1


        # fuera de la palabra
        else:

            # r1
            # esta seria la condicion completa para que cumpla con las condiciones
            # lo unico toma en cuenta que ese ultimo or tiene que si o si ir entre parentesis
            # porque sino daria un error
            if r1_cont_caract == 6 and r1_tiene_digito and (r1_cont_vocal == 1 or r1_cont_vocal == 2):
                r1 += 1
            '''
            no se retorna nada dentro de principal esta condicion esta masomenos bien 
            if r1_cont_caract == 6 and r1_es_vocal <= 2 and r1_es_digito > 1:
                return True
            '''

            # r2
            # if r2_contador_r and r2_palabras_con_e >= 2:
            # recorda que aca abajo de la palabra ponemos las condiciones para saber si cumple o no nuestra palabra
            # ejemplo "aree" cumple porque arrastra un cont_r = 1 y un cont_e = 2

            if r2_contador_r == 1 and r2_contador_e >= 2:
                r2_total_acum += r2_cont_caract
                r2_total_cant += 1

            # reiniciar contadores y banderas
            r1_cont_caract = 0
            # r1_es_vocal = False   # estos en realidad fueron variables creadas dentro de la palabra
            # r1_es_digito = False  # estos en realidad fueron variables creadas dentro de la palabra
            ''' recorda que seria mejor que vayas al principio y copies y pegues exactamente lo que
            creaste para el inicio del punto en este caso sería'''
            r1_cont_vocal = 0
            r1_tiene_digito = False
            r1_cont_caract = 0

            # Reiniciar contadores de r2
            # pero no todos las variables para el promedio no hay que reiniciarlas
            # ya que nos sirven fuera del ciclo for
            r2_cont_caract = 0  # se suma al acumulador necesario bien
            r2_contador_r = 0  # contador necesario porque necesitamos SOLO una r
            r2_contador_e = 0

    # r2
    r2 = 0          # en realidad r2 hace referencia a la respuesta osea es el promedio
    if r2_total_cant != 0:
        r2 = r2_total_acum // r2_total_cant

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)


#  print("Tercer resultado:", r3)
#   print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()
