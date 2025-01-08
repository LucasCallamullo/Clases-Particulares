from soporteTP3 import *

def main():

    fd = "envios-tp3.txt"


    #linea = archivo.readline()
    # control = 'Soft Control'
    # if 'HC' in linea:
    #     control = 'Hard Control'

    envios = []
    opc = -1
    
    while opc != 0:

        print("1- cargar registro de todos los datos de los envios del archivo")
        print("2- Cargar por teclado los datos de un envio")
        # print("3-Mostrar todos los registros/objetos del arreglo.")
        # print("4- busqueda por direccion de envio")
        # print("5- busqueda por codigo postal.")
        # print("6- cantidad de envios con direccion de envio valida segun HC o SC.")
        # print("7- importe final acumulado con vector conteo segun HC o SC.")
        # print("8- tipo de envio con mayor importe final acumulado.")
        # print("9- importe final promedio.")
        print("0 - salir")
        opc = int(input("ingrese la opcion:"))

        if opc == 1:
            if len(envios) > 0:
                borrar(envios, fd)

            else:
                cargar_envios_archivo(envios, fd)


            # envios = borrar(envios,archivo)

        if opc == 2:

            # if envios:
            # if len(envios) > 0:
            if envios != []:
            
                print("a continuacion ingrese los datos del envio:")
                cp = int(input("Codigo postal:" ))
                direccion = int(input("Direccion:" ))
                tipo = validar_tipo_envio()
                pago = validar_forma_pago()
                
                cargar_envios_teclado(envios,cp,direccion,tipo,pago)
                for envio in envios:
                    print(envio)
            else:
                print('Debe cargar el arreglo de envios antes')

        if opc == 3:
            for i in envios:
                print(i)
            print("Se mostraron un total de:", len(envios))

        # if opc == 4:
       
        # if opc == 5:
        
        # if opc == 6:
        
        # if opc == 7:
        
        # if opc == 8:
        
        # if opc == 9:
        
    archivo.close()
    
if __name__ == '__main__':
    main()
