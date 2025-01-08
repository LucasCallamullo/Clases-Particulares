class Envio:
    def __init__(self, cp, direccion, tipo, pago):
        self.cp = cp
        self.direccion = direccion
        self.tipo_envio = tipo
        self.forma_pago = pago    
        
    def __str__(self):
        cad = "codigo postal: " + str(self.cp) +"  -  "+ "direccion: " + str(self.direccion) +"  -  "+ "tipo de envio: " + str(self.tipo_envio) + "  -  " + "forma de pago: " + str(self.forma_pago)
        return cad



#PUNTO 1
def cargar_envios_archivo(envios, fd):
    archivo = open(fd, 'rt')

    for linea in archivo:
        # No es necesaria
        if len(linea) >= 31 or len(linea) == 0: #mayor o igual a 31 para que no lea la primer linea ó == a 0 para cuando se borra el arrelgo
            cp = linea[0:9].strip().upper()
            direccion = linea[9:29].strip()
            tipo = int(linea[29])
            pago = int(linea[30])
            envio = Envio(cp,direccion,tipo,pago) #crea el envio
            envios.append(envio) #lo agrega al arreglo envio

    archivo.close()
    print("Se cargaron la cantidad de registros:", len(envios))


def borrar(envios, fd):
    if len(envios) > 0:
        opcion = int(input("Ingrese 1 si desea borrar el arreglo, de lo contrario, ingrese 0: "))

        if opcion == 1:
            print("el arreglo viejo fue borrado con exito")
            envios.clear()          #limpia el archivo
            # envios = []
            cargar_envios_archivo(envios, fd)
            # return envios
        else:
            print("La operacion fue cancelada")
            # return envios

    # archivo.seek(0) #vuelve a leer el archivo

# PUNTO 2
# def validar_tipo_envio(lim_inf, lim_sup, mensaje1, mensaje2):
def validar_tipo_envio():
    tipo = int(input('Ingrese el tipo de envio: '))
    while (tipo < 0  or tipo > 6):
        tipo = int(input('Error: Ingrese un tipo de envio correcto (entre 0 y 6): '))
    return tipo

def validar_forma_pago():
    fp = int(input('Ingrese una forma de pago: '))
    while (fp < 1  or fp > 2):
        fp = int(input('Error: Ingrese una forma de pago correcta (1 o 2): '))
    return fp

def cargar_envios_teclado(envios,cp,direccion,tipo,pago):

    envio = Envio(cp,direccion,tipo,pago)
    envios.append(envio)
    