#Interaccion Usuario

import random

def obtener_adivinanza():
    while True:
        try:
            adivinar = int(input("Adivina el número del 1 al 10: "))
            if 1 <= adivinar <= 10:
                return adivinar
            else:
                print("Por favor, ingresa un número entre 1 y 10.")
        except ValueError:
            print("Error: Debes ingresar un número entero.")

def jugar():
    num = random.randint(1, 10)
    intentos = 3  # Número de intentos permitidos

    print("Tienes 3 intentos para adivinar el número.")
    
    for i in range(intentos):
        adivinar = obtener_adivinanza()
        
        if num == adivinar:
            print("¡Has ganado!")
            return
        else:
            print(f"Intento {i + 1} fallido.")
    
    print(f"Has perdido, el número era: {num}")

def main():
    while True:
        jugar()
        continuar = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if continuar != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break
main()