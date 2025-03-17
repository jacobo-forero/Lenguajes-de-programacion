//FUNCIONES
package main

import (
	"fmt"
	"strings"
)

func main() {
	for {
		nombre := obtenerNombre()
		saludo(nombre)

		var continuar string
		fmt.Print("¿Deseas saludar a otra persona? (s/n): ")
		fmt.Scanln(&continuar)
		if strings.ToLower(continuar) != "s" {
			fmt.Println("Gracias por usar el programa. ¡Hasta luego!")
			break
		}
	}
}

func obtenerNombre() string {
	var nombre string
	for {
		fmt.Print("Ingrese su nombre: ")
		fmt.Scanln(&nombre)
		nombre = strings.TrimSpace(nombre)
		if nombre != "" {
			return nombre
		} else {
			fmt.Println("El nombre no puede estar vacío. Inténtalo de nuevo.")
		}
	}
}

func saludo(nombre string) {
	fmt.Printf("Hola %s, bienvenido/a!\n", nombre)
}