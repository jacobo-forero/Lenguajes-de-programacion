//Condicioanles IF ELSE

#include <iostream>
#include <limits>

int obtener_edad() {
    int edad;
    while (true) {
        std::cout << "Ingresa tu edad: ";
        std::cin >> edad;

        // Validar la entrada
        if (std::cin.fail() || edad < 0) {
            std::cin.clear(); // Limpiar el estado de error
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Ignorar la entrada incorrecta
            std::cout << "La edad no puede ser negativa. Inténtalo de nuevo." << std::endl;
        } else {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Limpiar el buffer
            return edad;
        }
    }
}

void mayoria_edad() {
    int edad = obtener_edad();
    
    if (edad >= 18) {
        std::cout << "Eres mayor de edad." << std::endl;
    } else {
        std::cout << "Eres menor de edad." << std::endl;
    }
}

int main() {
    mayoria_edad();
    return 0;
}