//BUCLES WHILE

package main

import (
	"fmt"
	"strconv"
)

func main() {
	for {
		numero := obtenerNumero()
		mostrarTabla(numero)

		var continuar string
		fmt.Print("\n¿Desea calcular otra tabla? (s/n): ")
		fmt.Scanln(&continuar)
		if continuar != "s" {
			fmt.Println("Gracias por usar el programa. ¡Hasta luego!")
			break
		}
	}
}

func obtenerNumero() int {
	for {
		fmt.Print("Ingrese un número para conocer la tabla de multiplicar: ")
		var input string
		fmt.Scanln(&input)
		num, err := strconv.Atoi(input)
		if err == nil {
			return num
		}
		fmt.Println("Error, por favor ingrese un número entero.")
	}
}

func mostrarTabla(num int) {
	fmt.Printf("\nTabla de multiplicar del %d:\n", num)
	for i := 1; i <= 10; i++ {
		fmt.Printf("%d x %d = %d\n", num, i, num*i)
	}
}