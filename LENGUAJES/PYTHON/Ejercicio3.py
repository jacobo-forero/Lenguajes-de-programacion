#CAJERO

def mostrar_menu():
    print("\nBienvenido al cajero")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Ver saldo")
    print("4. Salir")

def obtener_monto(mensaje):
    while True:
        try:
            monto = float(input(mensaje))
            if monto < 0:
                print("El monto debe ser un número positivo. Inténtalo de nuevo.")
            else:
                return monto
        except ValueError:
            print("Error, por favor ingrese un número válido.")

def cajero():
    saldo = 1000
    while True:
        mostrar_menu()
        opcion = input("¿Qué deseas hacer? ")
        
        if opcion == "1":
            monto = obtener_monto("¿Cuánto dinero deseas ingresar? $")
            saldo += monto
            print(f"Se ha ingresado ${monto:.2f} a tu cuenta. Tu saldo actual es ${saldo:.2f}.")
        
        elif opcion == "2":
            monto = obtener_monto("¿Cuánto dinero deseas retirar? $")
            if monto <= saldo:
                saldo -= monto
                print(f"Se ha retirado ${monto:.2f} de tu cuenta. Tu saldo actual es ${saldo:.2f}.")
            else:
                print("Error: No tienes suficiente saldo para realizar esta operación.")
        
        elif opcion == "3":
            print(f"Tu saldo actual es ${saldo:.2f}.")
        
        elif opcion == "4":
            print("Gracias por utilizar el cajero.")
            break
        
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
cajero()