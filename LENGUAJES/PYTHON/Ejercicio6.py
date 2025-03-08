#DICCIONARIO

def obtener_divisas():
    return {
        'Dollar': '$',
        'Euro': '€',
        'Yen': '¥',
        'Peso': '$'
    }

def conversor():
    divisas = obtener_divisas()
    
    while True:
        divisa = input("Ingrese el tipo de divisa (o 'salir' para terminar): ").capitalize()
        
        if divisa.lower() == 'salir':
            print("Gracias por usar el conversor de divisas. ¡Hasta luego!")
            break
        
        if divisa in divisas:
            print("Esta es la divisa:", divisas[divisa])
        else:
            print("Divisa no encontrada. Por favor, intenta de nuevo.")
conversor()