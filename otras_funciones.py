import os


def limpiar_consola():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')

def pide_datos():
    numeros = []
    nro1 = float(input('Ingrese el primer número para la operación '))
    if type(nro1) == float:
        numeros.append(nro1)
    else:
        print('Error: Debe ingresar un número')
        return []
    nro2= float(input('Ingrese el segundo número para la operación '))
    if type(nro2) == float:
        numeros.append(nro2)
    else:
        print('Error: Debe ingresar un número')
        return []
    
    return(numeros)


def muestra_menu():
    
    print('\n--- Elige una operación ---')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División')
    print('5. Muestra Historial')
    print('0. Salir')