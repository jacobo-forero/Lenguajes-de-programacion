//BUCLES FOR
package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	mostrarPalabra()
}

func mostrarPalabra() {
	var palabra string
	fmt.Print("Ingrese la palabra que quiere que se repita: ")
	fmt.Scanln(&palabra)
	palabra = strings.TrimSpace(palabra)


	for palabra == "" {
		fmt.Println("La entrada no puede estar vacía. Inténtalo de nuevo.")
		fmt.Print("Ingrese la palabra que quiere que se repita: ")
		fmt.Scanln(&palabra)
		palabra = strings.TrimSpace(palabra)
	}

	var repeticiones int
	for {
		fmt.Print("¿Cuántas veces quiere que se repita la palabra? ")
		var input string
		fmt.Scanln(&input)
		var err error
		repeticiones, err = strconv.Atoi(input)
		if err != nil || repeticiones <= 0 {
			fmt.Println("Entrada no válida. Por favor, ingrese un número entero positivo.")
		} else {
			break
		}
	}

	for i := 0; i < repeticiones; i++ {
		fmt.Println(palabra)
	}
}