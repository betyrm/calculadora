def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: División por cero"
    
def mostrar_historial(datos):
    if datos == []:
        print('El historial está vacío')
    else:
        print('--- Historial ---')
        for i, operacion in enumerate(datos):
            print(f'{i}. {operacion[0]} {operacion[2]} {operacion[1]} = {operacion[3]}')
        print('--- ---')