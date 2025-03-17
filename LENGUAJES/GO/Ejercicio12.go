//TABLA DE LA VERDAD

package main

import (
	"fmt"
)

func generarCombinaciones(variables []string) [][]bool {
	// Genera todas las combinaciones de valores booleanos para las variables dadas.
	n := len(variables)
	combinaciones := make([][]bool, 0)

	for i := 0; i < (1 << n); i++ {
		combinacion := make([]bool, n)
		for j := 0; j < n; j++ {
			combinacion[j] = (i & (1 << j)) != 0
		}
		combinaciones = append(combinaciones, combinacion)
	}
	return combinaciones
}

func imprimirTablaVerdad(variables []string) {
	// Imprime la tabla de verdad para la operación A y B.
	combinaciones := generarCombinaciones(variables)

	// Imprimimos la cabecera de la tabla
	fmt.Printf("%s | %s\n", join(variables, " | "), join(variables, " y "))
	fmt.Println(strings.Repeat("-", len(variables)*4+10)) // Ajusta el ancho de la línea

	// Evaluamos la expresión para cada combinación
	for _, combinacion := range combinaciones {
		resultado := true
		for _, val := range combinacion {
			resultado = resultado && val // A y B
		}
		fmt.Printf("%s | %v\n", joinBool(combinacion), resultado)
	}
}

func join(arr []string, sep string) string {
	result := ""
	for i, s := range arr {
		result += s
		if i < len(arr)-1 {
			result += sep
		}
	}
	return result
}

func joinBool(arr []bool) string {
	result := ""
	for i, b := range arr {
		result += fmt.Sprintf("%v", b)
		if i < len(arr)-1 {
			result += " | "
		}
	}
	return result
}

func main() {
	// Definimos las variables
	variables := []string{"A", "B"}
	imprimirTablaVerdad(variables)
}