#Bucles FOR

def mostrar_palabra():
    # Solicitar al usuario que ingrese una palabra
    palabra = input("Ingrese la palabra que quiere que se repita: ").strip()
    
    # Validar que la palabra no esté vacía
    while not palabra:
        print("La entrada no puede estar vacía. Inténtalo de nuevo.")
        palabra = input("Ingrese la palabra que quiere que se repita: ").strip()
    
    # Solicitar al usuario cuántas veces quiere que se repita la palabra
    while True:
        try:
            repeticiones = int(input("¿Cuántas veces quiere que se repita la palabra? "))
            if repeticiones <= 0:
                print("Por favor, ingrese un número positivo.")
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
            
    # Imprimir la palabra la cantidad de veces especificada
    for _ in range(repeticiones):
        print(palabra)
mostrar_palabra()