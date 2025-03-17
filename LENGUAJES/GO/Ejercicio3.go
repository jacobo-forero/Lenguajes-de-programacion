//CAJERO
package main

import (
	"fmt"
)

func main() {
	cajero()
}

func mostrarMenu() {
	fmt.Println("\nBienvenido al cajero")
	fmt.Println("1. Ingresar dinero")
	fmt.Println("2. Retirar dinero")
	fmt.Println("3. Ver saldo")
	fmt.Println("4. Salir")
}

func obtenerMonto(mensaje string) float64 {
	var monto float64
	for {
		fmt.Print(mensaje)
		_, err := fmt.Scan(&monto)
		if err != nil || monto < 0 {
			fmt.Println("El monto debe ser un número positivo. Inténtalo de nuevo.")
			// Limpiar el buffer de entrada
			var dummy string
			fmt.Scanln(&dummy)
		} else {
			return monto
		}
	}
}

func cajero() {
	saldo := 1000.0
	for {
		mostrarMenu()
		var opcion string
		fmt.Print("¿Qué deseas hacer? ")
		fmt.Scan(&opcion)

		switch opcion {
		case "1":
			monto := obtenerMonto("¿Cuánto dinero deseas ingresar? $")
			saldo += monto
			fmt.Printf("Se ha ingresado $%.2f a tu cuenta. Tu saldo actual es $%.2f.\n", monto, saldo)

		case "2":
			monto := obtenerMonto("¿Cuánto dinero deseas retirar? $")
			if monto <= saldo {
				saldo -= monto
				fmt.Printf("Se ha retirado $%.2f de tu cuenta. Tu saldo actual es $%.2f.\n", monto, saldo)
			} else {
				fmt.Println("Error: No tienes suficiente saldo para realizar esta operación.")
			}

		case "3":
			fmt.Printf("Tu saldo actual es $%.2f.\n", saldo)

		case "4":
			fmt.Println("Gracias por utilizar el cajero.")
			return

		default:
			fmt.Println("Opción no válida. Por favor, intenta de nuevo.")
		}
	}
}