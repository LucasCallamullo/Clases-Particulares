def principal():
    archivo = "expresiones.txt"

    # Diccionario que relaciona cierres con sus aperturas correspondientes
    pares = {')': '(', ']': '[', '}': '{'}

    with open(archivo, "rt") as f:
        for linea in f:
            expresion = linea.strip()
            print(expresion)

            pila = []

            for char in expresion:
                # Si es un símbolo de apertura, lo apilamos
                if char in pares.values():
                    pila.append(char)

                # Si es un símbolo de cierre, comprobamos la correspondencia
                elif char in pares:
                    if not pila:
                        print("Sobran cierres")
                        break
                    if pila.pop() != pares[char]:
                        print("Desequilibrio interno")
                        break
            else:
                # Solo se ejecuta si el bucle no se rompió con 'break'
                if pila:
                    print("Sobran aperturas")
                else:
                    print("ok")

            print("\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    principal()