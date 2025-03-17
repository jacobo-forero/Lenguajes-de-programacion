//Condicionales IF, ELSE
package main

import (
	"fmt"
)

func main() {
	mayoriaEdad()
}

func obtenerEdad() int {
	var edad int
	for {
		fmt.Print("Ingresa tu edad: ")
		_, err := fmt.Scan(&edad)
		if err != nil || edad < 0 {
			fmt.Println("La edad no puede ser negativa. Inténtalo de nuevo.")
			// Limpiar el buffer de entrada
			var dummy string
			fmt.Scanln(&dummy)
		} else {
			return edad
		}
	}
}

func mayoriaEdad() {
	edad := obtenerEdad()
	
	if edad >= 18 {
		fmt.Println("Eres mayor de edad.")
	} else {
		fmt.Println("Eres menor de edad.")
	}
}