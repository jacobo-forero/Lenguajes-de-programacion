//LISTAS
package main

import (
	"fmt"
	"strings"
)

func main() {
	lista := []string{"Matematicas", "Fisica", "Quimica", "Historia", "Lengua"}
	mostrar(lista)

	for {
		var continuar string
		fmt.Print("¿Deseas agregar una nueva materia? (s/n): ")
		fmt.Scanln(&continuar)
		continuar = strings.ToLower(continuar)

		if continuar == "s" {
			agregarMateria(&lista)
			mostrar(lista)
		} else if continuar == "n" {
			fmt.Println("Gracias por usar el programa. ¡Hasta luego!")
			break
		} else {
			fmt.Println("Opción no válida. Por favor, ingresa 's' o 'n'.")
		}
	}
}

func mostrar(materias []string) {
	if len(materias) > 0 {
		fmt.Printf("Yo estudio %d materias.\n", len(materias))
		fmt.Println("Las materias son:")
		for _, materia := range materias {
			fmt.Printf("- %s\n", materia)
		}
	} else {
		fmt.Println("No hay materias para mostrar.")
	}
}

func agregarMateria(materias *[]string) {
	var nuevaMateria string
	fmt.Print("Ingresa el nombre de la nueva materia: ")
	fmt.Scanln(&nuevaMateria)
	nuevaMateria = strings.TrimSpace(nuevaMateria)

	if nuevaMateria != "" {
		*materias = append(*materias, nuevaMateria)
		fmt.Printf("La materia '%s' ha sido agregada.\n", nuevaMateria)
	} else {
		fmt.Println("El nombre de la materia no puede estar vacío.")
	}
}