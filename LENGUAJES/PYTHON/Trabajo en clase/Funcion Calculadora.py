#Funciones para indicar que que operacion se utilizara
def suma(a, b):
    return a + b 

def resta(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def exp(a, b):
    return a ** b

#Funcion para crear el bucle de la calculadora
def calculadora():
    while True:
        print("\n--- Calculadora en PYTHOM ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. Diviión")
        print("5. Exponente")
        print("6. Salir")

        #Input para seleccionar la opción
        opcion = input("Seleccione una opción (1-6): ")

        #Opcion 6: Salir del programa
        if opcion == "6":
            print("Saliendo de la calculadora...")
            break
        
        #Opcion que reconoce los elementos de la tabla y si el digito ingresado no esta, no inicia 
        if opcion not in ["1", "2", "3", "4", "5"]:
            print("Opcion no valida. Intente de nuevo.")
            continue

        #Try para ingresar los datos, tanto de la tabla como de la calculadora
        try:
            num1 = float(input("Ingrese el primer digito: "))
            num2 = float(input("Ingrese el segundo digito: "))

            operaciones = {
                "1": suma,
                "2": resta,
                "3": mul,
                "4": div,
                "5": exp
            }

            resultado = operaciones[opcion](num1, num2)
            print(f"Resultado {resultado}")

        except ValueError:
            print("Error: Ingrese un solo números validos")

calculadora()