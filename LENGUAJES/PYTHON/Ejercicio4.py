#CICLO FOR

def obtener_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("El valor debe ser un número positivo. Inténtalo de nuevo.")
            else:
                return valor
        except ValueError:
            print("Error, por favor ingrese un número válido.")

def obtener_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("El valor debe ser un número entero positivo. Inténtalo de nuevo.")
            else:
                return valor
        except ValueError:
            print("Error, por favor ingrese un número válido.")

def inversion():
    cant = obtener_float("Ingrese la cantidad a invertir: $")
    inter = obtener_float("Ingrese el interés anual (en %): ")
    años = obtener_int("Ingrese el número de años: ")
    
    print("\nResumen de la inversión:")
    for i in range(1, años + 1):
        cant += cant * (inter / 100)
        print(f"Año {i}: Capital obtenido será: ${cant:.2f}")       
inversion()