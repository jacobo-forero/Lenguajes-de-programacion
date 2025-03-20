//INTERACCION CON EL USUARIO
#include <iostream>
#include <limits>
#include <cstdlib>
#include <ctime>

int obtener_adivinanza() {
    int adivinar;
    while (true) {
        std::cout << "Adivina el número del 1 al 10: ";
        std::cin >> adivinar;

        // Validar la entrada
        if (std::cin.fail()) {
            std::cin.clear(); // Limpiar el estado de error
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Ignorar la entrada incorrecta
            std::cout << "Error: Debes ingresar un número entero." << std::endl;
        } else if (adivinar < 1 || adivinar > 10) {
            std::cout << "Por favor, ingresa un número entre 1 y 10." << std::endl;
        } else {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Limpiar el buffer
            return adivinar;
        }
    }
}

void jugar() {
    std::srand(static_cast<unsigned int>(std::time(0))); // Inicializar la semilla para rand
    int num = std::rand() % 10 + 1; // Generar un número aleatorio entre 1 y 10
    int intentos = 3; // Número de intentos permitidos

    std::cout << "Tienes 3 intentos para adivinar el número." << std::endl;
    
    for (int i = 0; i < intentos; ++i) {
        int adivinar = obtener_adivinanza();
        
        if (num == adivinar) {
            std::cout << "¡Has ganado!" << std::endl;
            return;
        } else {
            std::cout << "Intento " << (i + 1) << " fallido." << std::endl;
        }
    }
    
    std::cout << "Has perdido, el número era: " << num << std::endl;
}

int main() {
    while (true) {
        jugar();
        std::string continuar;
        std::cout << "¿Quieres jugar de nuevo? (s/n): ";
        std::getline(std::cin, continuar);
        
        if (continuar != "s" && continuar != "S") {
            std::cout << "Gracias por jugar. ¡Hasta luego!" << std::endl;
            break;
        }
    }
    return 0;
}