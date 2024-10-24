def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplica(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: División por cero"
    
def muestra_historial(datos):
    if datos == []:
        print('El historial está vacío')
    else:
        print('--- Historial ---')
        for i, operacion in enumerate(datos):
            print(f'{i}. {operacion[0]} {operacion[2]} {operacion[1]} = {operacion[3]}')
        print('--- ---')