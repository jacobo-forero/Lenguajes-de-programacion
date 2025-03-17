//LEY OHM
package main

import (
	"fmt"
)

func main() {
	calcularLeyOhm()
}

func obtenerFloat(mensaje string) float64 {
	var valor float64
	for {
		fmt.Print(mensaje)
		_, err := fmt.Scan(&valor)
		if err != nil || valor < 0 {
			fmt.Println("El valor no puede ser negativo. Inténtalo de nuevo.")
			// Limpiar el buffer de entrada
			var dummy string
			fmt.Scanln(&dummy)
		} else {
			return valor
		}
	}
}

func calcularLeyOhm() {
	fmt.Println("Calculadora de la Ley de Ohm")
	
	for {
		fmt.Println("\nSelecciona la variable que deseas calcular:")
		fmt.Println("1. Voltaje (V)")
		fmt.Println("2. Corriente (I)")
		fmt.Println("3. Resistencia (R)")
		fmt.Println("4. Salir")

		var opcion string
		fmt.Print("Ingresa el número de la opción (1, 2, 3 o 4): ")
		fmt.Scanln(&opcion)

		switch opcion {
		case "1":
			I := obtenerFloat("Ingresa la corriente (I) en amperios: ")
			R := obtenerFloat("Ingresa la resistencia (R) en ohmios: ")
			V := I * R
			fmt.Printf("El voltaje (V) es: %.2f voltios\n", V)

		case "2":
			V := obtenerFloat("Ingresa el voltaje (V) en voltios: ")
			R := obtenerFloat("Ingresa la resistencia (R) en ohmios: ")
			I := V / R
			fmt.Printf("La corriente (I) es: %.2f amperios\n", I)

		case "3":
			V := obtenerFloat("Ingresa el voltaje (V) en voltios: ")
			I := obtenerFloat("Ingresa la corriente (I) en amperios: ")
			R := V / I
			fmt.Printf("La resistencia (R) es: %.2f ohmios\n", R)

		case "4":
			fmt.Println("Gracias por usar la calculadora de la Ley de Ohm. ¡Hasta luego!")
			return

		default:
			fmt.Println("Opción no válida. Por favor, selecciona 1, 2, 3 o 4.")
		}
	}
}