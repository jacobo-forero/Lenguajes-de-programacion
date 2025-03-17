//OCTAVOS DE FINAL
package main

import (
	"fmt"
	"math/rand"
	"time"
)

func simularPartido(equipo1, equipo2 string) string {
	if rand.Intn(2) == 0 {
		return equipo1
	}
	return equipo2
}

func octavosDeFinal(equipos []string) []string {
	fmt.Println("Octavos de Final:")
	ganadores := []string{}

	if len(equipos)%2 != 0 {
		fmt.Println("El número de equipos debe ser par.")
		return nil
	}

	for i := 0; i < len(equipos); i += 2 {
		equipo1 := equipos[i]
		equipo2 := equipos[i+1]
		ganador := simularPartido(equipo1, equipo2)
		ganadores = append(ganadores, ganador)
		fmt.Printf("Partido: %s vs %s - Ganador: %s\n", equipo1, equipo2, ganador)
	}

	return ganadores
}

func main() {
	rand.Seed(time.Now().UnixNano())

	equipos := []string{
		"FC Barcelona",
		"Real Madrid",
		"Arsenal",
		"Manchester City",
		"Chelsea",
		"Liverpool",
		"PSG",
		"Benfica",
	}

	ganadores := octavosDeFinal(equipos)

	fmt.Println("\nEquipos que avanzan a los cuartos de final:")
	for _, ganador := range ganadores {
		fmt.Println(ganador)
	}
}