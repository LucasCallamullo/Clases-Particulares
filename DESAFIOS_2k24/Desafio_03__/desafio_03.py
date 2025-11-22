
import generador


class FrecuenciaPalabra:
    def __init__(self, palabra, cantidad):
        self.palabra = palabra
        self.cantidad = cantidad

    def __str__(self):
        c = "Palabra: " + self.palabra + " | Cantidad: " + str(self.cantidad)
        return c


def principal():

    v_frecuencias = []
    palabras = [
        "libro", "ventana", "cielo", "mariposa", "camino", "esperanza",
        "nube", "sol", "luz", "silencio", "noche", "flor"
    ]
    matriz = generador.generar_matriz(palabras)

    for palabra in palabras:
        frecuencia = FrecuenciaPalabra(palabra, 0)
        tamano = len(palabra)

        for f in range(64):

            for c in range(64-tamano):
                palabra_temp = ""

                for i in range(tamano):
                    palabra_temp += matriz[f][c+i]

                if palabra_temp == frecuencia.palabra:
                    frecuencia.cantidad += 1

        for c in range(64):
            for f in range(64-tamano):
                palabra_temp = ""

                for i in range(tamano):
                    palabra_temp += matriz[f+i][c]

                if palabra_temp == frecuencia.palabra:
                    frecuencia.cantidad += 1

        v_frecuencias.append(frecuencia)

    for frecuencia in v_frecuencias:
        print(frecuencia)



if __name__ == '__main__':
    principal()