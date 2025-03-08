#FUNCIONES

def obtener_nombre():
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if nombre:
            return nombre
        else:
            print("El nombre no puede estar vacío. Inténtalo de nuevo.")

def saludo(nombre):
    print(f"Hola {nombre}, bienvenido/a!")

def main():
    while True:
        nombre = obtener_nombre()
        saludo(nombre)
        
        continuar = input("¿Deseas saludar a otra persona? (s/n): ").strip().lower()
        if continuar != 's':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
main()