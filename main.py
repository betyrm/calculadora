from operaciones import *
from otras_funciones import *


def main():
    limpiar_consola()
    historial = []
    control = True
    while True:
        datos = list(pide_datos())
        print (datos)
        if datos == []:
             print('Debe ingresar  números')
             break
        muestra_menu()
        opcion = input('Elige una opcion (0-4): ')
        
        resultado = 0
        match opcion:
            case '1':
                resultado = suma(datos[0], datos[1])
                datos.append('+')
            case '2':
                resultado = resta(datos[0], datos[1])
                datos.append('-')
            case '3':
                resultado = multiplica(datos[0], datos[1])
                datos.append('*')
            case '4':
                resultado = divide(datos[0], datos[1])
                datos.append('/')
            case '5':
                muestra_historial(historial)
                continue
            case '0':
                print('Saliendo del menu ')
                control = False
                break
            case _:
                print('Opción inválida')
                control = False
        if control:
            datos.append(resultado)      
            print(f'{datos[0]} {datos[2]} {datos[1]} = {datos[3]}')
            historial.append(datos)
        

if __name__ == "__main__":
    main()
    
