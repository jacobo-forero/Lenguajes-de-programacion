//INTERACCION CON EL USUARIO
package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	for {
		jugar()
		var continuar string
		fmt.Print("¿Quieres jugar de nuevo? (s/n): ")
		fmt.Scanln(&continuar)
		if continuar != "s" {
			fmt.Println("Gracias por jugar. ¡Hasta luego!")
			break
		}
	}
}

func obtenerAdivinanza() int {
	var adivinar int
	for {
		fmt.Print("Adivina el número del 1 al 10: ")
		_, err := fmt.Scan(&adivinar)
		if err != nil || adivinar < 1 || adivinar > 10 {
			fmt.Println("Por favor, ingresa un número entre 1 y 10.")
		} else {
			return adivinar
		}
	}
}

func jugar() {
	rand.Seed(time.Now().UnixNano()) // Inicializa la semilla para el generador de números aleatorios
	num := rand.Intn(10) + 1          // Genera un número aleatorio entre 1 y 10
	intentos := 3                      // Número de intentos permitidos

	fmt.Println("Tienes 3 intentos para adivinar el número.")
	
	for i := 0; i < intentos; i++ {
		adivinar := obtenerAdivinanza()
		
		if num == adivinar {
			fmt.Println("¡Has ganado!")
			return
		} else {
			fmt.Printf("Intento %d fallido.\n", i+1)
		}
	}

	fmt.Printf("Has perdido, el número era: %d\n", num)
}