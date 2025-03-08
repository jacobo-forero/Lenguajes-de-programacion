#LEY OHM

def obtener_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo. Inténtalo de nuevo.")
            else:
                return valor
        except ValueError:
            print("Error: Debes ingresar un número válido.")

def calcularLeyOhm():
    print("Calculadora de la Ley de Ohm")
    
    while True:
        print("\nSelecciona la variable que deseas calcular:")
        print("1. Voltaje (V)")
        print("2. Corriente (I)")
        print("3. Resistencia (R)")
        print("4. Salir")

        opcion = input("Ingresa el número de la opción (1, 2, 3 o 4): ")

        if opcion == '1':
            I = obtener_float("Ingresa la corriente (I) en amperios: ")
            R = obtener_float("Ingresa la resistencia (R) en ohmios: ")
            V = I * R
            print(f"El voltaje (V) es: {V:.2f} voltios")

        elif opcion == '2':
            V = obtener_float("Ingresa el voltaje (V) en voltios: ")
            R = obtener_float("Ingresa la resistencia (R) en ohmios: ")
            I = V / R
            print(f"La corriente (I) es: {I:.2f} amperios")

        elif opcion == '3':
            V = obtener_float("Ingresa el voltaje (V) en voltios: ")
            I = obtener_float("Ingresa la corriente (I) en amperios: ")
            R = V / I
            print(f"La resistencia (R) es: {R:.2f} ohmios")

        elif opcion == '4':
            print("Gracias por usar la calculadora de la Ley de Ohm. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, selecciona 1, 2, 3 o 4.")
calcularLeyOhm()