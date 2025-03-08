#Bucles WHILE

def obtener_numero():
    while True:
        try:
            num = int(input("Ingrese un número para conocer la tabla de multiplicar: "))
            return num
        except ValueError:
            print("Error, por favor ingrese un número entero.")

def mostrar_tabla(num):
    print(f"\nTabla de multiplicar del {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def main():
    while True:
        numero = obtener_numero()
        mostrar_tabla(numero)
        
        continuar = input("\n¿Desea calcular otra tabla? (s/n): ").strip().lower()
        if continuar != 's':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
main()