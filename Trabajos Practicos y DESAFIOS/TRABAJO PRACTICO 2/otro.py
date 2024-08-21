def codigo_postal(cp):
    destino = None
    if len(cp) == 8:
        if "0" <= cp[4] <= "9":
            if "A" <= cp[0] <= "Z":
                destino = "Argentina"
            else:
                destino = "Otro"
    elif len(cp) == 4:
        destino = "Bolivia"
    elif len(cp) == 9:
        if cp[5] == "-":
            destino = "Brasil"
    elif len(cp) == 7:
        destino = "Chile"
    elif len(cp) == 6:
        destino = "Paraguay"
    elif len(cp) == 5:
        if cp[0] == "1":
            destino = "Montevideo"
        else:
            destino = "Uruguay"
    else:
        destino = "Otro"
    return destino


def validar_dir(direccion):
    tiene_mayus = False
    solo_dig = False

    for i in direccion:
        if i != " " and i !=".":
            if tiene_mayus and "A" <= i <= "Z":
                return False
            elif "A" <= i <= "Z":
                tiene_mayus = True
            else:
                tiene_mayus = False

            if not "a" <= i.lower() <= "z" and not "0" <= i <= "9":
                return False

            if i.isdigit():
                solo_dig = True

            if solo_dig:
                if not i.isdigit():
                    return False
    return True


def principal():
    m = open("envios25.txt")
    texto = m.readlines()
    m.close()

    primera_linea = True
    ban_h = False
    ban_s = False
    control = None
    cedvalid = 0
    cedinvalid = 0

    for linea in texto:
        if primera_linea:
            for car in linea:
                if car == "H":
                    ban_h = True
                elif ban_h and car == "C":
                    control = "Hard Control"

                if car == "S":
                    ban_s = True
                elif ban_s and car == "C":
                    control = "Soft Control"
            primera_linea = False

        elif primera_linea == False:
            direccion = linea[9:29].strip()

            if control == "Hard Control":
                if validar_dir(direccion):
                    cedvalid += 1
                else:
                    cedinvalid += 1
            else:
                cedvalid += 1

    print(' (r1) - Tipo de control de direcciones:', control)
    print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
    print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)

principal()
