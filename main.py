from opera_principal.operaciones import *
from funciones_consola.otras_funciones import *


def main():
    limpiar_consola()
    historial = []
    print(" CALCULADORA ")
    print("Ingrese dos números para realizar una operación")
    while True:
        numeros : list = cargar_datos()
        opcion : int = mostrar_menu()
        datos : list = realizar_operacion(numeros, opcion, historial)
        if datos[1] == 0:
            break
        print(f'{numeros[0]} {datos[1]} {numeros[1]} = {datos[2]}')
        historial.append(datos)
        

if __name__ == "__main__":
    main()
    
