//OPERACIONES
package main

import (
	"fmt"
)

func suma(num1, num2 float64) float64 {
	return num1 + num2
}

func resta(num1, num2 float64) float64 {
	return num1 - num2
}

func multiplicacion(num1, num2 float64) float64 {
	return num1 * num2
}

func division(num1, num2 float64) string {
	if num2 != 0 {
		return fmt.Sprintf("%.2f", num1/num2)
	} else {
		return "No se puede dividir entre cero"
	}
}

func potencia(num1, num2 float64) float64 {
	resultado := 1.0
	for i := 0; i < int(num2); i++ {
		resultado *= num1
	}
	return resultado
}

func main() {
	for {
		fmt.Println("\nCalculadora")
		fmt.Println("1. Suma")
		fmt.Println("2. Resta")
		fmt.Println("3. Multiplicación")
		fmt.Println("4. División")
		fmt.Println("5. Potencia")
		fmt.Println("6. Salir")

		var opcion string
		fmt.Print("Selecciona una opción (1-6): ")
		fmt.Scanln(&opcion)

		if opcion == "6" {
			fmt.Println("Gracias por usar la calculadora. ¡Hasta luego!")
			break
		}

		var num1, num2 float64
		fmt.Print("Ingresa el primer número: ")
		fmt.Scanln(&num1)
		fmt.Print("Ingresa el segundo número: ")
		fmt.Scanln(&num2)

		switch opcion {
		case "1":
			fmt.Printf("Resultado de la suma: %.2f\n", suma(num1, num2))
		case "2":
			fmt.Printf("Resultado de la resta: %.2f\n", resta(num1, num2))
		case "3":
			fmt.Printf("Resultado de la multiplicación: %.2f\n", multiplicacion(num1, num2))
		case "4":
			resultado := division(num1, num2)
			fmt.Printf("Resultado de la división: %s\n", resultado)
		case "5":
			fmt.Printf("Resultado de la potencia: %.2f\n", potencia(num1, num2))
		default:
			fmt.Println("Opción no válida. Por favor, selecciona una opción del 1 al 6.")
		}
	}
}