import os

from termcolor import colored

def limpiar_consola():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')

def pedir_datos() -> float:
    try:
        return float(input('Ingrese un número '))
    except ValueError as ex:
        print('Debe ser un número decimal', ex)
        return pedir_datos()
    
def cargar_datos() -> list[float]:
    datos_operacion: list[float] = []
    while len(datos_operacion) < 2:
            datos_operacion.append(pedir_datos())
    return datos_operacion

def mostrar_menu():
    text = colored('\n--- Elige una operación ---', 'red', attrs=['reverse'])
    print(text)
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División')
    print('5. Muestra Historial')
    print('0. Salir')
    opcion = input('Elige una opcion (0-5): ')
    return opcion
  
    
