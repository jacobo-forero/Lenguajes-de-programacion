#Condicionales IF, ELSE

def obtener_edad():
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if edad < 0:
                print("La edad no puede ser negativa. Inténtalo de nuevo.")
            else:
                return edad
        except ValueError:
            print("Error, por favor ingresa un número entero válido.")

def mayoria_edad():
    edad = obtener_edad()
    
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
mayoria_edad()