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
            numero1, numero2 = operacion[0]
            print(f'{i}. {numero1} {operacion[1]} {numero2} = {operacion[2]}')
        print('--- ---')

def realizar_operacion(numeros: list, opcion: int, historial: list):
    datos = []
    datos.append(numeros)
    resultado : float = 0
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
        case '0':
            print('Saliendo del menu ')
       
    datos.append(resultado)
    return datos