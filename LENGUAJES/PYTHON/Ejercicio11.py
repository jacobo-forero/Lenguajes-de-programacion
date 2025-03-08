#OPERACIONES

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "No se puede dividir entre cero"

def potencia(num1, num2):
    return num1 ** num2

def main():
    while True:
        print("\nCalculadora")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == '6':
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break

        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            print("Resultado de la suma:", suma(num1, num2))
        elif opcion == '2':
            print("Resultado de la resta:", resta(num1, num2))
        elif opcion == '3':
            print("Resultado de la multiplicación:", multiplicacion(num1, num2))
        elif opcion == '4':
            resultado = division(num1, num2)
            print("Resultado de la división:", resultado)
        elif opcion == '5':
            print("Resultado de la potencia:", potencia(num1, num2))
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")
main()