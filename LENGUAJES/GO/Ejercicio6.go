//DICCIONARIO
package main

import (
	"fmt"
	"strings"
)

func main() {
	conversor()
}

func obtenerDivisas() map[string]string {
	return map[string]string{
		"Dollar": "$",
		"Euro":   "€",
		"Yen":    "¥",
		"Peso":   "$",
	}
}

func conversor() {
	divisas := obtenerDivisas()
	
	for {
		var divisa string
		fmt.Print("Ingrese el tipo de divisa (o 'salir' para terminar): ")
		fmt.Scanln(&divisa)
		divisa = strings.Title(divisa) // Capitaliza la primera letra

		if strings.ToLower(divisa) == "salir" {
			fmt.Println("Gracias por usar el conversor de divisas. ¡Hasta luego!")
			break
		}
		
		if valor, ok := divisas[divisa]; ok {
			fmt.Println("Esta es la divisa:", valor)
		} else {
			fmt.Println("Divisa no encontrada. Por favor, intenta de nuevo.")
		}
	}
}