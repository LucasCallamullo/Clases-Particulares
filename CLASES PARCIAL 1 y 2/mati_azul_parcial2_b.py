def validar_impar(i):
    impares="13579"
    if i in impares:
        return True
    return False

def validar_vocales(i):
    vocales="aeiou"
    if i.lower() in vocales:
        return True
    return False

def validar_consonantes(i):
    consonantes="qwrtypsdfghjklzxcvbnm"
    if i.lower() in consonantes:
        return True
    return False

def validar_mayusculas(i):
    mayusculas="QWERTYUIOPASDFGHJKLÑZXCVBNM"
    if i in mayusculas:
        return True
    return False


def principal():
    '''1 - determinar la cantidad de palabras que empiecen con digito impar y contenga al menos
una "s" pero no contenga ninguna "p" '''
    r1=0         #Cantidad de palabras
    contador_s=0
    contiene_s=False
    contador_p=0
    r1_comienza_impar=False

    '''2 - calcular la longitud de la menor palabra que contenga una vocal en la segunda posicion de 
la palabra, contenga al menos una "t".'''
    r2=None   #Longitud de la menor palabra
    contiene_t=False
    r2_contiene_vocal_2_pos=False

    '''3 - calcular el porcentaje entero de las palabras (sobre el total de palabras) que contengan mas 
vocales que consonantes.'''
    r3=0   #Porcentaje entero
    r3_contador_palabras=0
    contador_vocales=0
    contador_consonantes=0

    '''4- determinar la cantidad de palabras que contengan la sigla "mp" pero ademas contenga una 
mayuscula en alguno de sus primeros 3 caracteres.
'''
    r4=0
    r4_tiene_m=False
    r4_tiene_mp=False
    r4_tiene_mayuscula=False


    fd= "texto.txt"
    fd= "archivito.txt"
    m= open(fd , "rt")
    linea= m.readline()

    for i in linea:
        contador_caracteres=0
        #Estoy dentro de una palabra
        if i!=" " and i!=".":
            contador_caracteres+=1
            #r1
            digito_impar= validar_impar(i)
            if contador_caracteres==1 and digito_impar:
                r1_comienza_impar=True
            if i=="s":
                contiene_s=True
                contador_s+=1
            if i=="p":
                contador_p+=1
            #r2
            contiene_vocal= validar_vocales(i)
            if contador_caracteres==2 and contiene_vocal:
                r2_contiene_vocal_2_pos=True
            if i=="t":
                contiene_t=True
            #r3
            contiene_consonantes= validar_consonantes(i)
            if contiene_vocal:
                contador_vocales+=1
                r3_contador_palabras+=1
            if contiene_consonantes:
                contador_consonantes+=1
                r3_contador_palabras+=1
            #r4
            tiene_mayuscula= validar_mayusculas(i)
            if r4_tiene_m and i=="p":
                r4_tiene_mp=True
            elif i=="m":
                r4_tiene_m=True
            else:
                r4_tiene_m=False
            if (contador_caracteres==1 or contador_caracteres==2 or contador_caracteres==3) and tiene_mayuscula:
                r4_tiene_mayuscula=True


        #Estoy fuera de una palabra
        else:
            contador_total_palabras = 0
            if i==" " or ".":
                contador_total_palabras+=1
            #r1
            if r1_comienza_impar and contiene_s and contador_p>1:
                r1+=1
            #r2
            #si r2 es nada , o el contador d caracteres es mayor a r2 , entonces r2=contador
            if r2 is None or contador_caracteres>r2:
                r2= contador_caracteres
            #r3
            if contador_vocales>contador_consonantes:
                r3= (r3_contador_palabras*100)// contador_total_palabras
            #r4
            if r4_tiene_mp and r4_tiene_mayuscula:
                r4+=1


            #Apagar banderas,contadores,etc.
            #r1
            contador_s = 0
            contiene_s = False
            contador_p = 0
            r1_comienza_impar = False

            #r2
            contiene_t = False
            r2_contiene_vocal_2_pos = False

            #r3
            r3_contador_palabras = 0
            contador_vocales = 0
            contador_consonantes = 0

            #r4
            r4_tiene_m = False
            r4_tiene_mp = False
            r4_tiene_mayuscula = False

    #Termino el ciclo
    m.close()

    print("1 - Respuesta:", r1)
    print("2 - Respuesta:", r2)
    print("3 - Respuesta:", r3)
    print("4 - Respuesta:", r4)

if __name__ == '__main__':
    principal()
