



def main():
    m = open("entrada.txt")
    linea = m.read()
    indice = 0
    print(linea)

    cont = 0
    if True: cont += 1

    # g. Determinar cuántas palabras empiezan con una vocal, terminan con la letra "s", y poseen un
    # digito en tercera o en quinta. ()
    rg = 0
    rg_empieza_vocal = False
    rg_termina_s = ""
    rg_digito_pos35 = False

    for i in linea:
        if i != " " and i != ".":
            indice += 1

            # PUNTO G
            rg_termina_s = i.lower()

            if i.lower() in "aeiou" and indice == 1:
                rg_empieza_vocal = True
            if i in "0123456789" and (indice == 3 or indice == 5):
                rg_digito_pos35 = True

        else:
            # g
            if rg_termina_s.lower() == "s" and rg_empieza_vocal and rg_digito_pos35:
                rg += 1

            # g
            indice = 0
            rg_empieza_vocal = False
            rg_digito_pos35 = False

    print("G- resultado:", rg)

main()