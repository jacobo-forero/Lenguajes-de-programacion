//CICLO FOR

package main

import (
	"fmt"
)

func main() {
	inversion()
}

func obtenerFloat(mensaje string) float64 {
	var valor float64
	for {
		fmt.Print(mensaje)
		_, err := fmt.Scan(&valor)
		if err != nil || valor < 0 {
			fmt.Println("El valor debe ser un número positivo. Inténtalo de nuevo.")
			// Limpiar el buffer de entrada
			var dummy string
			fmt.Scanln(&dummy)
		} else {
			return valor
		}
	}
}

func obtenerInt(mensaje string) int {
	var valor int
	for {
		fmt.Print(mensaje)
		_, err := fmt.Scan(&valor)
		if err != nil || valor < 0 {
			fmt.Println("El valor debe ser un número entero positivo. Inténtalo de nuevo.")
			// Limpiar el buffer de entrada
			var dummy string
			fmt.Scanln(&dummy)
		} else {
			return valor
		}
	}
}

func inversion() {
	cant := obtenerFloat("Ingrese la cantidad a invertir: $")
	inter := obtenerFloat("Ingrese el interés anual (en %): ")
	años := obtenerInt("Ingrese el número de años: ")
	
	fmt.Println("\nResumen de la inversión:")
	for i := 1; i <= años; i++ {
		cant += cant * (inter / 100)
		fmt.Printf("Año %d: Capital obtenido será: $%.2f\n", i, cant)
	}
}