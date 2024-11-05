from opera_principal import *
from funciones_consola import *


def main():
    limpiar_consola()
    historial = []
    numeros = list(pedir_datos())
    if numeros == []:
        print('Debe ingresar  números')
    else:  
        datos = []
        while True:
            mostrar_menu()
            opcion = input('Elige una opcion (0-4): ')
            resultado = 0
            datos = []
            datos.append(numeros[0])
            datos.append(numeros[1])
            match opcion:
                case '1':
                    resultado = sumar(numeros[0], numeros[1])
                    datos.append('+')
                case '2':
                    resultado = restar(numeros[0], numeros[1])
                    datos.append('-')
                case '3':
                    resultado = multiplicar(numeros[0], numeros[1])
                    datos.append('*')
                case '4':
                    resultado = dividir(numeros[0], numeros[1])
                    datos.append('/')
                case '5':
                    mostrar_historial(historial)
                    continue
                case '0':
                    print('Saliendo del menu ')
                    break
                case _:
                    print('Opción inválida')
                    continue
        
            datos.append(resultado)      
            print(f'{datos[0]} {datos[2]} {datos[1]} = {datos[3]}')
            historial.append(datos)
           

if __name__ == "__main__":
    main()
    
