

"""

Desarrolle un programa o script Python que permita cargar por teclado un número entero que representa la
cantidad de segundos que pasaron desde un evento dado.  El programa debe convertir esa cantidad de segundos
a la cantidad de horas, minutos y segundos que transcurrieron. Por ejemplo, si la cantidad de segundos
ingresada es 4452 deberá mostrar un mensaje que informe que el tiempo transcurrido fue de 1 hora, 14 minutos
y 12 segundos. Pero la conversión solo debe mostrarse si la cantidad de horas totales obtenida
es menor o igual a 24. Si esa cantidad de horas totales es mayor a 24,
el programa debe mostrar un mensaje de la forma "Excedido". Se le pedirá comprobar su programa para cuatro
cantidades de segundos, que deberá cargar por teclado.

Además, el desafío incluye una consigna adicional, en la cual se le pedirá que haga el proceso inverso:
deberá tomar tres datos, que serán el valor en horas, el valor en minutos y el valor en segundos transcurridos
desde un evento dado, y su programa deberá calcular la cantidad total de segundos a partir de esos datos.
Por ejemplo, si los datos ingresados fuesen: horas = 4, minutos = 36 y segundos = 8 entonces el resultado
a obtener es que la cantidad total de segundos es 16568.

"""


def inverso():
    # int(input("ingresar valor "))
    horas = 1
    minutos = 14
    segundos = 12

    total_segundos = horas * 3600 + minutos * 60 + segundos
    print(total_segundos)


def principal():
    """
    si la cantidad de segundos ingresada es 4452 deberá mostrar un mensaje que informe que el
    tiempo transcurrido fue de 1 hora, 14 minutos y 12 segundos. Pero la conversión solo debe
    mostrarse si la cantidad de horas totales obtenida es menor o igual a 24.
    """

    # inverso()
    # return

    # 60 segundos = 1minuto
    # 60 minutos = 1 hora   = 3600 segundos

    # segundos = int(input("Ingresar segundos: "))
    total = 4452

    horas = total // 3600

    total -= 3600 * horas    # restar la cantidad horas multiplicada por la cantidad de segundos

    minutos = total // 60     # para obtener la cantidad de minutos

    total -= 60 * minutos

    segundos = total

    if horas > 24:
        print("EXCEDIDO")

    else:
        print("horas:", horas)
        print("minutos:", minutos)
        print("segundos:", segundos)

    # teorema del resto
    # minutos = (segundos % 3600) // 60
    # segundos = (segundos % 3600) % 60


if __name__ == '__main__':
    principal()
